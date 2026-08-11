from knowledge_retrieval import retrieve


def records():
    return [
        {
            "status": "PROMOTED",
            "pattern": "validated function accepts inputs and returns a predictable result",
            "knowledge_scope": "tested_claim_only",
            "task_id": "SYN-001",
        },
        {
            "status": "CANDIDATE",
            "pattern": "unvalidated candidate must not be retrieved as knowledge",
            "knowledge_scope": "tested_claim_only",
            "task_id": "SYN-002",
        },
    ]


def test_retrieval_uses_promoted_records_only():
    result = retrieve(records(), claim="function returns predictable result")
    assert [item["task_id"] for item in result] == ["SYN-001"]


def test_retrieval_can_enforce_scope():
    result = retrieve(records(), claim="function returns predictable result", scope="other_scope")
    assert result == []
