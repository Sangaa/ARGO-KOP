"""Small governed execution entrypoint for the current connectivity baseline.

This module does not grant authorization or perform arbitrary side effects. It
provides the missing runtime handoff: an authorized execution request is
recorded through the canonical execution-trace producer and returns the trace
identifier needed by downstream outcome evaluation.
"""

from uuid import uuid4

from execution_trace_producer import record_execution_trace


class ExecutionDenied(ValueError):
    """Raised when the execution request is not explicitly authorized."""


def execute(
    *,
    execution_id: str,
    task_id: str,
    session_id: str,
    source_trace_id: str,
    authorized: bool,
    final_status: str,
    side_effect: bool = False,
    stages: list[dict] | None = None,
) -> dict:
    """Record a governed execution and return its canonical trace handoff.

    The entrypoint intentionally records the execution boundary only. It does
    not infer authorization, execute arbitrary code, or promote learning.
    """
    if not authorized:
        raise ExecutionDenied("EXECUTION_NOT_AUTHORIZED")
    if not source_trace_id:
        raise ValueError("SOURCE_TRACE_REQUIRED")

    result = record_execution_trace(
        trace_id=f"TR-{uuid4().hex[:12]}",
        task_id=task_id,
        session_id=session_id,
        final_status=final_status,
        side_effect=side_effect,
        stages=stages or [],
    )
    if result.get("status") != "TRACE_RECORDED":
        raise ValueError(f"TRACE_RECORDING_FAILED: {result.get('issues', [])}")

    trace = result["trace"]
    return {
        "execution_id": execution_id,
        "source_trace_id": source_trace_id,
        "execution_trace_id": trace["trace_id"],
        "trace": trace,
    }
