"""Direct integration proof for persisted historical evidence -> new session Context."""

from Cognition.session_context_rehydrator import rehydrate


def test_persisted_historical_trace_rehydrates_without_fact_or_authority_promotion():
    result = rehydrate(
        current_task_id="T-NEW",
        current_project_id="P-1",
        current_facts=[{"claim": "shipment pending", "type": "FACT"}],
        historical_records=[
            {"trace_id": "TR-1", "task_id": "T-OLD", "project_id": "P-1", "record_type": "EXECUTION_TRACE"},
            {"trace_id": "TR-X", "task_id": "T-X", "project_id": "P-X", "record_type": "EXECUTION_TRACE"},
        ],
    )

    assert result["rehydrated"] is True
    assert result["status"] == "CONTEXT_READY"
    assert [item["trace_id"] for item in result["historical_evidence"]] == ["TR-1"]
    assert result["historical_evidence"][0]["context_role"] == "HISTORICAL_EVIDENCE"
    assert result["historical_is_active_context"] is False
    assert result["provenance_required"] is True
    assert result["current_facts"] == [{"claim": "shipment pending", "type": "FACT"}]
    assert result["excluded_history"][0]["trace_id"] == "TR-X"


def test_rehydration_does_not_create_execution_or_authority():
    result = rehydrate(
        current_task_id="T-1",
        current_project_id=None,
        current_facts=[],
        historical_records=[{"trace_id": "TR-1", "task_id": "T-1", "record_type": "EXECUTION_TRACE"}],
    )

    assert result["rehydrated"] is True
    assert result["historical_is_active_context"] is False
    assert result["provenance_required"] is True
    assert "authorization" not in result
    assert "execution" not in result
