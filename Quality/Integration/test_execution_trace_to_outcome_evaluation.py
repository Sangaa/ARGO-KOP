from connected_spine_runner import run
from outcome_evaluator import evaluate_outcome
from synthetic_task_fixture import make_fixture


def test_execution_trace_to_outcome_evaluation_preserves_runtime_provenance():
    result = run(make_fixture())
    execution = result["execution"]
    outcome = result["outcome"]

    assert execution["execution_trace_id"]
    assert outcome["execution_trace_ids"] == [execution["execution_trace_id"]]
    assert outcome["evidence_trace_ids"] == [execution["execution_trace_id"]]

    evaluated = evaluate_outcome(
        decision_id=result["decision_trace"]["trace_id"],
        execution_id=execution["execution_id"],
        outcome=outcome,
    )

    assert evaluated["status"] == "EVALUATED"
    assert evaluated["execution_trace_ids"] == [execution["execution_trace_id"]]
    assert evaluated["evidence_trace_ids"] == [execution["execution_trace_id"]]
    assert evaluated["learning_eligible"] is False


def test_outcome_evaluation_rejects_orphaned_evidence_trace():
    result = run(make_fixture())
    execution = result["execution"]
    outcome = dict(result["outcome"])
    outcome["evidence_trace_ids"] = ["TRACE-NOT-IN-EXECUTION"]

    evaluated = evaluate_outcome(
        decision_id=result["decision_trace"]["trace_id"],
        execution_id=execution["execution_id"],
        outcome=outcome,
    )

    assert evaluated["status"] == "EVALUATION_REJECTED"
    assert "OUTCOME_PROVENANCE_BROKEN" in evaluated["issues"]
