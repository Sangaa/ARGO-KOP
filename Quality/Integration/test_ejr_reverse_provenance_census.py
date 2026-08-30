from __future__ import annotations

import subprocess
from pathlib import Path

import ejr_reverse_provenance_census as census


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, stdout=subprocess.DEVNULL)


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _repo(tmp_path: Path) -> Path:
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@example.invalid")
    _git(tmp_path, "config", "user.name", "test")
    return tmp_path


def _report(paths_by_id: dict[str, list[str]], *, source: str = "FIRST_H1_FALLBACK") -> dict:
    return {
        "ambiguous_duplicate_records": {
            document_id: [
                {"path": path, "identity_source": source}
                for path in paths
            ]
            for document_id, paths in paths_by_id.items()
        }
    }


def _expected_paths() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for document_id, count in census.EXPECTED_CARDINALITY.items():
        paths = [f"EJR/{document_id}_ROOT.md"]
        for index in range(1, count):
            paths.append(f"Memory/Engineering_Journal/{document_id}_MEM{index}.md")
        result[document_id] = paths
    return result


def test_census_supports_heterogeneous_cardinality_and_references(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    paths_by_id = _expected_paths()
    for document_id, paths in paths_by_id.items():
        for index, path in enumerate(paths):
            _write(root, path, f"# {document_id} — member {index}\nbody {document_id} {index}\n")

    _write(
        root,
        "Repository/consumer.md",
        "See EJR-178 and Memory/Engineering_Journal/EJR-222_MEM1.md\n",
    )
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")

    result = census.classify_from_report(root, _report(paths_by_id))
    assert result["decision"] == "CENSUSED"
    assert result["classification_complete"] is True
    assert result["group_count"] == 4
    assert result["groups"]["EJR-178"]["member_count"] == 3
    assert result["groups"]["EJR-189"]["member_count"] == 2
    assert result["groups"]["EJR-222"]["member_count"] == 4
    assert result["groups"]["EJR-338"]["member_count"] == 2
    assert result["groups"]["EJR-178"]["content_all_distinct"] is True
    assert result["groups"]["EJR-178"]["external_exact_id_reference_paths"] == [
        "Repository/consumer.md"
    ]
    assert result["groups"]["EJR-222"]["external_exact_member_path_references"][
        "Memory/Engineering_Journal/EJR-222_MEM1.md"
    ] == ["Repository/consumer.md"]
    assert "owner" not in result["groups"]["EJR-178"]
    assert "canonical" not in result["groups"]["EJR-178"]


def test_cardinality_drift_fails_partial(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    paths_by_id = _expected_paths()
    paths_by_id["EJR-222"] = paths_by_id["EJR-222"][:-1]
    for document_id, paths in paths_by_id.items():
        for index, path in enumerate(paths):
            _write(root, path, f"# {document_id} — member {index}\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")

    result = census.classify_from_report(root, _report(paths_by_id))
    assert result["decision"] == "PARTIAL"
    assert "EJR-222" in result["incomplete_group_ids"]
    assert result["groups"]["EJR-222"]["membership_state"] == "UNEXPECTED_CURRENT_MEMBERSHIP"


def test_identity_source_drift_fails_partial(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    paths_by_id = _expected_paths()
    for document_id, paths in paths_by_id.items():
        for index, path in enumerate(paths):
            _write(root, path, f"# {document_id} — member {index}\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")

    result = census.classify_from_report(root, _report(paths_by_id, source="DOCUMENT_ID_METADATA"))
    assert result["decision"] == "PARTIAL"
    assert set(result["incomplete_group_ids"]) == set(census.TARGET_IDS)


def test_shallow_history_fails_closed(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)
    monkeypatch.setattr(census, "history_complete", lambda _: False)
    result = census.classify_from_report(root, {"ambiguous_duplicate_records": {}})
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["classification_complete"] is False
