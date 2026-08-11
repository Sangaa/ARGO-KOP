from session_context_rehydrator import rehydrate


def test_new_session_rehydrates_scoped_history():
    result = rehydrate(
        current_task_id="T-NEW",
        current_project_id="P-1",
        current_facts=[{"claim": "shipment pending", "type": "FACT"}],
        historical_records=[
            {
                "trace_id": "TR-1",
                "task_id": "T-OLD",
                "project_id": "P-1",
                "record_type": "EXECUTION_TRACE",
            },
            {
                "trace_id": "TR-X",
                "task_id": "T-X",
                "project_id": "P-X",
                "record_type": "EXECUTION_TRACE",
            },
        ],
    )
    assert result["rehydrated"] is True
    assert result["status"] == "CONTEXT_READY"
    assert [x["trace_id"] for x in result["historical_evidence"]] == ["TR-1"]
    assert result["historical_is_active_context"] is False
    assert result["excluded_history"][0]["trace_id"] == "TR-X"


def test_rehydration_preserves_current_fact_boundary():
    result = rehydrate(
        current_task_id="T-1",
        current_project_id=None,
        current_facts=[{"claim": "current fact", "type": "FACT"}],
        historical_records=[
            {"trace_id": "TR-1", "task_id": "T-1", "record_type": "EXECUTION_TRACE"}
        ],
    )
    assert result["current_facts"][0]["type"] == "FACT"
    assert result["historical_evidence"][0]["context_role"] == "HISTORICAL_EVIDENCE"
