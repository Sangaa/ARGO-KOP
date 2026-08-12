"""Deterministic first cognition pass: classify a prepared reasoning packet."""


def classify(packet: dict) -> dict:
    required = ("context", "knowledge")
    missing = [key for key in required if key not in packet]
    if missing:
        return {"status": "HOLD", "reason": "REASONING_PACKET_INCOMPLETE", "missing": missing}

    context = packet["context"]
    knowledge = packet["knowledge"]
    if not isinstance(context, dict):
        return {"status": "HOLD", "reason": "REASONING_CONTEXT_INVALID"}
    if isinstance(knowledge, dict):
        knowledge_items = [knowledge]
    elif isinstance(knowledge, list) and all(isinstance(item, dict) for item in knowledge):
        knowledge_items = knowledge
    else:
        return {"status": "HOLD", "reason": "REASONING_KNOWLEDGE_INVALID"}

    return {
        "status": "READY_FOR_REASONING",
        "facts": list(context.get("facts", [])),
        "assumptions": list(context.get("assumptions", [])),
        "known_knowledge": [item.get("task_id") for item in knowledge_items],
        "unresolved_questions": list(context.get("unresolved_questions", [])),
        "decision_status": "NOT_EVALUATED",
        "execution_status": "NOT_REQUESTED",
    }
