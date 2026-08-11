"""Build a provenance-first, human-readable explanation from recorded decision data."""


def explain(*, decision_id: str, context_id: str, evidence_ids: list[str],
            ruleset_id: str, authorization_id: str, execution_trace_id: str,
            decision_status: str) -> dict:
    return {
        "decision_id": decision_id,
        "context_id": context_id,
        "evidence_ids": sorted(set(evidence_ids)),
        "ruleset_id": ruleset_id,
        "authorization_id": authorization_id,
        "execution_trace_id": execution_trace_id,
        "decision_status": decision_status,
        "explanation_mode": "RECORDED_PROVENANCE",
        "is_reassessment": False,
    }
