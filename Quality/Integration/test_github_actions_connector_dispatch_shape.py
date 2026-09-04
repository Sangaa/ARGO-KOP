from __future__ import annotations

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


def _connector() -> GitHubActionsRepositoryConnector:
    return GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")


def test_dispatch_rejects_invalid_workflow_identity_shape_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = _connector()

    for workflow_id in (True, [], {}, None, "", "   "):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_WORKFLOW_ID"):
            connector.dispatch_workflow(workflow_id, ref="main")

    assert calls == []


def test_dispatch_rejects_invalid_ref_shape_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = _connector()

    for ref in (None, 1, True, "", "   "):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_REF"):
            connector.dispatch_workflow("full-stack-audit.yml", ref=ref)

    assert calls == []


def test_dispatch_rejects_invalid_inputs_shape_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = _connector()

    for inputs in ([], {1: "value"}, {"key": 1}, {"key": True}):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_INPUTS"):
            connector.dispatch_workflow("full-stack-audit.yml", ref="main", inputs=inputs)

    assert calls == []
