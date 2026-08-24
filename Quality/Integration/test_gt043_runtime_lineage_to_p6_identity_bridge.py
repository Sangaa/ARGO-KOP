"""GT-043 controlled adapter boundary: runtime lineage identity must remain explicit at P6 ingress."""
import unittest

from p6_reconciliation import Evidence, P6ReconciliationEngine
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence


def build_controlled_p6_payload(runtime_result: dict, run_id: str, head_sha: str, artifact_sha: str) -> dict:
    lineage = verify_runtime_outcome_evidence(runtime_result)
    if lineage.get("status") != "VERIFIED":
        raise ValueError("RUNTIME_LINEAGE_NOT_VERIFIED")
    return {
        "lineage": lineage,
        "evidence": Evidence(
            run_id=run_id,
            head_sha=head_sha,
            artifact_sha=artifact_sha,
            result=runtime_result["outcome"]["status"],
            observation_state="OBSERVED",
        ),
    }


class GT043RuntimeLineageToP6IdentityBridgeTests(unittest.TestCase):
    def test_verified_lineage_and_p6_evidence_are_explicitly_bound(self) -> None:
        runtime = {
            "execution": {
                "execution_trace_id": "trace-043",
                "trace": {"trace_id": "trace-043"},
            },
            "outcome": {
                "status": "PASS",
                "execution_trace_ids": ["trace-043"],
                "evidence_trace_ids": ["trace-043"],
            },
        }
        payload = build_controlled_p6_payload(runtime, "run-043", "sha-043", "sha-043")
        self.assertEqual(payload["lineage"]["status"], "VERIFIED")
        self.assertEqual(payload["lineage"]["execution_trace_id"], "trace-043")
        self.assertEqual(payload["evidence"].run_id, "run-043")
        self.assertEqual(P6ReconciliationEngine().reconcile(payload["evidence"], "sha-043"), "VALID_CURRENT_EXECUTION")

    def test_unverified_lineage_cannot_cross_controlled_adapter_boundary(self) -> None:
        runtime = {
            "execution": {
                "execution_trace_id": "trace-043-bad",
                "trace": {"trace_id": "different-trace"},
            },
            "outcome": {
                "status": "PASS",
                "execution_trace_ids": ["trace-043-bad"],
                "evidence_trace_ids": ["trace-043-bad"],
            },
        }
        with self.assertRaises(ValueError) as error:
            build_controlled_p6_payload(runtime, "run-043-bad", "sha-043", "sha-043")
        self.assertEqual(str(error.exception), "RUNTIME_LINEAGE_NOT_VERIFIED")

    def test_observation_provenance_remains_explicit_at_p6_boundary(self) -> None:
        runtime = {
            "execution": {
                "execution_trace_id": "trace-043-observed",
                "trace": {"trace_id": "trace-043-observed"},
            },
            "outcome": {
                "status": "PASS",
                "execution_trace_ids": ["trace-043-observed"],
                "evidence_trace_ids": ["trace-043-observed"],
            },
        }
        payload = build_controlled_p6_payload(runtime, "run-043-observed", "sha-043", "sha-043")
        self.assertEqual(payload["evidence"].observation_state, "OBSERVED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
