"""Build a cognition input that preserves current facts and historical provenance."""


def load(*, current_facts: list[dict], historical_evidence: list[dict]) -> dict:
    return {
        "status": "CONTEXT_READY",
        "current_facts": current_facts,
        "historical_evidence": historical_evidence,
        "provenance_required": True,
        "historical_is_active_context": False,
    }
