from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Models" / "_FOLDER_STATUS.md"
QUEUE = ROOT / "Repository" / "REP-016_PHASE1_PARTITION_WORK_QUEUE.md"
MANIFEST = ROOT / "Repository" / "REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md"

BOUNDED = "CLOSED_FOR_PHASE_1 / BOUNDED MODELS PARTITION CERTIFIED / DOWNSTREAM AND GLOBAL HOLDS REMAIN"


def test_models_status_queue_and_manifest_bind_same_bounded_closure() -> None:
    status = STATUS.read_text(encoding="utf-8")
    queue = QUEUE.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert "Version: 1.3.8" in status
    assert f"Status: {BOUNDED}" in status
    assert f"| 12 | Models | {BOUNDED} | MOD-001/002/003/004/011 | Model authority + REP-011/014 |" in queue
    assert "Version: 1.3.2" in queue
    assert "| REP-016 | Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md | 1.3.2 | Active / Phase 1 Open / Integrity Hold | P11 + P12 BOUNDED PARTITIONS CLOSED / PHASE 1 OPEN |" in manifest
    assert "Priority 12 Models: `CLOSED_FOR_PHASE_1 / BOUNDED MODELS PARTITION CERTIFIED / DOWNSTREAM AND GLOBAL HOLDS REMAIN`" in manifest


def test_bounded_models_closure_preserves_nonpromotion_boundaries() -> None:
    status = STATUS.read_text(encoding="utf-8")
    queue = QUEUE.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert "Canonical: Pending consolidated validation" in status
    assert "does **not** promote the maturity/status of individual model artifacts" in status
    assert "Phase 1 overall closure" in status
    assert "Global Integrity" in status
    assert "Phase 1 repository work: `OPEN`" in manifest
    assert "Global integrity: `HOLD`" in manifest
    assert "Global `BOOTED / INTEGRITY PASS`: `NOT CLAIMED`" in manifest
    assert "does not start Priority 13 merely by changing the queue row" in queue


def test_queue_history_preservation_markers_survive_closure_binding() -> None:
    queue = QUEUE.read_text(encoding="utf-8")
    for marker in (
        "## P291 Regression Repair — 2026-08-16",
        "## P348 Current Control-Plane Evidence Binding — 2026-08-17",
        "## Current Checkpoint — 2026-09-05 Priority-11 Closure / Priority-12 Entry Sync",
        "## Current Checkpoint — 2026-09-05 Priority-12 Models Closure-State Binding",
        "End of REP-016",
    ):
        assert marker in queue


def test_closure_does_not_start_knowledge_priority() -> None:
    queue = QUEUE.read_text(encoding="utf-8")
    assert "| 13 | Knowledge | INVENTORYING | KNW-002/003/004/008/009 | Knowledge authority + REP-011/014 |" in queue
    assert "Only then may live `main` be rediscovered and the first legal open priority recomputed" in queue
