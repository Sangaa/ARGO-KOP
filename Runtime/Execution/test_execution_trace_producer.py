from execution_trace_producer import record_execution_trace


def test_producer_materializes_canonical_trace():
    result = record_execution_trace(
        trace_id="TR-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        final_status="SUCCESS",
        side_effect=False,
        stages=[{"stage": "execution", "status": "SUCCESS"}],
        recorded_at="2026-08-12T12:00:00+00:00",
    )
    assert result["status"] == "TRACE_RECORDED"
    trace = result["trace"]
    assert trace["record_type"] == "EXECUTION_TRACE"
    assert trace["trace_id"] == "TR-1"
    assert trace["stages"]


def test_producer_rejects_missing_identity():
    result = record_execution_trace(
        trace_id="",
        task_id="TASK-1",
        session_id="SESSION-1",
        final_status="SUCCESS",
        side_effect=False,
        stages=[{"stage": "execution"}],
    )
    assert result["status"] == "TRACE_REJECTED"
    assert "TRACE_ID_REQUIRED" in result["issues"]


def test_producer_rejects_empty_stages():
    result = record_execution_trace(
        trace_id="TR-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        final_status="SUCCESS",
        side_effect=False,
        stages=[],
    )
    assert result["status"] == "TRACE_REJECTED"
    assert "STAGES_REQUIRED" in result["issues"]


def test_producer_does_not_create_authorization():
    result = record_execution_trace(
        trace_id="TR-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        final_status="SUCCESS",
        side_effect=True,
        stages=[{"stage": "execution", "status": "SUCCESS"}],
    )
    assert "authorization" not in result["trace"]
    assert "authorized" not in result["trace"]
