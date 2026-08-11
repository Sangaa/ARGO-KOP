from context_memory_selector import select


def test_selector_keeps_matching_task_evidence():
    result = select(
        current_task_id="T-1",
        current_project_id="P-1",
        historical_records=[
            {"trace_id": "TR-1", "task_id": "T-1", "project_id": "P-X"},
            {"trace_id": "TR-2", "task_id": "T-2", "project_id": "P-2"},
        ],
    )
    assert [x["trace_id"] for x in result["selected"]] == ["TR-1"]
    assert result["selected"][0]["context_role"] == "HISTORICAL_EVIDENCE"


def test_selector_keeps_matching_project_evidence():
    result = select(
        current_task_id="T-NEW",
        current_project_id="P-1",
        historical_records=[
            {"trace_id": "TR-1", "task_id": "T-OLD", "project_id": "P-1"},
        ],
    )
    assert [x["trace_id"] for x in result["selected"]] == ["TR-1"]


def test_selector_excludes_unrelated_history():
    result = select(
        current_task_id="T-1",
        current_project_id="P-1",
        historical_records=[
            {"trace_id": "TR-X", "task_id": "T-X", "project_id": "P-X"},
        ],
    )
    assert result["selected"] == []
    assert result["excluded"][0]["reason"] == "OUT_OF_SCOPE"
    assert result["historical_is_active_context"] is False
