from __future__ import annotations

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


def _connector() -> GitHubActionsRepositoryConnector:
    return GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")


def test_list_workflow_runs_rejects_non_string_filters_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = _connector()

    cases = (
        ({"branch": 1}, "GITHUB_ACTIONS_INVALID_BRANCH"),
        ({"event": True}, "GITHUB_ACTIONS_INVALID_EVENT"),
        ({"head_sha": []}, "GITHUB_ACTIONS_INVALID_HEAD_SHA"),
        ({"status": {}}, "GITHUB_ACTIONS_INVALID_STATUS"),
    )
    for kwargs, reason in cases:
        with pytest.raises(ConnectorError, match=reason):
            connector.list_workflow_runs(**kwargs)

    assert calls == []


def test_list_workflow_runs_requires_real_integer_per_page_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = _connector()

    for value in (True, 10.0, "10", 0, 101):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_PER_PAGE"):
            connector.list_workflow_runs(per_page=value)

    assert calls == []
