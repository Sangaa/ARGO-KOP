from learning_readiness_report import build_readiness_report


def test_ready_report_does_not_promote_knowledge():
    report = build_readiness_report(
        evaluation={
            "outcome_id": "OUT-1",
            "decision_id": "DEC-1",
            "result": "SUCCESS",
            "confidence": "HIGH",
            "evidence_trace_ids": ["TR-1"],
        },
        quality={"quality": "ACCEPTABLE", "learning_ready": True},
    )
    assert report["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert report["knowledge_promoted"] is False
    assert report["promotion_authority"] == "EXISTING_LEARNING_PROMOTION_GATE"


def test_not_ready_report_is_explicit():
    report = build_readiness_report(
        evaluation={"outcome_id": "OUT-2", "result": "INCONCLUSIVE"},
        quality={"quality": "INSUFFICIENT", "learning_ready": False},
    )
    assert report["status"] == "NOT_READY"
    assert report["knowledge_promoted"] is False
