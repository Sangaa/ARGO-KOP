"""Side-effect-free mock executor for controlled execution testing."""


def _valid_authorization_id(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def execute(plan: dict) -> dict:
    if not isinstance(plan, dict):
        return {"status": "BLOCKED", "reason": "INVALID_PLAN"}
    if plan.get("status") != "PLAN_READY":
        return {"status": "BLOCKED", "reason": "PLAN_NOT_READY"}
    if plan.get("execution_status") != "NOT_STARTED":
        return {"status": "BLOCKED", "reason": "INVALID_EXECUTION_STATE"}
    if not _valid_authorization_id(plan.get("authorization_id")):
        return {"status": "BLOCKED", "reason": "AUTHORIZATION_REQUIRED"}

    return {
        "status": "SIMULATED",
        "execution_status": "SIMULATED_ONLY",
        "action": plan.get("action"),
        "target": plan.get("target"),
        "authorization_id": plan["authorization_id"],
        "side_effect": False,
    }
