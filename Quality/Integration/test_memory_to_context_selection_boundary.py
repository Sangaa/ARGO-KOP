"""Direct integration proof for Historical Memory -> Cognition Context selection."""

from Cognition.context_loader import load
from Cognition.context_memory_selector import select


def test_memory_to_context_selection_preserves_historical_provenance():
    selected = select(
        current_task_id="TASK-001",
        current_project_id="PROJ-001",
        historical_records=[
            {"task_id": "TASK-001", "project_id": "OTHER", "trace_id": "trace-001"},
            {"task_id": "OTHER", "project_id": "PROJ-001", "trace_id": "trace-002"},
            {"task_id": "OTHER", "project_id": "OTHER", "trace_id": "trace-003"},
        ],
    )

    context = load(current_facts=[], historical_evidence=selected["selected"])

    assert context["status"] == "CONTEXT_READY"
    assert len(context["historical_evidence"]) == 2
    assert all(item["context_role"] == "HISTORICAL_EVIDENCE" for item in context["historical_evidence"])
    assert context["historical_is_active_context"] is False
    assert selected["excluded"][0]["reason"] == "OUT_OF_SCOPE"


def test_memory_selection_does_not_promote_history_to_current_fact():
    selected = select(
        current_task_id="TASK-001",
        current_project_id=None,
        historical_records=[{"task_id": "TASK-001", "trace_id": "trace-001"}],
    )

    context = load(current_facts=[], historical_evidence=selected["selected"])

    assert context["current_facts"] == []
    assert context["historical_evidence"][0]["context_role"] == "HISTORICAL_EVIDENCE"
    assert context["provenance_required"] is True
