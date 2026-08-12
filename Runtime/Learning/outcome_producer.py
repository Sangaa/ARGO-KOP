"""Materialize a canonical outcome directly from a governed execution result."""

from uuid import uuid4


_STATUS_TO_RESULT = {
    "SUCCESS": "SUCCESS",
    "PARTIAL": "PARTIAL",
    "FAILURE": "FAILURE",
    "INCONCLUSIVE": "INCONCLUSIVE",
    "SIMULATED": "INCONCLUSIVE",
}


def record_execution_outcome(*, decision_id: str, execution: dict) -> dict:
    """Create one bounded outcome from a completed governed execution.

    The producer consumes the execution trace ID emitted by the governed
    execution entrypoint. It does not evaluate the outcome or promote learning.
    Controlled/simulated execution is intentionally represented as
    INCONCLUSIVE rather than SUCCESS.
    """
    issues = []
    execution_id = execution.get("execution_id")
    execution_trace_id = execution.get("execution_trace_id")
    final_status = execution.get("trace", {}).get("final_status") or execution.get("final_status")

    if not decision_id:
        issues.append("DECISION_ID_REQUIRED")
    if not execution_id:
        issues.append("EXECUTION_ID_REQUIRED")
    if not execution_trace_id:
        issues.append("EXECUTION_TRACE_REQUIRED")
    if final_status not in _STATUS_TO_RESULT:
        issues.append("UNSUPPORTED_EXECUTION_STATUS")

    if issues:
        return {"status": "OUTCOME_REJECTED", "issues": issues}

    result = _STATUS_TO_RESULT[final_status]
    return {
        "status": "OUTCOME_RECORDED",
        "outcome": {
            "outcome_id": f"OUT-{uuid4().hex[:12]}",
            "result": result,
            "evidence_trace_ids": [execution_trace_id],
            "execution_trace_ids": [execution_trace_id],
            "confidence": "UNKNOWN" if result == "INCONCLUSIVE" else "HIGH",
        },
    }
