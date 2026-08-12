from connected_spine_runner import run
from synthetic_task_fixture import make_fixture
from runtime_result_persistence_adapter import persist_candidate, reread
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence


def test_connected_spine_trace_can_be_materialized_and_reread(tmp_path):
    fixture = make_fixture()
    result = run(fixture)
    trace = result["execution"]["trace"]

    target = tmp_path / "execution_trace.json"
    persisted = persist_candidate(trace, str(target))
    reread_result = reread(str(target))
    lineage = verify_runtime_outcome_evidence(result)

    assert persisted["status"] == "PERSISTED"
    assert persisted["trace_id"] == result["execution"]["execution_trace_id"]
    assert reread_result["status"] == "RE_READ"
    assert reread_result["trace_id"] == trace["trace_id"]
    assert reread_result["record_type"] == "EXECUTION_TRACE"
    assert reread_result["task_id"] == result["task_id"]
    assert reread_result["session_id"] == fixture["context"]["session_id"]
    assert reread_result["side_effect"] is False
    assert result["outcome"]["execution_trace_ids"] == [trace["trace_id"]]
    assert result["outcome"]["evidence_trace_ids"] == [trace["trace_id"]]
    assert lineage["status"] == "VERIFIED"
    assert lineage["execution_trace_id"] == trace["trace_id"]
