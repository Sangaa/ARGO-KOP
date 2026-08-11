from mock_executor import execute


def test_mock_executor_requires_ready_plan():
    result = execute({"status": "BLOCKED"})
    assert result["status"] == "BLOCKED"


def test_mock_executor_simulates_without_side_effect():
    plan = {
        "status": "PLAN_READY",
        "action": "DRAFT_RESPONSE",
        "target": "customer",
        "authorization_id": "AUTH-001",
        "execution_status": "NOT_STARTED",
    }
    result = execute(plan)
    assert result["status"] == "SIMULATED"
    assert result["execution_status"] == "SIMULATED_ONLY"
    assert result["side_effect"] is False
    assert result["authorization_id"] == "AUTH-001"


def test_mock_executor_rejects_already_started_plan():
    result = execute({
        "status": "PLAN_READY",
        "execution_status": "SIMULATED_ONLY",
    })
    assert result["status"] == "BLOCKED"
