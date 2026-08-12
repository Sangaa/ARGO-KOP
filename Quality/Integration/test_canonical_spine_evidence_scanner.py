from canonical_spine_evidence_scanner import scan


def test_scanner_is_conservative_and_never_claims_connected():
    evidence = scan(".")
    assert len(evidence) == 10
    assert set(evidence.values()).issubset({"PARTIAL", "MISSING"})


def test_empty_repository_has_no_unsupported_positive_claims(tmp_path):
    evidence = scan(tmp_path)
    assert len(evidence) == 10
    assert all(state == "MISSING" for state in evidence.values())


def test_unrelated_files_do_not_create_a_false_seam(tmp_path):
    (tmp_path / "decision.md").write_text("decision", encoding="utf-8")
    (tmp_path / "authorization.md").write_text("authorization", encoding="utf-8")
    evidence = scan(tmp_path)
    assert evidence["Decision -> Authorization"] == "MISSING"


def test_same_file_cooccurrence_is_only_a_partial_candidate(tmp_path):
    (tmp_path / "boundary.md").write_text(
        "decision and authorization boundary", encoding="utf-8"
    )
    evidence = scan(tmp_path)
    assert evidence["Decision -> Authorization"] == "PARTIAL"
    assert "CONNECTED" not in evidence.values()
