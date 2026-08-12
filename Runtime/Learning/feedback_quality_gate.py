"""Validate the evidence quality behind an evaluated outcome."""

VALID_RESULTS = {"SUCCESS", "PARTIAL", "FAILURE", "INCONCLUSIVE"}


def assess_feedback_quality(*, evaluation: dict) -> dict:
    issues = []
    result = evaluation.get("result")
    evidence = evaluation.get("evidence_trace_ids", [])
    confidence = evaluation.get("confidence")

    if evaluation.get("status") != "EVALUATED":
        issues.append("OUTCOME_NOT_EVALUATED")
    if result not in VALID_RESULTS:
        issues.append("INVALID_OUTCOME_RESULT")
    if not evidence:
        issues.append("OUTCOME_EVIDENCE_REQUIRED")
    if confidence not in {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}:
        issues.append("INVALID_FEEDBACK_CONFIDENCE")

    quality = "ACCEPTABLE" if not issues and confidence in {"HIGH", "MEDIUM"} else "INSUFFICIENT"
    return {
        "status": "QUALITY_ASSESSED" if not issues else "QUALITY_REJECTED",
        "quality": quality,
        "learning_ready": quality == "ACCEPTABLE" and result != "INCONCLUSIVE",
        "issues": issues,
    }
