"""Validate identity and authority continuity across the two-session prototype."""


def validate_cycle(result: dict) -> dict:
    findings = []

    context = result.get("context", {})
    evidence = context.get("historical_evidence", [])
    authorization = result.get("authorization", {})
    execution = result.get("execution", {})

    for record in evidence:
        if record.get("context_role") != "HISTORICAL_EVIDENCE":
            findings.append("HISTORICAL_ROLE_LOST")
        if record.get("side_effect", False) is True:
            findings.append("HISTORICAL_SIDE_EFFECT_FLAGGED")

    if result.get("status") == "COMPLETE":
        if authorization.get("status") != "AUTHORIZED":
            findings.append("AUTHORIZATION_CONTINUITY_BROKEN")
        if execution.get("execution_status") != "SIMULATED_ONLY":
            findings.append("EXECUTION_BOUNDARY_BROKEN")
        if execution.get("side_effect", True) is not False:
            findings.append("SIDE_EFFECT_BOUNDARY_BROKEN")

    return {
        "status": "VALID" if not findings else "INVALID",
        "findings": findings,
    }
