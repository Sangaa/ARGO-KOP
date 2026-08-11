import pytest

from reasoning_context_bridge import build_reasoning_packet


def context():
    return {
        "task_id": "TASK-003",
        "session_id": "SESSION-003",
        "project_id": "ARGO-KOP",
        "domain": "programming",
        "active_state": "learning",
        "claim": "function returns predictable result",
        "allowed_scope": "tested_claim_only",
    }


def test_bridge_creates_reasoning_ready_packet():
    result = build_reasoning_packet(context(), [{"task_id": "SYN-001", "status": "PROMOTED"}])
    assert result["reasoning_status"] == "READY"
    assert result["decision_status"] == "NOT_EVALUATED"
    assert result["execution_status"] == "NOT_REQUESTED"
    assert result["retrieved_knowledge"][0]["task_id"] == "SYN-001"


def test_bridge_fails_closed_on_incomplete_context():
    item = context()
    item["project_id"] = None
    with pytest.raises(ValueError):
        build_reasoning_packet(item, [])
