"""Build a safe context package from current facts plus historical evidence."""


def build_context(*, current_facts: list[dict], historical_evidence: list[dict]) -> dict:
    return {
        "current_facts": current_facts,
        "historical_evidence": historical_evidence,
        "historical_is_active_context": False,
        "promotion_required": bool(historical_evidence),
    }


def promote_history(context: dict, *, approved: bool = False) -> dict:
    if not approved:
        return {**context, "historical_is_active_context": False, "status": "HISTORICAL_ONLY"}
    return {**context, "historical_is_active_context": True, "status": "PROMOTED"}
