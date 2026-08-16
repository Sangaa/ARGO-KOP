import json
from pathlib import Path


def test_learning_pipeline_registry_handoff_points_to_its_own_certification_test_and_trace():
    root = Path(__file__).resolve().parents[2]
    registry_path = root / "Quality/Integration/evidence/runtime/learning_pipeline_to_verified_registry_verified_registry.json"
    payload = json.loads(registry_path.read_text(encoding="utf-8"))

    assert payload["seam"] == "Learning Pipeline -> Verified Registry"
    assert payload["state"] == "CONNECTED"
    assert payload["verification_status"] == "VERIFIED"
    assert payload["contract"] == "Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md"
    assert payload["test"] == "Quality/Integration/test_learning_pipeline_verified_registry_handoff.py"
    assert payload["trace"] == "Quality/Integration/canonical_evidence/LEARNING_PIPELINE_TO_VERIFIED_REGISTRY_TRACE.json"
    assert (root / payload["contract"]).is_file()
    assert (root / payload["test"]).is_file()
    assert (root / payload["trace"]).is_file()


def test_learning_pipeline_handoff_remains_outside_canonical_spine_and_promotion_authority():
    root = Path(__file__).resolve().parents[2]
    spine = (root / "Quality/Integration/canonical_spine_gap_map.py").read_text(encoding="utf-8")
    evidence = (root / "Quality/Integration/canonical_evidence/LEARNING_PIPELINE_TO_VERIFIED_REGISTRY.md").read_text(encoding="utf-8")
    contract = (root / "Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md").read_text(encoding="utf-8")
    assert '"Learning Pipeline -> Verified Registry"' not in spine
    assert "does not authorize autonomous knowledge promotion" in evidence
    assert "The existing Learning Promotion Gate remains the only downstream promotion authority." in contract


def test_learning_handoff_authorities_remain_aligned():
    root = Path(__file__).resolve().parents[2]
    learning = (root / "Engine/ENG-007_LEARNING_ENGINE.md").read_text(encoding="utf-8")
    memory = (root / "Memory/MEM-005_MEMORY_GOVERNANCE.md").read_text(encoding="utf-8")
    knowledge = (root / "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md").read_text(encoding="utf-8")
    assert "Parent ARGO + Responsible Engineer Review" in learning
    assert "Cross-Domain Promotion" in memory
    assert "Promotion or Reclassification Decision" in knowledge
