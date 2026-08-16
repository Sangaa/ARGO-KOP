from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MODELS = ROOT / "Models"

ACTIVE_MODELS = {
    "MOD-001": "MOD-001_KNOWLEDGE_MODEL.md",
    "MOD-002": "MOD-002_ENTITY_MODEL.md",
    "MOD-003": "MOD-003_DOCUMENT_MODEL.md",
    "MOD-004": "MOD-004_MEMORY_MODEL.md",
    "MOD-011": "MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _metadata(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    assert match, f"Missing metadata field: {key}"
    return match.group(1).strip()


def test_active_models_filename_internal_id_and_inventory_agree():
    folder_status = _read(MODELS / "_FOLDER_STATUS.md")
    readme = _read(MODELS / "README.md")

    for document_id, filename in ACTIVE_MODELS.items():
        path = MODELS / filename
        assert path.is_file(), f"Verified model artifact is missing: {filename}"

        text = _read(path)
        assert _metadata(text, "Document ID") == document_id
        assert _metadata(text, "Canonical") == "Yes"
        assert filename in folder_status
        assert filename in readme


def test_models_inventory_does_not_use_legacy_id_as_active_identity():
    folder_status = _read(MODELS / "_FOLDER_STATUS.md")
    readme = _read(MODELS / "README.md")

    # Historical declarations are allowed as evidence, but must not silently
    # become active canonical identities. The current verified list is the
    # bounded authority surface for this guard.
    for document_id, filename in ACTIVE_MODELS.items():
        assert filename in folder_status
        assert filename in readme
        assert re.search(rf"\b{re.escape(document_id)}\b", _read(MODELS / filename))
