import unittest
from Runtime.Prototype.multi_channel_m4_multi_user_harness import Request, schedule


class M4Tests(unittest.TestCase):
    def test_authorization_and_channel_isolation(self):
        result = schedule([
            Request("U1", "T1", "C1", "A", True),
            Request("U2", "T2", "C2", "B", True),
            Request("U3", "T3", "C3", "C", False),
            Request("U2", "T4", "C2", "D", True),
        ])
        self.assertEqual(len(result["accepted"]), 2)
        self.assertEqual(len(result["rejected"]), 2)
        self.assertEqual(result["users_served"], ["U1", "U2"])
        self.assertTrue(result["fairness"])
        self.assertFalse(result["canonical_mutation"])


if __name__ == "__main__":
    unittest.main()
