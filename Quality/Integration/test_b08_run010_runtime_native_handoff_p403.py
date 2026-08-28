"""P403 — runtime-native RUN-010 -> ENG-006 handoff observation.

This remains isolated: the runtime entrypoint and governed adapter are exercised
with an in-memory connector and a synthetic explicit authorization result.
It does not wire connected_spine_runner or contact a real repository provider.
"""
from __future__ import annotations

from dataclasses import dataclass

from Runtime.Execution.execution_entrypoint import execute
from Runtime.Execution.run010_handoff_contract import build_handoff_candidate
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
        return ConnectorFile(path=path, sha="sha-p403", content=value)

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        assert path not in self.content
        self.content[path] = content
        return "commit-p403"

    def update_file(self, path: str, content: str, commit_message: str, current_sha: str) -> str:
        assert path in self.content
        assert current_sha == "sha-p403"
        self.content[path] = content
        return "commit-p403-update"

    def read_back(self, path: str):
        return ConnectorFile(path=path, sha="sha-p403-readback", content=self.content[path])


def test_p403_runtime_native_handoff_uses_contract_before_governed_dispatch():
    execution = execute(
        execution_id="EXE-RUN010-B08-P403",
        task_id="TASK-RUN010-B08-P403",
        session_id="SESSION-RUN010-B08-P403",
        source_trace_id="SRC-RUN010-B08-P403",
        authorized=True,
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "RUN-010_HANDOFF", "status": "PASS"}],
    )
    authorization = {"status": "AUTHORIZED", "authorization_id": "AUTH-RUN010-B08-P403"}

    handoff = build_handoff_candidate(
        execution,
        authorization,
        path="Repository/_P403_B08_RUNTIME_NATIVE_OBSERVATION.md",
        content="# P403 isolated runtime-native handoff observation\n",
        purpose="isolated B08 runtime-native handoff observation",
        necessity_evidence="P289 handoff contract + P399 construction gate",
        commit_message="test: P403 runtime-native handoff observation",
    )

    assert handoff["execution_id"] == execution["execution_id"]
    assert handoff["task_id"] == execution["task_id"]
    assert handoff["session_id"] == execution["session_id"]
    assert handoff["source_trace_id"] == execution["source_trace_id"]
    assert handoff["authorization_id"] == authorization["authorization_id"]
    assert handoff["authorized"] is True

    candidate = ProductionExecutionCandidate(**handoff)
    connector = FakeConnector(content={})
    result = execute_update(candidate, connector=connector)

    assert result["status"] == "UPDATE_ACCEPTED"
    assert result["write_result"].post_read_verified is True
    assert result["execution"]["task_id"] == execution["task_id"]
    assert result["execution"]["session_id"] == execution["session_id"]
    assert result["execution"]["source_trace_id"] == execution["source_trace_id"]
    assert connector.content[candidate.path] == candidate.content
