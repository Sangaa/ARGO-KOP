from pathlib import Path


def test_rep011_current_session_addendum_exists_and_preserves_hold_boundary():
    root = Path(__file__).resolve().parents[2]
    addendum = root / "Repository/REP-011_P226_RECONCILIATION_ADDENDUM_2026-08-16.md"
    text = addendum.read_text(encoding="utf-8")
    assert "P216" in text and "P225" in text
    assert "PARTIALLY_RECONCILED / INTEGRITY HOLD" in text
    assert "RUN-010 -> SRV-009 remains below executable VERIFIED" in text


def test_rep011_addendum_does_not_claim_phase1_closure():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Repository/REP-011_P226_RECONCILIATION_ADDENDUM_2026-08-16.md").read_text(encoding="utf-8")
    assert "does not close Phase 1" in text
    assert "does not promote any relationship to VERIFIED" in text
