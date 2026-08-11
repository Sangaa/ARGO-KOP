from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_real_data_contracts_flow_between_stages():
    result = run(make_fixture())
    assert result["task_id"] == "SYN-TASK-001"
    assert result["final_status"] == "SIMULATED"
    assert result["stages"][0]["status"] == "READY_FOR_REASONING"
    assert result["stages"][1]["status"] == "REASONED"
    assert result["stages"][2]["status"] == "PROPOSAL_READY"
    assert result["stages"][3]["status"] == "AUTHORIZED"
    assert result["stages"][4]["status"] == "PLAN_READY"
    assert result["stages"][5]["side_effect"] is False


def test_missing_authorization_stops_before_execution():
    fixture = make_fixture()
    fixture["authorization"] = {"approved": False}
    result = run(fixture)
    assert result["stages"][3]["status"] == "BLOCKED"
    assert result["stages"][4]["status"] == "BLOCKED"
    assert result["stages"][5]["status"] == "BLOCKED"
