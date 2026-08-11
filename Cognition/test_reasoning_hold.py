from reasoning_hold import evaluate


def test_unresolved_conflict_blocks_downstream_actions():
    result = evaluate({"requires_reasoning": True})
    assert result["status"] == "HOLD"
    assert result["decision_allowed"] is False
    assert result["authorization_allowed"] is False
    assert result["execution_allowed"] is False


def test_clear_context_can_continue_to_decision_but_not_authorization():
    result = evaluate({"requires_reasoning": False})
    assert result["status"] == "CLEAR"
    assert result["decision_allowed"] is True
    assert result["authorization_allowed"] is False
    assert result["execution_allowed"] is False
