from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_real_data_contracts_flow_between_stages():
    result = run(make_fixture())
    assert result["task_id"] == "SYN-TASK-001"
    assert result["final_status"] == "SIMULATED"
    assert result["stages"][0]["status"] == "READY_FOR_REASONING"
    assert result["stages"][1]["status"] == "REASONED"
    assert result["stages"][4]["status"] == "PROPOSAL_READY"
    assert result["stages"][5]["status"] == "AUTHORIZED"
    assert result["stages"][6]["status"] == "PLAN_READY"
    assert result["stages"][7]["execution_trace_id"] == result["stages"][7]["trace"]["trace_id"]
    assert result["stages"][7]["trace"]["record_type"] == "EXECUTION_TRACE"
    assert result["stages"][7]["trace"]["side_effect"] is False
    assert result["decision_trace"]["record_type"] == "DECISION_TRACE"
    assert result["stages"][7]["source_trace_id"] == result["decision_trace"]["trace_id"]

    assert result["execution"]["execution_trace_id"] == result["outcome"]["execution_trace_ids"][0]
    assert result["outcome"]["evidence_trace_ids"] == result["outcome"]["execution_trace_ids"]
    assert result["outcome"]["result"] == "INCONCLUSIVE"
    assert result["outcome"]["confidence"] == "UNKNOWN"


def test_missing_authorization_stops_before_execution_and_outcome():
    fixture = make_fixture()
    fixture["authorization"] = {"approved": False}
    result = run(fixture)
    assert result["stages"][5]["status"] == "BLOCKED"
    assert result["stages"][6]["status"] == "BLOCKED"
    assert result["stages"][7]["status"] == "BLOCKED"
    assert result["outcome"] is None
