import unittest

from Runtime.Prototype.multi_channel_m3_reconciliation_harness import Proposal, reconcile


class M3ReconciliationTests(unittest.TestCase):
    def test_conflicting_proposals_become_explicit_conflict(self):
        result = reconcile([
            Proposal("TASK-001", "CH-001", "shipment:A", "A"),
            Proposal("TASK-002", "CH-002", "shipment:A", "B"),
        ])
        self.assertEqual(result["status"], "CONFLICT")
        self.assertFalse(result["canonical_mutation"])
        self.assertFalse(result["automatic_merge"])
        self.assertTrue(result["conflicts"])

    def test_non_conflicting_proposals_reconcile_without_mutation(self):
        result = reconcile([
            Proposal("TASK-001", "CH-001", "shipment:A", "A"),
            Proposal("TASK-002", "CH-002", "shipment:A", "A"),
            Proposal("TASK-003", "CH-003", "shipment:B", "B"),
        ])
        self.assertEqual(result["status"], "RECONCILED")
        self.assertFalse(result["canonical_mutation"])
        self.assertFalse(result["automatic_merge"])
        self.assertEqual(len(result["decisions"]), 2)


if __name__ == "__main__":
    unittest.main()
