"""Direct integration proof for evaluated outcome -> feedback quality gate."""

from Runtime.Learning.feedback_quality_gate import assess_feedback_quality


def _evaluation(**overrides):
    value = {
        "status": "EVALUATED",
        "result": "SUCCESS",
        "evidence_trace_ids": ["TRACE-INTEGRATION-QUALITY-001"],
        "confidence": "HIGH",
    }
    value.update(overrides)
    return value


def test_evaluated_outcome_with_trace_and_confidence_is_learning_ready():
    result = assess_feedback_quality(evaluation=_evaluation())

    assert result == {
        "status": "QUALITY_ASSESSED",
        "quality": "ACCEPTABLE",
        "learning_ready": True,
        "issues": [],
    }


def test_missing_outcome_evidence_is_rejected():
    result = assess_feedback_quality(evaluation=_evaluation(evidence_trace_ids=[]))

    assert result["status"] == "QUALITY_REJECTED"
    assert result["quality"] == "INSUFFICIENT"
    assert result["learning_ready"] is False
    assert "OUTCOME_EVIDENCE_REQUIRED" in result["issues"]


def test_low_confidence_never_becomes_learning_ready():
    result = assess_feedback_quality(evaluation=_evaluation(confidence="LOW"))

    assert result["status"] == "QUALITY_ASSESSED"
    assert result["quality"] == "INSUFFICIENT"
    assert result["learning_ready"] is False


def test_inconclusive_outcome_is_not_learning_ready():
    result = assess_feedback_quality(evaluation=_evaluation(result="INCONCLUSIVE"))

    assert result["status"] == "QUALITY_ASSESSED"
    assert result["quality"] == "ACCEPTABLE"
    assert result["learning_ready"] is False
