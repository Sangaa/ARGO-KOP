from __future__ import annotations

import subprocess
from pathlib import Path

import ejr_nonmonotonic_provenance_census as census


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


def _report(paths_by_id: dict[str, list[str]]) -> dict:
    return {
        "ambiguous_duplicate_records": {
            document_id: [
                {"path": path, "identity_source": "FIRST_H1_FALLBACK"}
                for path in paths
            ]
            for document_id, paths in paths_by_id.items()
        }
    }


def test_census_surfaces_distinct_content_and_external_references(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    paths_by_id: dict[str, list[str]] = {}
    for number in range(195, 199):
        document_id = f"EJR-{number}"
        paths = [
            f"EJR/{document_id}_A.md",
            f"Memory/Engineering_Journal/{document_id}_B.md",
            f"EJR/{document_id}_C.md",
        ]
        paths_by_id[document_id] = paths
        _write(root, paths[0], f"# {document_id} — Alpha\nalpha {number}\n")
        _write(root, paths[1], f"# {document_id} — Beta\nbeta {number}\n")
        _write(root, paths[2], f"# {document_id} — Gamma\ngamma {number}\n")

    _write(root, "Repository/consumer.md", "See EJR-195 and EJR/EJR-195_A.md\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")

    result = census.classify_from_report(root, _report(paths_by_id))
    assert result["decision"] == "CENSUSED"
    assert result["classification_complete"] is True
    assert result["group_count"] == 4
    assert result["groups"]["EJR-195"]["content_all_distinct"] is True
    assert result["groups"]["EJR-195"]["external_exact_id_reference_paths"] == [
        "Repository/consumer.md"
    ]
    assert result["groups"]["EJR-195"]["external_exact_sibling_path_references"][
        "EJR/EJR-195_A.md"
    ] == ["Repository/consumer.md"]
    assert "owner" not in result["groups"]["EJR-195"]


def test_unexpected_membership_fails_partial(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    _write(root, "EJR/EJR-195_A.md", "# EJR-195 — A\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")
    paths = {document_id: [] for document_id in census.TARGET_IDS}
    paths["EJR-195"] = ["EJR/EJR-195_A.md"]
    result = census.classify_from_report(root, _report(paths))
    assert result["decision"] == "PARTIAL"
    assert "EJR-195" in result["incomplete_group_ids"]


def test_shallow_history_fails_closed(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)
    monkeypatch.setattr(census, "history_complete", lambda _: False)
    result = census.classify_from_report(root, {"ambiguous_duplicate_records": {}})
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["classification_complete"] is False
