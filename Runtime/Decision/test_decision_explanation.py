from decision_explanation import explain


def test_explanation_preserves_complete_provenance_chain():
    result = explain(
        decision_id="DEC-1",
        context_id="CTX-2",
        evidence_ids=["TR-2", "TR-1", "TR-1"],
        ruleset_id="RULESET-1",
        authorization_id="AUTH-2",
        execution_trace_id="EXEC-2",
        decision_status="SIMULATED",
    )
    assert result["decision_id"] == "DEC-1"
    assert result["context_id"] == "CTX-2"
    assert result["evidence_ids"] == ["TR-1", "TR-2"]
    assert result["ruleset_id"] == "RULESET-1"
    assert result["authorization_id"] == "AUTH-2"
    assert result["execution_trace_id"] == "EXEC-2"
    assert result["explanation_mode"] == "RECORDED_PROVENANCE"
    assert result["is_reassessment"] is False


def test_explanation_does_not_claim_current_reassessment():
    result = explain(
        decision_id="DEC-1",
        context_id="CTX-2",
        evidence_ids=["TR-1"],
        ruleset_id="RULESET-HISTORICAL",
        authorization_id="AUTH-2",
        execution_trace_id="EXEC-2",
        decision_status="SIMULATED",
    )
    assert result["is_reassessment"] is False
