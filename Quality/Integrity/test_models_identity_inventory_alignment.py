"""Bounded Models identity/inventory guard.

This guard checks only the currently verified Models artifacts. It does not
certify the Models domain as complete or canonical as a whole.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
MODELS = ROOT / "Models"
VERIFIED = {
    "MOD-001": "MOD-001_KNOWLEDGE_MODEL.md",
    "MOD-002": "MOD-002_ENTITY_MODEL.md",
    "MOD-003": "MOD-003_DOCUMENT_MODEL.md",
    "MOD-004": "MOD-004_MEMORY_MODEL.md",
    "MOD-011": "MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
}


def _metadata(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_verified_models_have_filename_document_id_alignment():
    for document_id, filename in VERIFIED.items():
        path = MODELS / filename
        assert path.is_file(), f"verified Models artifact missing: {filename}"
        text = _metadata(path)
        assert re.search(rf"(?m)^Document ID:\s*{re.escape(document_id)}\s*$", text), (
            f"Document ID drift: {filename} != {document_id}"
        )
        assert re.search(r"(?m)^Canonical:\s*Yes\s*$", text), (
            f"verified artifact lost canonical marker: {filename}"
        )


def test_models_folder_inventory_does_not_reassign_verified_ids():
    status = (MODELS / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    for document_id in VERIFIED:
        assert document_id in status, f"Models inventory no longer references {document_id}"
    # The folder status is a status/evidence record, not a completion certificate.
    assert "Canonical: Pending consolidated validation" in status
    assert "INTEGRITY HOLD / STAGED RECONSTRUCTION" in status
