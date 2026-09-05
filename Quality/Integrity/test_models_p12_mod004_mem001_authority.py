from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOD004 = ROOT / "Models" / "MOD-004_MEMORY_MODEL.md"
MEM001 = ROOT / "Memory" / "MEM-001_MEMORY_MODEL.md"
EVIDENCE = ROOT / "Repository" / "REP-014_PRIORITY12_MOD004_MEM001_AUTHORITY_EVIDENCE_2026-09-05_I.tsv"


def test_mod004_is_semantic_schema_not_memory_domain_owner():
    text = MOD004.read_text(encoding="utf-8")
    assert "semantic object/schema contract" in text
    assert "does **not** own the Memory domain's operational taxonomy" in text
    assert "SEMANTIC SCHEMA AUTHORITY != MEMORY-DOMAIN OWNERSHIP != PROMOTION AUTHORITY" in text


def test_mem001_retains_memory_domain_and_promotion_contract():
    text = MEM001.read_text(encoding="utf-8")
    assert "canonical memory model of ARGO KOP" in text
    assert "Platform Memory" in text
    assert "User Memory" in text
    assert "Project / Deployment Memory" in text
    assert "# Promotion Rule" in text


def test_current_relationship_is_one_way_reference_only():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "MOD-004\tMEM-001\tREFERENCES\tAUTHORITY_BOUNDARY_REFERENCE" in evidence
    assert "MEM-001\tMOD-004\tNONE\tNO_REVERSE_EDGE_PROVEN" in evidence
    assert "MOD-004\tMEM-001\tDEPENDS_ON" not in evidence
    assert "MEM-001\tMOD-004\tDEPENDS_ON" not in evidence


def test_shared_title_does_not_recreate_duplicate_authority():
    mod = MOD004.read_text(encoding="utf-8")
    mem = MEM001.read_text(encoding="utf-8")
    assert "# MEMORY MODEL" in mod
    assert "# MEMORY MODEL" in mem
    assert "`MEM-001` MUST NOT be treated as a duplicate" in mod
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "NO_DUPLICATE_AUTHORITY" in evidence
