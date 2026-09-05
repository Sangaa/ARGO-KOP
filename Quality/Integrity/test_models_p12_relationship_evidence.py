import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv"
ARC006 = ROOT / "Architecture" / "ARC-006_DEPENDENCY_MODEL.md"
MOD004 = ROOT / "Models" / "MOD-004_MEMORY_MODEL.md"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_models_relationship_evidence_is_exact_bounded_cohort() -> None:
    rows = _rows()
    assert len(rows) == 18
    assert [row["candidate_id"] for row in rows] == [f"P12-BR-{i:03d}" for i in range(1, 19)]
    assert {row["controlled_type"] for row in rows} == {"REFERENCES", "DEPENDS_ON", "NONE"}


def test_every_candidate_has_current_source_target_and_direct_source_text() -> None:
    for row in _rows():
        source = ROOT / row["source_path"]
        target = ROOT / row["target_path"]
        assert source.is_file(), row
        assert target.is_file(), row
        source_text = source.read_text(encoding="utf-8")
        assert f"`{row['target_path']}`" in source_text, row
        assert row["source_state"] == "DIRECT_SOURCE_AND_TARGET_VERIFIED", row


def test_related_documents_are_bounded_reference_registration_candidates() -> None:
    rows = [
        row
        for row in _rows()
        if row["source_section"] == "Related Documents"
    ]
    assert len(rows) == 9
    for row in rows:
        assert row["controlled_type"] == "REFERENCES", row
        assert row["authority_disposition"] == "DOCUMENTARY_REFERENCE_BOUNDED", row
        assert row["registry_action"] == "REGISTRATION_CANDIDATE", row


def test_memory_model_semantic_dependencies_are_model_composition_only() -> None:
    rows = [
        row
        for row in _rows()
        if row["source_path"] == "Models/MOD-004_MEMORY_MODEL.md"
        and row["source_section"] == "Semantic Dependencies"
    ]
    assert len(rows) == 3
    assert {row["target_path"] for row in rows} == {
        "Models/MOD-002_ENTITY_MODEL.md",
        "Models/MOD-003_DOCUMENT_MODEL.md",
        "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
    }
    assert all(row["controlled_type"] == "DEPENDS_ON" for row in rows)
    assert all(row["authority_disposition"] == "SEMANTIC_MODEL_COMPOSITION_QUALIFIED" for row in rows)
    assert all(row["registry_action"] == "REGISTRATION_CANDIDATE" for row in rows)


def test_architecture_review_artifacts_are_references_not_dependencies() -> None:
    rows = [
        row
        for row in _rows()
        if row["source_section"] == "Related Authority and Evolution References"
    ]
    assert {row["target_path"] for row in rows} == {
        "Architecture/ARC-009_ARCHITECTURE_DECISIONS.md",
        "Architecture/ARC-010_EVOLUTION_MODEL.md",
    }
    assert all(row["controlled_type"] == "REFERENCES" for row in rows)
    assert all(row["registry_action"] == "REGISTRATION_CANDIDATE" for row in rows)


def test_runtime_engine_are_ripple_targets_not_memory_model_dependencies() -> None:
    ripple_targets = {
        "Runtime/RUN-004_CONTEXT_LOADING.md",
        "Runtime/RUN-008_RUNTIME_STATE.md",
        "Runtime/RUN-009_RECOVERY.md",
        "Engine/ENG-007_LEARNING_ENGINE.md",
    }
    rows = [row for row in _rows() if row["target_path"] in ripple_targets]
    assert {row["target_path"] for row in rows} == ripple_targets
    assert all(row["source_section"] == "Downstream Consumers / Revalidation Targets" for row in rows)
    assert all(row["controlled_type"] == "NONE" for row in rows)
    assert all(row["authority_disposition"] == "RIPPLE_REVIEW_TARGET_NON_DEPENDENCY" for row in rows)
    assert all(row["registry_action"] == "DO_NOT_REGISTER" for row in rows)

    mod004 = MOD004.read_text(encoding="utf-8")
    assert "These are consumer/ripple-review targets, not Memory Model dependencies." in mod004
    assert "SEMANTIC DEPENDENCY != RELATED AUTHORITY != DOWNSTREAM CONSUMER != REVALIDATION TARGET" in mod004

    arc006 = ARC006.read_text(encoding="utf-8")
    assert "Dependencies must not reverse this direction unless explicitly authorized" in arc006
    assert "A textual reference to a file path does not by itself establish an architectural dependency." in arc006


def test_reconstruction_reference_is_not_promoted_to_dependency() -> None:
    assert not any(
        row["target_path"] == "Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md"
        and row["controlled_type"] == "DEPENDS_ON"
        for row in _rows()
    )
