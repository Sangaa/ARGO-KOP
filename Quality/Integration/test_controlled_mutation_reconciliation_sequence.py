from pathlib import Path


def _read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def test_controlled_mutation_sequence_is_consistent_across_control_plane_contracts():
    root = Path(__file__).resolve().parents[2]
    bootstrap = _read(root, "Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md")
    ledger = _read(root, "Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md")
    allocation = _read(root, "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md")

    required = [
        "READ → IDENTITY → AUTHORITY → DEPENDENCIES → CONSUMERS → MUTATE → COMMIT → RE-READ → REGISTRY SYNC",
        "MUTATE → COMMIT → RE-READ → RECORD EVIDENCE → CONTINUE",
        "ONE MATERIAL CHANGE → COMMIT → RE-READ → RECORD EVIDENCE → NEXT CHANGE",
        "Path → Document ID → Commit SHA → Content/Blob SHA → Review Scope → Result",
        "REP-011",
        "REP-012",
        "REP-013",
        "REP-014",
    ]
    for text in required:
        assert text in bootstrap + "\n" + ledger + "\n" + allocation


def test_controlled_mutation_does_not_imply_semantic_acceptance():
    root = Path(__file__).resolve().parents[2]
    service = _read(root, "Services/SRV-009_UPDATE_SERVICE.md")
    allocation = _read(root, "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md")
    assert "Technical write completion is not equivalent to governed acceptance" in service
    assert "A commit is evidence of repository state, not proof of semantic correctness." in allocation


def test_reconciliation_remains_open_when_required_registry_views_are_missing():
    root = Path(__file__).resolve().parents[2]
    ledger = _read(root, "Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md")
    bootstrap = _read(root, "Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md")
    assert "PARTIALLY_RECONCILED / INTEGRITY HOLD" in ledger
    assert "PARTIALLY RECONCILED / INTEGRITY HOLD" in bootstrap
