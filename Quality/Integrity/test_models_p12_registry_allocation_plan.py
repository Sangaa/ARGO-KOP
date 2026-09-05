from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY12_REGISTRY_ALLOCATION_PLAN_2026-09-05_M.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def _plan_rows():
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    rows = []
    for line in lines[1:]:
        if not line or line.startswith("stable_correction"):
            break
        rel_id, source, target, rel_type, state_class, evidence = line.split("\t")
        rows.append((rel_id, source, target, rel_type, state_class, evidence))
    return rows


def test_allocation_is_contiguous_unique_and_not_already_registered() -> None:
    rows = _plan_rows()
    assert len(rows) == 43
    expected = [f"REL-{number:03d}" for number in range(81, 124)]
    assert [row[0] for row in rows] == expected
    assert len({row[0] for row in rows}) == 43
    assert len({(row[1], row[2], row[3]) for row in rows}) == 43

    registry = REGISTRY.read_text(encoding="utf-8")
    existing_ids = set(re.findall(r"\| (REL-\d{3}) \|", registry))
    assert existing_ids == {f"REL-{number:03d}" for number in range(1, 81)}
    assert not (set(expected) & existing_ids)


def test_plan_does_not_reintroduce_explicit_no_edge_ripple_targets() -> None:
    rows = _plan_rows()
    triples = {(source, target, rel_type) for _, source, target, rel_type, _, _ in rows}
    for target in ("RUN-004", "RUN-008", "RUN-009", "ENG-007"):
        assert ("MOD-004", target, "DEPENDS_ON") not in triples
        assert ("MOD-004", target, "REFERENCES") not in triples


def test_stable_id_repairs_are_allocated_as_corrections_not_new_ids() -> None:
    text = PLAN.read_text(encoding="utf-8")
    assert "REL-002\tSRV-004\tMOD-001\tDEPENDS_ON\tP12_STABLE_ID_CORRECTION\tC" in text
    assert "REL-012\tMOD-011\tKNW-004\tREFERENCES\tP12_STABLE_ID_TYPE_CORRECTION\tD" in text
    assert "REL-124" not in text
