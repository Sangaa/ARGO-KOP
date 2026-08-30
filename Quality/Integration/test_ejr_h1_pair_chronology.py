from __future__ import annotations

import subprocess
from pathlib import Path

from ejr_h1_pair_chronology import classify_from_report


def _git(root: Path, *args: str) -> None:
    subprocess.check_call(["git", *args], cwd=root)


def _commit(root: Path, message: str) -> None:
    _git(root, "add", ".")
    _git(root, "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", message)


def _report(path_a: str, path_b: str) -> dict:
    return {
        "ambiguous_duplicate_records": {
            "EJR-777": [
                {"path": path_a, "identity_source": "FIRST_H1_FALLBACK"},
                {"path": path_b, "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "EJR-778": [
                {"path": "x.md", "identity_source": "DOCUMENT_ID_FIELD"},
                {"path": "y.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "EJR-779": [
                {"path": "a.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "b.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "c.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
        }
    }


def test_pair_classifies_ancestor_order(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    first = tmp_path / "first.md"
    first.write_text("# EJR-777 first\n", encoding="utf-8")
    _commit(tmp_path, "first")
    second = tmp_path / "second.md"
    second.write_text("# EJR-777 second\n", encoding="utf-8")
    _commit(tmp_path, "second")

    result = classify_from_report(tmp_path, _report("first.md", "second.md"))
    group = result["groups"]["EJR-777"]
    assert result["history_complete"] is True
    assert result["group_count"] == 1
    assert group["relation"] == "LEFT_FIRST_SEEN_ANCESTOR"
    assert result["counts_by_relation"] == {"LEFT_FIRST_SEEN_ANCESTOR": 1}


def test_pair_same_first_seen_commit(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    (tmp_path / "a.md").write_text("# EJR-777 A\n", encoding="utf-8")
    (tmp_path / "b.md").write_text("# EJR-777 B\n", encoding="utf-8")
    _commit(tmp_path, "both")

    result = classify_from_report(tmp_path, _report("a.md", "b.md"))
    assert result["groups"]["EJR-777"]["relation"] == "SAME_FIRST_SEEN_COMMIT"


def test_missing_history_is_partial(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    (tmp_path / "a.md").write_text("# EJR-777 A\n", encoding="utf-8")
    _commit(tmp_path, "one")

    result = classify_from_report(tmp_path, _report("a.md", "missing.md"))
    assert result["decision"] == "PARTIAL"
    assert result["classification_complete"] is False
    assert result["groups"]["EJR-777"]["relation"] == "MISSING_PATH_HISTORY"


def test_shallow_history_fails_closed(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    _git(source, "init")
    (source / "a.md").write_text("# EJR-777 A\n", encoding="utf-8")
    _commit(source, "one")
    (source / "b.md").write_text("# EJR-777 B\n", encoding="utf-8")
    _commit(source, "two")

    shallow = tmp_path / "shallow"
    subprocess.check_call([
        "git", "clone", "--depth", "1", source.resolve().as_uri(), str(shallow)
    ])
    result = classify_from_report(shallow, _report("a.md", "b.md"))
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["history_complete"] is False
    assert result["classification_complete"] is False
    assert result["groups"] == {}
