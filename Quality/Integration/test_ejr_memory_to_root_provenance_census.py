from __future__ import annotations

import subprocess
from pathlib import Path

import ejr_memory_to_root_provenance_census as census


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


def _audit() -> dict:
    return {
        "ambiguous_duplicate_records": {
            "EJR-101": [
                {"path": "Memory/Engineering_Journal/EJR-101_A.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "EJR/EJR-101_B.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "EJR-102": [
                {"path": "Memory/Engineering_Journal/EJR-102_A.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "EJR/EJR-102_B.md", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "EJR/EJR-102_C.md", "identity_source": "FIRST_H1_FALLBACK"},
            ],
        }
    }


def _lineage() -> dict:
    return {
        "history_complete": True,
        "groups": {
            "EJR-101": {
                "classification": census.TARGET_CLASS,
                "cardinality": 2,
                "namespace_sequence": ["MEMORY_EJR", "ROOT_EJR"],
                "collapsed_namespace_sequence": ["MEMORY_EJR", "ROOT_EJR"],
            },
            "EJR-102": {
                "classification": census.TARGET_CLASS,
                "cardinality": 3,
                "namespace_sequence": ["MEMORY_EJR", "ROOT_EJR", "ROOT_EJR"],
                "collapsed_namespace_sequence": ["MEMORY_EJR", "ROOT_EJR"],
            },
            "EJR-999": {"classification": "ROOT_TO_MEMORY_EJR", "cardinality": 2},
        },
    }


def test_dynamic_cohort_census_and_reference_separation(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    for path, body in {
        "Memory/Engineering_Journal/EJR-101_A.md": "# EJR-101 — A\nalpha\n",
        "EJR/EJR-101_B.md": "# EJR-101 — B\nbeta\n",
        "Memory/Engineering_Journal/EJR-102_A.md": "# EJR-102 — A\none\n",
        "EJR/EJR-102_B.md": "# EJR-102 — B\ntwo\n",
        "EJR/EJR-102_C.md": "# EJR-102 — C\nthree\n",
        "Repository/consumer.md": "See EJR-101 and EJR/EJR-102_B.md\n",
    }.items():
        _write(root, path, body)
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")

    result = census.classify_from_reports(root, _audit(), _lineage(), expected_group_count=2)
    assert result["decision"] == "CENSUSED"
    assert result["target_ids"] == ["EJR-101", "EJR-102"]
    assert result["groups"]["EJR-101"]["content_all_distinct"] is True
    assert result["groups"]["EJR-101"]["external_exact_id_reference_paths"] == ["Repository/consumer.md"]
    assert result["groups"]["EJR-102"]["external_exact_member_path_references"]["EJR/EJR-102_B.md"] == ["Repository/consumer.md"]
    assert "owner" not in result["groups"]["EJR-101"]
    assert "canonical" not in result["groups"]["EJR-101"]


def test_cohort_count_drift_fails_partial(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    _write(root, "Memory/Engineering_Journal/EJR-101_A.md", "# EJR-101 — A\n")
    _write(root, "EJR/EJR-101_B.md", "# EJR-101 — B\n")
    _write(root, "Memory/Engineering_Journal/EJR-102_A.md", "# EJR-102 — A\n")
    _write(root, "EJR/EJR-102_B.md", "# EJR-102 — B\n")
    _write(root, "EJR/EJR-102_C.md", "# EJR-102 — C\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")
    result = census.classify_from_reports(root, _audit(), _lineage(), expected_group_count=3)
    assert result["decision"] == "PARTIAL"
    assert "__COHORT_COUNT_DRIFT__" in result["incomplete_group_ids"]


def test_identity_source_drift_fails_partial(tmp_path: Path) -> None:
    root = _repo(tmp_path)
    audit = _audit()
    audit["ambiguous_duplicate_records"]["EJR-101"][0]["identity_source"] = "DOCUMENT_ID_METADATA"
    for path in [
        "Memory/Engineering_Journal/EJR-101_A.md", "EJR/EJR-101_B.md",
        "Memory/Engineering_Journal/EJR-102_A.md", "EJR/EJR-102_B.md", "EJR/EJR-102_C.md",
    ]:
        _write(root, path, "# fixture\n")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "fixture")
    result = census.classify_from_reports(root, audit, _lineage(), expected_group_count=2)
    assert result["decision"] == "PARTIAL"
    assert "EJR-101" in result["incomplete_group_ids"]


def test_incomplete_history_fails_closed(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)
    monkeypatch.setattr(census, "history_complete", lambda _: False)
    result = census.classify_from_reports(root, {}, _lineage(), expected_group_count=2)
    assert result["decision"] == "HISTORY_INCOMPLETE"
    assert result["classification_complete"] is False
