from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCH = ROOT / "Architecture"
REPO = ROOT / "Repository"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_architecture_status_and_readme_are_synchronized_to_bounded_closure():
    status = read(ARCH / "_FOLDER_STATUS.md")
    readme = read(ARCH / "README.md")

    assert "🟢 CLOSED_FOR_PHASE_1 / BOUNDED ARCHITECTURE PARTITION CERTIFIED / GLOBAL HOLDS REMAIN" in status
    assert "Version\n\n1.6.0" in status
    assert "The Architecture folder is `CLOSED_FOR_PHASE_1 / BOUNDED ARCHITECTURE PARTITION CERTIFIED / GLOBAL HOLDS REMAIN`." in readme
    assert "Status: Approved / Revalidated / CLOSED_FOR_PHASE_1" in readme

    validation = status.split("# Current Validation Gate", 1)[1].split("\n---", 1)[0]
    for gate in range(1, 14):
        assert f"{gate}. " in validation
        line = next(line for line in validation.splitlines() if line.startswith(f"{gate}. "))
        assert "PASS" in line

    assert "Architecture is **not globally certified**" in status
    assert "BOUNDED ARCHITECTURE PARTITION CLOSURE != GLOBAL ARCHITECTURE CERTIFICATION" in status
    assert "Phase-1 closure" in readme
    assert "Connected Baseline closure" in readme
    assert "Global PASS" in readme


def test_architecture_closure_addenda_bind_inventory_review_and_queue_without_global_overclaim():
    decision = read(REPO / "P9_ARCHITECTURE_EXPLICIT_BOUNDED_CLOSURE_2026-09-03_T.md")
    rep011 = read(REPO / "REP-011_PRIORITY9_ARCHITECTURE_CLOSURE_ADDENDUM_2026-09-03_T.md")
    rep013 = read(REPO / "REP-013_PRIORITY9_ARCHITECTURE_CLOSURE_ADDENDUM_2026-09-03_T.md")
    rep016 = read(REPO / "REP-016_PRIORITY9_ARCHITECTURE_CLOSURE_ADDENDUM_2026-09-03_T.md")

    assert "PRIORITY 9 / ARCHITECTURE = CLOSED_FOR_PHASE_1" in decision
    assert "REP-011 PRIORITY 9 ARCHITECTURE REVIEW = CLOSED_FOR_PHASE_1 / BOUNDED COMPLETE" in rep011
    assert "ARCHITECTURE EXACT PHYSICAL INVENTORY = 15 / 15 RECONCILED" in rep013
    assert "ARCHITECTURE EXACT ALLOCATION = 15 / 15 RECONCILED" in rep013
    assert "Priority 9 — Architecture = CLOSED_FOR_PHASE_1 / RESUME-SAFE" in rep016
    assert "Phase 1 = OPEN" in rep016
    assert "Global Connected Baseline = OPEN" in rep016
    assert "Global Integrity PASS = NOT CLAIMED" in rep016
    assert "does not itself open or start Priority 10" in rep016


def test_local_rel073_hold_remains_unpromoted_and_nonblocking():
    decision = read(REPO / "P9_ARCHITECTURE_EXPLICIT_BOUNDED_CLOSURE_2026-09-03_T.md")
    disposition = read(REPO / "REP-014_PRIORITY9_ARCHITECTURE_RELATIONSHIP_DISPOSITION_ADDENDUM_2026-09-03_S.md")
    registry = read(REPO / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    b_matrix = read(REPO / "MUT-2026-09-03-P9-ARC001-ARC011-REGISTRY-B_MUTATION_MATRIX.md")

    assert "REL-073" in decision and "local" in decision.lower()
    assert "REL-073 = LOCAL REGISTRY COMPLETENESS HOLD / NON-BLOCKING FOR BOUNDED ARCHITECTURE PARTITION CLOSURE / DO NOT PROMOTE" in disposition
    assert "HARD HOLD / PRE-MATERIAL ABORT" in b_matrix
    assert "| ARC-001 | ARC-011 | REFERENCES |" not in registry
