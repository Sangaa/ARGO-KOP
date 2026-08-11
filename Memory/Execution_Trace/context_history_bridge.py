"""Bridge historical traces into context as explicitly labeled evidence."""


def load_historical(records: list[dict], *, task_id: str) -> dict:
    selected = [
        record for record in records
        if record.get("record_type") == "EXECUTION_TRACE"
        and record.get("task_id") == task_id
    ]
    return {
        "status": "HISTORICAL_CONTEXT_READY" if selected else "NO_HISTORY",
        "task_id": task_id,
        "historical_evidence": selected,
        "active_context": False,
        "promotion_status": "NOT_PROMOTED",
    }
