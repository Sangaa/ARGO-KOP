from canonical_spine_evidence_scanner import scan


def test_scanner_is_conservative_and_never_claims_connected():
    evidence = scan(".")
    assert len(evidence) == 10
    assert set(evidence.values()).issubset({"PARTIAL", "MISSING"})


def test_empty_repository_has_no_unsupported_positive_claims(tmp_path):
    evidence = scan(tmp_path)
    assert len(evidence) == 10
    assert all(state == "MISSING" for state in evidence.values())
