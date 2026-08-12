from feedback_quality_gate import assess_feedback_quality


def evaluation(result="SUCCESS", confidence="HIGH"):
    return {
        "status": "EVALUATED",
        "result": result,
        "evidence_trace_ids": ["TR-1"],
        "confidence": confidence,
    }


def test_high_confidence_evaluation_is_learning_ready():
    result = assess_feedback_quality(evaluation=evaluation())
    assert result["quality"] == "ACCEPTABLE"
    assert result["learning_ready"] is True


def test_low_confidence_is_not_learning_ready():
    result = assess_feedback_quality(evaluation=evaluation(confidence="LOW"))
    assert result["quality"] == "INSUFFICIENT"
    assert result["learning_ready"] is False


def test_inconclusive_is_not_learning_ready():
    result = assess_feedback_quality(evaluation=evaluation(result="INCONCLUSIVE"))
    assert result["learning_ready"] is False


def test_missing_evidence_is_rejected():
    result = assess_feedback_quality(evaluation={
        "status": "EVALUATED",
        "result": "SUCCESS",
        "evidence_trace_ids": [],
        "confidence": "HIGH",
    })
    assert result["status"] == "QUALITY_REJECTED"
    assert "OUTCOME_EVIDENCE_REQUIRED" in result["issues"]


def test_unassessed_outcome_is_rejected():
    result = assess_feedback_quality(evaluation={
        "status": "UNASSESSED",
        "result": "SUCCESS",
        "evidence_trace_ids": ["TR-1"],
        "confidence": "HIGH",
    })
    assert "OUTCOME_NOT_EVALUATED" in result["issues"]
