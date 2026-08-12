from canonical_spine_evidence_scanner import scan


def test_scanner_is_conservative_and_never_claims_connected():
    result = scan(".")
    evidence = result["evidence"]
    assert len(evidence) == 11
    assert set(evidence.values()).issubset({"PARTIAL", "MISSING"})
    assert "candidate_files" in result


def test_empty_repository_has_no_unsupported_positive_claims(tmp_path):
    result = scan(tmp_path)
    evidence = result["evidence"]
    assert len(evidence) == 11
    assert all(state == "MISSING" for state in evidence.values())
    assert all(files == [] for files in result["candidate_files"].values())


def test_unrelated_files_do_not_create_a_false_seam(tmp_path):
    (tmp_path / "decision.md").write_text("decision", encoding="utf-8")
    (tmp_path / "authorization.md").write_text("authorization", encoding="utf-8")
    result = scan(tmp_path)
    assert result["evidence"]["Decision -> Authorization"] == "MISSING"
    assert result["candidate_files"]["Decision -> Authorization"] == []


def test_same_file_cooccurrence_is_only_a_partial_candidate(tmp_path):
    (tmp_path / "boundary.md").write_text(
        "decision and authorization boundary", encoding="utf-8"
    )
    result = scan(tmp_path)
    assert result["evidence"]["Decision -> Authorization"] == "PARTIAL"
    assert result["candidate_files"]["Decision -> Authorization"] == ["boundary.md"]
    assert "CONNECTED" not in result["evidence"].values()


def test_candidate_provenance_is_repository_relative(tmp_path):
    nested = tmp_path / "Decision"
    nested.mkdir()
    (nested / "boundary.md").write_text(
        "decision authorization", encoding="utf-8"
    )
    result = scan(tmp_path)
    assert result["candidate_files"]["Decision -> Authorization"] == [
        "Decision/boundary.md"
    ]


def test_execution_to_outcome_is_part_of_the_canonical_spine(tmp_path):
    (tmp_path / "outcome.md").write_text(
        "execution produces outcome", encoding="utf-8"
    )
    result = scan(tmp_path)
    assert result["evidence"]["Execution -> Outcome"] == "PARTIAL"
    assert result["candidate_files"]["Execution -> Outcome"] == ["outcome.md"]
