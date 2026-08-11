from context_loader import load


def test_cognition_receives_current_and_historical_with_provenance():
    result = load(
        current_facts=[{"claim": "shipment pending", "type": "FACT"}],
        historical_evidence=[{"trace_id": "TRACE-001", "record_type": "EXECUTION_TRACE"}],
    )
    assert result["status"] == "CONTEXT_READY"
    assert result["current_facts"][0]["type"] == "FACT"
    assert result["historical_evidence"][0]["record_type"] == "EXECUTION_TRACE"
    assert result["provenance_required"] is True
    assert result["historical_is_active_context"] is False


def test_empty_history_does_not_create_history():
    result = load(current_facts=[], historical_evidence=[])
    assert result["historical_evidence"] == []
    assert result["historical_is_active_context"] is False
