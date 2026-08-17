from __future__ import annotations

from pathlib import Path

from Tools.controlled_rep001_gov014_candidate_builder import SOURCE_BLOB_SHA, build_candidate, git_blob_sha1


def test_rep001_tx002_candidate() -> None:
    repo = Path(__file__).resolve().parents[2]
    source_path = repo / "Repository" / "REP-001_MASTER_INDEX.md"
    source = source_path.read_text(encoding="utf-8")

    if git_blob_sha1(source) == SOURCE_BLOB_SHA:
        candidate, report = build_candidate(source)
        assert report["status"] == "PRE_COMMIT_VALIDATED"
        assert report["changed_sections"] == ["5. Governance Layer"]
        assert report["keep_hash_mismatches"] == []
        assert report["unexpected_changes"] == 0
        assert report["required_changes_present"] == 1
        assert "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md" in candidate
        return

    # Closed transaction state: the source snapshot has advanced, so validate the applied result.
    assert "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md" in source
    assert not (repo / "Repository" / "CONTROLLED_MUTATION_REQUEST.json").exists()
