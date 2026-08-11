from decision_explanation_completeness import validate_explanation


def complete_record():
    return {
        "context_id": "CTX-1",
        "evidence_trace_ids": ["TR-1", "TR-2"],
        "ruleset_id": "RULESET-1",
        "decision_id": "DEC-1",
        "authorization_id": "AUTH-1",
        "execution_id": "EXEC-1",
    }


def test_complete_explanation_is_accepted():
    result = validate_explanation(complete_record())
    assert result["status"] == "EXPLANATION_COMPLETE"
    assert result["complete"] is True
    assert result["missing_links"] == []


def test_missing_execution_link_is_detected():
    record = complete_record()
    del record["execution_id"]
    result = validate_explanation(record)
    assert result["status"] == "EXPLANATION_INCOMPLETE"
    assert "execution_id" in result["missing_links"]


def test_missing_evidence_is_detected():
    record = complete_record()
    record["evidence_trace_ids"] = []
    result = validate_explanation(record)
    assert result["status"] == "EXPLANATION_INCOMPLETE"
    assert "evidence_trace_ids" in result["missing_links"]
