from execution_trace_producer import record_execution_trace
from learning_pipeline_integration import assess_for_promotion


def test_pipeline_reaches_readiness_without_promotion():
    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TR-1"],
            "execution_trace_ids": ["TR-1"],
            "confidence": "HIGH",
        },
    )
    assert result["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert result["report"]["knowledge_promoted"] is False


def test_pipeline_stops_on_weak_quality():
    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-2",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TR-2"],
            "execution_trace_ids": ["TR-2"],
            "confidence": "LOW",
        },
    )
    assert result["status"] == "NOT_READY"
    assert result["stage"] == "READINESS"
    assert result["quality"]["learning_ready"] is False


def test_pipeline_stops_on_invalid_outcome():
    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-3",
            "result": "GUESS",
            "evidence_trace_ids": ["TR-3"],
            "execution_trace_ids": ["TR-3"],
            "confidence": "HIGH",
        },
    )
    assert result["status"] == "NOT_READY"
    assert result["stage"] == "EVALUATION"


def test_pipeline_rejects_orphaned_outcome_evidence():
    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-4",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TR-4"],
            "execution_trace_ids": ["TR-5"],
            "confidence": "HIGH",
        },
    )
    assert result["status"] == "NOT_READY"
    assert result["stage"] == "EVALUATION"
    assert "OUTCOME_PROVENANCE_BROKEN" in result["evaluation"]["issues"]


def test_produced_execution_trace_can_feed_outcome_pipeline():
    trace_result = record_execution_trace(
        trace_id="TR-PRODUCED-1",
        task_id="TASK-1",
        session_id="SESSION-1",
        final_status="SUCCESS",
        side_effect=False,
        stages=[{"stage": "execution", "status": "SUCCESS"}],
        recorded_at="2026-08-12T12:00:00+00:00",
    )
    assert trace_result["status"] == "TRACE_RECORDED"
    trace_id = trace_result["trace"]["trace_id"]

    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-PRODUCED-1",
            "result": "SUCCESS",
            "evidence_trace_ids": [trace_id],
            "execution_trace_ids": [trace_id],
            "confidence": "HIGH",
        },
    )
    assert result["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert result["evaluation"]["execution_trace_ids"] == [trace_id]
