from knowledge_retrieval import retrieve
from knowledge_correction import assess_contradiction


def promoted_record():
    return {
        "task_id": "SYN-001",
        "status": "PROMOTED",
        "pattern": "validated function accepts inputs and returns a predictable result",
        "knowledge_scope": "tested_claim_only",
        "evidence": ["SYNTHETIC_LEARNING_EVIDENCE_001.md"],
    }


def test_promoted_knowledge_is_reusable():
    result = retrieve([promoted_record()], claim="function returns predictable result")
    assert len(result) == 1
    assert result[0]["task_id"] == "SYN-001"


def test_reuse_does_not_expand_scope():
    result = retrieve([promoted_record()], claim="function returns predictable result", scope="unrelated_scope")
    assert result == []


def test_contradiction_enters_review_without_mutation():
    record = promoted_record()
    result = assess_contradiction(record, evidence=["SYN-REUSE-CONTRADICTION-001"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
    assert record["status"] == "PROMOTED"
