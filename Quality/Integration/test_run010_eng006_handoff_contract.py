from __future__ import annotations

from Runtime.Execution.execution_entrypoint import ExecutionDenied, execute
from Runtime.Execution.run010_handoff_contract import build_handoff_candidate
from Services.ENG006_SRV009_PRODUCTION_ADAPTER import ProductionExecutionCandidate


def _builder_execution() -> dict:
    return {
        "execution_id": "EXE-RUN010-BUILDER-001",
        "task_id": "TASK-RUN010-BUILDER-001",
        "session_id": "SESSION-RUN010-BUILDER-001",
        "source_trace_id": "SRC-RUN010-BUILDER-001",
        "trace": {
            "record_type": "EXECUTION_TRACE",
            "task_id": "TASK-RUN010-BUILDER-001",
            "session_id": "SESSION-RUN010-BUILDER-001",
        },
    }


def _builder_authorization() -> dict:
    return {
        "status": "AUTHORIZED",
        "authorization_id": "AUTH-RUN010-BUILDER-001",
    }


def _build(execution: dict | None = None, authorization: dict | None = None, **overrides) -> dict:
    fields = {
        "path": "Repository/_RUN010_HANDOFF_TEST.md",
        "content": "# direct RUN-010 handoff builder coverage\n",
        "purpose": "direct contract coverage",
        "necessity_evidence": "full-stack untested-candidate gap closure",
        "commit_message": "test: cover RUN-010 handoff builder",
    }
    fields.update(overrides)
    return build_handoff_candidate(
        execution if execution is not None else _builder_execution(),
        authorization if authorization is not None else _builder_authorization(),
        **fields,
    )


def _assert_builder_error(expected: str, execution: dict | None = None, authorization: dict | None = None, **overrides) -> None:
    try:
        _build(execution=execution, authorization=authorization, **overrides)
    except ValueError as exc:
        assert str(exc) == expected
    else:
        raise AssertionError(f"expected fail-closed builder error: {expected}")


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
        authorization_id="AUTH-RUN010-HANDOFF-001",
    )

    assert candidate.execution_id == execution["execution_id"]
    assert candidate.task_id == execution["task_id"]
    assert candidate.session_id == execution["session_id"]
    assert candidate.source_trace_id == execution["execution_trace_id"]
    assert candidate.authorized is True
    assert candidate.authorization_id == "AUTH-RUN010-HANDOFF-001"


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


def test_direct_builder_preserves_exact_governed_handoff_identity_and_fields():
    result = _build()

    assert result == {
        "execution_id": "EXE-RUN010-BUILDER-001",
        "task_id": "TASK-RUN010-BUILDER-001",
        "session_id": "SESSION-RUN010-BUILDER-001",
        "source_trace_id": "SRC-RUN010-BUILDER-001",
        "path": "Repository/_RUN010_HANDOFF_TEST.md",
        "content": "# direct RUN-010 handoff builder coverage\n",
        "purpose": "direct contract coverage",
        "necessity_evidence": "full-stack untested-candidate gap closure",
        "commit_message": "test: cover RUN-010 handoff builder",
        "authorized": True,
        "authorization_id": "AUTH-RUN010-BUILDER-001",
    }


def test_direct_builder_requires_execution_provenance():
    execution = _builder_execution()
    execution["source_trace_id"] = ""
    _assert_builder_error("HANDOFF_PROVENANCE_REQUIRED: source_trace_id", execution=execution)


def test_direct_builder_requires_authorized_status():
    authorization = _builder_authorization()
    authorization["status"] = "DENIED"
    _assert_builder_error("HANDOFF_AUTHORIZATION_REQUIRED", authorization=authorization)


def test_direct_builder_requires_authorization_identity():
    authorization = _builder_authorization()
    authorization["authorization_id"] = ""
    _assert_builder_error("HANDOFF_AUTHORIZATION_ID_REQUIRED", authorization=authorization)


def test_direct_builder_requires_all_mutation_fields():
    _assert_builder_error("HANDOFF_MUTATION_FIELDS_REQUIRED", purpose="")


def test_direct_builder_requires_execution_trace_record():
    execution = _builder_execution()
    execution["trace"] = {"record_type": "OTHER", "task_id": execution["task_id"], "session_id": execution["session_id"]}
    _assert_builder_error("HANDOFF_EXECUTION_TRACE_REQUIRED", execution=execution)


def test_direct_builder_rejects_trace_task_mismatch():
    execution = _builder_execution()
    execution["trace"]["task_id"] = "OTHER-TASK"
    _assert_builder_error("HANDOFF_TASK_ID_MISMATCH", execution=execution)


def test_direct_builder_rejects_trace_session_mismatch():
    execution = _builder_execution()
    execution["trace"]["session_id"] = "OTHER-SESSION"
    _assert_builder_error("HANDOFF_SESSION_ID_MISMATCH", execution=execution)
