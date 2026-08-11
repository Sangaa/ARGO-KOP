"""Convert unresolved cognition conditions into a downstream safety hold."""


def evaluate(conflict_result: dict) -> dict:
    if conflict_result.get("requires_reasoning"):
        return {
            "status": "HOLD",
            "reason": "UNRESOLVED_CONTEXT_CONFLICT",
            "decision_allowed": False,
            "authorization_allowed": False,
            "execution_allowed": False,
        }
    return {
        "status": "CLEAR",
        "reason": "NO_CONTEXT_CONFLICT",
        "decision_allowed": True,
        "authorization_allowed": False,
        "execution_allowed": False,
    }
