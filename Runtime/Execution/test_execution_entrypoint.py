import pytest

from execution_entrypoint import ExecutionDenied, execute


def test_execution_entrypoint_returns_canonical_trace_handoff():
    result = execute(
        execution_id="EXEC-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        source_trace_id="DECISION-TRACE-1",
        authorized=True,
        final_status="SUCCESS",
        stages=[{"name": "execute", "status": "SUCCESS"}],
    )
    assert result["execution_id"] == "EXEC-1"
    assert result["source_trace_id"] == "DECISION-TRACE-1"
    assert result["execution_trace_id"] == result["trace"]["trace_id"]
    assert result["trace"]["record_type"] == "EXECUTION_TRACE"


def test_execution_entrypoint_requires_authorization():
    with pytest.raises(ExecutionDenied, match="EXECUTION_NOT_AUTHORIZED"):
        execute(
            execution_id="EXEC-2",
            task_id="TASK-2",
            session_id="SESSION-2",
            source_trace_id="DECISION-TRACE-2",
            authorized=False,
            final_status="SUCCESS",
            stages=[{"name": "execute", "status": "SUCCESS"}],
        )


def test_execution_entrypoint_requires_source_trace():
    with pytest.raises(ValueError, match="SOURCE_TRACE_REQUIRED"):
        execute(
            execution_id="EXEC-3",
            task_id="TASK-3",
            session_id="SESSION-3",
            source_trace_id="",
            authorized=True,
            final_status="SUCCESS",
            stages=[{"name": "execute", "status": "SUCCESS"}],
        )


def test_execution_entrypoint_rejects_failed_trace_recording():
    with pytest.raises(ValueError, match="TRACE_RECORDING_FAILED"):
        execute(
            execution_id="EXEC-4",
            task_id="TASK-4",
            session_id="SESSION-4",
            source_trace_id="DECISION-TRACE-4",
            authorized=True,
            final_status="SUCCESS",
            stages=[],
        )
