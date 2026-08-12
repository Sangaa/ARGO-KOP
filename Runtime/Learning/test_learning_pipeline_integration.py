from learning_pipeline_integration import assess_for_promotion


def test_pipeline_reaches_readiness_without_promotion():
    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TR-1"],
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
            "confidence": "HIGH",
        },
    )
    assert result["status"] == "NOT_READY"
    assert result["stage"] == "EVALUATION"
