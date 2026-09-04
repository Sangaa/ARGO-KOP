from __future__ import annotations

import json

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
        return json.dumps(self.payload).encode("utf-8")


def _connector() -> GitHubActionsRepositoryConnector:
    return GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")


def test_list_jobs_accepts_positive_exact_integer_job_identity(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"jobs": [{"id": 9, "run_id": 123}]}),
    )
    result = _connector().list_workflow_run_jobs(123)
    assert result["jobs"][0]["id"] == 9
    assert result["jobs"][0]["run_id"] == 123


@pytest.mark.parametrize("invalid_job_id", [None, True, False, 0, -1, "9", 9.0])
def test_list_jobs_rejects_invalid_provider_job_identity(
    monkeypatch: pytest.MonkeyPatch, invalid_job_id: object
):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"jobs": [{"id": invalid_job_id, "run_id": 123}]}),
    )
    with pytest.raises(
        ConnectorError,
        match=r"GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID: GET runs/123/jobs\.jobs\[\]\.id",
    ):
        _connector().list_workflow_run_jobs(123)


def test_list_jobs_job_identity_guard_preserves_run_lineage_guard(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"jobs": [{"id": 9, "run_id": 124}]}),
    )
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_JOB_RUN_IDENTITY_MISMATCH"):
        _connector().list_workflow_run_jobs(123)


def test_list_jobs_empty_collection_remains_valid(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"total_count": 0, "jobs": []}),
    )
    assert _connector().list_workflow_run_jobs(123)["jobs"] == []
