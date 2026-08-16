from pathlib import Path


def test_control_plane_relationship_targets_are_present():
    root = Path(__file__).resolve().parents[2]
    required = [
        "Repository/REP-001_MASTER_INDEX.md",
        "Repository/REP-002_REPOSITORY_MAP.md",
        "Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md",
        "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md",
        "Repository/REP-013_REPOSITORY_CONTENT_TREE.md",
        "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md",
        "Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md",
    ]
    for path in required:
        assert (root / path).is_file(), path


def test_master_index_declares_control_plane_and_integrity_boundary():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    assert "REP-011" in text and "REP-015" in text
    assert "INTEGRITY HOLD" in text
    assert "Repository Reality > Previous Status Claims > Conversation Memory" in text


def test_relationship_registry_preserves_partial_runtime_consumer_boundary():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text(encoding="utf-8")
    assert "RUN-010" in text and "SRV-009" in text
    assert "executable consumer proof is not established" in text
    assert "no executable `VERIFIED` state is added" in text
