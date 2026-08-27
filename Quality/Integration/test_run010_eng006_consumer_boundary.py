import pytest

from Runtime.Execution.run010_eng006_consumer import (
    ConsumerBoundaryError,
    dispatch_run010,
)


def test_authorized_run010_reaches_eng006_and_preserves_trace():
    seen = {}

    def consumer(payload):
        seen.update(payload)
        return {"status": "ENG006_ACCEPTED"}

    result = dispatch_run010(
        candidate={
            "task_id": "RUN-010",
            "authorization_status": "AUTHORIZED",
            "source_trace_id": "DEC-P308-001",
        },
        eng006_consumer=consumer,
    )
    assert result["status"] == "ENG006_ACCEPTED"
    assert result["consumer_boundary"] == "RUN-010→ENG-006"
    assert result["source_trace_id"] == "DEC-P308-001"
    assert seen["consumer_boundary"] == "RUN-010→ENG-006"


def test_unauthorized_run010_never_reaches_eng006():
    called = False

    def consumer(_):
        nonlocal called
        called = True
        return {"status": "BAD"}

    with pytest.raises(ConsumerBoundaryError, match="EXECUTION_NOT_AUTHORIZED"):
        dispatch_run010(
            candidate={
                "task_id": "RUN-010",
                "authorization_status": "PENDING",
                "source_trace_id": "DEC-P308-002",
            },
            eng006_consumer=consumer,
        )
    assert called is False


def test_wrong_task_cannot_enter_run010_boundary():
    with pytest.raises(ConsumerBoundaryError, match="TASK_ID_NOT_RUN_010"):
        dispatch_run010(
            candidate={
                "task_id": "RUN-011",
                "authorization_status": "AUTHORIZED",
                "source_trace_id": "DEC-P308-003",
            },
            eng006_consumer=lambda _: {"status": "BAD"},
        )
