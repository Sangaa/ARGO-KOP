"""Detect conflicts between current facts and historical evidence without resolving them."""


def detect(context: dict) -> dict:
    current = {item.get("claim") for item in context.get("current_facts", []) if item.get("claim")}
    historical = {item.get("claim") for item in context.get("historical_evidence", []) if item.get("claim")}
    conflicts = sorted(current & historical)
    return {
        "status": "CONTEXT_ANALYZED",
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "requires_reasoning": bool(conflicts),
        "historical_is_active_context": context.get("historical_is_active_context", False),
    }
