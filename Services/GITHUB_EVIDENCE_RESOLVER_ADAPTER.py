"""Read-only GitHub immutable-artifact evidence resolver adapter.

This adapter can establish acquisition of an exact JSON artifact at an exact
GitHub commit/path. It cannot authenticate the model/provider claims contained
inside that artifact and performs no repository writes.

Participant/attestation observations retain their existing structured behavior.
Generic quarantine re-acquisition returns the decoded JSON value under
``evidence_content`` without laundering its fields into resolver control state.
"""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import (
    EvidenceResolverAdapterError,
    ResolverAcquisition,
    ResolverAdapterIdentity,
)


REF_PREFIX = "github+artifact://"
FULL_SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
RESERVED_OBSERVATION_KEYS = {"resolver_id", "resolution_id", "requested_ref"}


@dataclass(frozen=True)
class GitHubArtifactReference:
    owner: str
    repo: str
    commit_sha: str
    path: str


@dataclass(frozen=True)
class GitHubEvidenceResolverConfig:
    token: str
    api_base: str = "https://api.github.com"
    adapter_id: str = "resolver/github-immutable-artifact"
    adapter_kind: str = "github-artifact-evidence-resolver"
    implementation_id: str = "github-artifact-resolver-v1"

    @classmethod
    def from_environment(cls) -> "GitHubEvidenceResolverConfig":
        token = os.environ.get("ARGO_GITHUB_TOKEN", "").strip()
        if not token:
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_RESOLVER_TOKEN_MISSING")
        return cls(token=token)


def parse_github_artifact_reference(value: str) -> GitHubArtifactReference:
    if not isinstance(value, str) or not value.startswith(REF_PREFIX):
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_REFERENCE_SCHEME_INVALID")
    remainder = value[len(REF_PREFIX):]
    if "@" not in remainder:
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_REFERENCE_COMMIT_MISSING")
    repo_part, commit_and_path = remainder.split("@", 1)
    if repo_part.count("/") != 1:
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_REPOSITORY_IDENTITY_INVALID")
    owner, repo = repo_part.split("/", 1)
    if not owner or not repo:
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_REPOSITORY_IDENTITY_INVALID")
    if "/" not in commit_and_path:
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_PATH_MISSING")
    commit_sha, path = commit_and_path.split("/", 1)
    if not FULL_SHA_RE.match(commit_sha):
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_COMMIT_NOT_IMMUTABLE_FULL_SHA")
    if not path or path.startswith("/") or "\\" in path:
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_PATH_INVALID")
    segments = path.split("/")
    if any(segment in {"", ".", ".."} for segment in segments):
        raise EvidenceResolverAdapterError("GITHUB_ARTIFACT_PATH_INVALID")
    return GitHubArtifactReference(owner=owner, repo=repo, commit_sha=commit_sha.lower(), path=path)


class GitHubEvidenceResolverAdapter:
    """Read-only provider adapter for immutable GitHub JSON evidence artifacts."""

    def __init__(
        self,
        config: GitHubEvidenceResolverConfig,
        *,
        timeout: float = 20.0,
        transport: Callable[[urllib.request.Request, float], dict[str, Any]] | None = None,
    ) -> None:
        self._config = config
        self._timeout = timeout
        self._transport = transport or self._default_transport
        self._sequence = 0

    @property
    def identity(self) -> ResolverAdapterIdentity:
        return ResolverAdapterIdentity(
            adapter_id=self._config.adapter_id,
            adapter_kind=self._config.adapter_kind,
            implementation_id=self._config.implementation_id,
        )

    def _next_acquisition_id(self, channel: str) -> str:
        self._sequence += 1
        return f"GH-EVID-{channel}-{self._sequence:06d}"

    @staticmethod
    def _utc_now() -> str:
        return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    def _url(self, reference: GitHubArtifactReference) -> str:
        owner = urllib.parse.quote(reference.owner, safe="")
        repo = urllib.parse.quote(reference.repo, safe="")
        path = "/".join(urllib.parse.quote(segment, safe="") for segment in reference.path.split("/"))
        ref = urllib.parse.quote(reference.commit_sha, safe="")
        return f"{self._config.api_base}/repos/{owner}/{repo}/contents/{path}?ref={ref}"

    def _request(self, reference: GitHubArtifactReference) -> dict[str, Any]:
        request = urllib.request.Request(self._url(reference), method="GET")
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self._config.token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "ARGO-KOP-Evidence-Resolver")
        try:
            return self._transport(request, self._timeout)
        except FileNotFoundError:
            raise
        except EvidenceResolverAdapterError:
            raise
        except Exception as exc:
            raise EvidenceResolverAdapterError(f"GITHUB_EVIDENCE_RESOLVER_UNAVAILABLE:{exc}") from exc

    @staticmethod
    def _default_transport(request: urllib.request.Request, timeout: float) -> dict[str, Any]:
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise FileNotFoundError(request.full_url) from exc
            body = ""
            try:
                body = exc.read().decode("utf-8", errors="replace")
            except (AttributeError, OSError):
                pass
            raise EvidenceResolverAdapterError(f"GITHUB_EVIDENCE_HTTP_{exc.code}:{body[:300]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise EvidenceResolverAdapterError(f"GITHUB_EVIDENCE_RESOLVER_UNAVAILABLE:{exc}") from exc

    @staticmethod
    def _decode_json_value(payload: dict[str, Any], reference: GitHubArtifactReference) -> tuple[Any, str]:
        if not isinstance(payload, dict) or payload.get("type") != "file":
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_TARGET_NOT_FILE")
        blob_sha = payload.get("sha")
        if not isinstance(blob_sha, str) or not blob_sha.strip():
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_BLOB_SHA_MISSING")
        encoded = payload.get("content")
        if not isinstance(encoded, str):
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_CONTENT_MISSING")
        try:
            raw = base64.b64decode(encoded.replace("\n", ""), validate=True).decode("utf-8")
        except (ValueError, UnicodeDecodeError) as exc:
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_CONTENT_DECODE_FAILED") from exc
        try:
            return json.loads(raw), blob_sha
        except json.JSONDecodeError as exc:
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_JSON_INVALID") from exc

    @classmethod
    def _decode_json_artifact(cls, payload: dict[str, Any], reference: GitHubArtifactReference) -> tuple[dict, str]:
        observation, blob_sha = cls._decode_json_value(payload, reference)
        if not isinstance(observation, dict):
            raise EvidenceResolverAdapterError("GITHUB_EVIDENCE_JSON_NOT_OBJECT")
        injected = RESERVED_OBSERVATION_KEYS.intersection(observation)
        if injected:
            raise EvidenceResolverAdapterError(
                "GITHUB_EVIDENCE_RESERVED_IDENTITY_INJECTION:" + ",".join(sorted(injected))
            )
        observation = dict(observation)
        observation["github_artifact_owner"] = reference.owner
        observation["github_artifact_repo"] = reference.repo
        observation["github_artifact_commit_sha"] = reference.commit_sha
        observation["github_artifact_path"] = reference.path
        observation["github_artifact_blob_sha"] = blob_sha
        return observation, blob_sha

    def _unavailable(self, evidence_ref: str, channel: str, started: str) -> ResolverAcquisition:
        return ResolverAcquisition(
            adapter_id=self.identity.adapter_id,
            adapter_kind=self.identity.adapter_kind,
            acquisition_id=self._next_acquisition_id(channel),
            acquisition_surface="github-contents-api-immutable-ref",
            started_at=started,
            completed_at=self._utc_now(),
            requested_ref=evidence_ref,
            observation={"status": "UNAVAILABLE", "observed_ref": None},
        )

    def _acquire(self, evidence_ref: str, channel: str) -> ResolverAcquisition:
        reference = parse_github_artifact_reference(evidence_ref)
        acquisition_id = self._next_acquisition_id(channel)
        started = self._utc_now()
        try:
            payload = self._request(reference)
        except FileNotFoundError:
            completed = self._utc_now()
            return ResolverAcquisition(
                adapter_id=self.identity.adapter_id,
                adapter_kind=self.identity.adapter_kind,
                acquisition_id=acquisition_id,
                acquisition_surface="github-contents-api-immutable-ref",
                started_at=started,
                completed_at=completed,
                requested_ref=evidence_ref,
                observation={"status": "UNAVAILABLE", "observed_ref": None},
            )
        observation, _blob_sha = self._decode_json_artifact(payload, reference)
        observation.setdefault("status", "FOUND")
        observation.setdefault("observed_ref", evidence_ref)
        completed = self._utc_now()
        return ResolverAcquisition(
            adapter_id=self.identity.adapter_id,
            adapter_kind=self.identity.adapter_kind,
            acquisition_id=acquisition_id,
            acquisition_surface="github-contents-api-immutable-ref",
            started_at=started,
            completed_at=completed,
            requested_ref=evidence_ref,
            observation=observation,
        )

    def acquire_external(self, evidence_ref: str) -> ResolverAcquisition:
        """Re-acquire one immutable JSON value for quarantine correlation.

        The decoded value is nested under ``evidence_content`` so arbitrary
        external keys cannot become resolver control fields. Successful access
        proves only technical re-acquisition from the immutable GitHub ref.
        """
        reference = parse_github_artifact_reference(evidence_ref)
        acquisition_id = self._next_acquisition_id("EXTERNAL")
        started = self._utc_now()
        try:
            payload = self._request(reference)
        except FileNotFoundError:
            return ResolverAcquisition(
                adapter_id=self.identity.adapter_id,
                adapter_kind=self.identity.adapter_kind,
                acquisition_id=acquisition_id,
                acquisition_surface="github-contents-api-immutable-ref",
                started_at=started,
                completed_at=self._utc_now(),
                requested_ref=evidence_ref,
                observation={"status": "UNAVAILABLE", "observed_ref": None},
            )

        evidence_content, blob_sha = self._decode_json_value(payload, reference)
        return ResolverAcquisition(
            adapter_id=self.identity.adapter_id,
            adapter_kind=self.identity.adapter_kind,
            acquisition_id=acquisition_id,
            acquisition_surface="github-contents-api-immutable-ref",
            started_at=started,
            completed_at=self._utc_now(),
            requested_ref=evidence_ref,
            observation={
                "status": "FOUND",
                "observed_ref": evidence_ref,
                "evidence_content": evidence_content,
                "github_artifact_owner": reference.owner,
                "github_artifact_repo": reference.repo,
                "github_artifact_commit_sha": reference.commit_sha,
                "github_artifact_path": reference.path,
                "github_artifact_blob_sha": blob_sha,
            },
        )

    def acquire_participant(self, evidence_ref: str) -> ResolverAcquisition:
        return self._acquire(evidence_ref, "PARTICIPANT")

    def acquire_attestation(self, evidence_ref: str) -> ResolverAcquisition:
        return self._acquire(evidence_ref, "ATTESTATION")
