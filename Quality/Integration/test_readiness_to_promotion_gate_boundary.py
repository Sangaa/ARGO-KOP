"""Boundary test: readiness evidence remains separate from promotion authority."""

from Knowledge.Learning.promotion_gate_adapter import evaluate_evidence


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


def test_readiness_evidence_cannot_promote_without_explicit_authority():
    result = evaluate_evidence(_evidence(), authority=False)

    assert result == {
        "status": "HOLD",
        "reason": "PROMOTION_AUTHORITY_MISSING",
    }


def test_promotion_gate_accepts_only_explicit_authority():
    result = evaluate_evidence(_evidence(), authority=True)

    assert result["status"] == "PROMOTION_ELIGIBLE"
    assert result["promote"] is True
