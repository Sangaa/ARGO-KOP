from __future__ import annotations

import subprocess
from pathlib import Path

from ejr_h1_namespace_lineage import classify_from_report


def _git(root: Path, *args: str) -> None:
    subprocess.check_call(["git", *args], cwd=root)


def _commit(root: Path, message: str) -> None:
    _git(root, "add", ".")
    _git(root, "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", message)


def _add(root: Path, path: str, title: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"# EJR-777 {title}\n", encoding="utf-8")
    _commit(root, title)


def _report(paths: list[str]) -> dict:
    return {
        "ambiguous_duplicate_records": {
            "EJR-777": [
                {"path": path, "identity_source": "FIRST_H1_FALLBACK"}
                for path in paths
            ],
            "EJR-778": [
                {"path": "EJR/explicit.md", "identity_source": "DOCUMENT_ID_FIELD"},
                {"path": "EJR/h1.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
        }
    }


def test_memory_to_root_direction(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    paths = [
        "Memory/Engineering_Journal/a.md",
        "EJR/b.md",
    ]
    _add(tmp_path, paths[0], "memory")
    _add(tmp_path, paths[1], "root")
    result = classify_from_report(tmp_path, _report(paths))
    group = result["groups"]["EJR-777"]
    assert result["group_count"] == 1
    assert group["classification"] == "MEMORY_TO_ROOT_EJR"
    assert group["namespace_sequence"] == ["MEMORY_EJR", "ROOT_EJR"]
    assert group["transition_count"] == 1


def test_root_to_memory_direction(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    paths = ["EJR/a.md", "Memory/Engineering_Journal/b.md"]
    _add(tmp_path, paths[0], "root")
    _add(tmp_path, paths[1], "memory")
    result = classify_from_report(tmp_path, _report(paths))
    assert result["groups"]["EJR-777"]["classification"] == "ROOT_TO_MEMORY_EJR"


def test_same_root_multi_member_chain(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    paths = ["EJR/a.md", "EJR/b.md", "EJR/c.md"]
    for index, path in enumerate(paths):
        _add(tmp_path, path, f"root-{index}")
    result = classify_from_report(tmp_path, _report(paths))
    group = result["groups"]["EJR-777"]
    assert group["classification"] == "SAME_SURFACE_ROOT_EJR"
    assert group["collapsed_namespace_sequence"] == ["ROOT_EJR"]
    assert group["transition_count"] == 0


def test_multi_namespace_transition(tmp_path: Path) -> None:
    _git(tmp_path, "init")
    paths = [
        "Memory/Engineering_Journal/a.md",
        "EJR/b.md",
        "Memory/Engineering_Journal/c.md",
    ]
    for index, path in enumerate(paths):
        _add(tmp_path, path, f"step-{index}")
    result = classify_from_report(tmp_path, _report(paths))
    group = result["groups"]["EJR-777"]
    assert group["classification"] == "MULTI_NAMESPACE_TRANSITION"
    assert group["collapsed_namespace_sequence"] == ["MEMORY_EJR", "ROOT_EJR", "MEMORY_EJR"]
    assert group["transition_count"] == 2


def test_shallow_history_fails_closed(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    _git(source, "init")
    paths = ["EJR/a.md", "Memory/Engineering_Journal/b.md"]
    _add(source, paths[0], "one")
    _add(source, paths[1], "two")

    shallow = tmp_path / "shallow"
    subprocess.check_call(["git", "clone", "--depth", "1", source.resolve().as_uri(), str(shallow)])
    result = classify_from_report(shallow, _report(paths))
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["classification_complete"] is False
    assert result["groups"] == {}
