from connected_spine_runner import run
from synthetic_task_fixture import make_fixture


def test_clear_context_reaches_existing_gates():
    result = run(make_fixture())
    statuses = [stage.get("status") for stage in result["stages"]]
    assert result["final_status"] == "SIMULATED"
    assert "PROPOSAL_READY" in statuses
    assert "SIMULATED" in statuses


def test_conflict_context_halts_before_proposal():
    fixture = make_fixture()
    fixture["context"]["current_facts"] = [{"claim": "shipment pending"}]
    fixture["context"]["historical_evidence"] = [{"claim": "shipment pending"}]
    result = run(fixture)
    statuses = [stage.get("status") for stage in result["stages"]]
    assert result["final_status"] == "HOLD"
    assert "HOLD" in statuses
    assert "PROPOSAL_READY" not in statuses
    assert statuses[-1] == "BLOCKED"


def test_unrelated_history_does_not_trigger_hold():
    fixture = make_fixture()
    fixture["context"]["current_facts"] = [{"claim": "shipment delivered"}]
    fixture["context"]["historical_evidence"] = [{"claim": "shipment pending"}]
    result = run(fixture)
    assert result["final_status"] == "SIMULATED"
