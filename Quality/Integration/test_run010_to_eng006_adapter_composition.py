from __future__ import annotations

from connected_spine_runner import run
from Services.ENG006_SRV009_PRODUCTION_ADAPTER import ProductionExecutionCandidate, execute_update


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


def fixture() -> dict:
    return {
        "context": {"session_id": "SES-RUN010-COMPOSE-001", "topic": "controlled review"},
        "knowledge": {"source": "integration-fixture"},
        "task": {"task_id": "TASK-RUN010-COMPOSE-001"},
        "rules": {"allow_simulated_review": True},
        "authorization": {"approved": True, "authorization_id": "AUTH-RUN010-COMPOSE-001"},
    }


def test_run010_candidate_composes_into_eng006_adapter_without_production_io():
    result = run(fixture())
    handoff = result["handoff_candidate"]
    assert handoff is not None
    assert handoff["authorization_id"] == "AUTH-RUN010-COMPOSE-001"
    assert handoff["authorized"] is True

    candidate = ProductionExecutionCandidate(**handoff)
    connector = FakeConnector()
    accepted = execute_update(candidate, connector=connector)

    assert accepted["status"] == "UPDATE_ACCEPTED"
    assert accepted["execution"]["trace"]["final_status"] == "UPDATE_ACCEPTED"
    assert [name for name, _ in connector.calls] == [
        "read_current",
        "read_current",
        "create_file",
        "read_back",
    ]
    assert connector.files[handoff["path"]][1] == handoff["content"]


def test_run010_unauthorized_fixture_cannot_reach_adapter():
    fixture_data = fixture()
    fixture_data["authorization"] = {"approved": False, "authorization_id": "AUTH-RUN010-DENIED-001"}
    result = run(fixture_data)
    assert result["handoff_candidate"] is None
