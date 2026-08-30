from __future__ import annotations

import subprocess
from pathlib import Path

from ejr_h1_multi_chronology import classify_from_report


def _git(root: Path, *args: str) -> None:
    subprocess.check_call(["git", *args], cwd=root)


def _commit(root: Path, message: str) -> None:
    _git(root, "add", ".")
    _git(root, "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", message)


def _report(paths: list[str]) -> dict:
    return {
        "ambiguous_duplicate_records": {
            "EJR-777": [
                {"path": path, "identity_source": "FIRST_H1_FALLBACK"}
                for path in paths
            ],
            "EJR-778": [
                {"path": "m1.md", "identity_source": "DOCUMENT_ID_FIELD"},
                {"path": "m2.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "m3.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "EJR-779": [
                {"path": "p1.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "p2.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
        }
    }


def test_multi_total_ancestry_chain(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    for index, name in enumerate(["a.md", "b.md", "c.md"], start=1):
        (tmp_path / name).write_text(f"# EJR-777 {name}\n", encoding="utf-8")
        _commit(tmp_path, f"commit-{index}")

    result = classify_from_report(tmp_path, _report(["a.md", "b.md", "c.md"]))
    group = result["groups"]["EJR-777"]
    assert result["group_count"] == 1
    assert result["classification_complete"] is True
    assert group["classification"] == "TOTAL_ANCESTRY_CHAIN"
    assert group["cardinality"] == 3
    assert sum(group["pair_counts"].values()) == 3


def test_multi_same_first_seen_collision(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    (tmp_path / "a.md").write_text("# EJR-777 A\n", encoding="utf-8")
    (tmp_path / "b.md").write_text("# EJR-777 B\n", encoding="utf-8")
    _commit(tmp_path, "both")
    (tmp_path / "c.md").write_text("# EJR-777 C\n", encoding="utf-8")
    _commit(tmp_path, "third")

    result = classify_from_report(tmp_path, _report(["a.md", "b.md", "c.md"]))
    assert result["groups"]["EJR-777"]["classification"] == "SAME_FIRST_SEEN_COLLISION"


def test_missing_history_is_partial(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    for name in ["a.md", "b.md"]:
        (tmp_path / name).write_text(f"# EJR-777 {name}\n", encoding="utf-8")
        _commit(tmp_path, name)

    result = classify_from_report(tmp_path, _report(["a.md", "b.md", "missing.md"]))
    assert result["decision"] == "PARTIAL"
    assert result["classification_complete"] is False
    assert result["groups"]["EJR-777"]["classification"] == "MISSING_PATH_HISTORY"


def test_shallow_history_fails_closed(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    _git(source, "init")
    for name in ["a.md", "b.md", "c.md"]:
        (source / name).write_text(f"# EJR-777 {name}\n", encoding="utf-8")
        _commit(source, name)

    shallow = tmp_path / "shallow"
    subprocess.check_call([
        "git", "clone", "--depth", "1", source.resolve().as_uri(), str(shallow)
    ])
    result = classify_from_report(shallow, _report(["a.md", "b.md", "c.md"]))
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["history_complete"] is False
    assert result["classification_complete"] is False
    assert result["groups"] == {}
