from trace_inspector import inspect, project_history


def record(task="SYN-TASK-001", session="SYN-SESSION-001"):
    return {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-001",
        "task_id": task,
        "session_id": session,
        "final_status": "SIMULATED",
        "side_effect": False,
    }


def test_inspector_retrieves_history_without_activation():
    results = inspect([record(), record("OTHER")], task_id="SYN-TASK-001")
    assert len(results) == 1
    projected = project_history(results[0])
    assert projected["status"] == "HISTORICAL_ONLY"
    assert projected["active_context"] is False


def test_explicit_promotion_is_distinct():
    projected = project_history(record(), promote=True)
    assert projected["status"] == "PROMOTED"
    assert projected["active_context"] is True


def test_non_trace_record_is_rejected():
    result = project_history({"record_type": "CURRENT_STATE"})
    assert result["status"] == "HOLD"
