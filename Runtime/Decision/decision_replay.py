"""Deterministic replay scaffold for previously recorded governed decisions."""


def replay(*, evidence_ids: list[str], ruleset_id: str, proposal: dict,
           authorization: dict, execution: dict) -> dict:
    expected = sorted(set(evidence_ids))
    used = sorted(set(proposal.get("evidence_trace_ids", [])))
    issues = []

    if expected != used:
        issues.append("EVIDENCE_SET_MISMATCH")
    if proposal.get("ruleset_id") != ruleset_id:
        issues.append("RULESET_MISMATCH")
    if authorization.get("status") != "AUTHORIZED":
        issues.append("AUTHORIZATION_MISMATCH")
    if execution.get("execution_status") != "SIMULATED_ONLY":
        issues.append("EXECUTION_MODE_MISMATCH")

    return {
        "status": "REPLAY_MATCH" if not issues else "REPLAY_MISMATCH",
        "issues": issues,
        "evidence_ids": expected,
        "ruleset_id": ruleset_id,
    }
