"""Direct seam test: Feedback Quality -> Learning Readiness."""

from execution_entrypoint import execute
from learning_pipeline_integration import assess_for_promotion


def test_feedback_quality_propagates_to_learning_readiness_without_promotion():
    execution = execute(
        execution_id="EXEC-FEEDBACK-READINESS-001",
        task_id="TASK-FEEDBACK-READINESS-001",
        session_id="SESSION-FEEDBACK-READINESS-001",
        source_trace_id="DECISION-TRACE-FEEDBACK-001",
        authorized=True,
        final_status="SUCCESS",
        stages=[{"name": "execute", "status": "SUCCESS"}],
    )
    trace_id = execution["execution_trace_id"]

    report = assess_for_promotion(
        decision_id="DEC-FEEDBACK-READINESS-001",
        execution_id=execution["execution_id"],
        outcome={
            "outcome_id": "OUT-FEEDBACK-READINESS-001",
            "result": "SUCCESS",
            "evidence_trace_ids": [trace_id],
            "execution_trace_ids": [trace_id],
            "confidence": "HIGH",
        },
    )

    assert report["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert report["stage"] == "READINESS"
    assert report["quality"]["status"] == "QUALITY_ASSESSED"
    assert report["quality"]["learning_ready"] is True
    assert report["report"]["evidence_trace_ids"] == [trace_id]
    assert report["report"]["knowledge_promoted"] is False


def test_feedback_quality_failure_blocks_learning_readiness():
    report = assess_for_promotion(
        decision_id="DEC-FEEDBACK-READINESS-002",
        execution_id="EXEC-FEEDBACK-READINESS-002",
        outcome={
            "outcome_id": "OUT-FEEDBACK-READINESS-002",
            "result": "SUCCESS",
            "evidence_trace_ids": [],
            "execution_trace_ids": [],
            "confidence": "HIGH",
        },
    )

    assert report["status"] == "NOT_READY"
    assert report["stage"] == "EVALUATION"
    assert report["evaluation"]["status"] == "EVALUATION_REJECTED"
