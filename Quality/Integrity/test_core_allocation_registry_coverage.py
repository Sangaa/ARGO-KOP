from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "Core"
ADDENDUM = ROOT / "Repository" / "REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md"
STATUS = CORE / "_FOLDER_STATUS.md"


def _physical_core_files():
    return sorted(p.name for p in CORE.iterdir() if p.is_file())


def _index_members():
    text = (CORE / "Core.md").read_text(encoding="utf-8")
    start = text.index("# Current Repository Inventory")
    end = text.index("# Inventory Rules")
    section = text[start:end]
    return sorted(
        line.split("`", 2)[1]
        for line in section.splitlines()
        if line.startswith("- `")
    )


def _allocated_paths():
    text = ADDENDUM.read_text(encoding="utf-8")
    paths = []
    for line in text.splitlines():
        if line.startswith("| `Core/") and "| ALLOCATED |" in line:
            paths.append(line.split("`", 2)[1].removeprefix("Core/"))
    return sorted(paths)


def test_core_allocation_addendum_matches_exact_physical_inventory():
    physical = _physical_core_files()
    allocated = _allocated_paths()
    assert len(physical) == 18
    assert allocated == physical


def test_core_index_remains_self_excluding_and_matches_physical_members():
    physical = _physical_core_files()
    members = _index_members()
    assert "Core.md" in physical
    assert "Core.md" not in members
    assert members == sorted(name for name in physical if name != "Core.md")
    assert len(members) == 17


def test_legacy_core000_identity_is_allocated_without_canonical_promotion():
    text = ADDENDUM.read_text(encoding="utf-8")
    legacy_row = next(
        line for line in text.splitlines()
        if "`Core/CORE-000_PLATFORM_IDENTITY.md`" in line
    )
    assert "| ALLOCATED |" in legacy_row
    assert "Canonical: No / Legacy / Superseded" in legacy_row
    assert "not second active CORE-000 authority" in legacy_row


def test_allocation_evidence_does_not_promote_core_certification():
    addendum = ADDENDUM.read_text(encoding="utf-8")
    status = STATUS.read_text(encoding="utf-8")
    assert "Phase 1 Population In Progress" in addendum
    assert "ALLOCATION COMPLETE WITHIN CURRENT CORE PHYSICAL SET ≠ CORE CERTIFIED" in addendum
    assert "CROSS-LAYER VALIDATION OPEN" in status
    assert "CERTIFICATION REVIEW READY" in status
    assert "Folder Certification\n\n⏳ Pending" in status
