from pathlib import Path


def test_materialized_session_handoff_has_explicit_transfer_and_ingestion_states():
    root = Path(__file__).resolve().parents[2]
    template = (root / "Memory/Engineering_Journal/SESSION_LEARNING_HANDOFF_TEMPLATE.md").read_text(encoding="utf-8")
    assert "Handoff Status: COMPLETE / PENDING / FAILED / BLOCKED" in template
    assert "Status: NOT STARTED / UNDER REVIEW / ACCEPTED / REJECTED / DEFERRED / APPLIED" in template
    assert "A handoff is not ingestion, and ingestion is not canonical promotion." in template


def test_current_session_does_not_claim_handoff_or_ingestion_without_material_record():
    root = Path(__file__).resolve().parents[2]
    candidates = list((root / "Memory/Engineering_Journal").glob("*SESSION_LEARNING_HANDOFF*.md"))
    concrete = [p for p in candidates if p.name != "SESSION_LEARNING_HANDOFF_TEMPLATE.md"]
    assert not concrete, "a concrete handoff must contain explicit destination/status evidence before being treated as materialized"
