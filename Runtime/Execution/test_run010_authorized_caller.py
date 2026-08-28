"""Isolated RUN-010 caller construction proof.

This test composes the existing authorization gate, execution entrypoint, and
pure handoff contract. It performs no repository I/O and never invokes the
production adapter; the assertion is limited to governed payload construction.
"""

from Decision.authorization_gate import authorize
from Runtime.Execution.execution_entrypoint import execute
from Runtime.Execution.run010_handoff_contract import build_handoff_candidate


def test_run010_caller_preserves_governed_authorization_identity():
    proposal = {"status": "PROPOSAL_READY"}
    authorization = {
        "approved": True,
        "authorized_by": "test-operator",
        "authorization_id": "AUTH-TEST-001",
    }

    authorized = authorize(proposal, authorization)
    execution = execute(
        execution_id="EXEC-TEST-001",
        task_id="TASK-TEST-001",
        session_id="SESSION-TEST-001",
        source_trace_id="SRC-TEST-001",
        authorized=authorized["status"] == "AUTHORIZED",
        final_status="SIMULATED",
        side_effect=False,
    )
    candidate = build_handoff_candidate(
        execution,
        authorized,
        path="test/path.md",
        content="test",
        purpose="caller construction proof",
        necessity_evidence="P409 identity-owner reconciliation",
        commit_message="test governed handoff",
    )

    assert candidate["authorization_id"] == "AUTH-TEST-001"
    assert candidate["authorized"] is True
    assert execution["trace"]["record_type"] == "EXECUTION_TRACE"


def test_run010_caller_rejects_unapproved_authorization():
    proposal = {"status": "PROPOSAL_READY"}
    authorization = {"approved": False, "authorization_id": "AUTH-TEST-002"}
    result = authorize(proposal, authorization)
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "AUTHORIZATION_REQUIRED"
