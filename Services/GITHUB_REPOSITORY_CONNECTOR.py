"""Concrete GitHub Contents API connector for the governed repository boundary.

Provider-specific implementation. Credentials and repository identity come
from the runtime environment; no authority is inferred from technical access.
"""
from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError, ConnectorFile, RepositoryConnector


@dataclass(frozen=True)
class GitHubConnectorConfig:
    owner: str
    repo: str
    token: str
    branch: str = "main"
    api_base: str = "https://api.github.com"

    @classmethod
    def from_environment(cls) -> "GitHubConnectorConfig":
        owner = os.environ.get("ARGO_GITHUB_OWNER", "").strip()
        repo = os.environ.get("ARGO_GITHUB_REPO", "").strip()
        token = os.environ.get("ARGO_GITHUB_TOKEN", "").strip()
        branch = os.environ.get("ARGO_GITHUB_BRANCH", "main").strip() or "main"
        if not owner or not repo or not token:
            raise ConnectorError("GITHUB_CONNECTOR_CONFIGURATION_INCOMPLETE")
        return cls(owner=owner, repo=repo, token=token, branch=branch)


class GitHubRepositoryConnector(RepositoryConnector):
    """GitHub Contents API implementation of the provider-neutral connector."""

    def __init__(self, config: GitHubConnectorConfig, *, timeout: float = 20.0) -> None:
        self._config = config
        self._timeout = timeout

    def _url(self, path: str, *, include_ref: bool = False) -> str:
        encoded = "/".join(urllib.parse.quote(part, safe="") for part in path.split("/"))
        url = f"{self._config.api_base}/repos/{self._config.owner}/{self._config.repo}/contents/{encoded}"
        if include_ref:
            url += "?ref=" + urllib.parse.quote(self._config.branch, safe="")
        return url

    def _request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        *,
        include_ref: bool = False,
    ) -> dict[str, Any]:
        url = self._url(path, include_ref=include_ref)
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=data, method=method)
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self._config.token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "ARGO-KOP-Governed-Repository-Connector")
        if data is not None:
            request.add_header("Content-Type", "application/json")

        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = ""
            if getattr(exc, "fp", None) is not None:
                try:
                    body = exc.read().decode("utf-8", errors="replace")
                except (AttributeError, OSError):
                    body = ""
            if exc.code == 404:
                raise FileNotFoundError(path) from exc
            raise ConnectorError(f"GITHUB_HTTP_{exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ConnectorError(f"GITHUB_CONNECTOR_UNAVAILABLE: {exc}") from exc

    @staticmethod
    def _decode_content(payload: dict[str, Any], path: str) -> str:
        if payload.get("type") != "file":
            raise ConnectorError(f"GITHUB_TARGET_NOT_FILE: {path}")
        encoded = payload.get("content", "").replace("\n", "")
        try:
            return base64.b64decode(encoded).decode("utf-8")
        except (ValueError, UnicodeDecodeError) as exc:
            raise ConnectorError(f"GITHUB_CONTENT_DECODE_FAILED: {path}") from exc

    def read_current(self, path: str) -> ConnectorFile | None:
        try:
            payload = self._request("GET", path, None, include_ref=True)
        except FileNotFoundError:
            return None
        return ConnectorFile(path=path, sha=str(payload["sha"]), content=self._decode_content(payload, path))

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        if self.read_current(path) is not None:
            raise ConnectorError(f"GITHUB_CREATE_RACE_OR_EXISTING_FILE: {path}")
        payload = {
            "message": commit_message,
            "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
            "branch": self._config.branch,
        }
        result = self._request("PUT", path, payload)
        return str(result["commit"]["sha"])

    def update_file(self, path: str, content: str, commit_message: str, current_sha: str) -> str:
        current = self.read_current(path)
        if current is None:
            raise ConnectorError(f"GITHUB_UPDATE_TARGET_MISSING: {path}")
        if current.sha != current_sha:
            raise ConnectorError(f"GITHUB_STALE_TARGET_SHA: expected={current_sha} actual={current.sha}")
        payload = {
            "message": commit_message,
            "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
            "sha": current_sha,
            "branch": self._config.branch,
        }
        result = self._request("PUT", path, payload)
        return str(result["commit"]["sha"])

    def read_back(self, path: str) -> ConnectorFile:
        current = self.read_current(path)
        if current is None:
            raise ConnectorError(f"GITHUB_READ_BACK_MISSING: {path}")
        return current
