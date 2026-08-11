"""Side-effect-free execution plan representation."""


def build_plan(authorization: dict, *, action: str, target: str) -> dict:
    if authorization.get("status") != "AUTHORIZED":
        return {"status": "BLOCKED", "reason": "AUTHORIZATION_REQUIRED"}
    return {
        "status": "PLAN_READY",
        "action": action,
        "target": target,
        "authorization_id": authorization.get("authorization_id"),
        "execution_status": "NOT_STARTED",
    }
