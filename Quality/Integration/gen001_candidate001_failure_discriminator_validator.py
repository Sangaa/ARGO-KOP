"""Prospective validator for GEN-001 Candidate 001.

Validates the decision heuristic, not any production system.
The discriminator inspects the smallest available evidence boundary first.
"""


def discriminate(*, subject_failed: bool, channel_failed: bool) -> str:
    if channel_failed and not subject_failed:
        return "EXECUTION_CHANNEL"
    if subject_failed and not channel_failed:
        return "SUBJECT_UNDER_TEST"
    if subject_failed and channel_failed:
        return "AMBIGUOUS_COMPOSITE"
    return "NO_FAILURE"


def main() -> None:
    assert discriminate(subject_failed=False, channel_failed=True) == "EXECUTION_CHANNEL"
    assert discriminate(subject_failed=True, channel_failed=False) == "SUBJECT_UNDER_TEST"
    assert discriminate(subject_failed=True, channel_failed=True) == "AMBIGUOUS_COMPOSITE"
    assert discriminate(subject_failed=False, channel_failed=False) == "NO_FAILURE"
    print("GEN-001 Candidate 001 prospective discriminator: PASS")


if __name__ == "__main__":
    main()
