"""P6-08/P6-09 boundary regression tests.

The decision logic lives in p6_reconciliation.py. This module owns only
scenario coverage and an explicit stdlib test-runner entry point.
"""

import unittest

from p6_reconciliation import Evidence, P6ReconciliationEngine, OBSERVATION_STATES


class P6ReconciliationBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = P6ReconciliationEngine()

    def test_observation_state_vocabulary_is_explicit(self) -> None:
        self.assertEqual(
            OBSERVATION_STATES,
            {
                "OBSERVED",
                "EMPTY_RESULT",
                "SURFACE_UNAVAILABLE",
                "SURFACE_REJECTED",
            },
        )

    def test_p6_08_current_execution_is_evidence_bearing(self) -> None:
        evidence = Evidence("r1", "sha1", "sha1", "PASS", "OBSERVED")
        self.assertEqual(
            self.engine.reconcile(evidence, "sha1"), "VALID_CURRENT_EXECUTION"
        )

    def test_p6_08_stale_execution_is_not_current(self) -> None:
        evidence = Evidence("r1", "old", "old", "PASS", "OBSERVED")
        self.assertEqual(
            self.engine.reconcile(evidence, "sha1"),
            "VALID_EXECUTION_STALE_BASELINE",
        )

    def test_p6_09_first_failure_boundary_is_preserved(self) -> None:
        cases = [
            (Evidence(None, None, None, "PASS", "OBSERVED"), "NO_OBSERVATION"),
            (Evidence(None, None, None, "PASS", "EMPTY_RESULT"), "NO_OBSERVATION"),
            (Evidence(None, None, None, "PASS", "SURFACE_UNAVAILABLE"), "OBSERVATION_SURFACE_UNAVAILABLE"),
            (Evidence(None, None, None, "PASS", "SURFACE_REJECTED"), "OBSERVATION_SURFACE_REJECTED"),
            (Evidence(None, None, None, "PASS", "UNKNOWN_STATE"), "OBSERVATION_STATE_UNKNOWN"),
            (Evidence("r1", None, None, "PASS", "OBSERVED"), "IDENTITY_EVIDENCE_MISSING"),
            (Evidence("r1", "sha1", None, "PASS", "OBSERVED"), "ARTIFACT_EVIDENCE_MISSING"),
            (Evidence("r1", "sha1", "old", "PASS", "OBSERVED"), "ARTIFACT_IDENTITY_MISMATCH"),
            (Evidence("r1", "sha1", "sha1", "FAIL", "OBSERVED"), "EXECUTION_FAILED"),
        ]
        for evidence, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(self.engine.reconcile(evidence, "sha1"), expected)

    def test_p6_evidence_requires_explicit_observation_state(self) -> None:
        with self.assertRaises(TypeError):
            Evidence("r1", "sha1", "sha1", "PASS")

    def test_p6_never_promotes_stale_execution(self) -> None:
        evidence = Evidence("r1", "old", "old", "PASS", "OBSERVED")
        self.assertNotEqual(
            self.engine.reconcile(evidence, "sha1"), "VALID_CURRENT_EXECUTION"
        )

    def test_p6_never_collapses_surface_failure_into_no_observation(self) -> None:
        for state in ("SURFACE_UNAVAILABLE", "SURFACE_REJECTED"):
            with self.subTest(state=state):
                evidence = Evidence(None, None, None, "PASS", state)
                self.assertNotEqual(
                    self.engine.reconcile(evidence, "sha1"), "NO_OBSERVATION"
                )


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    if not result.result.wasSuccessful():
        raise SystemExit(1)
