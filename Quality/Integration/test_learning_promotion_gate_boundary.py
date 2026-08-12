from learning_pipeline_integration import assess_for_promotion


def _outcome():
    return {
        "outcome_id": "OUT-PROMO-1",
        "result": "SUCCESS",
        "evidence_trace_ids": ["TRACE-1"],
        "execution_trace_ids": ["TRACE-1"],
        "confidence": "HIGH",
    }


def test_readiness_does_not_promote_knowledge():
    result = assess_for_promotion(
        decision_id="DEC-PROMO-1",
        execution_id="EXEC-PROMO-1",
        outcome=_outcome(),
    )

    assert result["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert result["stage"] == "READINESS"
    assert result["report"]["promotion_authority"] == "EXISTING_LEARNING_PROMOTION_GATE"
    assert result["report"]["knowledge_promoted"] is False


def test_readiness_never_claims_promotion_authority():
    result = assess_for_promotion(
        decision_id="DEC-PROMO-2",
        execution_id="EXEC-PROMO-2",
        outcome=_outcome(),
    )

    assert result["report"]["promotion_authority"] != "LEARNING_PIPELINE_INTEGRATION"
    assert result["report"]["knowledge_promoted"] is False
