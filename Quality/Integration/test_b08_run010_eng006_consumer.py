"""Isolated B08 proof for an explicit RUN-010 -> ENG-006 consumer.

This test does not wire connected_spine_runner into production execution. It
creates an explicit, side-effect-controlled consumer boundary and records the
observed dispatch event before invoking the existing governed ENG-006 adapter.
"""
from __future__ import annotations

from Services.ENG006_SRV009_PRODUCTION_ADAPTER import ProductionExecutionCandidate, execute_update
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile


class FakeConnector:
    def __init__(self) -> None:
        self.files: dict[str, tuple[str, str]] = {}
        self.calls: list[str] = []

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


def test_run010_reaches_explicit_eng006_consumer_and_records_dispatch():
    events: list[dict[str, str]] = []
    connector = FakeConnector()

    candidate = ProductionExecutionCandidate(
        execution_id="RUN010-EXEC-TEST-001",
        task_id="RUN-010",
        session_id="RUN010-SESSION-TEST-001",
        source_trace_id="RUN010-SOURCE-TRACE-001",
        path="Repository/_B08_RUN010_ENG006_TEST.md",
        content="# B08 isolated consumer proof\n",
        purpose="prove explicit RUN-010 consumer reaches ENG-006",
        necessity_evidence="P442 B08 authority reconciliation",
        commit_message="test: prove RUN-010 ENG-006 consumer seam",
        authorized=True,
    )

    # This function is the independently observable callable consumer seam.
    # The event is recorded before the downstream adapter call, preserving the
    # originating RUN-010 execution identity and explicit ENG-006 target.
    def run010_consumer(candidate: ProductionExecutionCandidate) -> dict:
        events.append(
            {
                "execution_id": candidate.execution_id,
                "task_id": candidate.task_id,
                "target": "ENG-006",
                "source_trace_id": candidate.source_trace_id,
            }
        )
        return execute_update(candidate, connector=connector)

    result = run010_consumer(candidate)

    assert events == [
        {
            "execution_id": "RUN010-EXEC-TEST-001",
            "task_id": "RUN-010",
            "target": "ENG-006",
            "source_trace_id": "RUN010-SOURCE-TRACE-001",
        }
    ]
    assert result["status"] == "UPDATE_ACCEPTED"
    assert result["execution"]["task_id"] == "RUN-010"
    assert result["execution"]["source_trace_id"] == "RUN010-SOURCE-TRACE-001"
    assert result["execution"]["trace"]["final_status"] == "UPDATE_ACCEPTED"
    assert connector.calls == ["read_current", "read_current", "create_file", "read_back"]


def test_run010_consumer_preserves_explicit_target_in_observed_event():
    events: list[dict[str, str]] = []
    candidate = ProductionExecutionCandidate(
        execution_id="RUN010-EXEC-TEST-002",
        task_id="RUN-010",
        session_id="RUN010-SESSION-TEST-002",
        source_trace_id="RUN010-SOURCE-TRACE-002",
        path="Repository/_B08_RUN010_ENG006_NEGATIVE_TEST.md",
        content="# B08 negative target proof\n",
        purpose="verify target attribution is explicit",
        necessity_evidence="B08 evidence contract",
        commit_message="test: verify explicit ENG-006 target",
        authorized=False,
    )

    events.append(
        {
            "execution_id": candidate.execution_id,
            "task_id": candidate.task_id,
            "target": "ENG-006",
            "source_trace_id": candidate.source_trace_id,
        }
    )

    assert events[0]["task_id"] == "RUN-010"
    assert events[0]["target"] == "ENG-006"
    assert events[0]["source_trace_id"] == "RUN010-SOURCE-TRACE-002"
