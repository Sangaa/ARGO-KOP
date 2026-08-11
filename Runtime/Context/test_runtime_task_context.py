import pytest

from runtime_task_context import build_context


def state():
    return {
        "task_id": "TASK-002",
        "session_id": "SESSION-002",
        "project_id": "ARGO-KOP",
        "domain": "programming",
        "active_state": "learning",
        "claim": "function returns predictable result",
        "allowed_scope": "tested_claim_only",
    }


def test_runtime_state_builds_context():
    context = build_context(state())
    assert context["project_id"] == "ARGO-KOP"
    assert context["active_state"] == "learning"


def test_incomplete_runtime_state_fails_closed():
    item = state()
    item["allowed_scope"] = None
    with pytest.raises(ValueError):
        build_context(item)
