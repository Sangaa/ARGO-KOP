"""P336 regression for exact Core-local inventory reconciliation.

This test validates local physical inventory synchronization only. It does not
by itself certify Core cross-layer relationships or repository-wide integrity.
Transaction X may consume this inventory evidence only as one prerequisite of
an independent explicit certification review.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "Core"
CORE_INDEX = CORE / "Core.md"
CORE_STATUS = CORE / "_FOLDER_STATUS.md"
LEGACY_CORE000 = CORE / "CORE-000_PLATFORM_IDENTITY.md"
CORE012 = "CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md"


def _inventory_members(text: str) -> set[str]:
    match = re.search(
        r"# Current Repository Inventory\s+(.*?)(?=\n# Inventory Rules)",
        text,
        flags=re.DOTALL,
    )
    assert match, "Core.md Current Repository Inventory section not found"
    return set(re.findall(r"^- `([^`]+)`$", match.group(1), flags=re.MULTILINE))


def test_core_local_index_matches_exact_top_level_physical_inventory() -> None:
    physical = {p.name for p in CORE.iterdir() if p.is_file() and p.name != "Core.md"}
    indexed = _inventory_members(CORE_INDEX.read_text(encoding="utf-8"))
    assert indexed == physical
    assert CORE012 in indexed


def test_core_status_records_exact_inventory_after_separate_certification() -> None:
    status = CORE_STATUS.read_text(encoding="utf-8")
    assert "Exact top-level physical inventory reconciled — 18 files" in status
    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in status
    assert CORE012 in status
    assert "Folder Certification\n\n🟢 CLOSED_FOR_PHASE_1" in status
    assert "Core was not marked clean merely because local inventory" in status
    assert "CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED" in status


def test_legacy_core000_remains_noncanonical_provenance() -> None:
    legacy = LEGACY_CORE000.read_text(encoding="utf-8")
    assert "Canonical: No" in legacy
    assert "Legacy / Superseded" in legacy
    assert "Core/CORE-002_ARGO_IDENTITY.md" in legacy
    assert "Core/CORE-000_PLATFORM_ARCHITECTURE.md" in legacy


if __name__ == "__main__":
    test_core_local_index_matches_exact_top_level_physical_inventory()
    test_core_status_records_exact_inventory_after_separate_certification()
    test_legacy_core000_remains_noncanonical_provenance()
    print("P336_CORE_LOCAL_INVENTORY_RECONCILIATION=PASS")
