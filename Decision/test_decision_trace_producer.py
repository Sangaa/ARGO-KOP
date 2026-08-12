from decision_trace_producer import record_decision_trace


def test_decision_trace_producer_materializes_lineage():
    result = record_decision_trace(
        trace_id="DEC-TRACE-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        evidence_map=[{"type": "FACT", "claim": "verified"}],
        decision_status="NOT_EVALUATED",
    )
    assert result["status"] == "TRACE_RECORDED"
    assert result["trace"]["trace_id"] == "DEC-TRACE-1"
    assert result["trace"]["record_type"] == "DECISION_TRACE"


def test_decision_trace_producer_rejects_missing_evidence():
    result = record_decision_trace(
        trace_id="DEC-TRACE-2",
        task_id="TASK-2",
        session_id="SESSION-2",
        evidence_map=[],
        decision_status="NOT_EVALUATED",
    )
    assert result["status"] == "TRACE_REJECTED"
    assert "EVIDENCE_MAP_REQUIRED" in result["issues"]
