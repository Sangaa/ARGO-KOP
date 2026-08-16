from pathlib import Path


def test_historical_memory_preserves_temporal_and_provenance_boundary():
    root = Path(__file__).resolve().parents[2]
    readme = (root / "Memory/Historical_Memory/README.md").read_text(encoding="utf-8")
    provenance = (root / "Memory/Historical_Memory/HM-002_PROVENANCE_AND_TEMPORAL_CONTEXT.md").read_text(encoding="utf-8")
    transition = (root / "Memory/Historical_Memory/HM-004_HISTORICAL_TO_CURRENT_TRANSITION.md").read_text(encoding="utf-8")
    assert "Historical Record ≠ Current Fact ≠ Current Authority" in readme
    assert "Provenance strengthens traceability; it does not itself establish correctness or authority." in provenance
    assert "Current Authority (only after applicable approval)" in transition


def test_historical_memory_candidate_status_does_not_certify_current_authority():
    root = Path(__file__).resolve().parents[2]
    master_index = (root / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    assert "Memory/Historical_Memory/README.md" in master_index
    assert "Candidate / Integrity Hold" in master_index
    assert "preserve historical evidence without silently promoting it to current authority" in master_index
