from pathlib import Path


def test_memory_governance_preserves_scoped_promotion_boundary():
    root = Path(__file__).resolve().parents[2]
    memory = root / "Memory/MEM-005_MEMORY_GOVERNANCE.md"
    knowledge = root / "Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md"
    lifecycle = root / "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md"

    memory_text = memory.read_text(encoding="utf-8")
    knowledge_text = knowledge.read_text(encoding="utf-8")
    lifecycle_text = lifecycle.read_text(encoding="utf-8")

    assert "Shared Candidate" in memory_text
    assert "Promotion from User/Project/Deployment memory to Platform memory requires" in memory_text
    assert "Requires promotion gate" in memory_text
    assert "VALIDATED` does not automatically mean `CANONICAL" in knowledge_text
    assert "Promotion from `USER`, `PROJECT` or `DEPLOYMENT` toward `SHARED_CANDIDATE` or `PLATFORM` requires" in lifecycle_text


def test_memory_governance_never_equates_repetition_or_model_output_with_canonical_authority():
    text = (Path(__file__).resolve().parents[2] / "Memory/MEM-005_MEMORY_GOVERNANCE.md").read_text(encoding="utf-8")
    assert "Repeated does not mean canonical." in text
    assert "Model-generated does not mean canonical." in text
    assert "Useful does not mean canonical." in text
