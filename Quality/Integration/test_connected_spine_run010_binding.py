from Runtime.Execution.connected_spine_runner import run


def _fixture(consumer):
    return {
        "context": {"session_id": "P312", "signal": "clean"},
        "knowledge": {"facts": ["fixture"]},
        "rules": {"mode": "governed"},
        "authorization": {"approved": True},
        "task": {"task_id": "RUN-010"},
        "eng006_consumer": consumer,
    }


def test_run010_connected_spine_dispatches_authorized_consumer_and_preserves_trace():
    seen = {}

    def consumer(payload):
        seen.update(payload)
        return {"status": "ENG006_ACCEPTED", "execution_trace_id": "EXEC-P312"}

    result = run(_fixture(consumer))
    assert result["execution"]["status"] == "ENG006_ACCEPTED"
    assert result["execution"]["consumer_boundary"] == "RUN-010→ENG-006"
    assert result["execution"]["source_trace_id"] == result["decision_trace"]["trace_id"]
    assert seen["source_trace_id"] == result["decision_trace"]["trace_id"]


def test_run010_without_consumer_remains_simulated_and_does_not_claim_connectivity():
    fixture = _fixture(None)
    fixture.pop("eng006_consumer")
    result = run(fixture)
    assert result["final_status"] == "SIMULATED"
    assert result["execution"]["side_effect"] is False
