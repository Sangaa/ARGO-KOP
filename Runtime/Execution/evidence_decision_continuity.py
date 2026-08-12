"""Validate provenance continuity from historical evidence to a governed decision."""


def validate_continuity(*, evidence: list[dict], proposal: dict,
                        authorization: dict, execution: dict) -> dict:
    evidence_ids = {item.get("trace_id") for item in evidence if item.get("trace_id")}
    proposal_ids = set(proposal.get("evidence_trace_ids", []))

    missing_from_proposal = sorted(evidence_ids - proposal_ids)
    unauthorized = authorization.get("status") != "AUTHORIZED"
    execution_trace_id = execution.get("source_trace_id")
    decision_trace_ok = execution_trace_id in proposal_ids if execution_trace_id else False

    issues = []
    if missing_from_proposal:
        issues.append("EVIDENCE_DROPPED_BEFORE_DECISION")
    if unauthorized:
        issues.append("AUTHORIZATION_NOT_CONFIRMED")
    if not decision_trace_ok:
        issues.append("EXECUTION_PROVENANCE_BROKEN")
    if execution.get("execution_status") == "SIMULATED_ONLY" and execution.get("side_effect") is True:
        issues.append("SIMULATION_SIDE_EFFECT_CONFLICT")

    return {
        "status": "CONTINUOUS" if not issues else "BROKEN",
        "issues": issues,
        "evidence_trace_ids": sorted(evidence_ids),
        "proposal_trace_ids": sorted(proposal_ids),
        "execution_source_trace_id": execution_trace_id,
    }
