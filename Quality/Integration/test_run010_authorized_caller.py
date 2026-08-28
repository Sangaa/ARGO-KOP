"""P411 — minimal RUN-010 authorized caller composition proof.

This is an isolated composition test only. It does not wire connected_spine_runner
or contact a real repository provider.
"""
from __future__ import annotations

from Decision.authorization_gate import authorize
from Runtime.Execution.execution_entrypoint import execute
from Runtime.Execution.run010_handoff_contract import build_handoff_candidate


def test_run010_authorized_caller_preserves_authorization_identity():
    proposal = {"status": "PROPOSAL_READY"}
    authorization = {
        "approved": True,
        "authorized_by": "P411",
        "authorization_id": "AUTH-P411-RUN010",
    }

    auth_result = authorize(proposal, authorization)
    execution = execute(
        execution_id="EXE-P411",
        task_id="TASK-P411",
        session_id="SESSION-P411",
        source_trace_id="SRC-P411",
        authorized=auth_result["status"] == "AUTHORIZED",
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "RUN-010_AUTHORIZED_CALLER", "status": "PASS"}],
    )

    handoff = build_handoff_candidate(
        execution,
        auth_result,
        path="Repository/_P411_AUTHORIZED_CALLER_PROOF.md",
        content="# isolated P411 proof\n",
        purpose="prove governed authorization identity composition",
        necessity_evidence="P409 authorization identity owner reconciliation",
        commit_message="test: P411 authorized caller composition",
    )

    assert auth_result["authorization_id"] == authorization["authorization_id"]
    assert handoff["authorization_id"] == authorization["authorization_id"]
    assert handoff["execution_id"] == execution["execution_id"]


def test_run010_authorized_caller_fails_closed_when_authorization_is_missing():
    auth_result = authorize({"status": "PROPOSAL_READY"}, None)
    assert auth_result["status"] == "BLOCKED"
    assert auth_result["reason"] == "AUTHORIZATION_REQUIRED"

    try:
        execute(
            execution_id="EXE-P411-DENIED",
            task_id="TASK-P411-DENIED",
            session_id="SESSION-P411-DENIED",
            source_trace_id="SRC-P411-DENIED",
            authorized=False,
            final_status="BLOCKED",
            side_effect=False,
        )
    except ValueError as exc:
        assert str(exc) == "EXECUTION_NOT_AUTHORIZED"
    else:
        raise AssertionError("missing authorization must fail closed")
