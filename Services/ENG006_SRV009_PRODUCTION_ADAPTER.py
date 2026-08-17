"""Production handoff adapter for ENG-006 -> SRV-009.

This module binds the governed execution entrypoint to the existing governed
write dispatcher through a provider-neutral RepositoryConnector. It does not
select authorization, invent canonical authority, or bypass SRV-005 controls.

Real repository mutation is possible only when the caller supplies an
authorized execution candidate and a real connector implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from Runtime.Execution.execution_entrypoint import execute
from Tools.GOVERNED_WRITE_DISPATCH import FileImportance, WriteIntent, WriteResult, dispatch_write
from Services.REPOSITORY_CONNECTOR_INTERFACE import RepositoryConnector


@dataclass(frozen=True)
class ProductionExecutionCandidate:
    execution_id: str
    task_id: str
    session_id: str
    source_trace_id: str
    path: str
    content: str
    purpose: str
    necessity_evidence: str
    commit_message: str
    authorized: bool


def execute_update(
    candidate: ProductionExecutionCandidate,
    *,
    connector: RepositoryConnector,
) -> dict[str, Any]:
    """Execute one governed repository update and return traceable evidence.

    Authorization must already be explicit. Technical connector access never
    grants canonical authority. The dispatcher performs target identity checks
    and mandatory post-write read-back.
    """
    if not candidate.authorized:
        raise ValueError("EXECUTION_NOT_AUTHORIZED")

    intent = WriteIntent(
        path=candidate.path,
        content=candidate.content,
        commit_message=candidate.commit_message,
        purpose=candidate.purpose,
        importance=FileImportance.REPOSITORY_EVIDENCE,
        necessity_evidence=candidate.necessity_evidence,
        canonical_scope=False,
    )

    result: WriteResult = dispatch_write(
        intent,
        read_current=connector.read_current,
        create_file=connector.create_file,
        update_file=connector.update_file,
        read_back=connector.read_back,
    )

    if not result.post_read_verified:
        return {
            "status": "UPDATE_BLOCKED",
            "write_result": result,
            "execution": None,
        }

    execution = execute(
        execution_id=candidate.execution_id,
        task_id=candidate.task_id,
        session_id=candidate.session_id,
        source_trace_id=candidate.source_trace_id,
        authorized=candidate.authorized,
        final_status="UPDATE_ACCEPTED",
        side_effect=True,
        stages=[
            {"stage": "AUTHORIZED_CANDIDATE", "status": "PASS"},
            {"stage": "SRV-009_GOVERNED_DISPATCH", "status": "PASS"},
            {"stage": "POST_WRITE_READ_BACK", "status": "PASS"},
        ],
    )
    return {
        "status": "UPDATE_ACCEPTED",
        "write_result": result,
        "execution": execution,
    }
