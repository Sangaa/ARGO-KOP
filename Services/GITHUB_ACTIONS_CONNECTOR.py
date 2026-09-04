"""Concrete GitHub Actions control/observation connector.

This surface is intentionally separate from the Contents connector. Repository
read/write authority does not imply Actions invocation or execution visibility.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from Services.GITHUB_ACTIONS_CONNECTOR_INTERFACE import GitHubActionsConnector
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


class GitHubActionsRepositoryConnector(GitHubActionsConnector):
    """GitHub REST Actions implementation for governed execution evidence."""

    def __init__(self, *, owner: str, repo: str, token: str,
                 api_base: str = "https://api.github.com", timeout: float = 20.0) -> None:
        self._owner = owner
        self._repo = repo
        self._token = token
        self._api_base = api_base.rstrip("/")
        self._timeout = timeout

    @classmethod
    def from_environment(cls) -> "GitHubActionsRepositoryConnector":
        owner = os.environ.get("ARGO_GITHUB_OWNER", "").strip()
        repo = os.environ.get("ARGO_GITHUB_REPO", "").strip()
        token = os.environ.get("ARGO_GITHUB_TOKEN", "").strip()
        if not owner or not repo or not token:
            raise ConnectorError("GITHUB_ACTIONS_CONNECTOR_CONFIGURATION_INCOMPLETE")
        return cls(owner=owner, repo=repo, token=token)

    def _url(self, path: str, params: dict[str, Any] | None = None) -> str:
        url = f"{self._api_base}/repos/{self._owner}/{self._repo}/actions/{path.lstrip('/') }"
        if params:
            url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        return url

    @staticmethod
    def _decode_response(response: Any, context: str, *, allow_empty: bool) -> dict[str, Any]:
        raw = response.read()
        if not raw:
            if allow_empty:
                return {}
            raise ConnectorError(f"GITHUB_ACTIONS_EMPTY_RESPONSE: {context}")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ConnectorError(f"GITHUB_ACTIONS_RESPONSE_ENCODING_INVALID: {context}") from exc
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ConnectorError(f"GITHUB_ACTIONS_RESPONSE_JSON_INVALID: {context}") from exc
        if not isinstance(payload, dict):
            raise ConnectorError(f"GITHUB_ACTIONS_RESPONSE_STRUCTURE_INVALID: {context}")
        return payload

    def _request(self, method: str, path: str, *, params: dict[str, Any] | None = None,
                 payload: dict[str, Any] | None = None, allow_empty: bool = False) -> dict[str, Any]:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(self._url(path, params), data=data, method=method)
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self._token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "ARGO-KOP-Governed-Actions-Connector")
        if data is not None:
            request.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                return self._decode_response(response, f"{method} {path}", allow_empty=allow_empty)
        except urllib.error.HTTPError as exc:
            body = ""
            if getattr(exc, "fp", None) is not None:
                try:
                    body = exc.read().decode("utf-8", errors="replace")
                except (AttributeError, OSError):
                    body = ""
            raise ConnectorError(f"GITHUB_ACTIONS_HTTP_{exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ConnectorError(f"GITHUB_ACTIONS_CONNECTOR_UNAVAILABLE: {exc}") from exc

    def list_workflow_runs(self, *, branch: str | None = None, event: str | None = None,
                           head_sha: str | None = None, status: str | None = None,
                           per_page: int = 10) -> dict:
        if not 1 <= per_page <= 100:
            raise ConnectorError("GITHUB_ACTIONS_INVALID_PER_PAGE")
        return self._request("GET", "runs", params={
            "branch": branch,
            "event": event,
            "head_sha": head_sha,
            "status": status,
            "per_page": per_page,
        })

    def get_workflow_run(self, run_id: int) -> dict:
        if run_id <= 0:
            raise ConnectorError("GITHUB_ACTIONS_INVALID_RUN_ID")
        return self._request("GET", f"runs/{run_id}")

    def dispatch_workflow(self, workflow_id: str | int, *, ref: str,
                          inputs: dict[str, str] | None = None) -> bool:
        if not ref.strip():
            raise ConnectorError("GITHUB_ACTIONS_INVALID_REF")
        if isinstance(workflow_id, str) and not workflow_id.strip():
            raise ConnectorError("GITHUB_ACTIONS_INVALID_WORKFLOW_ID")
        self._request("POST", f"workflows/{workflow_id}/dispatches",
                      payload={"ref": ref, "inputs": inputs or {}}, allow_empty=True)
        return True

    def list_workflow_run_jobs(self, run_id: int) -> dict:
        if run_id <= 0:
            raise ConnectorError("GITHUB_ACTIONS_INVALID_RUN_ID")
        return self._request("GET", f"runs/{run_id}/jobs", params={"per_page": 100})

    def get_workflow_job_logs(self, job_id: int) -> str:
        if job_id <= 0:
            raise ConnectorError("GITHUB_ACTIONS_INVALID_JOB_ID")
        request = urllib.request.Request(self._url(f"jobs/{job_id}/logs"), method="GET")
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self._token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "ARGO-KOP-Governed-Actions-Connector")
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            body = ""
            if getattr(exc, "fp", None) is not None:
                try:
                    body = exc.read().decode("utf-8", errors="replace")
                except (AttributeError, OSError):
                    body = ""
            raise ConnectorError(f"GITHUB_ACTIONS_HTTP_{exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ConnectorError(f"GITHUB_ACTIONS_CONNECTOR_UNAVAILABLE: {exc}") from exc
