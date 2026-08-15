"""Direct seam test: Outcome Evaluation -> Feedback Quality."""

from execution_entrypoint import execute
from feedback_quality_gate import assess_feedback_quality
from outcome_evaluator import evaluate_outcome


def test_outcome_evaluation_feeds_feedback_quality():
    execution = execute(
        execution_id="EXEC-OUTCOME-QUALITY-001",
        task_id="TASK-OUTCOME-QUALITY-001",
        session_id="SESSION-OUTCOME-QUALITY-001",
        source_trace_id="DECISION-TRACE-OUTCOME-QUALITY-001",
        authorized=True,
        final_status="SUCCESS",
        stages=[{"name": "execute", "status": "SUCCESS"}],
    )
    trace_id = execution["execution_trace_id"]

    evaluation = evaluate_outcome(
        decision_id="DEC-OUTCOME-QUALITY-001",
        execution_id=execution["execution_id"],
        outcome={
            "outcome_id": "OUT-OUTCOME-QUALITY-001",
            "result": "SUCCESS",
            "evidence_trace_ids": [trace_id],
            "execution_trace_ids": [trace_id],
            "confidence": "HIGH",
        },
    )
    quality = assess_feedback_quality(evaluation=evaluation)

    assert evaluation["status"] == "EVALUATED"
    assert quality["status"] == "QUALITY_ASSESSED"
    assert quality["quality"] == "ACCEPTABLE"
    assert quality["learning_ready"] is True


def test_invalid_outcome_does_not_reach_feedback_quality_as_valid():
    evaluation = evaluate_outcome(
        decision_id="DEC-OUTCOME-QUALITY-002",
        execution_id="EXEC-OUTCOME-QUALITY-002",
        outcome={
            "outcome_id": "OUT-OUTCOME-QUALITY-002",
            "result": "INVALID",
            "evidence_trace_ids": ["trace-invalid-002"],
            "execution_trace_ids": ["trace-invalid-002"],
            "confidence": "HIGH",
        },
    )
    quality = assess_feedback_quality(evaluation=evaluation)

    assert evaluation["status"] == "EVALUATION_REJECTED"
    assert quality["status"] == "QUALITY_REJECTED"
    assert "OUTCOME_NOT_EVALUATED" in quality["issues"]
