from outcome_producer import record_execution_outcome


def test_outcome_producer_carries_execution_trace_lineage():
    result = record_execution_outcome(
        decision_id="DEC-1",
        execution={
            "execution_id": "EXEC-1",
            "execution_trace_id": "TR-1",
            "trace": {"final_status": "SUCCESS"},
        },
    )
    assert result["status"] == "OUTCOME_RECORDED"
    outcome = result["outcome"]
    assert outcome["evidence_trace_ids"] == ["TR-1"]
    assert outcome["execution_trace_ids"] == ["TR-1"]
    assert outcome["result"] == "SUCCESS"


def test_simulated_execution_is_not_promoted_to_success():
    result = record_execution_outcome(
        decision_id="DEC-2",
        execution={
            "execution_id": "EXEC-2",
            "execution_trace_id": "TR-2",
            "trace": {"final_status": "SIMULATED"},
        },
    )
    assert result["outcome"]["result"] == "INCONCLUSIVE"
    assert result["outcome"]["confidence"] == "UNKNOWN"


def test_outcome_requires_execution_trace():
    result = record_execution_outcome(
        decision_id="DEC-3",
        execution={
            "execution_id": "EXEC-3",
            "trace": {"final_status": "SUCCESS"},
        },
    )
    assert result["status"] == "OUTCOME_REJECTED"
    assert "EXECUTION_TRACE_REQUIRED" in result["issues"]
