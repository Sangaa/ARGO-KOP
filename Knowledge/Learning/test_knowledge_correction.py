from knowledge_correction import assess_contradiction


def promoted():
    return {"task_id": "SYN-001", "status": "PROMOTED"}


def test_non_contradiction_keeps_record_unchanged():
    record = promoted()
    snapshot = dict(record)
    result = assess_contradiction(record, evidence=["new-test"], contradiction=False)
    assert result["status"] == "NO_CHANGE"
    assert result["record"] == snapshot
    assert record == snapshot


def test_contradiction_requires_review():
    record = promoted()
    snapshot = dict(record)
    result = assess_contradiction(record, evidence=["contradictory-test"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
    assert result["record_id"] == "SYN-001"
    assert record == snapshot


def test_empty_or_malformed_evidence_holds():
    for evidence in ([], [""], ["ok", 7], "not-a-list"):
        result = assess_contradiction(promoted(), evidence=evidence, contradiction=True)
        assert result["status"] == "HOLD"
        assert result["reason"] == "INVALID_EVIDENCE"


def test_missing_identity_holds():
    record = {"task_id": "", "status": "PROMOTED"}
    result = assess_contradiction(record, evidence=["proof"], contradiction=True)
    assert result["status"] == "HOLD"
    assert result["reason"] == "MISSING_STABLE_TASK_ID"


def test_non_promoted_source_holds():
    record = {"task_id": "SYN-001", "status": "CANDIDATE"}
    result = assess_contradiction(record, evidence=["proof"], contradiction=True)
    assert result["status"] == "HOLD"
    assert result["reason"] == "SOURCE_NOT_PROMOTED"


def test_truthy_non_boolean_signal_holds():
    record = promoted()
    result = assess_contradiction(record, evidence=["proof"], contradiction="true")
    assert result["status"] == "HOLD"
    assert result["reason"] == "INVALID_CONTRADICTION_SIGNAL"
