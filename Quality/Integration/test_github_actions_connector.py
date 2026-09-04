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
        return FakeResponse({
            "total_count": 1,
            "workflow_runs": [{"id": 123, "head_sha": "abc", "head_branch": "main", "event": "push", "status": "completed"}],
        })

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    result = connector.list_workflow_runs(branch="main", event="push", head_sha="abc", status="completed")
    assert result["workflow_runs"][0]["id"] == 123
    assert result["workflow_runs"][0]["head_branch"] == "main"
    assert result["workflow_runs"][0]["event"] == "push"
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


def test_get_workflow_run_requires_matching_provider_identity(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse({"id": 123, "status": "completed"}))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    result = connector.get_workflow_run(123)
    assert result["id"] == 123


def test_get_workflow_run_rejects_missing_or_mismatched_provider_identity(monkeypatch: pytest.MonkeyPatch):
    responses = [FakeResponse({"status": "completed"}), FakeResponse({"id": 124, "status": "completed"})]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.get_workflow_run(123)
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RUN_IDENTITY_MISMATCH"):
        connector.get_workflow_run(123)


def test_boolean_execution_identity_is_rejected_before_transport(monkeypatch: pytest.MonkeyPatch):
    calls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: calls.append(request))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_RUN_ID"):
        connector.get_workflow_run(True)
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_RUN_ID"):
        connector.list_workflow_run_jobs(True)
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_INVALID_JOB_ID"):
        connector.get_workflow_job_logs(True)
    assert calls == []


def test_list_workflow_runs_accepts_empty_collection(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse({"total_count": 0, "workflow_runs": []}))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.list_workflow_runs()["workflow_runs"] == []


def test_list_workflow_runs_rejects_invalid_collection_shape(monkeypatch: pytest.MonkeyPatch):
    responses = [FakeResponse({"total_count": 0}), FakeResponse({"workflow_runs": {}}), FakeResponse({"workflow_runs": [123]})]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    for _ in range(3):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
            connector.list_workflow_runs()


def test_list_workflow_run_jobs_accepts_empty_collection(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse({"total_count": 0, "jobs": []}))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.list_workflow_run_jobs(123)["jobs"] == []


def test_list_workflow_run_jobs_rejects_invalid_collection_shape(monkeypatch: pytest.MonkeyPatch):
    responses = [FakeResponse({"total_count": 0}), FakeResponse({"jobs": {}}), FakeResponse({"jobs": [123]})]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    for _ in range(3):
        with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
            connector.list_workflow_run_jobs(123)


def test_list_workflow_run_jobs_requires_matching_run_lineage(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"total_count": 1, "jobs": [{"id": 9, "run_id": 123}]}),
    )
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    result = connector.list_workflow_run_jobs(123)
    assert result["jobs"][0]["run_id"] == 123


def test_list_workflow_run_jobs_rejects_missing_or_mismatched_run_lineage(monkeypatch: pytest.MonkeyPatch):
    responses = [
        FakeResponse({"jobs": [{"id": 9}]}),
        FakeResponse({"jobs": [{"id": 9, "run_id": 124}]}),
    ]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_run_jobs(123)
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_JOB_RUN_IDENTITY_MISMATCH"):
        connector.list_workflow_run_jobs(123)


def test_list_workflow_run_jobs_rejects_boolean_provider_run_identity(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"jobs": [{"id": 9, "run_id": True}]}),
    )
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_run_jobs(123)


def test_list_workflow_runs_binds_exact_head_sha_filter(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "urllib.request.urlopen",
        lambda request, timeout: FakeResponse({"workflow_runs": [{"id": 1, "head_sha": "abc"}]}),
    )
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.list_workflow_runs(head_sha="abc")["workflow_runs"][0]["head_sha"] == "abc"


def test_list_workflow_runs_rejects_missing_or_mismatched_head_sha_when_filtered(monkeypatch: pytest.MonkeyPatch):
    responses = [
        FakeResponse({"workflow_runs": [{"id": 1}]}),
        FakeResponse({"workflow_runs": [{"id": 1, "head_sha": "def"}]}),
    ]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_runs(head_sha="abc")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_HEAD_SHA_FILTER_MISMATCH"):
        connector.list_workflow_runs(head_sha="abc")


def test_list_workflow_runs_does_not_require_head_sha_without_filter(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse({"workflow_runs": [{"id": 1}]}))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.list_workflow_runs()["workflow_runs"][0]["id"] == 1


def test_list_workflow_runs_rejects_missing_or_mismatched_direct_filter_fields(monkeypatch: pytest.MonkeyPatch):
    responses = [
        FakeResponse({"workflow_runs": [{"id": 1, "event": "push"}]}),
        FakeResponse({"workflow_runs": [{"id": 1, "head_branch": "dev", "event": "push"}]}),
        FakeResponse({"workflow_runs": [{"id": 1, "head_branch": "main"}]}),
        FakeResponse({"workflow_runs": [{"id": 1, "head_branch": "main", "event": "pull_request"}]}),
    ]
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: responses.pop(0))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_runs(branch="main", event="push")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_BRANCH_FILTER_MISMATCH"):
        connector.list_workflow_runs(branch="main", event="push")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID"):
        connector.list_workflow_runs(branch="main", event="push")
    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_EVENT_FILTER_MISMATCH"):
        connector.list_workflow_runs(branch="main", event="push")


def test_list_workflow_runs_direct_filters_accept_empty_collection(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda request, timeout: FakeResponse({"workflow_runs": []}))
    connector = GitHubActionsRepositoryConnector(owner="Sangaa", repo="ARGO-KOP", token="test")
    assert connector.list_workflow_runs(branch="main", event="push")["workflow_runs"] == []
