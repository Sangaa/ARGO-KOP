"""Inspect historical execution traces without promoting them to active context."""


def inspect(records: list[dict], *, task_id: str | None = None, session_id: str | None = None) -> list[dict]:
    matches = []
    for record in records:
        if record.get("record_type") != "EXECUTION_TRACE":
            continue
        if task_id is not None and record.get("task_id") != task_id:
            continue
        if session_id is not None and record.get("session_id") != session_id:
            continue
        matches.append(record)
    return matches


def project_history(record: dict, *, promote: bool = False) -> dict:
    """Return historical evidence explicitly; never mark it active by default."""
    if record.get("record_type") != "EXECUTION_TRACE":
        return {"status": "HOLD", "reason": "NOT_AN_EXECUTION_TRACE"}
    return {
        "status": "PROMOTED" if promote else "HISTORICAL_ONLY",
        "source_trace_id": record.get("trace_id"),
        "task_id": record.get("task_id"),
        "final_status": record.get("final_status"),
        "side_effect": record.get("side_effect", False),
        "active_context": bool(promote),
    }
