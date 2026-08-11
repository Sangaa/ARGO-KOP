from knowledge_correction import assess_contradiction


def test_non_contradiction_keeps_record_unchanged():
    record = {"task_id": "SYN-001", "status": "PROMOTED"}
    result = assess_contradiction(record, evidence=["new-test"], contradiction=False)
    assert result["status"] == "NO_CHANGE"
    assert result["record"] == record


def test_contradiction_requires_review():
    record = {"task_id": "SYN-001", "status": "PROMOTED"}
    result = assess_contradiction(record, evidence=["contradictory-test"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
    assert result["record_id"] == "SYN-001"
