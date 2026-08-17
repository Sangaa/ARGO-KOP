"""Provider-neutral repository connector interface for the SRV-009 boundary.

This module defines the callable surface required by the production
ENG-006 -> SRV-009 adapter. It intentionally contains no provider-specific
network logic, credentials, or repository authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Optional


class ConnectorError(RuntimeError):
    """Explicit connector failure; callers must not infer success."""


@dataclass(frozen=True)
class ConnectorFile:
    path: str
    sha: str
    content: str


class RepositoryConnector(Protocol):
    def read_current(self, path: str) -> Optional[ConnectorFile]:
        """Return the current artifact or None only for confirmed absence."""

    def create_file(self, path: str, content: str, commit_message: str) -> str:
        """Create a confirmed-absent artifact and return commit identity."""

    def update_file(
        self,
        path: str,
        content: str,
        commit_message: str,
        current_sha: str,
    ) -> str:
        """Update only against the currently observed artifact identity."""

    def read_back(self, path: str) -> ConnectorFile:
        """Read the persisted artifact after mutation."""


PRODUCTION_CONNECTOR_REQUIREMENTS = (
    "confirmed existence/absence",
    "current artifact identity",
    "create/update separation",
    "post-write read-back",
    "explicit connector failure states",
    "no authority inference from technical access",
)
