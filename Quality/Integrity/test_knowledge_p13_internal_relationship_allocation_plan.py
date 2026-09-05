from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_INTERNAL_RELATIONSHIP_ALLOCATION_PLAN_2026-09-05_B.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
MANIFEST = ROOT / "Repository" / "REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md"


def _rows() -> list[tuple[str, str, str, str]]:
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "id\tsource\ttarget\ttype\tevidence_class\tstate"
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        rel_id, source, target, rel_type, evidence, state = line.split("\t")
        assert evidence == "DIRECT_RELATED_DOCUMENTS"
        assert state == "P13_INTERNAL_KNOWLEDGE_DOCUMENTARY_NON_DEPENDENCY"
        rows.append((rel_id, source, target, rel_type))
    return rows


def test_p13_internal_relationship_cohort_is_registered_exactly_once() -> None:
    rows = _rows()
    registry = REGISTRY.read_text(encoding="utf-8")
    assert "Version: 1.2.21" in registry
    assert len(rows) == 44
    assert [r[0] for r in rows] == [f"REL-{i:03d}" for i in range(124, 168)]
    for rel_id, source, target, rel_type in rows:
        exact = (
            f"| {rel_id} | {source} | {target} | {rel_type} | "
            "**P13 DIRECT-SOURCE-REVALIDATED / INTERNAL DOCUMENTARY / NON-DEPENDENCY** |"
        )
        assert registry.count(exact) == 1


def test_p13_internal_registration_does_not_create_stronger_semantics() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    cohort = registry.split("| REL-124 |", 1)[1].split("## Current Review-Cycle Reconciliation", 1)[0]
    assert "DEPENDS_ON" not in cohort
    assert "CONSUMES" not in cohort
    assert "GOVERNS" not in cohort
    assert "OWNS" not in cohort
    assert cohort.count("| REFERENCES |") == 44


def test_control_plane_manifest_is_rebound_to_rep014_1_2_21() -> None:
    manifest = MANIFEST.read_text(encoding="utf-8")
    expected = (
        "| REP-014 | Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md | 1.2.21 | "
        "Active / Relationship Enumeration In Progress | CURRENT RELATIONSHIP EVIDENCE / BROADER GRAPH OPEN |"
    )
    assert expected in manifest
    assert "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md | 1.2.20 |" not in manifest
