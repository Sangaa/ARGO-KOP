from pathlib import Path

from Memory.Execution.runtime_result_persistence_adapter import persist_candidate, reread
from Runtime.Execution.execution_trace_producer import record_execution_trace


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "Memory/Execution/EXEC-001_RUNTIME_RESULT_PERSISTENCE_CONTRACT.md"


def _trace():
    result = record_execution_trace(
        trace_id="TRACE-P10-G",
        task_id="TASK-P10-G",
        session_id="SESSION-P10-G",
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "execution", "status": "SIMULATED"}],
        recorded_at="2026-09-03T00:00:00+00:00",
    )
    assert result["status"] == "TRACE_RECORDED"
    return result["trace"]


def test_runtime_trace_identity_and_status_survive_memory_boundary(tmp_path):
    trace = _trace()
    target = tmp_path / "trace.json"
    assert persist_candidate(trace, str(target)) == {
        "status": "PERSISTED",
        "path": str(target),
        "trace_id": "TRACE-P10-G",
    }
    loaded = reread(str(target))
    assert loaded["status"] == "RE_READ"
    for field in ("trace_id", "task_id", "session_id", "final_status", "side_effect"):
        assert loaded[field] == trace[field]


def test_incomplete_or_unknown_safety_trace_never_reaches_disk(tmp_path):
    trace = _trace()
    trace["task_id"] = ""
    target = tmp_path / "invalid.json"
    result = persist_candidate(trace, str(target))
    assert result["reason"] == "TRACE_IDENTITY_INCOMPLETE"
    assert not target.exists()

    trace = _trace()
    del trace["side_effect"]
    result = persist_candidate(trace, str(target))
    assert result == {"status": "HOLD", "reason": "SIDE_EFFECT_STATE_REQUIRED"}
    assert not target.exists()


def test_contract_prohibits_silent_safety_default_and_canonical_promotion():
    contract = CONTRACT.read_text(encoding="utf-8")
    assert "absent or unknown safety state must not be interpreted as side-effect-free" in contract
    assert "does not promote results into Knowledge" in contract
    assert "must not silently mutate canonical Memory" in contract
