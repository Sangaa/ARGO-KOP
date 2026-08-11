"""Governed decision pass: convert reasoning into a proposal, never an action."""


def propose(reasoning: dict, *, rules: list[str]) -> dict:
    required = ("status", "observations", "evidence_map")
    missing = [key for key in required if key not in reasoning]
    if missing:
        return {"status": "HOLD", "reason": "REASONING_INCOMPLETE", "missing": missing}
    if reasoning.get("status") != "REASONED":
        return {"status": "HOLD", "reason": "REASONING_NOT_READY"}

    unresolved = reasoning["observations"].get("unresolved_questions", [])
    if unresolved:
        return {
            "status": "REVIEW_REQUIRED",
            "reason": "UNRESOLVED_QUESTIONS",
            "questions": unresolved,
            "rules_considered": rules,
            "execution_status": "NOT_REQUESTED",
        }

    return {
        "status": "PROPOSAL_READY",
        "proposal": "REVIEW_AND_AUTHORIZE_NEXT_ACTION",
        "rules_considered": rules,
        "execution_status": "NOT_REQUESTED",
    }
