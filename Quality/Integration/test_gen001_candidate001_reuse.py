import unittest

from gen001_candidate001_reuse_validation import FailureEvidence, classify


class TestGEN001Candidate001Reuse(unittest.TestCase):
    def test_execution_channel_discrimination(self):
        self.assertEqual(
            classify(FailureEvidence(False, True, True)),
            "EXECUTION_CHANNEL",
        )

    def test_subject_discrimination(self):
        self.assertEqual(
            classify(FailureEvidence(True, False, True)),
            "SUBJECT_UNDER_TEST",
        )

    def test_evidence_gap_is_not_invented(self):
        self.assertEqual(
            classify(FailureEvidence(False, False, False)),
            "EVIDENCE_GAP",
        )

    def test_composite_failure_remains_ambiguous(self):
        self.assertEqual(
            classify(FailureEvidence(True, True, True)),
            "AMBIGUOUS_COMPOSITE",
        )


if __name__ == "__main__":
    unittest.main()
