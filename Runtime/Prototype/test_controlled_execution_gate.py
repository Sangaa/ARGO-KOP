"""Tests for the controlled execution gate."""

from cognitive_loop_harness import run
from controlled_execution_gate import evaluate


def payload():
    return {
        "task_id": "GATE-001",
        "session_id": "SESSION-GATE",
        "active_state": "ready_for_draft",
        "evidence": ["source:001"],
        "knowledge": ["rule:001"],
        "requested_outcome": "prepare proposal",
    }


def test_unauthorized_trace_is_held():
    trace = run(payload(), human_approved=False)
    result = evaluate(trace)
    assert result["status"] == "HOLD"
    assert result["reason"] == "AUTHORIZATION_MISSING"


def test_authorized_safe_trace_is_handoff_ready():
    trace = run(payload(), human_approved=True)
    result = evaluate(trace)
    assert result["status"] == "READY_FOR_CONTROLLED_HANDOFF"
    assert result["side_effects"] is False


def test_incomplete_trace_is_held():
    result = evaluate({"task_id": "BROKEN"})
    assert result["status"] == "HOLD"
    assert result["reason"] == "TRACE_INCOMPLETE"
