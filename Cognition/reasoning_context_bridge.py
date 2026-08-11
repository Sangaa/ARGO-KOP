"""Bridge runtime context and retrieved knowledge into a safe reasoning packet."""


def build_reasoning_packet(context: dict, knowledge: list[dict]) -> dict:
    """Prepare cognition input without making a decision or executing an action."""
    required = ("task_id", "session_id", "project_id", "domain", "active_state", "claim", "allowed_scope")
    missing = [key for key in required if not context.get(key)]
    if missing:
        raise ValueError(f"reasoning context incomplete: {', '.join(missing)}")

    return {
        "task_id": context["task_id"],
        "session_id": context["session_id"],
        "context": context.copy(),
        "retrieved_knowledge": list(knowledge),
        "reasoning_status": "READY",
        "decision_status": "NOT_EVALUATED",
        "execution_status": "NOT_REQUESTED",
    }
