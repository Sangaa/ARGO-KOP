from promotion_gate_adapter import build_candidate


def evidence():
    return {
        "task_id": "SYN-001",
        "session_id": "SYN-SESSION-001",
        "evidence": ["synthetic_function_fixture.py", "test_synthetic_function_fixture.py"],
        "observed_result": {"add(2, 3)": 5},
        "pattern": "validated function accepts inputs and returns a predictable result",
        "confidence": 0.9,
        "validation": "VALIDATED",
    }


def test_candidate_mapping_defaults_to_no_promotion_authority():
    candidate = build_candidate(evidence())
    assert candidate["promotion_authority"] is False
    assert candidate["governing_conflict"] is False
    assert candidate["task_id"] == "SYN-001"
    assert candidate["validation"] == "VALIDATED"


def test_candidate_mapping_preserves_explicit_authority():
    candidate = build_candidate(evidence(), authority=True)
    assert candidate["promotion_authority"] is True
    assert candidate["confidence"] == 0.9
    assert candidate["observed_result"] == {"add(2, 3)": 5}


def test_candidate_mapping_preserves_governing_conflict():
    candidate = build_candidate(evidence(), authority=True, governing_conflict=True)
    assert candidate["promotion_authority"] is True
    assert candidate["governing_conflict"] is True
