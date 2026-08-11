"""Acceptance tests for the learning promotion gate."""

from learning_promotion_gate import evaluate


def candidate():
    return {
        "task_id": "LEARN-001",
        "session_id": "SESSION-LEARN",
        "evidence": ["source:001"],
        "observed_result": "draft accepted",
        "pattern": "validated response structure",
        "confidence": 0.95,
        "validation": "VALIDATED",
        "promotion_authority": True,
    }


def test_verified_candidate_is_eligible():
    result = evaluate(candidate())
    assert result["status"] == "PROMOTION_ELIGIBLE"
    assert result["promote"] is True


def test_missing_authority_is_held():
    item = candidate()
    item["promotion_authority"] = False
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "PROMOTION_AUTHORITY_MISSING"


def test_missing_evidence_is_held():
    item = candidate()
    item["evidence"] = []
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "NO_EVIDENCE"


def test_low_confidence_is_held():
    item = candidate()
    item["confidence"] = 0.5
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "LOW_CONFIDENCE"


def test_unobserved_result_is_held():
    item = candidate()
    item["observed_result"] = None
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "RESULT_NOT_OBSERVED"
