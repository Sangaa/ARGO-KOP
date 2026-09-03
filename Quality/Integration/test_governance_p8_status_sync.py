from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Governance" / "_FOLDER_STATUS.md"
QUEUE = ROOT / "Repository" / "REP-016_PRIORITY8_GOVERNANCE_CLOSURE_ADDENDUM_2026-09-03_H.md"
CLOSURE = ROOT / "Repository" / "P8_GOVERNANCE_EXPLICIT_BOUNDED_CLOSURE_2026-09-03_H.md"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def test_priority8_current_state_is_explicit_bounded_closure() -> None:
    status = STATUS.read_text(encoding="utf-8")
    queue = QUEUE.read_text(encoding="utf-8")
    assert "CLOSED_FOR_PHASE_1 / BOUNDED GOVERNANCE PARTITION CERTIFIED" in status
    assert "GOVERNANCE PHYSICAL INVENTORY + ALLOCATION = 52 / 52 RECONCILED" in status
    assert "PRIORITY 8 = CLOSED_FOR_PHASE_1" in queue
    assert "GLOBAL PHASE 1 REMAINS OPEN" in queue
    assert "does not auto-start Priority 9" in queue


def test_rel011_is_preserved_as_nonblocking_not_promoted() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    closure = CLOSURE.read_text(encoding="utf-8")
    assert "| REL-011 | MOD-011 | KNW-003 | REFERENCES | Revalidation Required |" in registry
    assert "REL-011 is correctly typed `REFERENCES / Revalidation Required` and is non-blocking" in closure
    assert "REL-011 target revalidation remains Knowledge-domain work" in closure


def test_closure_preserves_global_nonclaims() -> None:
    status = STATUS.read_text(encoding="utf-8")
    queue = QUEUE.read_text(encoding="utf-8")
    closure = CLOSURE.read_text(encoding="utf-8")
    assert "PRIORITY 8 CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED" in status
    assert "GOVERNANCE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE" in status
    assert "BOUNDED INTEGRITY WORKFLOW PASS != GLOBAL INTEGRITY PASS" in status
    assert "Global Connected Baseline remains open" in queue
    assert "does not establish a complete repository graph" in closure
