from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_clear_path_preserves_identity_to_simulated_execution():
    fixture = make_fixture()
    result = run(fixture)

    assert result["task_id"] == fixture["task"]["task_id"]
    assert result["stages"][0]["task_id"] == fixture["context"]["task_id"]
    assert result["stages"][5]["authorization_id"] == fixture["authorization"]["authorization_id"]
    assert result["stages"][6]["status"] == "PLAN_READY"
    assert result["stages"][7]["status"] == "SIMULATED"
    assert result["stages"][7]["side_effect"] is False


def test_hold_path_preserves_task_identity():
    fixture = make_fixture()
    fixture["context"]["unresolved_questions"] = ["Which vessel is confirmed?"]

    result = run(fixture)

    assert result["task_id"] == fixture["task"]["task_id"]
    assert result["final_status"] == "HOLD"
    assert all(stage["status"] == "BLOCKED" for stage in result["stages"][4:])
