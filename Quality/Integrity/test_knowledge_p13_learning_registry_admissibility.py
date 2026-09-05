from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
BRIDGE = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_REGISTRATION_BRIDGE_2026-09-05_D.md"
AUDIT = ROOT / "Repository" / "P13_KNOWLEDGE_LEARNING_REGISTRY_ADMISSIBILITY_2026-09-05_J.tsv"
RUNTIME_PIPELINE = ROOT / "Runtime" / "Context" / "runtime_context_pipeline.py"
P10_CORRECTION = ROOT / "Repository" / "REP-011_PRIORITY10_RUNTIME_KNOWLEDGE_CORRECTION_ADDENDUM_2026-09-03_H.md"


def test_cross_layer_cohort_must_fold_before_new_learning_rel_id() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")
    assert "| REL-167 |" in registry
    assert "| REL-168 |" not in registry
    assert "| REL-206 |" not in registry
    assert "REL-168..REL-206" in bridge
    assert "CANONICAL REP-014 SYNCHRONIZATION = OPEN" in bridge
    assert "| REL-207 |" not in registry


def test_contextual_retrieval_is_verified_executable_consumer_candidate() -> None:
    pipeline = RUNTIME_PIPELINE.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    assert "from contextual_retrieval import retrieve_in_context" in pipeline
    assert "knowledge = retrieve_in_context(records, context)" in pipeline
    assert "Runtime/Context/runtime_context_pipeline.py\tKnowledge/Learning/contextual_retrieval.py\tCONSUMES\tDIRECT_IMPORT_AND_CALL_VERIFIED\tADMISSIBLE_AFTER_REL168_206_CANONICAL_FOLD_NEXT_ID_REVIEW_REQUIRED" in audit


def test_knowledge_correction_seam_reuses_p10_evidence_without_duplicate_inference() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    p10 = P10_CORRECTION.read_text(encoding="utf-8")
    assert "Runtime/Context/runtime_context_pipeline.py\tKnowledge/Learning/knowledge_correction.py\tCONSUMES\tDIRECT_IMPORT_AND_CALL_PLUS_P10_GOVERNED_BOUNDARY\tNO_DUPLICATE_RELATIONSHIP_INFERENCE_P10_EVIDENCE_RETAINED" in audit
    assert "delegates contradiction assessment to `Knowledge/Learning/knowledge_correction.py`" in p10
    assert "Runtime receives no Knowledge authority" in p10


def test_removed_reverse_dependency_is_rejected_not_canonicalized() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    assert "Knowledge/Learning/promotion_gate_adapter.py\tRuntime/Prototype/learning_promotion_gate.py\tDEPENDS_ON\tHISTORICAL_REVERSE_IMPORT_REMOVED_UNIT15\tREJECTED_NOT_REGISTRY_ADMISSIBLE" in audit
