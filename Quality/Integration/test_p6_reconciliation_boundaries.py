"""P6-08/P6-09 boundary regression tests.

The decision logic lives in p6_reconciliation.py. This module owns only
scenario coverage and an explicit stdlib test-runner entry point.
"""

import unittest

from p6_reconciliation import Evidence, P6ReconciliationEngine


class P6ReconciliationBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = P6ReconciliationEngine()

    def test_p6_08_current_execution_is_evidence_bearing(self) -> None:
        evidence = Evidence("r1", "sha1", "sha1", "PASS")
        self.assertEqual(
            self.engine.reconcile(evidence, "sha1"), "VALID_CURRENT_EXECUTION"
        )

    def test_p6_08_stale_execution_is_not_current(self) -> None:
        evidence = Evidence("r1", "old", "old", "PASS")
        self.assertEqual(
            self.engine.reconcile(evidence, "sha1"),
            "VALID_EXECUTION_STALE_BASELINE",
        )

    def test_p6_09_first_failure_boundary_is_preserved(self) -> None:
        cases = [
            (Evidence(None, None, None, "PASS"), "NO_OBSERVATION"),
            (Evidence("r1", None, None, "PASS"), "IDENTITY_EVIDENCE_MISSING"),
            (Evidence("r1", "sha1", None, "PASS"), "ARTIFACT_EVIDENCE_MISSING"),
            (Evidence("r1", "sha1", "old", "PASS"), "ARTIFACT_IDENTITY_MISMATCH"),
            (Evidence("r1", "sha1", "sha1", "FAIL"), "EXECUTION_FAILED"),
        ]
        for evidence, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(self.engine.reconcile(evidence, "sha1"), expected)

    def test_p6_never_promotes_stale_execution(self) -> None:
        evidence = Evidence("r1", "old", "old", "PASS")
        self.assertNotEqual(
            self.engine.reconcile(evidence, "sha1"), "VALID_CURRENT_EXECUTION"
        )


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    if not result.result.wasSuccessful():
        raise SystemExit(1)
