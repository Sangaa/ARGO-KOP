"""Negative integration proof: prototype authorization is not execution authority."""

import pytest

from Runtime.Execution.run010_handoff_contract import build_handoff_candidate
from Runtime.Prototype.cognitive_loop_harness import run


def _payload():
    return {
        "task_id": "RUN010-AUTH-BOUNDARY-001",
        "session_id": "SESSION-RUN010-AUTH-001",
        "active_state": "awaiting_review",
        "evidence": ["evidence:run010:auth-boundary-001"],
        "knowledge": ["rule:controlled-handoff"],
        "requested_outcome": "prepare a non-destructive repository proposal",
    }


def test_prototype_authorization_does_not_supply_execution_authorization_id():
    result = run(_payload(), human_approved=True)

    assert result["authorization"]["status"] == "AUTHORIZED"
    assert "authorization_id" not in result["authorization"]
    assert result["result"]["executed"] is False


def test_handoff_contract_fails_closed_when_prototype_authorization_id_is_absent():
    result = run(_payload(), human_approved=True)

    execution = {
        "execution_id": "EXEC-RUN010-AUTH-001",
        "task_id": result["task_id"],
        "session_id": result["context"]["session_id"],
        "source_trace_id": "TRACE-RUN010-AUTH-001",
        "trace": {
            "record_type": "EXECUTION_TRACE",
            "task_id": result["task_id"],
            "session_id": result["context"]["session_id"],
        },
    }

    with pytest.raises(ValueError, match="HANDOFF_AUTHORIZATION_ID_REQUIRED"):
        build_handoff_candidate(
            execution,
            result["authorization"],
            path="Repository/test.txt",
            content="boundary-test",
            purpose="prove authorization boundary",
            necessity_evidence="test-only negative boundary",
            commit_message="test: authorization id boundary",
        )
