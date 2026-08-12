import json

from connected_spine_runner import run
from runtime_evidence_capture import capture_execution_evidence
from verified_seam_evidence_registry import register


def _fixture():
    return {
        "context": {"session_id": "SES-EVIDENCE-001", "topic": "controlled review"},
        "knowledge": {"source": "integration-fixture"},
        "task": {"task_id": "TASK-EVIDENCE-001"},
        "rules": {"allow_simulated_review": True},
        "authorization": {"approved": True},
    }


def test_actual_runtime_trace_can_form_registry_ready_evidence_set(tmp_path):
    result = run(_fixture())
    assert result["execution"]["execution_trace_id"]
    assert result["outcome"]["execution_trace_ids"] == [result["execution"]["execution_trace_id"]]

    target = tmp_path / "evidence_trace.json"
    captured = capture_execution_evidence(result, str(target))
    assert captured["status"] == "CAPTURED"
    assert captured["record_type"] == "EXECUTION_TRACE"

    payload = json.loads(target.read_text(encoding="utf-8"))
    assert payload["trace_id"] == result["execution"]["execution_trace_id"]

    registry = register([
        {
            "seam": "Execution -> Execution Trace",
            "contract": "Runtime/Execution/execution_trace_producer.py",
            "test": "Quality/Integration/test_runtime_to_registry_evidence_set.py",
            "trace": "evidence_trace.json",
            "verification_status": "VERIFIED",
        }
    ])
    assert registry["Execution -> Execution Trace"]["state"] == "CONNECTED"
