"""Shared P6 reconciliation domain model and decision engine.

Test modules should consume this component rather than duplicate reconciliation
rules. Live CI evidence remains outside this domain layer.

Important boundary: an empty observation result and an unavailable/rejected
observation surface are different states. The engine must not collapse a
connector capability failure into ``NO_OBSERVATION``.

Observation-state provenance is explicit and mandatory: callers must state
whether evidence was observed, whether the query legitimately returned an
empty set, or whether the observation surface was unavailable/rejected. This
prevents adapters from silently converting capability failures into repository
claims.
"""

from dataclasses import dataclass


OBSERVATION_STATES = {
    "OBSERVED",
    "EMPTY_RESULT",
    "SURFACE_UNAVAILABLE",
    "SURFACE_REJECTED",
}


@dataclass(frozen=True)
class Evidence:
    run_id: str | None
    head_sha: str | None
    artifact_sha: str | None
    result: str
    observation_state: str


class P6ReconciliationEngine:
    """Apply P6 evidence boundaries in a deterministic order."""

    def reconcile(self, evidence: Evidence, expected_sha: str) -> str:
        if evidence.observation_state == "SURFACE_UNAVAILABLE":
            return "OBSERVATION_SURFACE_UNAVAILABLE"
        if evidence.observation_state == "SURFACE_REJECTED":
            return "OBSERVATION_SURFACE_REJECTED"
        if evidence.observation_state not in {"OBSERVED", "EMPTY_RESULT"}:
            return "OBSERVATION_STATE_UNKNOWN"
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
