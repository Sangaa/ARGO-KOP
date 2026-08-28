"""Pure RUN-010 -> ENG-006 handoff contract builder.

This module deliberately performs no dispatch and no repository I/O. It turns
an already-recorded RUN-010 execution result plus the existing authorization
result into the minimum governed ProductionExecutionCandidate contract.
"""
from __future__ import annotations


def build_handoff_candidate(
    execution: dict,
    authorization: dict,
    *,
    path: str,
    content: str,
    purpose: str,
    necessity_evidence: str,
    commit_message: str,
) -> dict:
    """Return a validated handoff payload without invoking downstream code."""
    required_execution = ("execution_id", "task_id", "session_id", "source_trace_id")
    missing = [key for key in required_execution if not execution.get(key)]
    if missing:
        raise ValueError(f"HANDOFF_PROVENANCE_REQUIRED: {','.join(missing)}")
    if authorization.get("status") != "AUTHORIZED":
        raise ValueError("HANDOFF_AUTHORIZATION_REQUIRED")
    if not authorization.get("authorization_id"):
        raise ValueError("HANDOFF_AUTHORIZATION_ID_REQUIRED")
    if not path or not content or not purpose or not necessity_evidence or not commit_message:
        raise ValueError("HANDOFF_MUTATION_FIELDS_REQUIRED")

    trace = execution.get("trace") or {}
    if trace.get("record_type") != "EXECUTION_TRACE":
        raise ValueError("HANDOFF_EXECUTION_TRACE_REQUIRED")
    if trace.get("task_id") != execution["task_id"]:
        raise ValueError("HANDOFF_TASK_ID_MISMATCH")
    if trace.get("session_id") != execution["session_id"]:
        raise ValueError("HANDOFF_SESSION_ID_MISMATCH")

    return {
        "execution_id": execution["execution_id"],
        "task_id": execution["task_id"],
        "session_id": execution["session_id"],
        "source_trace_id": execution["source_trace_id"],
        "path": path,
        "content": content,
        "purpose": purpose,
        "necessity_evidence": necessity_evidence,
        "commit_message": commit_message,
        "authorized": True,
        "authorization_id": authorization["authorization_id"],
    }
