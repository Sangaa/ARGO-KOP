from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_ALLOCATION_PLAN_2026-09-05_C.tsv"
BRIDGE = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_REGISTRATION_BRIDGE_2026-09-05_D.md"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
MANIFEST = ROOT / "Repository" / "REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md"


def _rows():
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "id\tsource\ttarget\ttype\ttarget_path\tevidence_class\tstate"
    return [line.split("\t") for line in lines[1:] if line.strip()]


def test_verified_cross_layer_plan_is_preserved_exactly_in_bridge() -> None:
    rows = _rows()
    assert len(rows) == 39
    assert [r[0] for r in rows] == [f"REL-{i:03d}" for i in range(168, 207)]
    bridge = BRIDGE.read_text(encoding="utf-8")
    for rel_id, source, target, rel_type, target_path, evidence, state in rows:
        assert rel_type == "REFERENCES"
        assert evidence == "DIRECT_RELATED_DOCUMENTS"
        assert state == "P13_CROSS_LAYER_DOCUMENTARY_NON_DEPENDENCY"
        expected = f"| {rel_id} | {source} | {target} | REFERENCES | `{target_path}` |"
        assert bridge.count(expected) == 1


def test_bridge_is_explicitly_noncanonical_and_canonical_fold_remains_open() -> None:
    bridge = BRIDGE.read_text(encoding="utf-8")
    assert "BRIDGE EVIDENCE != CANONICAL REGISTRATION" in bridge
    assert "CANONICAL REP-014 SYNCHRONIZATION = OPEN" in bridge
    assert "PRIORITY 13 = OPEN" in bridge

    registry = REGISTRY.read_text(encoding="utf-8")
    assert "Version: 1.2.21" in registry
    assert "| REL-168 |" not in registry
    assert "| REL-206 |" not in registry

    manifest = MANIFEST.read_text(encoding="utf-8")
    assert "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md | 1.2.21 |" in manifest
    assert "Phase 1 repository work: `OPEN`" in manifest
    assert "Global integrity: `HOLD`" in manifest


def test_bridge_does_not_promote_documentary_edges() -> None:
    bridge = BRIDGE.read_text(encoding="utf-8")
    cohort = bridge.split("## Verified bridge cohort", 1)[1].split("## Canonical synchronization requirement", 1)[0]
    assert cohort.count("| REFERENCES |") == 39
    assert "DEPENDS_ON" not in cohort
    assert "CONSUMES" not in cohort
    assert "GOVERNS" not in cohort
    assert "OWNS" not in cohort
    assert "IMPLEMENTS" not in cohort
