from knowledge_promotion import promote


def candidate():
    return {
        "task_id": "SYN-001",
        "session_id": "SYN-SESSION-001",
        "evidence": ["synthetic_function_fixture.py", "test_synthetic_function_fixture.py"],
        "pattern": "validated function accepts inputs and returns a predictable result",
        "confidence": 0.9,
        "validation": "VALIDATED",
    }


def test_missing_authority_holds():
    result = promote(candidate())
    assert result["status"] == "HOLD"


def test_valid_candidate_promotes():
    result = promote(candidate(), authority=True)
    assert result["status"] == "PROMOTED"
    assert result["provenance_preserved"] is True
    assert result["knowledge_scope"] == "tested_claim_only"


def test_unvalidated_candidate_cannot_promote():
    item = candidate()
    item["validation"] = "UNVALIDATED"
    result = promote(item, authority=True)
    assert result["status"] == "HOLD"
    assert result["reason"] == "VALIDATION_REQUIRED"


def test_low_confidence_candidate_cannot_promote():
    item = candidate()
    item["confidence"] = 0.79
    result = promote(item, authority=True)
    assert result["status"] == "HOLD"
    assert result["reason"] == "CONFIDENCE_BELOW_THRESHOLD"
