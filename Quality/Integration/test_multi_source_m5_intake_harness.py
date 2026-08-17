import unittest
from Runtime.Prototype.multi_source_m5_intake_harness import Report, intake


class M5Tests(unittest.TestCase):
    def test_provenance_and_conflict_quarantine(self):
        result = intake([
            Report("A", "R1", "SA", "shipment:1", "eta", "20"),
            Report("B", "R2", "SB", "shipment:1", "eta", "21"),
            Report("C", "R3", "SC", "shipment:2", "status", "READY"),
        ])
        self.assertTrue(result["provenance_preserved"])
        self.assertEqual(len(result["conflicts"]), 1)
        self.assertEqual(len(result["accepted"]), 1)
        self.assertFalse(result["canonical_mutation"])


if __name__ == "__main__":
    unittest.main()
