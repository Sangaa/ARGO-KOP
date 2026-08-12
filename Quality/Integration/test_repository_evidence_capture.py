from runtime_evidence_capture import capture_repository_evidence


def test_repository_capture_rejects_path_traversal():
    result = capture_repository_evidence(
        {"execution": {"trace": {}}},
        "/repo",
        "../outside.json",
    )
    assert result == {"status": "HOLD", "reason": "INVALID_EVIDENCE_TARGET"}


def test_repository_capture_uses_governed_evidence_root(tmp_path):
    trace = {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "trace-001",
        "task_id": "task-001",
        "session_id": "session-001",
        "final_status": "COMPLETED",
        "side_effect": False,
    }
    result = capture_repository_evidence(
        {
            "task_id": "task-001",
            "execution": {
                "execution_trace_id": "trace-001",
                "trace": trace,
            },
        },
        str(tmp_path),
        "checkpoint-001.json",
    )
    assert result["status"] == "CAPTURED"
    assert result["repository_relative_path"] == "Quality/Integration/evidence/runtime/checkpoint-001.json"
