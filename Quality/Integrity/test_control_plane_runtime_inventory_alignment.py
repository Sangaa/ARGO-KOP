from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "Repository/REP-001_MASTER_INDEX.md"
MAP = ROOT / "Repository/REP-002_REPOSITORY_MAP.md"
RUNTIME_STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"

CURRENT_RUNTIME_CANDIDATES = {
    "RUN-011": "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md",
    "RUN-012": "Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md",
    "RUN-013": "Runtime/RUN-013_CONTROLLED_HANDOFF.md",
    "RUN-014": "Runtime/RUN-014_LEARNING_PROMOTION_TEST.md",
    "RUN-015": "Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md",
}

STALE_RUNTIME_PATHS = {
    "Runtime/RUN-011_COGNITIVE_EXECUTION_TARGET.md",
    "Runtime/RUN-012_COGNITIVE_CONTEXT_HANDOFF.md",
    "Runtime/RUN-013_COGNITIVE_DECISION_GATE.md",
    "Runtime/RUN-014_COGNITIVE_TRACE_TARGET.md",
    "Runtime/RUN-015_COGNITIVE_ACCEPTANCE_TARGET.md",
}


def test_current_runtime_candidate_paths_are_present_in_both_control_plane_surfaces():
    index = INDEX.read_text(encoding="utf-8")
    mapping = MAP.read_text(encoding="utf-8")
    for run_id, path in CURRENT_RUNTIME_CANDIDATES.items():
        assert (ROOT / path).is_file(), f"missing physical Runtime candidate: {path}"
        assert path in index, f"missing current Runtime path from REP-001: {path}"
        assert path in mapping, f"missing current Runtime path from REP-002: {path}"
        assert run_id in index
        assert run_id in mapping


def test_known_stale_runtime_candidate_paths_are_not_active_control_plane_inventory():
    index = INDEX.read_text(encoding="utf-8")
    mapping = MAP.read_text(encoding="utf-8")
    for stale_path in STALE_RUNTIME_PATHS:
        assert stale_path not in index, f"stale Runtime path remains in REP-001: {stale_path}"
        assert stale_path not in mapping, f"stale Runtime path remains in REP-002: {stale_path}"


def test_runtime_status_agrees_with_current_candidate_scope_and_authority_boundary():
    status = RUNTIME_STATUS.read_text(encoding="utf-8")
    for run_id in CURRENT_RUNTIME_CANDIDATES:
        assert run_id in status
    assert "CROSS-LAYER INTEGRATION HOLD" in status
    assert "prototype evidence" in status
    assert "global Runtime certification" in status


# Bounded guard only. It does not certify repository-wide inventory completeness,
# Runtime implementation, or Phase 1 closure.
