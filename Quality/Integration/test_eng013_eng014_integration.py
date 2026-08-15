"""Bounded integration proof for ENG-013/ENG-014 cognitive execution loop."""

from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_eng013_eng014_safe_loop_acceptance_path():
    result = run(make_fixture())

    assert result["final_status"] == "SIMULATED"
    assert result["stages"][0]["status"] == "READY_FOR_REASONING"
    assert result["stages"][1]["status"] == "REASONED"
    assert result["stages"][4]["status"] == "PROPOSAL_READY"
    assert result["stages"][5]["status"] == "AUTHORIZED"
    assert result["stages"][6]["status"] == "PLAN_READY"

    execution = result["execution"]
    assert execution["execution_trace_id"] == execution["trace"]["trace_id"]
    assert execution["trace"]["record_type"] == "EXECUTION_TRACE"
    assert execution["trace"]["side_effect"] is False
    assert execution["source_trace_id"] == result["decision_trace"]["trace_id"]
    assert result["outcome"]["execution_trace_ids"] == [execution["execution_trace_id"]]


def test_eng013_eng014_authorization_failure_halts_before_execution():
    fixture = make_fixture()
    fixture["authorization"] = {"approved": False}

    result = run(fixture)

    assert result["stages"][5]["status"] == "BLOCKED"
    assert result["stages"][6]["status"] == "BLOCKED"
    assert result["stages"][7]["status"] == "BLOCKED"
    assert result["outcome"] is None
