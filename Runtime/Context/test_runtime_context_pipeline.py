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
    result = evaluate_new_evidence(record(), ["contradictory-test"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
