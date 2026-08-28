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


def test_execution_service_boundary_preserves_isolated_vs_ordinary_runtime_scope():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    matrix = _read(root, "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md")

    assert (
        "| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | "
        "**BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E** |"
    ) in registry
    assert "RUN-E03" in matrix
    assert "PARTIALLY_VERIFIED" in matrix
    assert "ordinary RUN-010 runtime path" in matrix


def test_rel009_directional_state_is_observed_but_non_universal():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    matrix = _read(root, "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md")
    runtime = _read(root, "Runtime/RUN-010_RUNTIME_REFERENCE.md")

    expected_row = (
        "| REL-009 | RUN-010 | SRV-009 | CONSUMES | "
        "**INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL** |"
    )
    assert expected_row in registry
    assert "SERVICE_DISPATCH" in matrix
    assert "isolated governed observation" in matrix
    assert "ordinary connected-spine routing remains unproven" in matrix
    assert (
        "This is a relationship description, not a claim that every runtime operation "
        "follows this exact path."
    ) in runtime


def test_historical_lifecycle_collision_does_not_reappear_as_active_authority():
    root = Path(__file__).resolve().parents[2]
    lifecycle = _read(root, "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md")
    assert "LIF-001" in lifecycle
    assert "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md" in lifecycle
    assert not (root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md").exists()
