from decision_temporal_replay import compare


def test_same_ruleset_is_historical_replay():
    result = compare(
        recorded_evidence=["TR-1"],
        recorded_ruleset="R-1",
        current_ruleset="R-1",
        proposal_evidence=["TR-1"],
    )
    assert result["mode"] == "HISTORICAL_REPLAY"
    assert result["status"] == "SAME_DECISION_BASIS"


def test_changed_ruleset_is_not_historical_replay():
    result = compare(
        recorded_evidence=["TR-1"],
        recorded_ruleset="R-1",
        current_ruleset="R-2",
        proposal_evidence=["TR-1"],
    )
    assert result["mode"] == "CURRENT_RULE_REASSESSMENT"
    assert result["status"] == "RULESET_CHANGED"


def test_changed_evidence_blocks_reconstruction():
    result = compare(
        recorded_evidence=["TR-1"],
        recorded_ruleset="R-1",
        current_ruleset="R-1",
        proposal_evidence=["TR-2"],
    )
    assert result["mode"] == "RECONSTRUCTION_BLOCKED"
    assert result["status"] == "EVIDENCE_CHANGED"
