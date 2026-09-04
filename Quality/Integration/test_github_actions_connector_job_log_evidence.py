from __future__ import annotations

import json

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self.payload


def test_job_logs_preserve_valid_utf8_exactly(monkeypatch: pytest.MonkeyPatch):
    payload = "job line\nمرحبا ARGO\n".encode("utf-8")
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse(payload))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")

    assert connector.get_workflow_job_logs(9) == payload.decode("utf-8")


def test_job_logs_reject_lossy_utf8_replacement(monkeypatch: pytest.MonkeyPatch):
    payload = b"provider-log:\xff:end"
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse(payload))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")

    with pytest.raises(
        ConnectorError,
        match=r"GITHUB_ACTIONS_RESPONSE_ENCODING_INVALID: GET jobs/9/logs",
    ):
        connector.get_workflow_job_logs(9)


def test_job_log_encoding_failure_is_not_reported_as_transport_failure(monkeypatch: pytest.MonkeyPatch):
    payload = b"\x80"
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse(payload))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")

    with pytest.raises(ConnectorError) as exc_info:
        connector.get_workflow_job_logs(17)

    message = str(exc_info.value)
    assert message == "GITHUB_ACTIONS_RESPONSE_ENCODING_INVALID: GET jobs/17/logs"
    assert "CONNECTOR_UNAVAILABLE" not in message
