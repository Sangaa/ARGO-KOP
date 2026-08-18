"""Reuse validation for GEN-001 Candidate 001.

Candidate 001 hypothesis:
Before mutating a subject or its execution channel after an unexpected
failure, run the smallest discriminator that separates the two failure
layers.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FailureEvidence:
    subject_failed: bool
    channel_failed: bool
    evidence_available: bool


def classify(evidence: FailureEvidence) -> str:
    if not evidence.evidence_available:
        return "EVIDENCE_GAP"
    if evidence.subject_failed and not evidence.channel_failed:
        return "SUBJECT_UNDER_TEST"
    if evidence.channel_failed and not evidence.subject_failed:
        return "EXECUTION_CHANNEL"
    if evidence.subject_failed and evidence.channel_failed:
        return "AMBIGUOUS_COMPOSITE"
    return "NO_FAILURE"


def main() -> None:
    cases = {
        "M3": FailureEvidence(False, True, True),
        "MULTI_MATRIX": FailureEvidence(False, True, True),
        "REP001_METADATA_DRIFT": FailureEvidence(True, False, True),
    }
    expected = {
        "M3": "EXECUTION_CHANNEL",
        "MULTI_MATRIX": "EXECUTION_CHANNEL",
        "REP001_METADATA_DRIFT": "SUBJECT_UNDER_TEST",
    }
    for name, evidence in cases.items():
        result = classify(evidence)
        assert result == expected[name], (name, result, expected[name])
    print("GEN-001 Candidate 001 reuse validation: PASS")


if __name__ == "__main__":
    main()
