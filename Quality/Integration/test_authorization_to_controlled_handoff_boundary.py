"""Direct integration proof for Authorization -> Controlled Handoff safety gate."""

from Runtime.Prototype.cognitive_loop_harness import run


def _payload():
    return {
        "task_id": "INTEGRATION-AUTH-HANDOFF-001",
        "session_id": "SESSION-INTEGRATION-AUTH-001",
        "active_state": "awaiting_review",
        "evidence": ["evidence:integration:auth-handoff-001"],
        "knowledge": ["rule:integration-safe-handoff"],
        "requested_outcome": "prepare a non-destructive repository proposal",
    }


def test_authorization_is_required_before_controlled_handoff():
    result = run(_payload(), human_approved=False)

    assert result["state"] == "HOLD"
    assert result["authorization"]["status"] == "HOLD"
    assert result["action"]["status"] == "NOT_EXECUTED"
    assert result["result"]["executed"] is False
    assert result["result"]["external_side_effect"] is False


def test_authorized_prototype_reaches_proposal_only_not_execution():
    result = run(_payload(), human_approved=True)

    assert result["authorization"]["status"] == "AUTHORIZED"
    assert result["action"]["status"] == "PROPOSED"
    assert result["action"]["proposal"]["side_effects"] is False
    assert result["result"]["executed"] is False
    assert result["result"]["external_side_effect"] is False


def test_controlled_handoff_preserves_trace_identity_and_non_execution():
    payload = _payload()
    result = run(payload, human_approved=True)

    assert result["task_id"] == result["context"]["task_id"] == payload["task_id"]
    assert result["context"]["session_id"] == payload["session_id"]
    assert all(stage in result for stage in ("context", "reasoning", "decision", "validation", "authorization", "action", "result"))
    assert result["result"]["executed"] is False
