from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_context_conflict_halts_connected_spine_before_decision():
    fixture = make_fixture()
    fixture["context"]["historical_evidence"] = [{"claim": "shipment is pending"}]
    fixture["context"]["current_facts"] = [{"claim": "shipment is pending"}]

    result = run(fixture)

    assert result["final_status"] == "HOLD"
    assert result["stages"][3]["status"] == "HOLD"
    assert result["stages"][4]["status"] == "BLOCKED"
    assert result["stages"][5]["status"] == "BLOCKED"
    assert result["stages"][6]["status"] == "BLOCKED"
