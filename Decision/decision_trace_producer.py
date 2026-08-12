"""Materialize a canonical trace for a completed reasoning/decision boundary."""

from datetime import datetime, timezone


def record_decision_trace(
    *,
    trace_id: str,
    task_id: str,
    session_id: str,
    evidence_map: list[dict],
    decision_status: str,
    recorded_at: str | None = None,
) -> dict:
    """Record decision-lineage evidence without authorizing or executing."""
    issues = []
    if not trace_id:
        issues.append("TRACE_ID_REQUIRED")
    if not task_id:
        issues.append("TASK_ID_REQUIRED")
    if not session_id:
        issues.append("SESSION_ID_REQUIRED")
    if not isinstance(evidence_map, list) or not evidence_map:
        issues.append("EVIDENCE_MAP_REQUIRED")
    if not decision_status:
        issues.append("DECISION_STATUS_REQUIRED")

    if issues:
        return {"status": "TRACE_REJECTED", "issues": issues}

    return {
        "status": "TRACE_RECORDED",
        "trace": {
            "trace_id": trace_id,
            "task_id": task_id,
            "session_id": session_id,
            "recorded_at": recorded_at or datetime.now(timezone.utc).isoformat(),
            "record_type": "DECISION_TRACE",
            "decision_status": decision_status,
            "evidence_map": evidence_map,
        },
    }
