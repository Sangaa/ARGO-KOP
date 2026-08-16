from pathlib import Path


EXPECTED_MODELS = {
    "MOD-001_KNOWLEDGE_MODEL.md": "MOD-001",
    "MOD-002_ENTITY_MODEL.md": "MOD-002",
    "MOD-003_DOCUMENT_MODEL.md": "MOD-003",
    "MOD-004_MEMORY_MODEL.md": "MOD-004",
    "MOD-011_KNOWLEDGE_SOURCE_MODEL.md": "MOD-011",
}


def _metadata_value(text: str, key: str):
    import re

    match = re.search(
        rf"^\s*{re.escape(key)}\s*:\s*(.+?)\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    if match:
        return match.group(1).strip().lower()
    return None


def _document_id(text: str):
    import re

    match = re.search(r"^Document ID:\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def test_models_folder_status_lists_currently_verified_model_artifacts():
    root = Path(__file__).resolve().parents[2]
    status = (root / "Models/_FOLDER_STATUS.md").read_text(encoding="utf-8")
    finding = status.split("# Reconstruction Decision", 1)[0]

    for filename, document_id in EXPECTED_MODELS.items():
        assert f"`{filename}`" in finding
        text = (root / "Models" / filename).read_text(encoding="utf-8")
        assert _document_id(text) == document_id
        assert _metadata_value(text, "Canonical") == "yes"


def test_models_folder_status_does_not_invent_missing_numeric_sequence():
    root = Path(__file__).resolve().parents[2]
    status = (root / "Models/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    assert "No missing artifact is to be recreated merely to complete a numeric sequence." in status
