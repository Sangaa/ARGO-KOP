from pathlib import Path


def test_ai_006_tracks_mod_011_bounded_revalidated_boundary():
    root = Path(__file__).resolve().parents[2]
    adapter = root / "AI/AI-006_MODEL_ADAPTER.md"
    model = root / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
    adapter_text = adapter.read_text(encoding="utf-8")
    model_text = model.read_text(encoding="utf-8")

    assert model.is_file()
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in adapter_text
    assert "Status: Proposed / Future-Ready / Revalidated" in model_text
    assert "historical pre-failure provenance remains preserved as evidence" in model_text
    assert "does not promote model maturity" in model_text
    assert "repository-wide integrity" in model_text


def test_revalidated_source_does_not_auto_promote_the_adapter():
    root = Path(__file__).resolve().parents[2]
    model_text = (root / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md").read_text(encoding="utf-8")
    adapter_text = (root / "AI/AI-006_MODEL_ADAPTER.md").read_text(encoding="utf-8")

    assert "Status: Proposed / Future-Ready / Revalidated" in model_text
    assert "Integrity Hold / Revalidation Required" in adapter_text
    assert "AI-006 consumes these semantics but does not redefine or grant authority through them" in adapter_text
    assert "does not by itself establish canonical knowledge" in adapter_text
    assert "this reference does not transfer canonical authority to the adapter" in adapter_text
