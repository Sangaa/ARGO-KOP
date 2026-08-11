from promotion_gate_adapter import evaluate_evidence


def evidence():
    return {
        "task_id": "SYN-001",
        "session_id": "SYN-SESSION-001",
        "evidence": ["synthetic_function_fixture.py", "test_synthetic_function_fixture.py"],
        "observed_result": {"add(2, 3)": 5},
        "pattern": "validated function accepts inputs and returns a predictable result",
        "confidence": 0.9,
        "validation": "VALIDATED",
    }


def test_candidate_holds_without_authority():
    result = evaluate_evidence(evidence())
    assert result["status"] == "HOLD"
    assert result["reason"] == "PROMOTION_AUTHORITY_MISSING"


def test_candidate_becomes_promotion_eligible_with_authority():
    result = evaluate_evidence(evidence(), authority=True)
    assert result["status"] == "PROMOTION_ELIGIBLE"
    assert result["promote"] is True
