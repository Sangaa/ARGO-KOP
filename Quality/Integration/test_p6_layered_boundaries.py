"""Layered P6 regression: isolate failures by execution boundary.

This module owns scenario coverage only. The functional classification logic
remains in the shared integration layer, while unittest provides the standard
CI discovery/execution contract.
"""

import unittest

from ci_impact_correlation import classify_execution_evidence


def p6_a_functional(execution_passed: bool) -> str:
    return "PASS" if execution_passed else "FAIL"


def p6_b_observation(run_present: bool, job_present: bool) -> str:
    if not run_present:
        return "MISSING"
    if not job_present:
        return "INVALID"
    return "PRESENT"


def p6_c_identity(baseline_sha: str, run_sha: str) -> str:
    if not baseline_sha or not run_sha:
        return "MISSING"
    return "CURRENT" if baseline_sha == run_sha else "STALE"


def p6_d_artifact(artifact_present: bool, artifact_sha: str, run_sha: str) -> str:
    if not artifact_present or not artifact_sha:
        return "MISSING"
    return "VALID" if artifact_sha == run_sha else "INVALID"


def p6_e_classification(
    execution_passed: bool, baseline_sha: str, run_sha: str, artifact_sha: str
) -> str:
    return classify_execution_evidence(
        baseline_sha, run_sha, artifact_sha, execution_passed
    )


class P6LayeredBoundaryTests(unittest.TestCase):
    def test_p6_functional_failure_isolated(self) -> None:
        self.assertEqual(p6_a_functional(False), "FAIL")
        self.assertEqual(p6_b_observation(False, False), "MISSING")

    def test_p6_missing_observation_is_not_execution_failure(self) -> None:
        self.assertEqual(p6_a_functional(True), "PASS")
        self.assertEqual(p6_b_observation(False, False), "MISSING")
        self.assertEqual(
            p6_e_classification(True, "HEAD", "HEAD-OLD", "HEAD-OLD"),
            "VALID_EXECUTION_STALE_BASELINE",
        )

    def test_p6_current_chain_requires_all_identity_links(self) -> None:
        self.assertEqual(p6_b_observation(True, True), "PRESENT")
        self.assertEqual(p6_c_identity("HEAD", "HEAD"), "CURRENT")
        self.assertEqual(p6_d_artifact(True, "HEAD", "HEAD"), "VALID")
        self.assertEqual(
            p6_e_classification(True, "HEAD", "HEAD", "HEAD"),
            "VALID_CURRENT_EXECUTION",
        )

    def test_p6_artifact_mismatch_isolated(self) -> None:
        self.assertEqual(p6_a_functional(True), "PASS")
        self.assertEqual(p6_b_observation(True, True), "PRESENT")
        self.assertEqual(p6_c_identity("HEAD", "HEAD"), "CURRENT")
        self.assertEqual(p6_d_artifact(True, "ARTIFACT-OLD", "HEAD"), "INVALID")
        self.assertEqual(
            p6_e_classification(True, "HEAD", "HEAD", "ARTIFACT-OLD"),
            "ARTIFACT_IDENTITY_MISMATCH",
        )

    def test_p6_missing_artifact_is_not_execution_failure(self) -> None:
        self.assertEqual(p6_a_functional(True), "PASS")
        self.assertEqual(p6_d_artifact(False, "", "HEAD"), "MISSING")
        self.assertEqual(
            p6_e_classification(True, "HEAD", "HEAD", ""),
            "ARTIFACT_EVIDENCE_MISSING",
        )

    def test_p6_missing_identity_is_not_execution_failure(self) -> None:
        self.assertEqual(p6_a_functional(True), "PASS")
        self.assertEqual(p6_c_identity("", "HEAD"), "MISSING")
        self.assertEqual(
            p6_e_classification(True, "", "HEAD", "HEAD"),
            "IDENTITY_EVIDENCE_MISSING",
        )

    def test_p6_failed_execution_remains_failure(self) -> None:
        self.assertEqual(
            p6_e_classification(False, "HEAD", "HEAD", "HEAD"),
            "EXECUTION_FAILED",
        )
