from pathlib import Path

from runtime_result_persistence_adapter import persist_candidate, reread


def test_persist_and_reread_preserves_trace_identity(tmp_path: Path):
    record = {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-T-42-S-42",
        "task_id": "T-42",
        "session_id": "S-42",
        "final_status": "SIMULATED",
        "side_effect": False,
    }

    target = tmp_path / "trace.json"
    result = persist_candidate(record, str(target))
    assert result["status"] == "PERSISTED"

    loaded = reread(str(target))
    assert loaded["status"] == "RE_READ"
    assert loaded["trace_id"] == "TRACE-T-42-S-42"
    assert loaded["task_id"] == "T-42"
    assert loaded["session_id"] == "S-42"
    assert loaded["final_status"] == "SIMULATED"
    assert loaded["side_effect"] is False


def test_external_side_effect_record_is_rejected(tmp_path: Path):
    record = {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-UNSAFE",
        "task_id": "T-UNSAFE",
        "session_id": "S-UNSAFE",
        "final_status": "EXTERNAL",
        "side_effect": True,
    }

    result = persist_candidate(record, str(tmp_path / "unsafe.json"))
    assert result["status"] == "HOLD"
    assert result["reason"] == "EXTERNAL_SIDE_EFFECT_NOT_ALLOWED"


def test_non_trace_record_is_rejected(tmp_path: Path):
    result = persist_candidate(
        {"record_type": "KNOWLEDGE", "trace_id": "K-1"},
        str(tmp_path / "invalid.json"),
    )
    assert result["status"] == "HOLD"
    assert result["reason"] == "INVALID_RECORD_TYPE"


def test_incomplete_trace_identity_is_not_materialized(tmp_path: Path):
    target = tmp_path / "incomplete.json"
    result = persist_candidate(
        {
            "record_type": "EXECUTION_TRACE",
            "trace_id": "TRACE-INCOMPLETE",
            "task_id": "T-INCOMPLETE",
            "session_id": "",
            "side_effect": False,
        },
        str(target),
    )
    assert result == {
        "status": "HOLD",
        "reason": "TRACE_IDENTITY_INCOMPLETE",
        "missing": ["session_id", "final_status"],
    }
    assert not target.exists()


def test_unknown_side_effect_state_is_not_materialized(tmp_path: Path):
    target = tmp_path / "unknown-safety.json"
    result = persist_candidate(
        {
            "record_type": "EXECUTION_TRACE",
            "trace_id": "TRACE-UNKNOWN",
            "task_id": "T-UNKNOWN",
            "session_id": "S-UNKNOWN",
            "final_status": "SIMULATED",
        },
        str(target),
    )
    assert result == {"status": "HOLD", "reason": "SIDE_EFFECT_STATE_REQUIRED"}
    assert not target.exists()


def test_reread_fails_closed_for_malformed_trace(tmp_path: Path):
    target = tmp_path / "malformed.json"
    target.write_text('{"record_type": "EXECUTION_TRACE"}\n', encoding="utf-8")
    result = reread(str(target))
    assert result["status"] == "HOLD"
    assert result["reason"] == "TRACE_IDENTITY_INCOMPLETE"
