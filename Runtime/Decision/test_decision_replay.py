from decision_replay import replay


def test_identical_inputs_replay_successfully():
    result = replay(
        evidence_ids=["TR-1"],
        ruleset_id="RULESET-1",
        proposal={"evidence_trace_ids": ["TR-1"], "ruleset_id": "RULESET-1"},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "SIMULATED_ONLY"},
    )
    assert result["status"] == "REPLAY_MATCH"
    assert result["issues"] == []


def test_replay_detects_evidence_change():
    result = replay(
        evidence_ids=["TR-1"],
        ruleset_id="RULESET-1",
        proposal={"evidence_trace_ids": ["TR-2"], "ruleset_id": "RULESET-1"},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "SIMULATED_ONLY"},
    )
    assert result["status"] == "REPLAY_MISMATCH"
    assert "EVIDENCE_SET_MISMATCH" in result["issues"]


def test_replay_detects_ruleset_change():
    result = replay(
        evidence_ids=["TR-1"],
        ruleset_id="RULESET-2",
        proposal={"evidence_trace_ids": ["TR-1"], "ruleset_id": "RULESET-1"},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "SIMULATED_ONLY"},
    )
    assert "RULESET_MISMATCH" in result["issues"]


def test_replay_detects_unauthorized_or_real_execution():
    result = replay(
        evidence_ids=["TR-1"],
        ruleset_id="RULESET-1",
        proposal={"evidence_trace_ids": ["TR-1"], "ruleset_id": "RULESET-1"},
        authorization={"status": "HOLD"},
        execution={"execution_status": "EXECUTED"},
    )
    assert result["status"] == "REPLAY_MISMATCH"
    assert "AUTHORIZATION_MISMATCH" in result["issues"]
    assert "EXECUTION_MODE_MISMATCH" in result["issues"]
