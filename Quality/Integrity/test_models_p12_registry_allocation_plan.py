from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY12_REGISTRY_ALLOCATION_PLAN_2026-09-05_M.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
MANIFEST = ROOT / "Repository" / "REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md"


def _plan_rows():
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    rows = []
    for line in lines[1:]:
        if not line or line.startswith("stable_correction"):
            break
        rel_id, source, target, rel_type, state_class, evidence = line.split("\t")
        rows.append((rel_id, source, target, rel_type, state_class, evidence))
    return rows


def _registry_rows():
    text = REGISTRY.read_text(encoding="utf-8")
    rows = {}
    for rel_id, source, target, rel_type in re.findall(
        r"^\| (REL-\d{3}) \| ([^|]+?) \| ([^|]+?) \| ([A-Z_]+) \|",
        text,
        flags=re.MULTILINE,
    ):
        rows[rel_id] = (source.strip(), target.strip(), rel_type)
    return rows


def test_registered_ids_are_contiguous_through_p12_cohort() -> None:
    rows = _registry_rows()
    expected = {f"REL-{number:03d}" for number in range(1, 124)}
    assert set(rows) == expected
    assert len(rows) == 123


def test_unit15_allocation_plan_is_bound_exactly_to_registry() -> None:
    registry = _registry_rows()
    plan = _plan_rows()
    assert len(plan) == 43
    for rel_id, source, target, rel_type, _, _ in plan:
        assert registry[rel_id] == (source, target, rel_type)


def test_stable_id_repairs_are_exact_and_stale_forms_are_absent() -> None:
    text = REGISTRY.read_text(encoding="utf-8")
    rows = _registry_rows()
    assert rows["REL-002"] == ("SRV-004", "MOD-001", "DEPENDS_ON")
    assert rows["REL-012"] == ("MOD-011", "KNW-004", "REFERENCES")
    assert "| REL-002 | MOD-001 | SRV-004 | CONSUMES |" not in text
    assert "| REL-012 | MOD-011 | KNW-004 | DEPENDS_ON |" not in text


def test_no_edge_ripple_dispositions_remain_absent_from_registry() -> None:
    rows = _registry_rows().values()
    forbidden_targets = {"RUN-004", "RUN-008", "RUN-009", "ENG-007"}
    for source, target, _ in rows:
        assert not (source == "MOD-004" and target in forbidden_targets)


def test_registry_and_current_manifest_are_same_change_set_bound() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")
    assert "Version: 1.2.20" in registry
    assert "Last Audit: 2026-09-05" in registry
    assert "| REP-014 | Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md | 1.2.20 | Active / Relationship Enumeration In Progress | CURRENT RELATIONSHIP EVIDENCE / BROADER GRAPH OPEN |" in manifest
    assert "P12-B-MODELS-RELATIONSHIP-CONTENT / CANONICAL REP-014 SYNCHRONIZATION" in manifest


def test_historical_registry_sections_are_preserved() -> None:
    text = REGISTRY.read_text(encoding="utf-8")
    for marker in (
        "## P346 Current Control-Plane Evidence Binding — 2026-08-17",
        "## P10 REL-056 Runtime Validation Direction Reconciliation — 2026-09-03",
        "## P11 INTF-010 Integration Relationship Registration — 2026-09-03",
        "## P12 Models Relationship/Content Canonical Registry Reconciliation — 2026-09-05",
        "End of REP-014",
    ):
        assert marker in text
