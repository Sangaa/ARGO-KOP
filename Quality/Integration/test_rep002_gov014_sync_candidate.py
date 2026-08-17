from pathlib import Path

from Tools.controlled_rep002_candidate_builder import SOURCE_BLOB_SHA, build_candidate, git_blob_sha1


def test_rep002_gov014_sync_candidate() -> None:
    repo = Path(__file__).resolve().parents[2]
    source_path = repo / "Repository" / "REP-002_REPOSITORY_MAP.md"
    source = source_path.read_text(encoding="utf-8")

    if git_blob_sha1(source) == SOURCE_BLOB_SHA:
        candidate, report = build_candidate(source)
        assert report["status"] == "PRE_COMMIT_VALIDATED"
        assert report["changed_sections"] == ["4. Repository Layer", "5. Governance Layer"]
        assert report["keep_hash_mismatches"] == []
        assert report["unexpected_changes"] == 0
        assert report["required_changes_present"] == 5
        for path in (
            "Repository/REP-004_REPOSITORY_NAVIGATION.md",
            "Repository/REP-005_REPOSITORY_COMPONENTS.md",
            "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
            "Repository/REP-008_REPOSITORY_BASELINE.md",
            "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md",
        ):
            assert path in candidate
        return

    # Closed transaction state: source snapshot advanced, so validate the applied map.
    for path in (
        "Repository/REP-004_REPOSITORY_NAVIGATION.md",
        "Repository/REP-005_REPOSITORY_COMPONENTS.md",
        "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
        "Repository/REP-008_REPOSITORY_BASELINE.md",
        "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md",
    ):
        assert path in source
