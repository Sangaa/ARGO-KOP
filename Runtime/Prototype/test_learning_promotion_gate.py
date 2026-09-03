"""Acceptance tests for the learning promotion gate."""

from cognitive_loop_harness import run
from learning_promotion_gate import candidate_from_trace, evaluate


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
        "governing_conflict": False,
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


def test_cognitive_trace_requires_separate_learning_authority():
    trace = run(
        {
            "task_id": "LEARN-TRACE-001",
            "session_id": "SESSION-TRACE",
            "active_state": "outcome_observed",
            "evidence": ["source:trace:001"],
            "knowledge": ["rule:promotion-boundary"],
            "requested_outcome": "prepare safe proposal",
        },
        human_approved=True,
    )
    item = candidate_from_trace(
        trace,
        observed_result="proposal accepted",
        pattern="validated proposal structure",
        confidence=0.95,
        promotion_authority=False,
        governing_conflict=False,
    )

    assert trace["authorization"]["status"] == "AUTHORIZED"
    assert evaluate(item) == {"status": "HOLD", "reason": "PROMOTION_AUTHORITY_MISSING"}

    item["promotion_authority"] = True
    assert evaluate(item) == {"status": "PROMOTION_ELIGIBLE", "promote": True}
    assert trace["result"] == {"executed": False, "external_side_effect": False}
