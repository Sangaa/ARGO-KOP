"""Validate that a recorded decision explanation contains its required provenance chain."""

REQUIRED_LINKS = (
    "context_id",
    "evidence_trace_ids",
    "ruleset_id",
    "decision_id",
    "authorization_id",
    "execution_id",
)


def validate_explanation(explanation: dict) -> dict:
    missing = [key for key in REQUIRED_LINKS if not explanation.get(key)]
    evidence = explanation.get("evidence_trace_ids") or []

    if not evidence:
        missing.append("evidence_trace_ids")

    return {
        "status": "EXPLANATION_COMPLETE" if not missing else "EXPLANATION_INCOMPLETE",
        "missing_links": sorted(set(missing)),
        "complete": not missing,
    }
