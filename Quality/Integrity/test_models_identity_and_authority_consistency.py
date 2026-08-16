"""Models identity/authority guard.

This guard intentionally checks only the inspected canonical Models set and
its folder inventory. It does not certify the entire Models domain.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MODELS = ROOT / "Models"

CANONICAL_MODELS = {
    "MOD-001": MODELS / "MOD-001_KNOWLEDGE_MODEL.md",
    "MOD-002": MODELS / "MOD-002_ENTITY_MODEL.md",
    "MOD-003": MODELS / "MOD-003_DOCUMENT_MODEL.md",
    "MOD-004": MODELS / "MOD-004_MEMORY_MODEL.md",
    "MOD-011": MODELS / "MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
}


def _field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*(.+?)\s*$", text)
    assert match, f"Missing {name} metadata"
    return match.group(1).strip()


def test_models_filename_internal_id_and_canonical_metadata_agree():
    for document_id, path in CANONICAL_MODELS.items():
        assert path.is_file(), f"Missing expected canonical model: {path}"
        text = path.read_text(encoding="utf-8")
        assert _field(text, "Document ID") == document_id
        assert _field(text, "Canonical") == "Yes"


def test_models_inventory_does_not_assign_a_second_canonical_identity():
    inventory = (MODELS / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    for document_id in CANONICAL_MODELS:
        assert document_id in inventory
    assert "Canonical: Pending consolidated validation" in inventory


def test_models_authority_boundaries_are_explicit():
    mod001 = (MODELS / "MOD-001_KNOWLEDGE_MODEL.md").read_text(encoding="utf-8")
    mod002 = (MODELS / "MOD-002_ENTITY_MODEL.md").read_text(encoding="utf-8")
    mod003 = (MODELS / "MOD-003_DOCUMENT_MODEL.md").read_text(encoding="utf-8")
    mod004 = (MODELS / "MOD-004_MEMORY_MODEL.md").read_text(encoding="utf-8")
    mod011 = (MODELS / "MOD-011_KNOWLEDGE_SOURCE_MODEL.md").read_text(encoding="utf-8")

    assert "does not certify the entire Models" in mod001
    assert "does not, by itself, prove that every concrete entity instance is canonical" in mod002
    assert "A historical reference does not establish active authority." in mod003
    assert "Memory is not automatically authoritative" in mod004
    assert "no source automatically defines truth" in mod011
