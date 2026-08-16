from pathlib import Path


def test_knowledge_lifecycle_points_to_current_document_lifecycle_authority():
    root = Path(__file__).resolve().parents[2]
    lifecycle = root / "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md"
    current = root / "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md"
    retired = root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md"

    text = lifecycle.read_text(encoding="utf-8")
    assert current.is_file()
    assert not retired.exists()
    assert "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md" in text
    assert "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md" not in text
