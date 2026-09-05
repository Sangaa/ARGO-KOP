from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Repository" / "REP-014_PRIORITY12_MOD011_EXTERNAL_CONSUMER_EVIDENCE_2026-09-05_H.tsv"
MOD011 = ROOT / "Models" / "MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
AI006 = ROOT / "AI" / "AI-006_MODEL_ADAPTER.md"
AI007 = ROOT / "AI" / "AI-007_MULTI_MODEL_SUPPORT.md"
AI008 = ROOT / "AI" / "AI-008_AI_GOVERNANCE.md"
GOV011 = ROOT / "Governance" / "GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md"
HANDOFF = ROOT / "Memory" / "Engineering_Journal" / "SESSION_LEARNING_HANDOFF_TEMPLATE.md"
ENG007 = ROOT / "Engine" / "ENG-007_LEARNING_ENGINE.md"


def test_explicit_ai006_semantic_consumption_is_preserved():
    text = AI006.read_text(encoding="utf-8")
    assert "AI-006 consumes these semantics" in text
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "AI-006\tMOD-011\tCONSUMES\tEXPLICIT_SEMANTIC_CONSUMPTION" in evidence


def test_ai007_and_ai008_semantic_alignment_is_not_downgraded_to_navigation():
    ai007 = AI007.read_text(encoding="utf-8")
    ai008 = AI008.read_text(encoding="utf-8")
    assert "shall remain aligned with `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`" in ai007
    assert "according to `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`" in ai008
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "AI-007\tMOD-011\tDEPENDS_ON\tQUALIFIED_SEMANTIC_DEPENDENCY" in evidence
    assert "AI-008\tMOD-011\tDEPENDS_ON\tQUALIFIED_SEMANTIC_DEPENDENCY" in evidence


def test_endpoint_maturity_is_kept_separate_from_relationship_semantics():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    for path in (AI006, AI007, AI008):
        text = path.read_text(encoding="utf-8")
        assert "Integrity Hold / Revalidation Required" in text
    assert evidence.count("REGISTRATION_CANDIDATE_ENDPOINT_HOLD") == 5


def test_gov011_is_not_promoted_to_active_dependency():
    mod011 = MOD011.read_text(encoding="utf-8")
    gov011 = GOV011.read_text(encoding="utf-8")
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md" in mod011
    assert "Status: Proposed / Integrity Hold" in gov011
    assert "Canonical: No" in gov011
    assert "MOD-011\tGOV-011\tREFERENCES\tPROPOSED_GOVERNANCE_FORMAT_REFERENCE" in evidence
    assert "MOD-011\tGOV-011\tDEPENDS_ON" not in evidence


def test_reverse_edges_are_not_manufactured_for_handoff_or_gov011():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "SESSION_LEARNING_HANDOFF_TEMPLATE\tMOD-011\tNONE\tNO_REVERSE_EDGE_PROVEN" in evidence
    assert "GOV-011\tMOD-011\tNONE\tNO_REVERSE_EDGE_PROVEN" in evidence
    assert "MOD-011" not in HANDOFF.read_text(encoding="utf-8")
    assert "MOD-011" not in GOV011.read_text(encoding="utf-8")


def test_eng007_reference_is_bidirectionally_declared_but_non_dependency():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "MOD-011\tENG-007\tREFERENCES\tDIRECT_SOURCE_REFERENCE" in evidence
    assert "ENG-007\tMOD-011\tREFERENCES\tDIRECT_SOURCE_REFERENCE" in evidence
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in ENG007.read_text(encoding="utf-8")
