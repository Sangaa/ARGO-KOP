from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "Specifications" / "01-Knowledge-Organization.md"
MOD001 = ROOT / "Models" / "MOD-001_KNOWLEDGE_MODEL.md"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
EVIDENCE = ROOT / "Repository" / "REP-014_PRIORITY12_SPEC_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_L.tsv"


def test_rel001_remains_bounded_dependency_from_current_authority_evidence() -> None:
    spec = SPEC.read_text(encoding="utf-8")
    mod001 = MOD001.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")

    assert "Canonical Models applicable to the knowledge object" in spec
    assert "This Specification" in spec
    assert "Specifications/01-Knowledge-Organization.md" in mod001
    assert "does not override the canonical knowledge schema" in mod001
    assert "| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | Revalidated within inspected authority scope |" in registry


def test_generic_model_authority_does_not_manufacture_concrete_edges() -> None:
    spec = SPEC.read_text(encoding="utf-8")
    evidence = EVIDENCE.read_text(encoding="utf-8")

    for model_id in ("MOD-002", "MOD-003", "MOD-004", "MOD-011"):
        assert model_id not in spec
        assert f"SPEC-001-KNOWLEDGE-ORGANIZATION\t{model_id}" in evidence
        assert "DO_NOT_REGISTER" in evidence


def test_reverse_mod001_reference_has_independent_source_evidence() -> None:
    mod001 = MOD001.read_text(encoding="utf-8")
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "Specifications/01-Knowledge-Organization.md" in mod001
    assert "MOD-001\tSPEC-001-KNOWLEDGE-ORGANIZATION" in evidence
    assert "REFERENCES\tDIRECT_SOURCE_CANDIDATE" in evidence
