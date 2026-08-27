"""Isolated upstream consumer seam for RUN-010 -> ENG-006.

This adapter deliberately accepts an injected ENG-006 callable. It does not
change the connected spine runner or grant authorization. The caller must
supply an already-authorized candidate; production promotion remains gated by
CI and full trace validation.
"""
from __future__ import annotations

from typing import Any, Callable


class ConsumerBoundaryError(RuntimeError):
    """Explicit upstream handoff failure."""


def dispatch_run010(
    *,
    candidate: dict[str, Any],
    eng006_consumer: Callable[[dict[str, Any]], dict[str, Any]],
) -> dict[str, Any]:
    if candidate.get("task_id") != "RUN-010":
        raise ConsumerBoundaryError("TASK_ID_NOT_RUN_010")
    if candidate.get("authorization_status") != "AUTHORIZED":
        raise ConsumerBoundaryError("EXECUTION_NOT_AUTHORIZED")
    source_trace_id = candidate.get("source_trace_id")
    if not source_trace_id:
        raise ConsumerBoundaryError("SOURCE_TRACE_REQUIRED")

    payload = dict(candidate)
    payload["consumer_boundary"] = "RUN-010→ENG-006"
    payload["source_trace_id"] = source_trace_id
    result = eng006_consumer(payload)
    if not isinstance(result, dict):
        raise ConsumerBoundaryError("INVALID_ENG006_RESULT")
    result["consumer_boundary"] = "RUN-010→ENG-006"
    result["source_trace_id"] = source_trace_id
    return result
