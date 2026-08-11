"""Edge-case acceptance tests for learning promotion."""

from learning_promotion_gate import evaluate
from test_learning_promotion_gate import candidate


def test_invalid_confidence_is_held():
    item = candidate()
    item["confidence"] = 1.5
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "INVALID_CONFIDENCE"


def test_unvalidated_candidate_is_held():
    item = candidate()
    item["validation"] = "PENDING"
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "VALIDATION_FAILED"


def test_incomplete_candidate_is_held():
    item = candidate()
    del item["pattern"]
    result = evaluate(item)
    assert result["status"] == "HOLD"
    assert result["reason"] == "CANDIDATE_INCOMPLETE"
