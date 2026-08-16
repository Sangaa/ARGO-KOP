from pathlib import Path


def test_service_reverse_edge_states_remain_bounded_by_available_evidence():
    root = Path(__file__).resolve().parents[2]
    journal = (root / "Memory/Engineering_Journal/EJR-179_2026-08-14_SERVICE_REVERSE_EDGE_REVIEW.md").read_text(encoding="utf-8")
    matrix = (root / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(encoding="utf-8")

    assert "documentation reciprocity should be represented as `PARTIALLY_VERIFIED`" in journal
    assert "SRV-006 ↔ SRV-007" in journal
    assert "SRV-007 ↔ SRV-008" in journal
    assert "SRV-008 ↔ SRV-009" in journal
    assert "runtime/operational coupling" in journal
    assert "PARTIALLY_VERIFIED" in matrix


def test_service_reverse_edge_review_does_not_claim_executable_runtime_coupling():
    root = Path(__file__).resolve().parents[2]
    journal = (root / "Memory/Engineering_Journal/EJR-179_2026-08-14_SERVICE_REVERSE_EDGE_REVIEW.md").read_text(encoding="utf-8")
    assert "runtime/operational coupling" in journal
    assert "until implementation/runtime evidence is available" in journal
