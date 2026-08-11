"""Experimental persistence adapter for runtime results.

This adapter deliberately writes to an explicit target supplied by the caller;
it never mutates canonical Memory implicitly.
"""

from pathlib import Path
import json


def persist_candidate(record: dict, target: str) -> dict:
    if record.get("record_type") != "EXECUTION_TRACE":
        return {"status": "HOLD", "reason": "INVALID_RECORD_TYPE"}
    if record.get("side_effect") is True:
        return {"status": "HOLD", "reason": "EXTERNAL_SIDE_EFFECT_NOT_ALLOWED"}

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
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {
        "status": "RE_READ",
        "trace_id": data.get("trace_id"),
        "record_type": data.get("record_type"),
        "task_id": data.get("task_id"),
        "session_id": data.get("session_id"),
        "side_effect": data.get("side_effect", False),
    }
