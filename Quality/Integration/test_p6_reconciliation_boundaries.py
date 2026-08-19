"""P6-08/P6-09 boundary regression fixtures.

These tests intentionally validate the decision boundary, not live GitHub state.
Live execution evidence remains a separate CI responsibility.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    run_id: str | None
    head_sha: str | None
    artifact_sha: str | None
    result: str


def reconcile(evidence: Evidence, expected_sha: str) -> str:
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


def test_p6_08_matrix_update_boundary_is_evidence_bearing():
    assert reconcile(Evidence("r1", "sha1", "sha1", "PASS"), "sha1") == "VALID_CURRENT_EXECUTION"
    assert reconcile(Evidence("r1", "old", "old", "PASS"), "sha1") == "VALID_EXECUTION_STALE_BASELINE"


def test_p6_09_reconciliation_preserves_first_failure_boundary():
    assert reconcile(Evidence(None, None, None, "PASS"), "sha1") == "NO_OBSERVATION"
    assert reconcile(Evidence("r1", None, None, "PASS"), "sha1") == "IDENTITY_EVIDENCE_MISSING"
    assert reconcile(Evidence("r1", "sha1", None, "PASS"), "sha1") == "ARTIFACT_EVIDENCE_MISSING"
    assert reconcile(Evidence("r1", "sha1", "old", "PASS"), "sha1") == "ARTIFACT_IDENTITY_MISMATCH"
    assert reconcile(Evidence("r1", "sha1", "sha1", "FAIL"), "sha1") == "EXECUTION_FAILED"


def test_p6_reconciliation_never_promotes_stale_execution():
    assert reconcile(Evidence("r1", "old", "old", "PASS"), "sha1") != "VALID_CURRENT_EXECUTION"
