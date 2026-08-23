"""Provider-neutral GitHub Actions control/observation surface.

The interface is deliberately separate from the repository Contents connector:
repository authority, Actions invocation, and execution observation are distinct
capabilities and must not be inferred from one another.
"""
from __future__ import annotations

from typing import Protocol


class GitHubActionsConnector(Protocol):
    def list_workflow_runs(
        self,
        *,
        branch: str | None = None,
        event: str | None = None,
        head_sha: str | None = None,
        status: str | None = None,
        per_page: int = 10,
    ) -> dict:
        """List workflow runs using explicit execution filters."""

    def get_workflow_run(self, run_id: int) -> dict:
        """Return one exact workflow run by authoritative run identity."""

    def dispatch_workflow(
        self,
        workflow_id: str | int,
        *,
        ref: str,
        inputs: dict[str, str] | None = None,
    ) -> bool:
        """Dispatch a workflow and return True only after GitHub accepts it."""

    def list_workflow_run_jobs(self, run_id: int) -> dict:
        """List jobs for an already identified workflow run."""

    def get_workflow_job_logs(self, job_id: int) -> str:
        """Return logs for an already identified workflow job."""
