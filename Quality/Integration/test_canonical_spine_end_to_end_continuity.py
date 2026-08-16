from connected_spine_runner import run
from learning_pipeline_integration import assess_for_promotion
from synthetic_task_fixture import make_fixture


def test_connected_spine_preserves_trace_lineage_into_outcome_evaluation_and_readiness():
    result = run(make_fixture())

    assert result["final_status"] == "SIMULATED"
    decision_trace_id = result["decision_trace"]["trace_id"]
    execution_trace_id = result["execution"]["execution_trace_id"]

    assert result["execution"]["source_trace_id"] == decision_trace_id
    assert execution_trace_id == result["outcome"]["execution_trace_ids"][0]
    assert result["outcome"]["evidence_trace_ids"] == [execution_trace_id]

    readiness = assess_for_promotion(
        decision_id=decision_trace_id,
        execution_id=result["execution"]["execution_id"],
        outcome=result["outcome"],
    )

    assert readiness["status"] == "NOT_READY"
    assert readiness["stage"] == "READINESS"
    assert readiness["quality"]["status"] == "QUALITY_ASSESSED"
    assert readiness["quality"]["quality"] == "INSUFFICIENT"
    assert readiness["report"]["knowledge_promoted"] is False


def test_unauthorized_path_does_not_enter_downstream_learning_chain():
    fixture = make_fixture()
    fixture["authorization"] = {"approved": False}
    result = run(fixture)

    assert result["stages"][5]["status"] == "BLOCKED"
    assert result["stages"][7]["status"] == "BLOCKED"
    assert result["outcome"] is None
