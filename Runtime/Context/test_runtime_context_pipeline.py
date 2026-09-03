from runtime_context_pipeline import evaluate_new_evidence, prepare_task


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


def record():
    return {
        "task_id": "SYN-001",
        "project_id": "ARGO-KOP",
        "status": "PROMOTED",
        "pattern": "validated function accepts inputs and returns a predictable result",
        "knowledge_scope": "tested_claim_only",
    }


def test_runtime_pipeline_builds_context_and_retrieves():
    result = prepare_task(state(), [record()])
    assert result["context"]["project_id"] == "ARGO-KOP"
    assert [item["task_id"] for item in result["knowledge"]] == ["SYN-001"]


def test_runtime_pipeline_keeps_contradiction_governed():
    original = record()
    snapshot = dict(original)
    result = evaluate_new_evidence(original, ["contradictory-test"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
    assert original == snapshot


def test_runtime_pipeline_holds_unsupported_review_inputs():
    original = record()
    snapshot = dict(original)
    result = evaluate_new_evidence(original, [], contradiction=True)
    assert result["status"] == "HOLD"
    assert result["reason"] == "INVALID_EVIDENCE"
    assert original == snapshot

    result = evaluate_new_evidence(original, ["proof"], contradiction="true")
    assert result["status"] == "HOLD"
    assert result["reason"] == "INVALID_CONTRADICTION_SIGNAL"
    assert original == snapshot
