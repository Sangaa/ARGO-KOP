from pathlib import Path

from runtime_result_persistence_adapter import persist_candidate, reread


def test_persist_and_reread_preserves_trace_identity(tmp_path: Path):
    record = {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-T-42-S-42",
        "task_id": "T-42",
        "session_id": "S-42",
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
    assert loaded["side_effect"] is False


def test_external_side_effect_record_is_rejected(tmp_path: Path):
    record = {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "TRACE-UNSAFE",
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
