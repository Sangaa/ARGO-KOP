from evidence_decision_continuity import validate_continuity


def test_evidence_survives_to_simulated_execution():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": ["TR-1"]},
        authorization={"status": "AUTHORIZED"},
        execution={
            "execution_status": "SIMULATED_ONLY",
            "side_effect": False,
            "source_trace_id": "TR-1",
        },
    )
    assert result["status"] == "CONTINUOUS"
    assert result["issues"] == []


def test_dropped_evidence_is_detected():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": []},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "SIMULATED_ONLY", "side_effect": False},
    )
    assert result["status"] == "BROKEN"
    assert "EVIDENCE_DROPPED_BEFORE_DECISION" in result["issues"]


def test_simulated_execution_cannot_have_side_effect():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": ["TR-1"]},
        authorization={"status": "AUTHORIZED"},
        execution={
            "execution_status": "SIMULATED_ONLY",
            "side_effect": True,
            "source_trace_id": "TR-1",
        },
    )
    assert result["status"] == "BROKEN"
    assert "SIMULATION_SIDE_EFFECT_CONFLICT" in result["issues"]


def test_unauthorized_path_is_detected():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": ["TR-1"]},
        authorization={"status": "HOLD"},
        execution={"execution_status": "SIMULATED_ONLY", "side_effect": False, "source_trace_id": "TR-1"},
    )
    assert "AUTHORIZATION_NOT_CONFIRMED" in result["issues"]


def test_real_execution_without_provenance_is_detected():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": ["TR-1"]},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "EXECUTED", "side_effect": True, "source_trace_id": "TR-2"},
    )
    assert result["status"] == "BROKEN"
    assert "EXECUTION_PROVENANCE_BROKEN" in result["issues"]


def test_real_execution_without_source_trace_is_detected():
    result = validate_continuity(
        evidence=[{"trace_id": "TR-1"}],
        proposal={"evidence_trace_ids": ["TR-1"]},
        authorization={"status": "AUTHORIZED"},
        execution={"execution_status": "EXECUTED", "side_effect": True},
    )
    assert result["status"] == "BROKEN"
    assert "EXECUTION_PROVENANCE_BROKEN" in result["issues"]
