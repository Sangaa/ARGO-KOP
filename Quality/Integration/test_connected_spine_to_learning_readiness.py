from connected_spine_runner import run
from learning_pipeline_integration import assess_for_promotion
from synthetic_task_fixture import make_fixture


def test_connected_spine_outcome_reaches_learning_readiness_without_promotion():
    result = run(make_fixture())

    assert result["execution"]["execution_trace_id"]
    assert result["outcome"]["outcome_id"]

    execution_trace_id = result["execution"]["execution_trace_id"]
    outcome = {
        **result["outcome"],
        "result": "SUCCESS",
        "evidence_trace_ids": [execution_trace_id],
        "execution_trace_ids": [execution_trace_id],
        "confidence": "HIGH",
    }

    readiness = assess_for_promotion(
        decision_id=result["decision_trace"]["trace_id"],
        execution_id=result["execution"]["execution_id"],
        outcome=outcome,
    )

    assert readiness["stage"] == "READINESS"
    assert readiness["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert readiness["report"]["knowledge_promoted"] is False


def test_connected_spine_cannot_promote_orphaned_outcome_evidence():
    result = run(make_fixture())
    execution = result["execution"]

    outcome = {
        **result["outcome"],
        "result": "SUCCESS",
        "evidence_trace_ids": ["ORPHAN-EVIDENCE"],
        "execution_trace_ids": [execution["execution_trace_id"]],
        "confidence": "HIGH",
    }

    readiness = assess_for_promotion(
        decision_id=result["decision_trace"]["trace_id"],
        execution_id=execution["execution_id"],
        outcome=outcome,
    )

    assert readiness["status"] == "NOT_READY"
    assert readiness["stage"] == "EVALUATION"
