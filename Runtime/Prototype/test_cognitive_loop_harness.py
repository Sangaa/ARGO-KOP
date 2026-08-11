"""Acceptance tests for the safe cognitive-loop harness."""

from cognitive_loop_harness import run


def base_payload():
    return {
        "task_id": "TEST-001",
        "session_id": "SESSION-TEST",
        "active_state": "awaiting_customer_response",
        "evidence": ["email:test:001"],
        "knowledge": ["rule:test-response"],
        "requested_outcome": "prepare a response draft",
    }


def test_requires_human_authorization():
    result = run(base_payload(), human_approved=False)
    assert result["authorization"]["approved"] is False
    assert result["action"]["status"] == "NOT_EXECUTED"
    assert result["result"]["external_side_effect"] is False


def test_authorized_run_only_proposes_safe_action():
    result = run(base_payload(), human_approved=True)
    assert result["state"] == "PROPOSED"
    assert result["action"]["status"] == "PROPOSED"
    assert result["action"]["proposal"]["side_effects"] is False
    assert result["result"]["executed"] is False


def test_missing_evidence_holds():
    payload = base_payload()
    payload["evidence"] = []
    result = run(payload, human_approved=True)
    assert result["state"] == "HOLD"
    assert result["result"]["executed"] is False


def test_trace_preserves_pipeline_stages():
    result = run(base_payload(), human_approved=True)
    for key in ("context", "reasoning", "decision", "validation", "authorization", "action", "result"):
        assert key in result
