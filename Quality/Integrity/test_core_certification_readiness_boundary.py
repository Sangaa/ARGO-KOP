from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"
CORE_INDEX = ROOT / "Core" / "Core.md"
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE000A = ROOT / "Core" / "CORE-000A_PLATFORM_GLOSSARY.md"
CORE001 = ROOT / "Core" / "CORE-001_ARGO_MANIFEST.md"
CORE002 = ROOT / "Core" / "CORE-002_ARGO_IDENTITY.md"
CORE004 = ROOT / "Core" / "CORE-004_CORE_PRINCIPLES.md"
CORE005 = ROOT / "Core" / "CORE-005_COGNITIVE_MODEL.md"
CORE006 = ROOT / "Core" / "CORE-006_SYSTEM_PHILOSOPHY.md"
CORE007 = ROOT / "Core" / "CORE-007_DESIGN_PRINCIPLES.md"
CORE008 = ROOT / "Core" / "CORE-008_ARCHITECTURAL_LAWS.md"
CORE010 = ROOT / "Core" / "CORE-010_PLATFORM_ROADMAP.md"
QUEUE_ADDENDUM = ROOT / "Repository" / "REP-016_PRIORITY7_CORE_CLOSURE_ADDENDUM_2026-09-01_X.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_core_certification_readiness_was_consumed_by_separate_explicit_certification():
    status = read(CORE_STATUS)
    index = read(CORE_INDEX)
    queue = read(QUEUE_ADDENDUM)

    assert "Version\n\n1.3.14" in status
    assert "CLOSED_FOR_PHASE_1" in status
    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in status
    assert "Certification Readiness\n\n🟢 PASS — CONSUMED BY TRANSACTION X / EXPLICIT CORE CERTIFICATION REVIEW COMPLETED" in status
    assert "Folder Certification\n\n🟢 CLOSED_FOR_PHASE_1 — EXPLICITLY CERTIFIED WITHIN BOUNDED PRIORITY-7 CORE SCOPE" in status
    assert "CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED" in status
    assert "CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE" in status
    assert "18 top-level files" in status
    assert "17 member files" in status
    assert "CORE-000_PLATFORM_IDENTITY.md" in index
    assert "Canonical: No" in status

    assert "PRIORITY 7 = CLOSED_FOR_PHASE_1" in queue
    assert "GLOBAL PHASE 1 REMAINS OPEN" in queue


def test_run002_core003_remains_validated_but_not_forced_into_registry():
    status = read(CORE_STATUS)
    registry = read(REP014)

    assert "RUN-002 → CORE-003 = REFERENCES" in status
    assert "VALIDATED-NOT-REGISTERED" in status
    assert "INITIALIZATION-AUTHORITY-RESOLUTION-ALIGNED" in status
    assert "NON-DEPENDENCY" in status

    assert "This is **not** a complete graph." in registry
    assert "| RUN-002 | CORE-003 | REFERENCES |" not in registry
    assert "| RUN-002 | CORE-003 | DEPENDS_ON |" not in registry
    assert "| CORE-003 | RUN-002 |" not in registry


def test_remaining_core_members_preserve_non_coupling_boundaries():
    glossary = read(CORE000A)
    manifest = read(CORE001)
    identity = read(CORE002)
    principles = read(CORE004)
    cognitive = read(CORE005)
    philosophy = read(CORE006)
    design = read(CORE007)
    laws = read(CORE008)
    roadmap = read(CORE010)

    assert "A glossary entry shall not be used as evidence that an implementation, architecture, process or capability exists merely because the entry names it." in glossary
    assert "It does not define governance, architecture or implementation authority." in manifest
    assert "It does not define governance, implementation, workflows or architecture." in identity
    assert "These principles guide interpretation and engineering behavior; they are not execution permissions" in principles
    assert "When a principle conflicts with a higher-authority constitutional, governance or architectural rule, the higher authority prevails" in principles
    assert "Execution is governed by applicable Architecture, Governance and Runtime controls." in cognitive
    assert "A valid reasoning result does not itself grant permission to execute an action." in cognitive
    assert "Philosophy guides design and reasoning. It does not grant permission to bypass the Constitution, Governance, Architecture or Runtime validation." in philosophy
    assert "These principles guide design decisions. They do not override Constitution, Governance or Canonical Architecture." in design
    assert "A design principle cannot itself authorize a repository change." in design
    assert "A reference, filename, numeric sequence, folder location or naming convention does not by itself prove an architectural relationship." in laws
    assert "A roadmap dependency is a planning relationship until the underlying technical or governance relationship is verified." in roadmap


def test_certification_scope_remains_bounded_and_reversible_on_new_evidence():
    status = read(CORE_STATUS)
    registry = read(REP014)

    assert "no additional direct material external coupling requiring REP-014 registration was established" in status
    assert "bounded current-evidence conclusion, not a repository-wide complete-graph claim" in status
    assert "repository-wide relationship/consumer graph" in status
    assert "Global Connected Baseline" in status
    assert "Global integrity HOLD" in status
    assert "This is **not** a complete graph." in registry
