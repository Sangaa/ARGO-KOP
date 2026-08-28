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


def test_relationship_registry_preserves_bounded_runtime_consumer_boundary():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text(encoding="utf-8")
    assert "RUN-010" in text and "SRV-009" in text
    assert (
        "| REL-009 | RUN-010 | SRV-009 | CONSUMES | "
        "**INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL** |"
    ) in text
    assert "this state does not mean every RUN-010 operation invokes SRV-009" in text
    assert "this state does not convert the normal connected spine to production dispatch" in text
