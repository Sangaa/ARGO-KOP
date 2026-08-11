"""Explicit authorization gate between proposal and execution."""


def authorize(proposal: dict, authorization: dict | None) -> dict:
    if proposal.get("status") != "PROPOSAL_READY":
        return {"status": "BLOCKED", "reason": "PROPOSAL_NOT_READY"}
    if not authorization or authorization.get("approved") is not True:
        return {"status": "BLOCKED", "reason": "AUTHORIZATION_REQUIRED"}
    return {
        "status": "AUTHORIZED",
        "authorized_by": authorization.get("authorized_by"),
        "authorization_id": authorization.get("authorization_id"),
        "execution_status": "NOT_STARTED",
    }
