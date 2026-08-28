"""P394 — isolated B08 runtime dispatch observation.

This test proves the minimum non-canonical seam required by P374:
RUN-010 execution identity is handed to the existing governed ENG-006 ->
SRV-009 adapter, and the adapter produces an observed execution trace after a
side-effect-controlled repository dispatch.
"""
from __future__ import annotations

from dataclasses import dataclass

from Runtime.Execution.execution_entrypoint import execute
from Services.ENG006_SRV009_PRODUCTION_ADAPTER import (
    ProductionExecutionCandidate,
    execute_update,
)
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile


@dataclass
class FakeConnector:
    content: dict[str, str]

    def read_current(self, path: str):
        value = self.content.get(path)
        if value is None:
            return None
        return ConnectorFile(path=path, sha="sha-current", content=value)

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        assert path not in self.content
        self.content[path] = content
        return "commit-create-p394"

    def update_file(self, path: str, content: str, commit_message: str, current_sha: str) -> str:
        assert path in self.content
        assert current_sha == "sha-current"
        self.content[path] = content
        return "commit-update-p394"

    def read_back(self, path: str):
        return ConnectorFile(path=path, sha="sha-readback", content=self.content[path])


def test_b08_same_run010_execution_reaches_srv009_dispatch_boundary():
    execution = execute(
        execution_id="EXE-RUN010-B08-P394",
        task_id="TASK-RUN010-B08-P394",
        session_id="SESSION-RUN010-B08-P394",
        source_trace_id="SRC-RUN010-B08-P394",
        authorized=True,
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "RUN-010_HANDOFF", "status": "PASS"}],
    )

    candidate = ProductionExecutionCandidate(
        execution_id=execution["execution_id"],
        task_id=execution["task_id"],
        session_id=execution["session_id"],
        source_trace_id=execution["execution_trace_id"],
        path="Repository/_P394_B08_OBSERVATION.md",
        content="# P394 isolated B08 observation\n",
        purpose="isolated B08 dispatch observation",
        necessity_evidence="P374 minimum B08 observation design",
        commit_message="test: P394 B08 dispatch observation",
        authorized=True,
    )
    connector = FakeConnector(content={})

    result = execute_update(candidate, connector=connector)

    assert result["status"] == "UPDATE_ACCEPTED"
    assert result["write_result"].post_read_verified is True
    assert result["execution"] is not None
    assert result["execution"]["task_id"] == execution["task_id"]
    assert result["execution"]["session_id"] == execution["session_id"]
    assert result["execution"]["source_trace_id"] == execution["execution_trace_id"]
    assert result["execution"]["trace"]["final_status"] == "UPDATE_ACCEPTED"
    assert result["execution"]["trace"]["side_effect"] is True
    assert connector.content[candidate.path] == candidate.content


def test_b08_dispatch_still_fails_closed_without_authorization():
    candidate = ProductionExecutionCandidate(
        execution_id="EXE-RUN010-B08-P394-DENIED",
        task_id="TASK-RUN010-B08-P394-DENIED",
        session_id="SESSION-RUN010-B08-P394-DENIED",
        source_trace_id="SRC-RUN010-B08-P394-DENIED",
        path="Repository/_P394_B08_DENIED.md",
        content="must-not-write\n",
        purpose="negative authorization observation",
        necessity_evidence="P374 minimum B08 observation design",
        commit_message="test: P394 denied B08 dispatch",
        authorized=False,
    )
    connector = FakeConnector(content={})

    try:
        execute_update(candidate, connector=connector)
    except ValueError as exc:
        assert str(exc) == "EXECUTION_NOT_AUTHORIZED"
    else:
        raise AssertionError("unauthorized B08 dispatch must fail closed")

    assert connector.content == {}
