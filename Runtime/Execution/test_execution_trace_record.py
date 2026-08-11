from execution_trace_record import build_trace_record


def test_trace_record_is_inspectable_and_preserves_safety_state():
    result = {
        "task_id": "SYN-TASK-001",
        "final_status": "SIMULATED",
        "stages": [
            {"status": "READY"},
            {"status": "SIMULATED", "side_effect": False},
        ],
    }
    record = build_trace_record(result, session_id="SYN-SESSION-001")
    assert record["record_type"] == "EXECUTION_TRACE"
    assert record["task_id"] == "SYN-TASK-001"
    assert record["final_status"] == "SIMULATED"
    assert record["side_effect"] is False
    assert record["stages"] == result["stages"]


def test_incomplete_result_fails_closed():
    record = build_trace_record({"task_id": "SYN-TASK-001"}, session_id="SYN-SESSION-001")
    assert record["status"] == "HOLD"
