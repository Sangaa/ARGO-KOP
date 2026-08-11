"""Controlled selector for historical Memory evidence entering a session Context."""


def select(*, current_task_id: str, current_project_id: str | None,
           historical_records: list[dict]) -> dict:
    selected = []
    excluded = []

    for record in historical_records:
        task_match = record.get("task_id") == current_task_id
        project_match = current_project_id is not None and record.get("project_id") == current_project_id
        if task_match or project_match:
            selected.append({**record, "context_role": "HISTORICAL_EVIDENCE"})
        else:
            excluded.append({"trace_id": record.get("trace_id"), "reason": "OUT_OF_SCOPE"})

    return {
        "status": "SELECTED",
        "task_id": current_task_id,
        "project_id": current_project_id,
        "selected": selected,
        "excluded": excluded,
        "historical_is_active_context": False,
    }
