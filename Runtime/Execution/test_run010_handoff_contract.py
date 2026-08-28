import pytest

from run010_handoff_contract import build_handoff_candidate


def _execution():
    return {
        "execution_id": "EXEC-1",
        "task_id": "TASK-1",
        "session_id": "SESSION-1",
        "source_trace_id": "DECISION-1",
        "trace": {
            "record_type": "EXECUTION_TRACE",
            "task_id": "TASK-1",
            "session_id": "SESSION-1",
        },
    }


def _authorization():
    return {"status": "AUTHORIZED", "authorization_id": "AUTH-1"}


def _fields():
    return dict(
        path="Repository/test.txt",
        content="controlled synthetic evidence",
        purpose="test handoff contract",
        necessity_evidence="P400 contract validation",
        commit_message="test: validate RUN-010 handoff contract",
    )


def test_build_handoff_preserves_execution_and_authorization_identity():
    candidate = build_handoff_candidate(_execution(), _authorization(), **_fields())
    assert candidate["execution_id"] == "EXEC-1"
    assert candidate["task_id"] == "TASK-1"
    assert candidate["session_id"] == "SESSION-1"
    assert candidate["source_trace_id"] == "DECISION-1"
    assert candidate["authorization_id"] == "AUTH-1"
    assert candidate["authorized"] is True


def test_handoff_rejects_missing_authorization_before_any_dispatch():
    with pytest.raises(ValueError, match="HANDOFF_AUTHORIZATION_REQUIRED"):
        build_handoff_candidate(_execution(), {"status": "BLOCKED"}, **_fields())


def test_handoff_rejects_missing_provenance():
    execution = _execution()
    execution["source_trace_id"] = ""
    with pytest.raises(ValueError, match="HANDOFF_PROVENANCE_REQUIRED"):
        build_handoff_candidate(execution, _authorization(), **_fields())


def test_handoff_rejects_trace_identity_mismatch():
    execution = _execution()
    execution["trace"]["task_id"] = "OTHER-TASK"
    with pytest.raises(ValueError, match="HANDOFF_TASK_ID_MISMATCH"):
        build_handoff_candidate(execution, _authorization(), **_fields())
