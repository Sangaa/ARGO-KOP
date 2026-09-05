"""Boundary test: Knowledge candidate mapping remains separate from Runtime promotion authority."""

from Knowledge.Learning.promotion_gate_adapter import build_candidate
from Runtime.Prototype.learning_promotion_gate import evaluate


def _evidence():
    return {
        "task_id": "TASK-BOUNDARY-001",
        "session_id": "SESSION-BOUNDARY-001",
        "evidence": ["TRACE-BOUNDARY-001"],
        "observed_result": "SUCCESS",
        "pattern": "stable",
        "confidence": 0.95,
        "validation": "VALIDATED",
    }


def _evaluate(*, authority: bool):
    candidate = build_candidate(_evidence(), authority=authority)
    return evaluate(candidate)


def test_readiness_evidence_cannot_promote_without_explicit_authority():
    result = _evaluate(authority=False)

    assert result == {
        "status": "HOLD",
        "reason": "PROMOTION_AUTHORITY_MISSING",
    }


def test_runtime_promotion_gate_accepts_only_explicit_authority():
    result = _evaluate(authority=True)

    assert result["status"] == "PROMOTION_ELIGIBLE"
    assert result["promote"] is True
