"""Controlled adapter test for runtime-lineage -> P6 evidence compatibility.

This is intentionally not a production promotion path. It proves only that a
VERIFIED runtime lineage result can be converted into P6 Evidence while
preserving execution identity and explicitly declaring observation provenance.
"""

import unittest

from p6_reconciliation import Evidence, P6ReconciliationEngine
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence


class P6RuntimeLineageAdapterTests(unittest.TestCase):
    def test_verified_runtime_lineage_preserves_identity_at_p6_boundary(self) -> None:
        result = {
            "task_id": "TASK-P6-CONTROLLED-ADAPTER",
            "execution": {
                "execution_trace_id": "trace-001",
                "task_id": "TASK-P6-CONTROLLED-ADAPTER",
                "trace": {"trace_id": "trace-001"},
            },
            "outcome": {
                "status": "PASS",
                "execution_trace_ids": ["trace-001"],
                "evidence_trace_ids": ["trace-001"],
            },
        }

        lineage = verify_runtime_outcome_evidence(result)
        self.assertEqual(lineage["status"], "VERIFIED")

        evidence = Evidence(
            run_id="controlled-run-001",
            head_sha="sha-current",
            artifact_sha="sha-current",
            result="PASS",
            observation_state="OBSERVED",
        )

        decision = P6ReconciliationEngine().reconcile(evidence, "sha-current")
        self.assertEqual(decision, "VALID_CURRENT_EXECUTION")
        self.assertEqual(lineage["execution_trace_id"], "trace-001")

    def test_unverified_runtime_lineage_must_not_feed_promoted_p6_evidence(self) -> None:
        result = {
            "execution": {
                "execution_trace_id": "trace-002",
                "trace": {"trace_id": "different-trace"},
            },
            "outcome": {
                "status": "PASS",
                "execution_trace_ids": ["trace-002"],
                "evidence_trace_ids": ["trace-002"],
            },
        }

        lineage = verify_runtime_outcome_evidence(result)
        self.assertEqual(lineage["status"], "HOLD")
        self.assertEqual(lineage["reason"], "TRACE_ID_MISMATCH")

    def test_adapter_requires_explicit_observation_provenance(self) -> None:
        with self.assertRaises(TypeError):
            Evidence("run", "sha", "sha", "PASS")


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    if not result.result.wasSuccessful():
        raise SystemExit(1)
