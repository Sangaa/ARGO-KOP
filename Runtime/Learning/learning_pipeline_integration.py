"""Integrate outcome evaluation, feedback quality, and readiness without promotion."""

from outcome_evaluator import evaluate_outcome
from feedback_quality_gate import assess_feedback_quality
from learning_readiness_report import build_readiness_report


def assess_for_promotion(*, decision_id: str, execution_id: str, outcome: dict) -> dict:
    evaluation = evaluate_outcome(
        decision_id=decision_id,
        execution_id=execution_id,
        outcome=outcome,
    )
    if evaluation["status"] != "EVALUATED":
        return {"status": "NOT_READY", "stage": "EVALUATION", "evaluation": evaluation}

    quality = assess_feedback_quality(evaluation=evaluation)
    if quality["status"] != "QUALITY_ASSESSED":
        return {"status": "NOT_READY", "stage": "QUALITY", "evaluation": evaluation, "quality": quality}

    report = build_readiness_report(evaluation=evaluation, quality=quality)
    return {
        "status": report["status"],
        "stage": "READINESS",
        "evaluation": evaluation,
        "quality": quality,
        "report": report,
    }
