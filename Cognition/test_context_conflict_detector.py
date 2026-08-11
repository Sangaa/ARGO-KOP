from context_conflict_detector import detect


def test_conflicting_claim_is_flagged_not_resolved():
    result = detect({
        "current_facts": [{"claim": "shipment pending"}],
        "historical_evidence": [{"claim": "shipment pending"}],
        "historical_is_active_context": False,
    })
    assert result["status"] == "CONTEXT_ANALYZED"
    assert result["conflict_count"] == 1
    assert result["requires_reasoning"] is True
    assert result["historical_is_active_context"] is False


def test_non_matching_history_is_not_called_a_conflict():
    result = detect({
        "current_facts": [{"claim": "shipment delivered"}],
        "historical_evidence": [{"claim": "shipment pending"}],
    })
    assert result["conflict_count"] == 0
    assert result["requires_reasoning"] is False
