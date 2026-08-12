"""Verify that runtime trace and outcome evidence belong to one execution path.

This is an evidence verifier, not a promotion engine. It proves identity and
lineage consistency for already-produced runtime artifacts and returns HOLD
when the relationship cannot be established.
"""


def verify_runtime_outcome_evidence(result: dict) -> dict:
    if not isinstance(result, dict):
        return {"status": "HOLD", "reason": "INVALID_RUNTIME_RESULT"}

    execution = result.get("execution")
    outcome = result.get("outcome")
    if not isinstance(execution, dict):
        return {"status": "HOLD", "reason": "MISSING_EXECUTION"}
    if not isinstance(outcome, dict):
        return {"status": "HOLD", "reason": "MISSING_OUTCOME"}

    trace_id = execution.get("execution_trace_id")
    trace = execution.get("trace")
    outcome_trace_ids = outcome.get("execution_trace_ids")
    evidence_trace_ids = outcome.get("evidence_trace_ids")

    if not isinstance(trace, dict) or not trace_id:
        return {"status": "HOLD", "reason": "MISSING_EXECUTION_TRACE"}
    if trace.get("trace_id") != trace_id:
        return {"status": "HOLD", "reason": "TRACE_ID_MISMATCH"}
    if not isinstance(outcome_trace_ids, list) or trace_id not in outcome_trace_ids:
        return {"status": "HOLD", "reason": "OUTCOME_TRACE_LINEAGE_MISSING"}
    if not isinstance(evidence_trace_ids, list) or trace_id not in evidence_trace_ids:
        return {"status": "HOLD", "reason": "EVIDENCE_TRACE_LINEAGE_MISSING"}

    return {
        "status": "VERIFIED",
        "execution_trace_id": trace_id,
        "task_id": execution.get("task_id"),
        "outcome_status": outcome.get("status"),
    }
