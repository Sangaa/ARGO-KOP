from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE = ROOT / "Governance"
ALLOCATION = ROOT / "Repository" / "REP-012_PRIORITY8_GOVERNANCE_ALLOCATION_ADDENDUM_2026-09-03_G.md"
REP001 = ROOT / "Repository" / "REP-001_MASTER_INDEX.md"
REP002 = ROOT / "Repository" / "REP-002_REPOSITORY_MAP.md"
REP013 = ROOT / "Repository" / "REP-013_REPOSITORY_CONTENT_TREE.md"


def _physical_paths() -> list[str]:
    return sorted(str(path.relative_to(ROOT)) for path in GOVERNANCE.rglob("*") if path.is_file())


def _allocated_paths() -> list[str]:
    text = ALLOCATION.read_text(encoding="utf-8")
    return sorted(
        line.split("`", 2)[1]
        for line in text.splitlines()
        if line.startswith("| `Governance/") and "| ALLOCATED |" in line
    )


def test_exact_governance_allocation_matches_physical_inventory() -> None:
    physical = _physical_paths()
    allocated = _allocated_paths()
    assert len(physical) == 52
    assert allocated == physical


def test_authority_classification_totals_cover_every_allocated_path() -> None:
    text = ALLOCATION.read_text(encoding="utf-8")
    rows = [line for line in text.splitlines() if line.startswith("| `Governance/")]
    assert len(rows) == 52
    assert sum("ACTIVE_CURRENT" in row for row in rows) == 17
    assert sum("NON_ACTIVE_CANDIDATE" in row for row in rows) == 8
    assert sum("LEGACY_THIN" in row for row in rows) == 3
    assert sum("COMPATIBILITY" in row for row in rows) == 10
    assert sum("SUPPORT" in row or "STATUS" in row for row in rows) == 14


def test_gov014a_is_mapped_active_and_gov013b_remains_nonactive() -> None:
    active = "Governance/GOV-014A_HERMUZ_PREWRITE_MUTATION_MATRIX_GATE.md"
    candidate = "Governance/GOV-013B_HERMUZ_TOOL_SURFACE_DECISION_BOUNDARY.md"
    for path in (REP001, REP002):
        text = path.read_text(encoding="utf-8")
        assert active in text
        assert candidate in text
    tree = REP013.read_text(encoding="utf-8")
    assert active.removeprefix("Governance/") in tree
    assert candidate.removeprefix("Governance/") in tree
    allocation = ALLOCATION.read_text(encoding="utf-8")
    assert f"`{active}` | Governance | ALLOCATED | ACTIVE_CURRENT" in allocation
    assert f"`{candidate}` | Governance | ALLOCATED | NON_ACTIVE_CANDIDATE" in allocation
    assert "GOV-013B MAPPED AS NON_ACTIVE_CANDIDATE != GOV-013B PROMOTED" in allocation


def test_inventory_evidence_keeps_global_and_priority_boundaries() -> None:
    text = (ROOT / "Repository" / "REP-013_PRIORITY8_GOVERNANCE_INVENTORY_ADDENDUM_2026-09-03_G.md").read_text(encoding="utf-8")
    status = (GOVERNANCE / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "REL-011 / KNW-003 boundary" in text
    assert "valid deferred non-blocking item for P8" in text
    assert "does not close Priority 8 by itself" in text
    assert "CONTENT REVIEW HOLDS REMAIN" in status
    assert "P8 CLOSURE REVIEW PENDING" in status
