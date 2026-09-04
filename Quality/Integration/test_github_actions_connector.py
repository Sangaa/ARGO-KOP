from __future__ import annotations

import json
import urllib.error

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


class FakeResponse:
    def __init__(self, payload: object):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        if isinstance(self.payload, bytes):
            return self.payload
        return json.dumps(self.payload).encode("utf-8")


def test_list_workflow_runs_preserves_execution_filters(monkeypatch: pytest.MonkeyPatch):
    requests = []

    def fake_urlopen(request, timeout):
        requests.append(request)
        return FakeResponse({"total_count": 1, "workflow_runs": [{"id": 123}]})

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    result = connector.list_workflow_runs(branch="main", event="push", head_sha="abc", status="completed")
    assert result["workflow_runs"][0]["id"] == 123
    assert "branch=main" in requests[0].full_url
    assert "event=push" in requests[0].full_url
    assert "head_sha=abc" in requests[0].full_url


def test_get_workflow_run_requires_real_id(monkeypatch: pytest.MonkeyPatch):
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="INVALID_RUN_ID"):
        connector.get_workflow_run(0)


def test_dispatch_workflow_accepts_204(monkeypatch: pytest.MonkeyPatch):
    requests = []

    def fake_urlopen(request, timeout):
        requests.append(request)
        return FakeResponse(b"")

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.dispatch_workflow("full-stack-audit.yml", ref="main") is True
    assert requests[0].method == "POST"
    assert requests[0].full_url.endswith("/actions/workflows/full-stack-audit.yml/dispatches")
    assert json.loads(requests[0].data.decode("utf-8"))["ref"] == "main"


def test_dispatch_rejects_empty_ref(monkeypatch: pytest.MonkeyPatch):
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="INVALID_REF"):
        connector.dispatch_workflow("full-stack-audit.yml", ref="")


def test_actions_http_failure_is_explicit(monkeypatch: pytest.MonkeyPatch):
    def fake_urlopen(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, None)

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_HTTP_403"):
        connector.list_workflow_runs()


def test_actions_invalid_provider_json_fails_closed(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse(b"{not-json"))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_JSON_INVALID"):
        connector.list_workflow_runs()


def test_actions_non_object_provider_payload_fails_closed(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse([{"id": 123}]))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_runs()


def test_actions_empty_observation_response_fails_closed(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse(b""))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_EMPTY_RESPONSE"):
        connector.get_workflow_run(123)
