from pathlib import Path


CANONICAL_SEAMS = [
    ("Memory / Context", "Cognition"),
    ("Cognition", "Reasoning"),
    ("Reasoning", "Decision"),
    ("Decision", "Authorization"),
    ("Authorization", "Execution"),
    ("Execution", "Execution Trace"),
    ("Execution Trace", "Outcome Evaluation"),
    ("Outcome Evaluation", "Feedback Quality"),
    ("Feedback Quality", "Learning Readiness"),
    ("Learning Readiness", "Learning Pipeline"),
]


def test_canonical_spine_is_explicit_and_ordered():
    assert len(CANONICAL_SEAMS) == 10
    assert CANONICAL_SEAMS[0][0] == "Memory / Context"
    assert CANONICAL_SEAMS[-1][1] == "Learning Pipeline"


def test_audit_map_exists():
    target = Path(__file__).with_name("CANONICAL_SPINE_COVERAGE.md")
    assert target.exists()
