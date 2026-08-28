from __future__ import annotations

import pytest

from Decision.authorization_gate import authorize
from Runtime.Execution.execution_entrypoint import execute
from Runtime.Execution.run010_srv009_observation import observe_run010_srv009_dispatch
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile


class FakeConnector:
    def __init__(self) -> None:
        self.calls: list[str] = []
        self.files: dict[str, tuple[str, str]] = {}

    def read_current(self, path: str):
        self.calls.append("read_current")
        current = self.files.get(path)
        if current is None:
            return None
        sha, content = current
        return ConnectorFile(path=path, sha=sha, content=content)

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        self.calls.append("create_file")
        if path in self.files:
            raise RuntimeError("EXISTING")
        self.files[path] = ("sha-created", content)
        return "commit-created"

    def update_file(self, path: str, content: str, commit_message: str, current_sha: str) -> str:
        self.calls.append("update_file")
        current = self.files.get(path)
        if current is None or current[0] != current_sha:
            raise RuntimeError("STALE")
        self.files[path] = ("sha-updated", content)
        return "commit-updated"

    def read_back(self, path: str):
        self.calls.append("read_back")
        sha, content = self.files[path]
        return ConnectorFile(path=path, sha=sha, content=content)


def _execution_and_authorization():
    authorization = authorize(
        {"status": "PROPOSAL_READY"},
        {
            "approved": True,
            "authorized_by": "REL009-CLEAN-TEST",
            "authorization_id": "AUTH-REL009-CLEAN-001",
        },
    )
    execution = execute(
        execution_id="EXEC-REL009-CLEAN-001",
        task_id="RUN-010",
        session_id="SESSION-REL009-CLEAN-001",
        source_trace_id="DEC-REL009-CLEAN-001",
        authorized=authorization["status"] == "AUTHORIZED",
        final_status="SIMULATED",
        side_effect=False,
        stages=[{"stage": "RUN-010_ISOLATED_OBSERVATION", "status": "PASS"}],
    )
    return execution, authorization


def test_rel009_observes_same_run010_execution_at_srv009_dispatch_boundary():
    execution, authorization = _execution_and_authorization()
    connector = FakeConnector()

    observed = observe_run010_srv009_dispatch(
        execution,
        authorization,
        connector=connector,
        path="Repository/_REL009_CLEAN_OBSERVATION.md",
        content="# isolated REL-009 observation\n",
        purpose="prove P374 RUN-010 to SRV-009 observation boundary",
        necessity_evidence="P374 minimum B07/B08 observation contract",
        commit_message="test: observe clean REL-009 dispatch boundary",
    )

    event = observed["event"]
    result = observed["result"]

    assert event["runtime_reference"] == "RUN-010"
    assert event["target"] == "SRV-009"
    assert event["callable_boundary"] == "Services.ENG006_SRV009_PRODUCTION_ADAPTER.execute_update"
    assert event["execution_id"] == execution["execution_id"]
    assert event["task_id"] == "RUN-010"
    assert event["session_id"] == execution["session_id"]
    assert event["source_trace_id"] == execution["source_trace_id"]
    assert event["authorization_id"] == authorization["authorization_id"]
    assert event["dispatch_status"] == "UPDATE_ACCEPTED"
    assert event["post_read_verified"] is True
    assert event["downstream_execution_trace_id"] == result["execution"]["execution_trace_id"]

    assert result["execution"]["task_id"] == "RUN-010"
    assert result["execution"]["source_trace_id"] == execution["source_trace_id"]
    assert result["execution"]["trace"]["side_effect"] is True
    assert result["write_result"].post_read_verified is True
    assert connector.calls == ["read_current", "read_current", "create_file", "read_back"]


def test_rel009_observation_fails_closed_without_authorization_identity():
    execution, authorization = _execution_and_authorization()
    authorization["authorization_id"] = None
    connector = FakeConnector()

    with pytest.raises(ValueError, match="HANDOFF_AUTHORIZATION_ID_REQUIRED"):
        observe_run010_srv009_dispatch(
            execution,
            authorization,
            connector=connector,
            path="Repository/_REL009_DENIED.md",
            content="must-not-write\n",
            purpose="negative authorization identity boundary",
            necessity_evidence="P374 authorization/provenance invariant",
            commit_message="test: reject missing REL-009 authorization identity",
        )

    assert connector.calls == []


def test_rel009_observation_fails_closed_when_authorization_is_blocked():
    execution, _ = _execution_and_authorization()
    blocked = authorize({"status": "PROPOSAL_READY"}, {"approved": False})
    connector = FakeConnector()

    with pytest.raises(ValueError, match="HANDOFF_AUTHORIZATION_REQUIRED"):
        observe_run010_srv009_dispatch(
            execution,
            blocked,
            connector=connector,
            path="Repository/_REL009_BLOCKED.md",
            content="must-not-write\n",
            purpose="negative authorization state boundary",
            necessity_evidence="P374 authorization invariant",
            commit_message="test: reject blocked REL-009 dispatch",
        )

    assert connector.calls == []
