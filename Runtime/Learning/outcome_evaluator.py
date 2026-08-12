"""Classify a recorded decision outcome without promoting it to knowledge."""

VALID_RESULTS = {"SUCCESS", "PARTIAL", "FAILURE", "INCONCLUSIVE"}


def evaluate_outcome(*, decision_id: str, execution_id: str, outcome: dict) -> dict:
    """Evaluate an outcome only when its evidence is tied to the execution trace.

    Outcome evidence is not accepted merely because it is non-empty. The outcome
    must identify the execution trace IDs that produced it, and every cited
    evidence trace must belong to that execution trace set.
    """
    issues = []
    outcome_id = outcome.get("outcome_id")
    result = outcome.get("result")
    evidence_ids = sorted(set(outcome.get("evidence_trace_ids", [])))
    execution_trace_ids = sorted(set(outcome.get("execution_trace_ids", [])))
    confidence = outcome.get("confidence", "UNKNOWN")

    if not decision_id:
        issues.append("DECISION_ID_REQUIRED")
    if not execution_id:
        issues.append("EXECUTION_ID_REQUIRED")
    if not outcome_id:
        issues.append("OUTCOME_ID_REQUIRED")
    if result not in VALID_RESULTS:
        issues.append("INVALID_OUTCOME_RESULT")
    if not evidence_ids:
        issues.append("OUTCOME_EVIDENCE_REQUIRED")
    if not execution_trace_ids:
        issues.append("EXECUTION_TRACE_REQUIRED")

    orphaned_evidence = sorted(set(evidence_ids) - set(execution_trace_ids))
    if orphaned_evidence:
        issues.append("OUTCOME_PROVENANCE_BROKEN")

    if issues:
        return {"status": "EVALUATION_REJECTED", "issues": issues}

    return {
        "status": "EVALUATED",
        "decision_id": decision_id,
        "execution_id": execution_id,
        "outcome_id": outcome_id,
        "result": result,
        "evidence_trace_ids": evidence_ids,
        "execution_trace_ids": execution_trace_ids,
        "confidence": confidence,
        "learning_eligible": result in {"SUCCESS", "FAILURE", "PARTIAL"},
    }
