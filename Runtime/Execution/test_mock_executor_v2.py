from mock_executor_v2 import execute


def test_authorized_plan_is_simulated_without_side_effect():
    result = execute({
        "status": "PLAN_READY",
        "action": "DRAFT_RESPONSE",
        "target": "customer",
        "authorization_id": "AUTH-001",
    })
    assert result["status"] == "SIMULATED"
    assert result["side_effect"] is False


def test_unapproved_plan_is_blocked():
    result = execute({"status": "BLOCKED", "action": "SEND_EMAIL"})
    assert result["status"] == "BLOCKED"
