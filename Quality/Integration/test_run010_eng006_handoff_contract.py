from __future__ import annotations

from Runtime.Execution.execution_entrypoint import ExecutionDenied, execute
from Services.ENG006_SRV009_PRODUCTION_ADAPTER import ProductionExecutionCandidate


def test_run010_execution_result_provides_traceable_handoff_identity():
    execution = execute(
        execution_id="EXE-RUN010-HANDOFF-001",
        task_id="TASK-RUN010-HANDOFF-001",
        session_id="SESSION-RUN010-HANDOFF-001",
        source_trace_id="SRC-RUN010-001",
        authorized=True,
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "RUN-010_HANDOFF_PRECONDITION", "status": "PASS"}],
    )

    assert execution["execution_id"] == "EXE-RUN010-HANDOFF-001"
    assert execution["task_id"] == "TASK-RUN010-HANDOFF-001"
    assert execution["session_id"] == "SESSION-RUN010-HANDOFF-001"
    assert execution["source_trace_id"] == "SRC-RUN010-001"
    assert execution["execution_trace_id"]

    candidate = ProductionExecutionCandidate(
        execution_id=execution["execution_id"],
        task_id=execution["task_id"],
        session_id=execution["session_id"],
        source_trace_id=execution["execution_trace_id"],
        path="Repository/_RUN010_HANDOFF_TEST.md",
        content="# RUN-010 handoff contract test\n",
        purpose="contract-only handoff verification",
        necessity_evidence="P289 handoff contract",
        commit_message="test: RUN-010 ENG-006 handoff contract",
        authorized=True,
    )

    assert candidate.execution_id == execution["execution_id"]
    assert candidate.task_id == execution["task_id"]
    assert candidate.session_id == execution["session_id"]
    assert candidate.source_trace_id == execution["execution_trace_id"]
    assert candidate.authorized is True


def test_handoff_contract_rejects_missing_trace_identity():
    try:
        execute(
            execution_id="EXE-RUN010-HANDOFF-002",
            task_id="TASK-RUN010-HANDOFF-002",
            session_id="SESSION-RUN010-HANDOFF-002",
            source_trace_id="",
            authorized=True,
            final_status="SIMULATED",
            side_effect=False,
        )
    except ValueError as exc:
        assert str(exc) == "SOURCE_TRACE_REQUIRED"
    else:
        raise AssertionError("missing source trace must fail closed")


def test_handoff_contract_rejects_unauthorized_execution():
    try:
        execute(
            execution_id="EXE-RUN010-HANDOFF-003",
            task_id="TASK-RUN010-HANDOFF-003",
            session_id="SESSION-RUN010-HANDOFF-003",
            source_trace_id="SRC-RUN010-003",
            authorized=False,
            final_status="SIMULATED",
            side_effect=False,
        )
    except ExecutionDenied as exc:
        assert str(exc) == "EXECUTION_NOT_AUTHORIZED"
    else:
        raise AssertionError("unauthorized execution must fail closed")
