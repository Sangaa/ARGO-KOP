"""Side-effect-free executor for controlled runtime experiments."""


def execute(plan: dict) -> dict:
    if plan.get("status") != "PLAN_READY":
        return {"status": "BLOCKED", "reason": "PLAN_NOT_READY"}
    if not plan.get("authorization_id"):
        return {"status": "BLOCKED", "reason": "AUTHORIZATION_ID_REQUIRED"}
    return {
        "status": "SIMULATED",
        "action": plan.get("action"),
        "target": plan.get("target"),
        "authorization_id": plan.get("authorization_id"),
        "side_effect": False,
    }
