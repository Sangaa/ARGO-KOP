from pathlib import Path


def _read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def test_core_runtime_edge_preserves_explicit_two_direction_evidence():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    assert "CORE-003 | RUN-001" in registry
    assert "RUN-001 | CORE-003" in registry
    assert "GOVERNS" in registry
    assert "REFERENCES" in registry


def test_control_plane_edges_preserve_explicit_bidirectional_inventory_scope():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    for edge in (
        "REP-001 | REP-002",
        "REP-002 | REP-001",
    ):
        assert edge in registry
    assert "Verified within control-plane scope" in registry


def test_execution_service_edge_remains_partial_without_runtime_service_proof():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    matrix = _read(root, "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md")
    assert "ENG-006 | SRV-009" in registry
    assert "RUN-E03" in matrix
    assert "PARTIALLY_VERIFIED" in matrix
    assert "executable consumer proof is not established" in registry


def test_historical_lifecycle_collision_does_not_reappear_as_active_authority():
    root = Path(__file__).resolve().parents[2]
    lifecycle = _read(root, "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md")
    assert "LIF-001" in lifecycle
    assert "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md" in lifecycle
    assert not (root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md").exists()
