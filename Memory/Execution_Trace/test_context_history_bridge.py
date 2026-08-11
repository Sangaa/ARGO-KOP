from context_history_bridge import build_context, promote_history


def test_history_is_evidence_not_active_context():
    context = build_context(
        current_facts=[{"claim": "shipment pending", "type": "FACT"}],
        historical_evidence=[{"trace_id": "TRACE-001", "record_type": "EXECUTION_TRACE"}],
    )
    assert context["current_facts"]
    assert context["historical_evidence"]
    assert context["historical_is_active_context"] is False
    assert context["promotion_required"] is True


def test_history_requires_explicit_promotion():
    context = build_context(current_facts=[], historical_evidence=[{"trace_id": "TRACE-001"}])
    assert promote_history(context)["status"] == "HISTORICAL_ONLY"
    promoted = promote_history(context, approved=True)
    assert promoted["status"] == "PROMOTED"
    assert promoted["historical_is_active_context"] is True
