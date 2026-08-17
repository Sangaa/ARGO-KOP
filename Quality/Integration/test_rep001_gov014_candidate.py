from __future__ import annotations

from pathlib import Path

from Tools.controlled_rep001_candidate_builder import (
    SOURCE_BLOB_SHA,
    build_candidate,
    git_blob_sha1,
)


def test_rep001_gov014_candidate_pre_commit_validation(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[2]
    source_path = repo / "Repository" / "REP-001_MASTER_INDEX.md"
    source = source_path.read_text(encoding="utf-8")

    candidate, report = build_candidate(source)

    assert report["source_blob_sha"] == SOURCE_BLOB_SHA
    assert report["status"] == "PRE_COMMIT_VALIDATED"
    assert report["unexpected_changes"] == 0
    assert report["keep_hash_mismatches"] == []
    assert report["section_count_source"] == report["section_count_candidate"]
    assert report["required_changes_present"] == 7
    assert "Repository/REP-004_REPOSITORY_NAVIGATION.md" in candidate
    assert "Repository/REP-005_REPOSITORY_COMPONENTS.md" in candidate
    assert "Repository/REP-007_REPOSITORY_GOVERNANCE.md" in candidate
    assert "Repository/REP-008_REPOSITORY_BASELINE.md" in candidate
    assert "Intelligence/INT-001_INTELLIGENCE_LAYER.md" in candidate
    assert "Intelligence/INT-002_PATTERN_EXTRACTION.md" in candidate
    assert "Intelligence/INT-003_ANOMALY_DETECTOR.md" in candidate
    assert git_blob_sha1(source) == SOURCE_BLOB_SHA

    candidate_path = tmp_path / "REP-001.candidate.md"
    candidate_path.write_text(candidate, encoding="utf-8")
    assert candidate_path.read_text(encoding="utf-8") == candidate
