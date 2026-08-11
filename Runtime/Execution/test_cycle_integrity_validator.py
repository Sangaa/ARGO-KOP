from cycle_integrity_validator import validate_cycle


def test_complete_cycle_preserves_boundaries():
    result = validate_cycle({
        "status": "COMPLETE",
        "context": {
            "historical_evidence": [
                {
                    "trace_id": "TR-S1-001",
                    "context_role": "HISTORICAL_EVIDENCE",
                    "side_effect": False,
                }
            ]
        },
        "authorization": {
            "status": "AUTHORIZED",
            "authorization_id": "AUTH-S2-001",
        },
        "execution": {
            "execution_status": "SIMULATED_ONLY",
            "side_effect": False,
        },
    })
    assert result == {"status": "VALID", "findings": []}


def test_validator_detects_execution_boundary_break():
    result = validate_cycle({
        "status": "COMPLETE",
        "context": {"historical_evidence": []},
        "authorization": {"status": "AUTHORIZED"},
        "execution": {
            "execution_status": "EXECUTED",
            "side_effect": True,
        },
    })
    assert result["status"] == "INVALID"
    assert "EXECUTION_BOUNDARY_BROKEN" in result["findings"]
    assert "SIDE_EFFECT_BOUNDARY_BROKEN" in result["findings"]


def test_validator_detects_historical_role_loss():
    result = validate_cycle({
        "status": "BLOCKED",
        "context": {
            "historical_evidence": [
                {"trace_id": "TR-X", "context_role": "FACT"}
            ]
        },
        "authorization": {"status": "BLOCKED"},
    })
    assert result["status"] == "INVALID"
    assert "HISTORICAL_ROLE_LOST" in result["findings"]
