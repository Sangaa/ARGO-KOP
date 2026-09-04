from __future__ import annotations

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


def _connector() -> GitHubActionsRepositoryConnector:
    return GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")


def test_status_filter_accepts_conclusion_match(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{"status": "completed", "conclusion": "success"}]},
    )

    result = connector.list_workflow_runs(status="success")

    assert result["workflow_runs"][0]["conclusion"] == "success"


def test_status_filter_accepts_runtime_status_match(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{"status": "in_progress", "conclusion": None}]},
    )

    result = connector.list_workflow_runs(status="in_progress")

    assert result["workflow_runs"][0]["status"] == "in_progress"


def test_status_filter_rejects_unrepresented_requested_value(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{"status": "completed", "conclusion": "failure"}]},
    )

    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_STATUS_FILTER_MISMATCH"):
        connector.list_workflow_runs(status="success")


def test_status_filter_rejects_missing_semantic_representation(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{}]},
    )

    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_STATUS_FILTER_MISMATCH"):
        connector.list_workflow_runs(status="success")


def test_no_status_filter_adds_no_status_or_conclusion_requirement(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(connector, "_request", lambda *args, **kwargs: {"workflow_runs": [{}]})

    assert connector.list_workflow_runs() == {"workflow_runs": [{}]}
