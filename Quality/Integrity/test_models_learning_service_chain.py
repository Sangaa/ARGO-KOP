from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOD_011 = ROOT / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
ENG_007 = ROOT / "Engine/ENG-007_LEARNING_ENGINE.md"
SRV_009 = ROOT / "Services/SRV-009_UPDATE_SERVICE.md"


def test_mod011_declares_eng007_learning_dependency():
    text = MOD_011.read_text(encoding="utf-8")
    assert "Engine/ENG-007_LEARNING_ENGINE.md" in text


def test_eng007_declares_mod011_semantic_model_and_srv009_service():
    text = ENG_007.read_text(encoding="utf-8")
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in text
    assert "Services/SRV-009_UPDATE_SERVICE.md" in text


def test_srv009_preserves_learning_ingestion_boundary():
    text = SRV_009.read_text(encoding="utf-8")
    assert "Reviewed Learning Ingestion" in text
    assert "never promote unreviewed model output directly into protected canonical knowledge" in text
    assert "Technical write completion is not equivalent to governed acceptance" in text


def test_chain_does_not_infer_direct_mod011_to_srv009_authority():
    # The chain is semantic/operational evidence only:
    # MOD-011 -> ENG-007 -> SRV-009.
    # No direct MOD-011 -> SRV-009 authority edge is inferred by this guard.
    assert "Services/SRV-009_UPDATE_SERVICE.md" not in MOD_011.read_text(encoding="utf-8")
