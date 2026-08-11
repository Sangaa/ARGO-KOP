"""Gate decision outcome feedback before it can influence learning."""


def evaluate_outcome(*, decision_id: str, execution_id: str,
                     outcome: dict) -> dict:
    issues = []
    if not decision_id:
        issues.append("DECISION_ID_REQUIRED")
    if not execution_id:
        issues.append("EXECUTION_ID_REQUIRED")
    if not outcome.get("outcome_id"):
        issues.append("OUTCOME_ID_REQUIRED")
    if outcome.get("evaluation_status") not in {"EVALUATED", "UNASSESSED"}:
        issues.append("INVALID_EVALUATION_STATUS")

    if issues:
        return {"status": "FEEDBACK_REJECTED", "issues": issues}

    return {
        "status": "OUTCOME_RECORDED",
        "decision_id": decision_id,
        "execution_id": execution_id,
        "outcome_id": outcome["outcome_id"],
        "evaluation_status": outcome["evaluation_status"],
        "learning_eligible": outcome["evaluation_status"] == "EVALUATED" and outcome.get("learning_eligible", False),
    }
