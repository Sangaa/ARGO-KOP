from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"
QUEUE_ADDENDUM = ROOT / "Repository" / "REP-016_PRIORITY7_CORE_CLOSURE_ADDENDUM_2026-09-01_X.md"


def test_closed_p7_control_plane_gaps_are_not_still_listed_as_open() -> None:
    text = STATUS.read_text(encoding="utf-8")

    assert "# Closed Priority-7 Control-Plane Gaps" in text
    assert "`REP-013` Core physical inventory representation — reconciled" in text
    assert "`REP-001` active Core inventory representation — reconciled" in text
    assert "`REP-002` Core physical map representation — reconciled" in text
    assert "`GOV-006` Core canonical parent/example — reconciled factually" in text

    assert "control-plane inventory drift and Governance naming/path discrepancy remain open" not in text
    assert "protected control-plane reconciliation for current Core representation" not in text


def test_priority7_current_state_is_explicit_bounded_closure() -> None:
    text = STATUS.read_text(encoding="utf-8")
    queue = QUEUE_ADDENDUM.read_text(encoding="utf-8")
    queue_semantic = queue.replace("**", "")

    assert "CLOSED_FOR_PHASE_1" in text
    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in text
    assert "CORE CERTIFIED" in text
    assert "VALIDATED-NOT-REGISTERED" in text
    assert "not a repository-wide complete-graph claim" in text
    assert "CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED" in text
    assert "CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE" in text

    assert "PRIORITY 7 = CLOSED_FOR_PHASE_1" in queue
    assert "GLOBAL PHASE 1 REMAINS OPEN" in queue
    assert "does not auto-start Priority 8" in queue_semantic
