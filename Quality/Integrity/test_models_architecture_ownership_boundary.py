from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MODEL = ROOT / "Models/MOD-002_ENTITY_MODEL.md"
ARCHITECTURE_SOURCES = {
    "Architecture/ARC-002_COMPONENT_ARCHITECTURE.md": "ARC-002",
    "Architecture/ARC-006_DEPENDENCY_MODEL.md": "ARC-006",
}


def _related_documents(text: str):
    marker = "# Related Documents"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1]


def test_model_architecture_references_remain_explicitly_referenced():
    text = MODEL.read_text(encoding="utf-8")
    related = _related_documents(text)
    for target in ARCHITECTURE_SOURCES:
        assert target in related, f"missing bounded Architecture reference: {target}"


def test_architecture_sources_expose_ownership_or_dependency_authority_boundary():
    arc002 = (ROOT / "Architecture/ARC-002_COMPONENT_ARCHITECTURE.md").read_text(encoding="utf-8")
    arc006 = (ROOT / "Architecture/ARC-006_DEPENDENCY_MODEL.md").read_text(encoding="utf-8")

    assert "ARC-002" in arc002
    assert "Category\n\nArchitecture" in arc002 or "Category: Architecture" in arc002
    assert "Every active canonical artifact MUST have one primary responsibility and one authoritative owner." in arc002

    assert "ARC-006" in arc006
    assert "Category\n\nArchitecture" in arc006 or "Category: Architecture" in arc006
    assert "A dependency does not transfer authority." in arc006


def test_reference_to_architecture_does_not_create_model_ownership():
    text = MODEL.read_text(encoding="utf-8")
    related = _related_documents(text)
    assert "OWNS" not in related
    assert "OWNER" not in related.upper()


# Bounded ownership-boundary guard. It does not certify the complete
# architecture graph, reverse ownership, or repository-wide absence of MOD-002
# ownership claims outside the inspected surfaces.
