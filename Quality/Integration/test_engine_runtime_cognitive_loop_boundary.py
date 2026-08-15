"""Cross-layer integration proof for the safe Engine -> Runtime cognitive loop prototype."""

from Runtime.Prototype.cognitive_loop_harness import run


def _payload():
    return {
        "task_id": "INTEGRATION-ENG-RUN-001",
        "session_id": "SESSION-INTEGRATION-001",
        "active_state": "awaiting_review",
        "evidence": ["evidence:integration:001"],
        "knowledge": ["rule:integration-safe-proposal"],
        "requested_outcome": "prepare a non-destructive repository proposal",
    }


def test_engine_runtime_loop_preserves_all_governed_stages_without_side_effects():
    result = run(_payload(), human_approved=True)

    assert result["state"] == "PROPOSED"
    assert result["context"]["task_id"] == "INTEGRATION-ENG-RUN-001"
    assert result["reasoning"]["status"] == "READY"
    assert result["decision"]["status"] == "CANDIDATE"
    assert result["validation"]["status"] == "VALIDATED"
    assert result["authorization"]["status"] == "AUTHORIZED"
    assert result["action"]["status"] == "PROPOSED"
    assert result["action"]["proposal"]["side_effects"] is False
    assert result["result"]["executed"] is False
    assert result["result"]["external_side_effect"] is False


def test_engine_runtime_loop_holds_before_execution_without_authorization():
    result = run(_payload(), human_approved=False)

    assert result["state"] == "HOLD"
    assert result["authorization"]["status"] == "HOLD"
    assert result["action"]["status"] == "NOT_EXECUTED"
    assert result["result"]["executed"] is False
    assert result["result"]["external_side_effect"] is False


def test_engine_runtime_loop_trace_is_complete_at_prototype_boundary():
    result = run(_payload(), human_approved=True)

    required = (
        "context",
        "reasoning",
        "decision",
        "validation",
        "authorization",
        "action",
        "result",
    )
    assert all(stage in result for stage in required)
    assert result["task_id"] == result["context"]["task_id"]
