from __future__ import annotations

import base64
import json
import os
import urllib.error

import pytest

from Services.GITHUB_REPOSITORY_CONNECTOR import GitHubConnectorConfig, GitHubRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


class FakeResponse:
    def __init__(self, payload: dict):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def github_file(sha: str, content: str) -> dict:
    return {
        "type": "file",
        "sha": sha,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }


def make_connector(monkeypatch: pytest.MonkeyPatch, responses: list[dict]) -> GitHubRepositoryConnector:
    def fake_urlopen(request, timeout):
        if not responses:
            raise AssertionError("NO_FAKE_RESPONSE_AVAILABLE")
        return FakeResponse(responses.pop(0))

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    return GitHubRepositoryConnector(
        GitHubConnectorConfig(owner="Sangaa", repo="ARGO-KOP", token="test-token"),
    )


def test_read_current_decodes_contents(monkeypatch: pytest.MonkeyPatch):
    connector = make_connector(monkeypatch, [github_file("sha-1", "hello")])
    result = connector.read_current("Repository/test.md")
    assert result is not None
    assert result.sha == "sha-1"
    assert result.content == "hello"


def test_create_requires_confirmed_absence(monkeypatch: pytest.MonkeyPatch):
    connector = make_connector(monkeypatch, [github_file("sha-1", "exists")])
    with pytest.raises(ConnectorError, match="EXISTING_FILE"):
        connector.create_file("Repository/test.md", "new", "create")


def test_create_uses_put_after_absence(monkeypatch: pytest.MonkeyPatch):
    requests = []
    responses = [
        {"message": "Not Found"},
        {"commit": {"sha": "commit-1"}},
    ]

    def fake_urlopen(request, timeout):
        requests.append(request)
        payload = responses.pop(0)
        if payload.get("message") == "Not Found":
            raise urllib.error.HTTPError(request.full_url, 404, "Not Found", {}, None)
        return FakeResponse(payload)

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubRepositoryConnector(
        GitHubConnectorConfig(owner="Sangaa", repo="ARGO-KOP", token="test-token"),
    )
    assert connector.create_file("Repository/new.md", "new", "create") == "commit-1"
    assert requests[1].method == "PUT"
    body = json.loads(requests[1].data.decode("utf-8"))
    assert body["content"] == base64.b64encode(b"new").decode("ascii")
    assert body["branch"] == "main"


def test_update_rejects_stale_sha(monkeypatch: pytest.MonkeyPatch):
    connector = make_connector(monkeypatch, [github_file("actual-sha", "old")])
    with pytest.raises(ConnectorError, match="STALE_TARGET_SHA"):
        connector.update_file("Repository/test.md", "new", "update", "stale-sha")


def test_read_back_requires_persisted_file(monkeypatch: pytest.MonkeyPatch):
    def fake_urlopen(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found", {}, None)

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubRepositoryConnector(
        GitHubConnectorConfig(owner="Sangaa", repo="ARGO-KOP", token="test-token"),
    )
    with pytest.raises(ConnectorError, match="READ_BACK_MISSING"):
        connector.read_back("Repository/missing.md")


def test_environment_config_requires_credentials(monkeypatch: pytest.MonkeyPatch):
    for key in ("ARGO_GITHUB_OWNER", "ARGO_GITHUB_REPO", "ARGO_GITHUB_TOKEN"):
        monkeypatch.delenv(key, raising=False)
    with pytest.raises(ConnectorError, match="CONFIGURATION_INCOMPLETE"):
        GitHubConnectorConfig.from_environment()
