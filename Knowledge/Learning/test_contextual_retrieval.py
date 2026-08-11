from contextual_retrieval import retrieve_in_context


def records():
    return [
        {
            "task_id": "SYN-001",
            "project_id": "ARGO-KOP",
            "status": "PROMOTED",
            "pattern": "validated function accepts inputs and returns a predictable result",
            "knowledge_scope": "tested_claim_only",
        },
        {
            "task_id": "OTHER-001",
            "project_id": "OTHER-PROJECT",
            "status": "PROMOTED",
            "pattern": "validated function accepts inputs and returns a predictable result",
            "knowledge_scope": "tested_claim_only",
        },
    ]


def context():
    return {
        "task_id": "TASK-002",
        "session_id": "SESSION-002",
        "project_id": "ARGO-KOP",
        "domain": "programming",
        "active_state": "learning",
        "claim": "function returns predictable result",
        "allowed_scope": "tested_claim_only",
    }


def test_context_limits_retrieval_to_project():
    result = retrieve_in_context(records(), context())
    assert [item["task_id"] for item in result] == ["SYN-001"]


def test_missing_context_does_not_widen_retrieval():
    item = context()
    item["allowed_scope"] = None
    assert retrieve_in_context(records(), item) == []
