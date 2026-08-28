"""Isolated observable RUN-010 -> SRV-009 composition seam.

The normal connected spine remains simulation-only. This module exists to make
the P374 evidence boundary directly observable without introducing an alternate
write implementation: it validates the RUN-010 handoff contract, reuses the
existing ENG-006/SRV-009 production adapter, and records the resulting dispatch
event with preserved execution and authorization provenance.
"""
from __future__ import annotations

from typing import Any

from Runtime.Execution.run010_handoff_contract import build_handoff_candidate
from Services.ENG006_SRV009_PRODUCTION_ADAPTER import (
    ProductionExecutionCandidate,
    execute_update,
)
from Services.REPOSITORY_CONNECTOR_INTERFACE import RepositoryConnector


def observe_run010_srv009_dispatch(
    execution: dict,
    authorization: dict,
    *,
    connector: RepositoryConnector,
    path: str,
    content: str,
    purpose: str,
    necessity_evidence: str,
    commit_message: str,
) -> dict[str, Any]:
    """Execute one isolated governed dispatch and return attributable evidence."""
    handoff = build_handoff_candidate(
        execution,
        authorization,
        path=path,
        content=content,
        purpose=purpose,
        necessity_evidence=necessity_evidence,
        commit_message=commit_message,
    )
    candidate = ProductionExecutionCandidate(**handoff)
    result = execute_update(candidate, connector=connector)

    downstream = result.get("execution")
    if result.get("status") != "UPDATE_ACCEPTED" or not downstream:
        raise RuntimeError("REL009_DISPATCH_NOT_OBSERVED")

    event = {
        "runtime_reference": "RUN-010",
        "target": "SRV-009",
        "callable_boundary": "Services.ENG006_SRV009_PRODUCTION_ADAPTER.execute_update",
        "execution_id": execution["execution_id"],
        "task_id": execution["task_id"],
        "session_id": execution["session_id"],
        "source_trace_id": execution["source_trace_id"],
        "authorization_id": authorization["authorization_id"],
        "downstream_execution_trace_id": downstream["execution_trace_id"],
        "dispatch_status": result["status"],
        "post_read_verified": result["write_result"].post_read_verified,
    }
    return {"event": event, "result": result}
