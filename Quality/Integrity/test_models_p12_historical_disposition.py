from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODELS = ROOT / "Models"
README = MODELS / "README.md"
STATUS = MODELS / "_FOLDER_STATUS.md"

HISTORICAL_IDS = {
    "MOD-005",
    "MOD-006",
    "MOD-007",
    "MOD-008",
    "MOD-009",
    "MOD-010",
}


def test_historical_ids_are_not_recreated_as_current_model_files() -> None:
    current = {path.name for path in MODELS.glob("MOD-*.md")}
    for model_id in HISTORICAL_IDS:
        assert not any(name.startswith(model_id + "_") for name in current), model_id


def test_readme_records_current_non_recreation_dispositions() -> None:
    text = README.read_text(encoding="utf-8")
    required = {
        "MOD-005_KNOWLEDGE_MODEL.md": "COVERED / NO DISTINCT GAP PROVEN",
        "MOD-006_RUNTIME_MODEL.md": "COVERED BY CURRENT RUNTIME AUTHORITY / NO RECREATE",
        "MOD-007_SERVICE_MODEL.md": "COVERED BY CURRENT SERVICES AUTHORITY / NO RECREATE",
        "MOD-008_RELATIONSHIP_MODEL.md": "OVERLAP / NO DISTINCT MODEL GAP PROVEN",
        "MOD-009_VERSION_MODEL.md": "AUTHORITY COLLISION AVOIDED / NO RECREATE",
        "MOD-010_MODEL_REFERENCE.md": "NAVIGATION/REFERENCE COVERED / NO RECREATE",
    }
    for historical_name, disposition in required.items():
        assert historical_name in text
        assert disposition in text
    assert "MISSING HISTORICAL FILE != MISSING CURRENT CONCEPT" in text
    assert "HISTORICAL IDENTIFIER != CURRENT AUTHORITY" in text


def test_status_marks_numeric_restoration_resolved_with_bounded_partition_closure() -> None:
    text = STATUS.read_text(encoding="utf-8")
    assert "numeric restoration disposition resolved / no blind recreation" in text.lower()
    assert "CLOSED_FOR_PHASE_1 / BOUNDED MODELS PARTITION CERTIFIED / DOWNSTREAM AND GLOBAL HOLDS REMAIN" in text
    assert "Canonical relationship registry synchronization complete / REP-014 v1.2.20" in text
    assert "relationship registry synchronization remains open" not in text
    assert "BOUNDED MODELS PARTITION CLOSURE != DOWNSTREAM PARTITION CERTIFICATION != GLOBAL CONNECTED BASELINE != GLOBAL INTEGRITY PASS" in text


def test_bounded_closure_does_not_promote_individual_models_or_global_state() -> None:
    text = STATUS.read_text(encoding="utf-8")
    assert "MOD-001_KNOWLEDGE_MODEL.md" in text and "Integrity Hold / Relationship-Revalidated" in text
    assert "MOD-002_ENTITY_MODEL.md" in text and "Approved / Revalidation Required" in text
    assert "MOD-003_DOCUMENT_MODEL.md" in text and "Approved / Revalidation Required" in text
    assert "MOD-004_MEMORY_MODEL.md" in text and "Approved / Revalidation Required" in text
    assert "MOD-011_KNOWLEDGE_SOURCE_MODEL.md" in text and "Proposed / Future-Ready / Revalidated" in text
    assert "Phase 1 overall closure" in text
    assert "Global Integrity" in text
    assert "PARTITION CLOSURE != TRANSACTION CLOSURE != PHASE-1 CLOSURE != GLOBAL CLOSURE" in text


def test_future_model_requires_current_semantic_gap_not_historical_number() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "distinct semantic responsibility, owner, authority boundary and material consumer need" in readme
    assert "a historical identifier is not automatically inherited" in readme
