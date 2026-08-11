"""Side-effect-free mock executor for controlled execution testing."""


def execute(plan: dict) -> dict:
    if plan.get("status") != "PLAN_READY":
        return {"status": "BLOCKED", "reason": "PLAN_NOT_READY"}
    if plan.get("execution_status") != "NOT_STARTED":
        return {"status": "BLOCKED", "reason": "INVALID_EXECUTION_STATE"}

    return {
        "status": "SIMULATED",
        "execution_status": "SIMULATED_ONLY",
        "action": plan.get("action"),
        "target": plan.get("target"),
        "authorization_id": plan.get("authorization_id"),
        "side_effect": False,
    }
