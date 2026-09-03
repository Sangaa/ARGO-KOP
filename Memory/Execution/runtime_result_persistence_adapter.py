"""Experimental persistence adapter for runtime results.

This adapter deliberately writes to an explicit target supplied by the caller;
it never mutates canonical Memory implicitly.
"""

from pathlib import Path
import json


REQUIRED_TRACE_IDENTITY = ("trace_id", "task_id", "session_id", "final_status")


def _validation_hold(record: dict) -> dict | None:
    if record.get("record_type") != "EXECUTION_TRACE":
        return {"status": "HOLD", "reason": "INVALID_RECORD_TYPE"}

    missing = [
        field
        for field in REQUIRED_TRACE_IDENTITY
        if not isinstance(record.get(field), str) or not record[field].strip()
    ]
    if missing:
        return {"status": "HOLD", "reason": "TRACE_IDENTITY_INCOMPLETE", "missing": missing}

    if not isinstance(record.get("side_effect"), bool):
        return {"status": "HOLD", "reason": "SIDE_EFFECT_STATE_REQUIRED"}
    if record["side_effect"] is True:
        return {"status": "HOLD", "reason": "EXTERNAL_SIDE_EFFECT_NOT_ALLOWED"}
    return None


def persist_candidate(record: dict, target: str) -> dict:
    hold = _validation_hold(record)
    if hold:
        return hold

    path = Path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    persisted = {
        "status": "PERSISTED",
        "path": str(path),
        "trace_id": record.get("trace_id"),
    }
    return persisted


def reread(path: str) -> dict:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {"status": "HOLD", "reason": "RE_READ_FAILED"}

    if not isinstance(data, dict):
        return {"status": "HOLD", "reason": "RE_READ_INVALID_RECORD"}
    hold = _validation_hold(data)
    if hold:
        return hold

    return {
        "status": "RE_READ",
        "trace_id": data["trace_id"],
        "record_type": data["record_type"],
        "task_id": data["task_id"],
        "session_id": data["session_id"],
        "final_status": data["final_status"],
        "side_effect": data["side_effect"],
    }
