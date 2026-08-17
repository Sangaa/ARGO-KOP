from __future__ import annotations

import json
from pathlib import Path

from Tools.controlled_rep001_candidate_builder import SOURCE_BLOB_SHA, build_candidate, git_blob_sha1


def test_rep001_gov014_candidate_pre_commit_validation(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[2]
    source_path = repo / "Repository" / "REP-001_MASTER_INDEX.md"
    request_path = repo / "Repository" / "CONTROLLED_MUTATION_REQUEST.json"
    source = source_path.read_text(encoding="utf-8")

    # Once the transaction is committed, the request is intentionally removed.
    # CI must then validate the closed-state result rather than re-run a stale
    # candidate against a mutated source document.
    if not request_path.exists():
        record = (repo / "Repository" / "MUT-2026-08-17-REP001-001_TRANSACTION_RECORD.md").read_text(encoding="utf-8")
        assert "COMMIT = PASS" in record
        assert "ALL_REQUIRED_VERIFIED = Y" in record
        for expected in (
            "Repository/REP-004_REPOSITORY_NAVIGATION.md",
            "Repository/REP-005_REPOSITORY_COMPONENTS.md",
            "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
            "Repository/REP-008_REPOSITORY_BASELINE.md",
            "Intelligence/INT-001_INTELLIGENCE_LAYER.md",
            "Intelligence/INT-002_PATTERN_EXTRACTION.md",
            "Intelligence/INT-003_ANOMALY_DETECTOR.md",
        ):
            assert expected in source
        return

    request = json.loads(request_path.read_text(encoding="utf-8"))
    assert request["transaction_id"] == "MUT-2026-08-17-REP001-001"
    assert request["source_blob_sha"] == SOURCE_BLOB_SHA

    candidate, report = build_candidate(source)

    assert report["source_blob_sha"] == request["source_blob_sha"]
    assert report["status"] == "PRE_COMMIT_VALIDATED"
    assert report["unexpected_changes"] == 0
    assert report["keep_hash_mismatches"] == []
    assert report["section_count_source"] == report["section_count_candidate"]
    assert report["required_changes_present"] == 7
    assert git_blob_sha1(source) == request["source_blob_sha"]

    for expected in (
        "Repository/REP-004_REPOSITORY_NAVIGATION.md",
        "Repository/REP-005_REPOSITORY_COMPONENTS.md",
        "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
        "Repository/REP-008_REPOSITORY_BASELINE.md",
        "Intelligence/INT-001_INTELLIGENCE_LAYER.md",
        "Intelligence/INT-002_PATTERN_EXTRACTION.md",
        "Intelligence/INT-003_ANOMALY_DETECTOR.md",
    ):
        assert expected in candidate

    candidate_path = tmp_path / "REP-001.candidate.md"
    candidate_path.write_text(candidate, encoding="utf-8")
    assert candidate_path.read_text(encoding="utf-8") == candidate
