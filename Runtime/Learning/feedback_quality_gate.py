"""Validate the evidence quality behind an evaluated outcome."""

VALID_RESULTS = {"SUCCESS", "PARTIAL", "FAILURE", "INCONCLUSIVE"}
VALID_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}


def assess_feedback_quality(*, evaluation: dict) -> dict:
    """Assess quality independently from learning eligibility.

    A valid but inconclusive or low-confidence outcome is still *assessed*;
    assessment and promotion readiness are deliberately separate boundaries.
    """
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
    if confidence not in VALID_CONFIDENCE:
        issues.append("INVALID_FEEDBACK_CONFIDENCE")

    quality = "ACCEPTABLE" if not issues and confidence in {"HIGH", "MEDIUM"} else "INSUFFICIENT"
    return {
        "status": "QUALITY_ASSESSED" if not issues else "QUALITY_REJECTED",
        "quality": quality,
        "learning_ready": quality == "ACCEPTABLE" and result != "INCONCLUSIVE",
        "issues": issues,
    }
