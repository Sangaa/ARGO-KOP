"""Capture controlled runtime evidence into an explicit governed target.

The adapter never mutates canonical Memory implicitly. Temporary targets remain
valid for tests; repository-backed capture is available only through the
explicit ``capture_repository_evidence`` boundary.
"""

from pathlib import Path, PurePosixPath

from runtime_result_persistence_adapter import persist_candidate, reread

_REPOSITORY_EVIDENCE_ROOT = PurePosixPath("Quality/Integration/evidence/runtime")


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


def capture_repository_evidence(runtime_result: dict, repository_root: str, relative_name: str) -> dict:
    """Capture runtime evidence only beneath the governed repository evidence root."""
    relative = PurePosixPath(relative_name)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        return {"status": "HOLD", "reason": "INVALID_EVIDENCE_TARGET"}

    governed = _REPOSITORY_EVIDENCE_ROOT / relative
    target = Path(repository_root) / Path(*governed.parts)
    result = capture_execution_evidence(runtime_result, str(target))
    if result.get("status") != "CAPTURED":
        return result

    result["repository_relative_path"] = governed.as_posix()
    return result
