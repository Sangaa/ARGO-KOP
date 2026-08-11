from end_to_end_session_cycle import run_cycle


def test_two_session_cycle_reuses_scoped_historical_evidence():
    session_1 = {
        "historical_record": {
            "record_type": "EXECUTION_TRACE",
            "trace_id": "TR-S1-001",
            "task_id": "T-OLD",
            "project_id": "P-1",
            "session_id": "S-1",
            "side_effect": False,
        }
    }
    session_2 = {
        "task_id": "T-NEW",
        "project_id": "P-1",
        "current_facts": [{"claim": "shipment pending", "type": "FACT"}],
        "authorization": {
            "approved": True,
            "authorized_by": "tester",
            "authorization_id": "AUTH-S2-001",
        },
    }

    result = run_cycle(session_1, session_2)

    assert result["status"] == "COMPLETE"
    assert result["context"]["historical_evidence"][0]["trace_id"] == "TR-S1-001"
    assert result["context"]["historical_evidence"][0]["session_id"] == "S-1"
    assert result["context"]["historical_is_active_context"] is False
    assert result["authorization"]["authorization_id"] == "AUTH-S2-001"
    assert result["execution"]["status"] == "SIMULATED"
    assert result["execution"]["side_effect"] is False


def test_two_session_cycle_blocks_without_authorization():
    session_1 = {
        "historical_record": {
            "record_type": "EXECUTION_TRACE",
            "trace_id": "TR-S1-002",
            "task_id": "T-OLD",
            "project_id": "P-1",
            "session_id": "S-1",
            "side_effect": False,
        }
    }
    session_2 = {"task_id": "T-NEW", "project_id": "P-1"}

    result = run_cycle(session_1, session_2)

    assert result["status"] == "BLOCKED"
    assert result["authorization"]["reason"] == "AUTHORIZATION_REQUIRED"
