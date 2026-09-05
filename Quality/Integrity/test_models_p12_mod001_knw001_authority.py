from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOD001 = ROOT / "Models" / "MOD-001_KNOWLEDGE_MODEL.md"
KNW001 = ROOT / "Knowledge" / "KNW-001_KNOWLEDGE_MODEL.md"
EVIDENCE = ROOT / "Repository" / "REP-014_PRIORITY12_MOD001_KNW001_AUTHORITY_EVIDENCE_2026-09-05_J.tsv"


def test_mod001_is_semantic_schema_not_knowledge_domain_owner():
    text = MOD001.read_text(encoding="utf-8")
    assert "semantic knowledge-object/schema contract" in text
    assert "does **not** own Knowledge-domain scope classification" in text
    assert "SEMANTIC KNOWLEDGE SCHEMA AUTHORITY != KNOWLEDGE-DOMAIN OWNERSHIP != LIFECYCLE/PROMOTION AUTHORITY" in text


def test_knw001_retains_knowledge_domain_lifecycle_and_promotion_contract():
    text = KNW001.read_text(encoding="utf-8")
    assert "canonical knowledge model of ARGO KOP" in text
    assert "# Knowledge Domains" in text
    assert "# Knowledge Lifecycle" in text
    assert "# Cross-Domain Promotion" in text
    assert "# Knowledge Ownership Boundary" in text


def test_current_relationship_is_one_way_reference_only():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "MOD-001\tKNW-001\tREFERENCES\tAUTHORITY_BOUNDARY_REFERENCE" in evidence
    assert "KNW-001\tMOD-001\tNONE\tNO_REVERSE_EDGE_PROVEN" in evidence
    assert "MOD-001\tKNW-001\tDEPENDS_ON" not in evidence
    assert "KNW-001\tMOD-001\tDEPENDS_ON" not in evidence


def test_shared_knowledge_model_language_does_not_create_duplicate_authority():
    mod = MOD001.read_text(encoding="utf-8")
    knw = KNW001.read_text(encoding="utf-8")
    assert "Canonical: Yes" in mod
    assert "Canonical: Yes" in knw
    assert "`KNW-001` MUST NOT be treated as a duplicate or replacement" in mod
    assert "MOD-001" not in knw
    assert "NO_DUPLICATE_AUTHORITY" in EVIDENCE.read_text(encoding="utf-8")
