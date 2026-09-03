from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCH = ROOT / "Architecture"
REPO = ROOT / "Repository"

EXPECTED = {
    "01-System-Overview.md",
    "ARC-001_PLATFORM_ARCHITECTURE.md",
    "ARC-002_COMPONENT_ARCHITECTURE.md",
    "ARC-003_INFORMATION_FLOW.md",
    "ARC-004_LAYER_MODEL.md",
    "ARC-005_ARCHITECTURE_RULES.md",
    "ARC-006_DEPENDENCY_MODEL.md",
    "ARC-007_INTEGRATION_MODEL.md",
    "ARC-008_REPOSITORY_LAYOUT.md",
    "ARC-009_ARCHITECTURE_DECISIONS.md",
    "ARC-010_EVOLUTION_MODEL.md",
    "ARC-011_CANONICAL_ARCHITECTURE_MODEL.md",
    "ARC_MAP.md",
    "README.md",
    "_FOLDER_STATUS.md",
}


def read(name: str) -> str:
    return (REPO / name).read_text(encoding="utf-8")


def test_exact_architecture_inventory_and_authority_classification():
    actual = {p.name for p in ARCH.iterdir() if p.is_file()}
    assert actual == EXPECTED
    readme = (ARCH / "README.md").read_text(encoding="utf-8")
    legacy = (ARCH / "01-System-Overview.md").read_text(encoding="utf-8")
    assert "Status: Approved / Integrity Hold" in readme
    assert "Canonical: Yes" in readme
    assert "ARC-011` is the current authoritative architectural reference" in readme
    assert "Status: Foundation Build" in legacy


def test_p9_repository_addenda_reconcile_index_map_allocation_inventory():
    idx = read("REP-001_PRIORITY9_ARCHITECTURE_INDEX_ADDENDUM_2026-09-03_S.md")
    m = read("REP-002_PRIORITY9_ARCHITECTURE_MAP_ADDENDUM_2026-09-03_S.md")
    alloc = read("REP-012_PRIORITY9_ARCHITECTURE_ALLOCATION_ADDENDUM_2026-09-03_S.md")
    inv = read("REP-013_PRIORITY9_ARCHITECTURE_INVENTORY_ADDENDUM_2026-09-03_S.md")
    assert "Architecture/README.md" in idx
    assert "01-System-Overview.md" in idx and "excluded from the active index" in idx
    assert "REP-001 P9 ACTIVE INDEX == REP-002 P9 ACTIVE MAP" in m
    assert "ARCHITECTURE PHYSICAL INVENTORY + ALLOCATION = 15 / 15 RECONCILED" in alloc
    assert "REP-013 P9 ARCHITECTURE EXACT PHYSICAL INVENTORY = 15 / 15 RECONCILED" in inv


def test_relationship_hold_is_preserved_as_local_nonblocking_debt():
    disp = read("REP-014_PRIORITY9_ARCHITECTURE_RELATIONSHIP_DISPOSITION_ADDENDUM_2026-09-03_S.md")
    base = (REPO / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text(encoding="utf-8")
    b = read("MUT-2026-09-03-P9-ARC001-ARC011-REGISTRY-B_MUTATION_MATRIX.md")
    assert "| REL-068 | CORE-003 | ARC-011 | GOVERNS |" in base
    assert "| REL-069 | ARC-011 | CORE-003 | REFERENCES |" in base
    assert "HARD HOLD / PRE-MATERIAL ABORT" in b
    assert "REL-073 = LOCAL REGISTRY COMPLETENESS HOLD / NON-BLOCKING FOR BOUNDED ARCHITECTURE PARTITION CLOSURE / DO NOT PROMOTE" in disp
    assert "| REL-073 |" not in base


def test_reconciliation_does_not_overclaim_global_closure():
    decision = read("P9_ARCHITECTURE_REPOSITORY_RECONCILIATION_2026-09-03_S.md")
    review = read("REP-011_PRIORITY9_ARCHITECTURE_REVIEW_ADDENDUM_2026-09-03_S.md")
    assert "This is not Priority-9 closure by itself." in decision
    assert "does not close Priority 9, Phase 1, Global Connected Baseline" in decision
    assert "READY FOR EXPLICIT P9 CLOSURE REVIEW" in review
