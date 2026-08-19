"""Shared P6 reconciliation domain model and decision engine.

Test modules should consume this component rather than duplicate reconciliation
rules. Live CI evidence remains outside this domain layer.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    run_id: str | None
    head_sha: str | None
    artifact_sha: str | None
    result: str


class P6ReconciliationEngine:
    """Apply P6 evidence boundaries in a deterministic order."""

    def reconcile(self, evidence: Evidence, expected_sha: str) -> str:
        if evidence.run_id is None:
            return "NO_OBSERVATION"
        if evidence.result != "PASS":
            return "EXECUTION_FAILED"
        if evidence.head_sha is None:
            return "IDENTITY_EVIDENCE_MISSING"
        if evidence.head_sha != expected_sha:
            return "VALID_EXECUTION_STALE_BASELINE"
        if evidence.artifact_sha is None:
            return "ARTIFACT_EVIDENCE_MISSING"
        if evidence.artifact_sha != evidence.head_sha:
            return "ARTIFACT_IDENTITY_MISMATCH"
        return "VALID_CURRENT_EXECUTION"
