from execution_entrypoint import execute
from learning_pipeline_integration import assess_for_promotion


def test_governed_execution_trace_reaches_learning_readiness():
    execution = execute(
        execution_id="EXEC-LIVE-1",
        task_id="TASK-LIVE-1",
        session_id="SESSION-LIVE-1",
        source_trace_id="DECISION-TRACE-1",
        authorized=True,
        final_status="SUCCESS",
        stages=[{"name": "execute", "status": "SUCCESS"}],
    )
    trace_id = execution["execution_trace_id"]

    result = assess_for_promotion(
        decision_id="DEC-1",
        execution_id=execution["execution_id"],
        outcome={
            "outcome_id": "OUT-LIVE-1",
            "result": "SUCCESS",
            "evidence_trace_ids": [trace_id],
            "execution_trace_ids": [trace_id],
            "confidence": "HIGH",
        },
    )

    assert result["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert result["report"]["knowledge_promoted"] is False
