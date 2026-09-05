from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_INTERNAL_RELATIONSHIP_ALLOCATION_PLAN_2026-09-05_B.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
KNOWLEDGE = ROOT / "Knowledge"


def _plan_rows() -> list[tuple[str, str, str, str]]:
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


def test_p13_internal_plan_is_exact_contiguous_and_noncolliding_before_registration() -> None:
    rows = _plan_rows()
    assert len(rows) == 44
    assert [row[0] for row in rows] == [f"REL-{i:03d}" for i in range(124, 168)]
    assert len({(row[1], row[2], row[3]) for row in rows}) == 44
    assert all(row[3] == "REFERENCES" for row in rows)

    registry = REGISTRY.read_text(encoding="utf-8")
    for rel_id, source, target, rel_type in rows:
        assert f"| {rel_id} |" not in registry
        assert f"| {source} | {target} | {rel_type} |" not in registry


def test_every_planned_edge_is_declared_by_its_current_source() -> None:
    for _, source, target, _ in _plan_rows():
        source_file = next(KNOWLEDGE.glob(f"{source}_*.md"))
        target_file = next(KNOWLEDGE.glob(f"{target}_*.md"))
        source_text = source_file.read_text(encoding="utf-8")
        assert target_file.name in source_text
        assert "Related Documents" in source_text


def test_plan_does_not_promote_reference_to_dependency_or_authority() -> None:
    text = PLAN.read_text(encoding="utf-8")
    assert "DEPENDS_ON" not in text
    assert "GOVERNS" not in text
    assert "OWNS" not in text
    assert "CONSUMES" not in text
