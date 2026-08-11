from context_history_bridge import load_historical


def test_history_is_labeled_and_not_active():
    records = [{
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-001",
        "task_id": "SYN-TASK-001",
        "session_id": "SYN-SESSION-001",
        "final_status": "SIMULATED",
        "side_effect": False,
    }]
    result = load_historical(records, task_id="SYN-TASK-001")
    assert result["status"] == "HISTORICAL_CONTEXT_READY"
    assert result["active_context"] is False
    assert result["promotion_status"] == "NOT_PROMOTED"
    assert len(result["historical_evidence"]) == 1


def test_missing_history_is_explicit():
    result = load_historical([], task_id="UNKNOWN")
    assert result["status"] == "NO_HISTORY"
    assert result["active_context"] is False
