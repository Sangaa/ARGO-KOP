"""Capture a controlled runtime result into an explicit audit-evidence target.

This is deliberately a thin adapter: it reuses the existing runtime result
persistence adapter and never writes to canonical Memory implicitly.
"""

from pathlib import Path

from runtime_result_persistence_adapter import persist_candidate, reread


def capture_execution_evidence(runtime_result: dict, target: str) -> dict:
    """Persist and re-read the exact runtime-produced execution trace."""
    execution = runtime_result.get("execution", {})
    trace = execution.get("trace")
    if not isinstance(trace, dict):
        return {"status": "HOLD", "reason": "MISSING_RUNTIME_TRACE"}

    persisted = persist_candidate(trace, target)
    if persisted.get("status") != "PERSISTED":
        return persisted

    reread_result = reread(str(Path(target)))
    if reread_result.get("trace_id") != execution.get("execution_trace_id"):
        return {"status": "HOLD", "reason": "TRACE_ID_MISMATCH"}

    return {
        "status": "CAPTURED",
        "path": persisted["path"],
        "trace_id": persisted["trace_id"],
        "record_type": reread_result.get("record_type"),
        "task_id": reread_result.get("task_id"),
        "session_id": reread_result.get("session_id"),
    }
