from connected_spine_runner import run
from learning_pipeline_integration import assess_for_promotion
from synthetic_task_fixture import make_fixture


def test_connected_spine_output_is_consumed_by_learning_pipeline():
    result = run(make_fixture())
    assert result["outcome"] is not None

    learning = assess_for_promotion(
        decision_id=result["decision_trace"]["trace_id"],
        execution_id=result["execution"]["execution_id"],
        outcome=result["outcome"],
    )

    assert learning["evaluation"]["status"] == "EVALUATED"
    assert learning["evaluation"]["execution_trace_ids"] == [
        result["execution"]["execution_trace_id"]
    ]
    assert learning["evaluation"]["evidence_trace_ids"] == [
        result["execution"]["execution_trace_id"]
    ]
    assert learning["quality"]["status"] == "QUALITY_ASSESSED"
    assert learning["quality"]["learning_ready"] is False
    assert learning["report"]["knowledge_promoted"] is False
