"""Separate historical decision replay from current-rule reassessment."""


def compare(*, recorded_evidence: list[str], recorded_ruleset: str,
            current_ruleset: str, proposal_evidence: list[str]) -> dict:
    evidence_match = sorted(set(recorded_evidence)) == sorted(set(proposal_evidence))
    historical_match = evidence_match and recorded_ruleset == current_ruleset

    if historical_match:
        mode = "HISTORICAL_REPLAY"
        status = "SAME_DECISION_BASIS"
    elif evidence_match:
        mode = "CURRENT_RULE_REASSESSMENT"
        status = "RULESET_CHANGED"
    else:
        mode = "RECONSTRUCTION_BLOCKED"
        status = "EVIDENCE_CHANGED"

    return {
        "status": status,
        "mode": mode,
        "evidence_match": evidence_match,
        "recorded_ruleset": recorded_ruleset,
        "current_ruleset": current_ruleset,
    }
