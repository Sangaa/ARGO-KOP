import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MOD011_RELATIONSHIP_EVIDENCE_2026-09-05_D.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_mod011_relationship_cohort_is_exact_and_current() -> None:
    rows = _rows()
    assert len(rows) == 7
    assert [row["candidate_id"] for row in rows] == [f"P12-D-{i:03d}" for i in range(1, 8)]
    for row in rows:
        assert (ROOT / row["source_path"]).is_file(), row
        assert (ROOT / row["target_path"]).is_file(), row


def test_existing_rel010_rel011_rel013_rel014_are_retained_only_when_current_text_supports_them() -> None:
    rows = {row["stable_rel_id"]: row for row in _rows() if row["stable_rel_id"] != "NONE"}
    assert rows["REL-010"]["controlled_type"] == "CONSUMES"
    assert rows["REL-011"]["controlled_type"] == "REFERENCES"
    assert rows["REL-013"]["controlled_type"] == "REFERENCES"
    assert rows["REL-014"]["controlled_type"] == "CONSUMES"
    assert all(rows[rel]["registry_action"] == "RETAIN_EXISTING" for rel in ("REL-010", "REL-011", "REL-013", "REL-014"))

    knw002 = (ROOT / "Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md").read_text(encoding="utf-8")
    knw009 = (ROOT / "Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md").read_text(encoding="utf-8")
    mod011 = (ROOT / "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md").read_text(encoding="utf-8")
    assert "Classification consumes those source and evidence semantics" in knw002
    assert "Knowledge evolution consumes those semantics" in knw009
    assert "Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md" in mod011
    assert "Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md" in mod011


def test_rel012_stable_id_is_reference_not_dependency_in_current_contract() -> None:
    row = next(row for row in _rows() if row["stable_rel_id"] == "REL-012")
    assert row["source_path"] == "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md"
    assert row["target_path"] == "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md"
    assert row["controlled_type"] == "REFERENCES"
    # The evidence surface records the pre-registration action boundary and is
    # preserved as provenance even after the later canonical write executes it.
    assert row["registry_action"] == "CORRECT_EXISTING_STABLE_ID_PENDING_SAFE_REGISTRY_WRITE"

    mod011 = (ROOT / row["source_path"]).read_text(encoding="utf-8")
    knw004 = (ROOT / row["target_path"]).read_text(encoding="utf-8")
    assert "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md" in mod011
    assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in knw004
    assert "source identity, provenance and evidence semantics" in knw004


def test_reverse_references_are_direct_and_not_manufactured_for_symmetry() -> None:
    candidates = [row for row in _rows() if row["stable_rel_id"] == "NONE"]
    assert {row["source_path"] for row in candidates} == {
        "Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md",
        "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md",
    }
    assert all(row["controlled_type"] == "REFERENCES" for row in candidates)
    assert all(row["registry_action"] == "REGISTRATION_CANDIDATE" for row in candidates)
    for row in candidates:
        source = (ROOT / row["source_path"]).read_text(encoding="utf-8")
        assert "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in source


def test_rel012_canonical_registry_matches_the_verified_current_contract() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    assert "| REL-012 | MOD-011 | KNW-004 | REFERENCES |" in registry
    assert "| REL-012 | MOD-011 | KNW-004 | DEPENDS_ON |" not in registry
    assert "STABLE-ID TYPE CORRECTION" in registry
