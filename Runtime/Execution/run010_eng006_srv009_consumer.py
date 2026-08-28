"""Minimal governed ENG-006 -> SRV-009 callable consumer seam.

This adapter proves the runtime-facing callable boundary without granting
canonical authority. Provider-specific I/O remains behind RepositoryConnector.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError, RepositoryConnector


@dataclass(frozen=True)
class DispatchResult:
    status: str
    operation: str
    path: str
    commit_sha: str | None = None


def dispatch_srv009_update(
    connector: RepositoryConnector,
    *,
    path: str,
    content: str,
    commit_message: str,
    authorized: bool,
    current_sha: str | None = None,
) -> DispatchResult:
    """Dispatch one governed SRV-009 repository update.

    The adapter requires explicit authorization and a caller-supplied current
    SHA for updates. It performs the SRV-009 read-before-write and read-back
    boundary; it does not infer governance authority from connector access.
    """
    if not authorized:
        return DispatchResult("REJECTED", "SRV-009", path)

    if current_sha is None:
        current = connector.read_current(path)
        if current is None:
            commit_sha = connector.create_file(path, content, commit_message)
            persisted = connector.read_back(path)
        else:
            commit_sha = connector.update_file(
                path, content, commit_message, current.sha
            )
            persisted = connector.read_back(path)
    else:
        commit_sha = connector.update_file(
            path, content, commit_message, current_sha
        )
        persisted = connector.read_back(path)

    if persisted.content != content:
        raise ConnectorError("SRV009_READ_BACK_CONTENT_MISMATCH")

    return DispatchResult("COMPLETED", "SRV-009", persisted.path, commit_sha)
