from connected_spine_runner import run
from runtime_evidence_capture import capture_execution_evidence
from synthetic_task_fixture import make_fixture


def test_capture_uses_exact_runtime_trace(tmp_path):
    result = run(make_fixture())
    target = tmp_path / "runtime_execution_trace.json"

    captured = capture_execution_evidence(result, str(target))

    assert captured["status"] == "CAPTURED"
    assert captured["trace_id"] == result["execution"]["execution_trace_id"]
    assert captured["record_type"] == "EXECUTION_TRACE"
    assert captured["task_id"] == result["task_id"]
    assert captured["session_id"] == result["execution"]["trace"]["session_id"]


def test_capture_holds_when_runtime_trace_is_missing(tmp_path):
    target = tmp_path / "runtime_execution_trace.json"

    captured = capture_execution_evidence({"execution": {}}, str(target))

    assert captured == {"status": "HOLD", "reason": "MISSING_RUNTIME_TRACE"}
