"""Rehydrate a new session context from scoped historical evidence."""

from context_loader import load
from context_memory_selector import select


def rehydrate(*, current_task_id: str, current_project_id: str | None,
              current_facts: list[dict], historical_records: list[dict]) -> dict:
    selection = select(
        current_task_id=current_task_id,
        current_project_id=current_project_id,
        historical_records=historical_records,
    )
    context = load(
        current_facts=current_facts,
        historical_evidence=selection["selected"],
    )
    return {
        **context,
        "selection_status": selection["status"],
        "excluded_history": selection["excluded"],
        "rehydrated": True,
    }
