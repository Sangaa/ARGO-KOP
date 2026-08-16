from pathlib import Path


def test_ai_model_adapter_preserves_learning_authority_boundary():
    root = Path(__file__).resolve().parents[2]
    adapter = root / "AI/AI-006_MODEL_ADAPTER.md"
    knowledge_source = root / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
    handoff = root / "Memory/Engineering_Journal/SESSION_LEARNING_HANDOFF_TEMPLATE.md"

    text = adapter.read_text(encoding="utf-8")
    assert knowledge_source.is_file()
    assert handoff.is_file()
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in text
    assert "SESSION_LEARNING_HANDOFF_TEMPLATE.md" in text
    assert "transport success" in text
    assert "does not by itself establish canonical knowledge" in text


def test_ai_model_adapter_remains_revalidation_hold_until_independent_verification():
    root = Path(__file__).resolve().parents[2]
    text = (root / "AI/AI-006_MODEL_ADAPTER.md").read_text(encoding="utf-8")
    assert "Status: Integrity Hold / Revalidation Required" in text
    assert "does not certify the 2026-08-09 mutation as finally validated" in text
