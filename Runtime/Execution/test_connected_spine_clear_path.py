from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_clear_context_preserves_normal_downstream_spine():
    fixture = make_fixture()
    result = run(fixture)

    assert result["final_status"] != "HOLD"
    assert result["stages"][3]["status"] == "CLEAR"
    assert result["stages"][4]["status"] != "BLOCKED"
    assert result["stages"][5]["status"] != "BLOCKED"
    assert result["stages"][6]["status"] != "BLOCKED"
