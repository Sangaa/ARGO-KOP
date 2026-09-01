from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_closed_p7_control_plane_gaps_are_not_still_listed_as_open() -> None:
    text = STATUS.read_text(encoding="utf-8")

    assert "# Closed Priority-7 Control-Plane Gaps" in text
    assert "`REP-013` Core physical inventory representation — reconciled" in text
    assert "`REP-001` active Core inventory representation — reconciled" in text
    assert "`REP-002` Core physical map representation — reconciled" in text
    assert "`GOV-006` Core canonical parent/example — reconciled factually" in text

    assert "control-plane inventory drift and Governance naming/path discrepancy remain open" not in text
    assert "protected control-plane reconciliation for current Core representation" not in text


def test_remaining_priority7_boundary_tracks_current_readiness_state() -> None:
    text = STATUS.read_text(encoding="utf-8")

    assert "CROSS-LAYER VALIDATION OPEN" in text
    assert "CERTIFICATION REVIEW READY" in text
    assert "VALIDATED-NOT-REGISTERED" in text
    assert "not a complete graph" in text
    assert "explicit final Core certification decision" in text
    assert "Priority 7 remains OPEN" in text
    assert "No Phase-1 closure, repository-wide graph completion, or Global Connected Baseline PASS is implied" in text

    # Pre-readiness remaining-work literals must not be treated as permanent closure gates.
    assert "continued dependency and consumer validation for remaining material Core authority relationships" not in text
    assert "REP-014 relationship-registry reconciliation" not in text
