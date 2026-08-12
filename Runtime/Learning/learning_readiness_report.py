"""Build an auditable readiness report without promoting knowledge."""


def build_readiness_report(*, evaluation: dict, quality: dict) -> dict:
    return {
        "status": "READY_FOR_PROMOTION_REVIEW"
        if quality.get("learning_ready") is True
        else "NOT_READY",
        "outcome_id": evaluation.get("outcome_id"),
        "decision_id": evaluation.get("decision_id"),
        "result": evaluation.get("result"),
        "confidence": evaluation.get("confidence"),
        "evidence_trace_ids": list(evaluation.get("evidence_trace_ids", [])),
        "quality": quality.get("quality"),
        "promotion_authority": "EXISTING_LEARNING_PROMOTION_GATE",
        "knowledge_promoted": False,
    }
