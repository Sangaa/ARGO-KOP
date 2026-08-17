from __future__ import annotations

import pytest

from Services.ENG006_SRV009_PRODUCTION_ADAPTER import (
    ProductionExecutionCandidate,
    execute_update,
)


class FakeConnector:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []
        self.files: dict[str, tuple[str, str]] = {}

    def read_current(self, path: str):
        self.calls.append(("read_current", path))
        current = self.files.get(path)
        if current is None:
            return None
        sha, content = current
        from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile
        return ConnectorFile(path=path, sha=sha, content=content)

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        self.calls.append(("create_file", path))
        if path in self.files:
            raise RuntimeError("EXISTING")
        self.files[path] = ("sha-created", content)
        return "commit-created"

    def update_file(self, path: str, content: str, commit_message: str, current_sha: str) -> str:
        self.calls.append(("update_file", path))
        actual = self.files.get(path)
        if actual is None or actual[0] != current_sha:
            raise RuntimeError("STALE")
        self.files[path] = ("sha-updated", content)
        return "commit-updated"

    def read_back(self, path: str):
        self.calls.append(("read_back", path))
        current = self.files.get(path)
        if current is None:
            raise RuntimeError("MISSING")
        from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile
        sha, content = current
        return ConnectorFile(path=path, sha=sha, content=content)


def candidate(authorized: bool = True) -> ProductionExecutionCandidate:
    return ProductionExecutionCandidate(
        execution_id="EXE-P3-001",
        task_id="TASK-P3-001",
        session_id="SESSION-P3-20260817",
        source_trace_id="SRC-P3-001",
        path="Repository/_P3_TEST_ARTIFACT.md",
        content="# P3 adapter test\n",
        purpose="governed adapter verification",
        necessity_evidence="P3 production adapter seam verification",
        commit_message="test: governed ENG-006 SRV-009 adapter",
        authorized=authorized,
    )


def test_authorized_candidate_uses_governed_dispatch_and_trace():
    connector = FakeConnector()
    result = execute_update(candidate(), connector=connector)
    assert result["status"] == "UPDATE_ACCEPTED"
    assert [name for name, _ in connector.calls] == [
        "read_current",
        "create_file",
        "read_current",
        "read_back",
    ]
    assert result["execution"]["trace"]["final_status"] == "UPDATE_ACCEPTED"


def test_unauthorized_candidate_stops_before_connector_call():
    connector = FakeConnector()
    with pytest.raises(ValueError, match="EXECUTION_NOT_AUTHORIZED"):
        execute_update(candidate(False), connector=connector)
    assert connector.calls == []
