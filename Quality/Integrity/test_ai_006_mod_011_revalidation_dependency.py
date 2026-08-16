from pathlib import Path


def test_ai_006_tracks_mod_011_revalidation_boundary():
    root = Path(__file__).resolve().parents[2]
    adapter = root / "AI/AI-006_MODEL_ADAPTER.md"
    model = root / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
    adapter_text = adapter.read_text(encoding="utf-8")
    model_text = model.read_text(encoding="utf-8")

    assert model.is_file()
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in adapter_text
    assert "Revalidation Required" in model_text
    assert "does not certify the full pre-failure semantic mutation" in model_text


def test_revalidation_required_source_cannot_be_reinterpreted_as_validated_dependency():
    root = Path(__file__).resolve().parents[2]
    model_text = (root / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md").read_text(encoding="utf-8")
    adapter_text = (root / "AI/AI-006_MODEL_ADAPTER.md").read_text(encoding="utf-8")

    assert "Status: Proposed / Future-Ready / Revalidation Required" in model_text
    assert "Integrity Hold / Revalidation Required" in adapter_text
