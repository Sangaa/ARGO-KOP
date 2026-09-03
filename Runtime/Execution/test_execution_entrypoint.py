import pytest

from execution_entrypoint import ExecutionDenied, execute


def _execute(**overrides):
    values = {
        "execution_id": "EXEC-1",
        "task_id": "TASK-1",
        "session_id": "SESSION-1",
        "source_trace_id": "DECISION-TRACE-1",
        "authorized": True,
        "final_status": "SUCCESS",
        "stages": [{"name": "execute", "status": "SUCCESS"}],
    }
    values.update(overrides)
    return execute(**values)


def test_execution_entrypoint_returns_canonical_trace_handoff():
    result = _execute()
    assert result["execution_id"] == "EXEC-1"
    assert result["source_trace_id"] == "DECISION-TRACE-1"
    assert result["execution_trace_id"] == result["trace"]["trace_id"]
    assert result["trace"]["record_type"] == "EXECUTION_TRACE"


@pytest.mark.parametrize("authorization", [False, 1, "yes", object()])
def test_execution_entrypoint_requires_exact_boolean_authorization(authorization):
    with pytest.raises(ExecutionDenied, match="EXECUTION_NOT_EXPLICITLY_AUTHORIZED"):
        _execute(authorized=authorization)


@pytest.mark.parametrize(
    "field",
    ["execution_id", "task_id", "session_id", "source_trace_id"],
)
def test_execution_entrypoint_requires_stable_identity(field):
    with pytest.raises(ValueError, match="EXECUTION_IDENTITY_REQUIRED"):
        _execute(**{field: "   "})


def test_execution_entrypoint_rejects_failed_trace_recording():
    with pytest.raises(ValueError, match="TRACE_RECORDING_FAILED"):
        _execute(stages=[])
