from pathlib import Path

from connected_spine_runner import run
from runtime_evidence_capture import capture_repository_evidence
from synthetic_task_fixture import make_fixture


def test_repository_evidence_capture_materializes_under_governed_root(tmp_path):
    result = run(make_fixture())

    captured = capture_repository_evidence(
        result,
        str(tmp_path),
        "connected_spine_execution_trace.json",
    )

    assert captured["status"] == "CAPTURED"
    assert captured["repository_relative_path"] == (
        "Quality/Integration/evidence/runtime/connected_spine_execution_trace.json"
    )
    assert captured["trace_id"] == result["execution"]["execution_trace_id"]

    target = Path(tmp_path) / captured["repository_relative_path"]
    assert target.exists()


def test_repository_evidence_capture_rejects_traversal(tmp_path):
    result = run(make_fixture())

    captured = capture_repository_evidence(result, str(tmp_path), "../escape.json")

    assert captured == {"status": "HOLD", "reason": "INVALID_EVIDENCE_TARGET"}
