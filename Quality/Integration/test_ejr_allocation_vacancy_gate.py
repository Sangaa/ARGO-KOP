from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from ejr_allocation_vacancy_gate import normalize_candidate, prove_vacancy


def _git(root: Path, *args: str) -> None:
    subprocess.check_call(
        ["git", *args],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def _init_repo(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    _git(root, "init")
    _git(root, "config", "user.name", "ARGO Test")
    _git(root, "config", "user.email", "argo-test@example.invalid")


def _commit_all(root: Path, message: str) -> None:
    _git(root, "add", "-A")
    _git(root, "commit", "-m", message)


def test_current_metadata_h1_and_filename_surfaces_are_occupied(tmp_path):
    _init_repo(tmp_path)
    (tmp_path / "explicit.md").write_text(
        "# Explicit record\n\nDocument ID: EJR-777\n",
        encoding="utf-8",
    )
    (tmp_path / "heading.md").write_text(
        "# EJR-777 — Heading-owned historical record\n",
        encoding="utf-8",
    )
    (tmp_path / "EJR-777_FILENAME_ONLY.bin").write_bytes(b"binary-placeholder")
    _commit_all(tmp_path, "seed occupied surfaces")

    report = prove_vacancy(tmp_path, "ejr-777")

    assert report["decision"] == "OCCUPIED"
    assert report["vacant"] is False
    assert report["history_complete"] is True
    surfaces = {item["surface"] for item in report["current_claims"]}
    assert {"DOCUMENT_ID_FIELD", "FIRST_H1_IDENTITY", "FILENAME_PREFIX"} <= surfaces


def test_deleted_historical_metadata_claim_remains_occupied(tmp_path):
    _init_repo(tmp_path)
    record = tmp_path / "legacy.md"
    record.write_text(
        "# Historical record\n\nDocument ID: EJR-778\n",
        encoding="utf-8",
    )
    _commit_all(tmp_path, "introduce historical identity")
    record.unlink()
    _commit_all(tmp_path, "remove current identity")

    report = prove_vacancy(tmp_path, "EJR-778")

    assert report["current_claims"] == []
    assert report["decision"] == "OCCUPIED"
    assert any(
        item["surface"] == "HISTORICAL_DOCUMENT_ID_FIELD"
        for item in report["historical_claims"]
    )


def test_deleted_historical_filename_prefix_remains_occupied(tmp_path):
    _init_repo(tmp_path)
    record = tmp_path / "EJR-779_FILENAME_ONLY.bin"
    record.write_bytes(b"historical-binary")
    _commit_all(tmp_path, "introduce historical filename")
    record.unlink()
    _commit_all(tmp_path, "delete historical filename")

    report = prove_vacancy(tmp_path, "EJR-779")

    assert report["current_claims"] == []
    assert report["decision"] == "OCCUPIED"
    assert any(
        item["surface"] == "HISTORICAL_FILENAME_PREFIX"
        for item in report["historical_claims"]
    )


def test_shallow_history_fails_closed_instead_of_claiming_vacancy(tmp_path):
    origin = tmp_path / "origin"
    _init_repo(origin)
    (origin / "one.txt").write_text("one\n", encoding="utf-8")
    _commit_all(origin, "one")
    (origin / "two.txt").write_text("two\n", encoding="utf-8")
    _commit_all(origin, "two")

    shallow = tmp_path / "shallow"
    subprocess.check_call(
        ["git", "clone", "--depth", "1", origin.resolve().as_uri(), str(shallow)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    report = prove_vacancy(shallow, "EJR-799")

    assert report["history_complete"] is False
    assert report["vacant"] is False
    assert report["decision"] == "HISTORY_INCOMPLETE"


def test_unused_candidate_is_vacant_only_with_complete_history(tmp_path):
    _init_repo(tmp_path)
    (tmp_path / "README.md").write_text("# Repository\n", encoding="utf-8")
    _commit_all(tmp_path, "seed unrelated history")

    report = prove_vacancy(tmp_path, "EJR-799")

    assert report["history_complete"] is True
    assert report["occupied"] is False
    assert report["vacant"] is True
    assert report["decision"] == "VACANT"


def test_candidate_format_is_strict():
    assert normalize_candidate("ejr-123") == "EJR-123"
    with pytest.raises(ValueError):
        normalize_candidate("EJR-1234")
