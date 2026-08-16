from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _has_document_id(content: str, doc_id: str) -> bool:
    return f"Document ID: {doc_id}" in content or f"Document ID\n{doc_id}" in content


def test_ring0_control_plane_artifacts_are_present_and_cross_referenced():
    paths = {
        "REP-011": "Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md",
        "REP-012": "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md",
        "REP-013": "Repository/REP-013_REPOSITORY_CONTENT_TREE.md",
        "REP-014": "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md",
        "REP-015": "Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md",
        "REP-016": "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md",
        "REP-020": "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md",
    }
    contents = {doc_id: _read(path) for doc_id, path in paths.items()}

    for doc_id, content in contents.items():
        assert _has_document_id(content, doc_id)

    # REP-011 explicitly defines the synchronized control-plane set.
    ledger = contents["REP-011"]
    for doc_id in ("REP-012", "REP-013", "REP-014", "REP-015", "REP-016", "REP-020"):
        assert doc_id in ledger

    # REP-015 defines Ring 0 load order and must include the active queue surface.
    bootstrap = contents["REP-015"]
    for doc_id in ("REP-011", "REP-012", "REP-013", "REP-014", "REP-016"):
        assert doc_id in bootstrap

    # REP-016 coordinates REP-011 through REP-015 and the provisional REP-020 surface.
    queue = contents["REP-016"]
    assert "RING 0 — CONTROL PLANE" in queue
    assert "REP-011 through REP-015" in queue
    assert "REP-020" in queue

    # P240/P241 must be represented by current repository evidence without
    # being mistaken for repository-wide closure.
    p240 = _read("Repository/REP-020_SESSION_DELTA_2026-08-16_P240.md")
    p241 = _read("Repository/REP-020_SESSION_DELTA_2026-08-16_P241.md")
    reconciliation = _read(
        "Repository/REP-011_RECONCILIATION_ADDENDUM_2026-08-16_P240.md"
    )
    assert "Checkpoint: P240" in p240
    assert "Checkpoint: P241" in p241
    assert "P240" in reconciliation
    assert "PARTIALLY_RECONCILED / INTEGRITY HOLD" in reconciliation
