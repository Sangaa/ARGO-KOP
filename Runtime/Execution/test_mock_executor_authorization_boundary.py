from mock_executor import execute


def test_executor_rejects_non_ready_plan():
    result = execute({"status": "REVIEW_REQUIRED", "execution_status": "NOT_STARTED"})
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "PLAN_NOT_READY"


def test_executor_rejects_invalid_execution_state():
    result = execute({
        "status": "PLAN_READY",
        "execution_status": "SIMULATED_ONLY",
        "authorization_id": "AUTH-001",
    })
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "INVALID_EXECUTION_STATE"


def test_executor_is_side_effect_free_after_authorization():
    result = execute({
        "status": "PLAN_READY",
        "execution_status": "NOT_STARTED",
        "authorization_id": "AUTH-001",
        "action": "SEND_DRAFT",
        "target": "TEST_TARGET",
    })
    assert result["status"] == "SIMULATED"
    assert result["execution_status"] == "SIMULATED_ONLY"
    assert result["authorization_id"] == "AUTH-001"
    assert result["side_effect"] is False
