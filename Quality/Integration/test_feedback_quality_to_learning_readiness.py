"""Direct seam test: Feedback Quality -> Learning Readiness."""

from Runtime.Learning.learning_pipeline_integration import assess_for_promotion


def test_feedback_quality_propagates_to_learning_readiness_without_promotion():
    outcome = {
        "result": "success",
        "evidence_trace_ids": ["trace-feedback-readiness-001"],
        "confidence": 0.95,
    }

    report = assess_for_promotion(outcome)

    assert report["readiness"] is True
    assert report["feedback_quality"]["accepted"] is True
    assert report["evidence_trace_ids"] == ["trace-feedback-readiness-001"]
    assert report["knowledge_promoted"] is False


def test_feedback_quality_failure_blocks_learning_readiness():
    outcome = {
        "result": "success",
        "evidence_trace_ids": [],
        "confidence": 0.95,
    }

    report = assess_for_promotion(outcome)

    assert report["readiness"] is False
    assert report["feedback_quality"]["accepted"] is False
    assert report["knowledge_promoted"] is False
