"""Create canonical execution-trace records from a completed execution result."""

from datetime import datetime, timezone


def record_execution_trace(
    *,
    trace_id: str,
    task_id: str,
    session_id: str,
    final_status: str,
    side_effect: bool,
    stages: list[dict],
    recorded_at: str | None = None,
) -> dict:
    """Materialize one canonical historical execution trace.

    This is a trace producer, not an executor and not an authorization path.
    It records a completed execution result without granting permission or
    promoting the trace into active state.
    """
    issues = []
    if not trace_id:
        issues.append("TRACE_ID_REQUIRED")
    if not task_id:
        issues.append("TASK_ID_REQUIRED")
    if not session_id:
        issues.append("SESSION_ID_REQUIRED")
    if not final_status:
        issues.append("FINAL_STATUS_REQUIRED")
    if not isinstance(side_effect, bool):
        issues.append("SIDE_EFFECT_BOOLEAN_REQUIRED")
    if not isinstance(stages, list) or not stages:
        issues.append("STAGES_REQUIRED")

    if issues:
        return {"status": "TRACE_REJECTED", "issues": issues}

    return {
        "status": "TRACE_RECORDED",
        "trace": {
            "trace_id": trace_id,
            "task_id": task_id,
            "session_id": session_id,
            "recorded_at": recorded_at or datetime.now(timezone.utc).isoformat(),
            "record_type": "EXECUTION_TRACE",
            "final_status": final_status,
            "side_effect": side_effect,
            "stages": stages,
        },
    }
