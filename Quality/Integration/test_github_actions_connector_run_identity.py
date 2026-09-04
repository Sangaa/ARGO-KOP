from __future__ import annotations

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


def _connector() -> GitHubActionsRepositoryConnector:
    return GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")


def test_list_workflow_runs_accepts_positive_exact_integer_identity(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(connector, "_request", lambda *args, **kwargs: {"workflow_runs": [{"id": 7}]})

    assert connector.list_workflow_runs()["workflow_runs"][0]["id"] == 7


@pytest.mark.parametrize("invalid_id", [None, True, False, 0, -1, "7", 7.0])
def test_list_workflow_runs_rejects_invalid_provider_identity(
    monkeypatch: pytest.MonkeyPatch, invalid_id: object
):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{"id": invalid_id}]},
    )

    with pytest.raises(
        ConnectorError,
        match=r"GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID: GET runs\.workflow_runs\[\]\.id",
    ):
        connector.list_workflow_runs()


def test_list_workflow_runs_identity_guard_preserves_filter_semantics(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(
        connector,
        "_request",
        lambda *args, **kwargs: {"workflow_runs": [{"id": 7, "head_branch": "dev"}]},
    )

    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_BRANCH_FILTER_MISMATCH"):
        connector.list_workflow_runs(branch="main")


def test_list_workflow_runs_identity_guard_accepts_empty_collection(monkeypatch: pytest.MonkeyPatch):
    connector = _connector()
    monkeypatch.setattr(connector, "_request", lambda *args, **kwargs: {"workflow_runs": []})

    assert connector.list_workflow_runs()["workflow_runs"] == []
