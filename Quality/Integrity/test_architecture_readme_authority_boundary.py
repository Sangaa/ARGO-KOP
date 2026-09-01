from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "Architecture" / "README.md"
ARCH_STATUS = ROOT / "Architecture" / "_FOLDER_STATUS.md"
CORE000 = ROOT / "Core" / "CORE-000_PLATFORM_ARCHITECTURE.md"
CORE003 = ROOT / "Core" / "CORE-003_CONSTITUTION.md"
ARC011 = ROOT / "Architecture" / "ARC-011_CANONICAL_ARCHITECTURE_MODEL.md"
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_architecture_readme_uses_current_authority_boundary():
    readme = README.read_text(encoding="utf-8")
    core000 = CORE000.read_text(encoding="utf-8")
    constitution = CORE003.read_text(encoding="utf-8")
    arc011 = ARC011.read_text(encoding="utf-8")

    assert "Version: 3.2.1" in readme
    assert "Status: Approved / Integrity Hold" in readme
    assert "Constitution / applicable Governance authority" in readme
    assert "Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md" in readme
    assert "current authoritative architectural reference for structural boundaries and dependency direction" in readme
    assert "Core-level platform architecture intent" in readme
    assert "does not establish a competing Architecture model" in readme

    assert "The Constitution defines the highest governing rules of the ARGO Platform." in constitution
    assert "For current structural boundaries and dependency direction, this Core authority is aligned with `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`" in core000
    assert "It is the authoritative architectural reference for structural boundaries and dependency direction" in arc011
    assert "subordinate only to the Constitution and applicable Governance authority" in arc011

    assert "ultimate guiding text" not in readme
    assert "globally locked" not in readme
    assert "Anti-Patch Policy" not in readme


def test_architecture_readme_matches_current_primary_arc_review_set():
    readme = README.read_text(encoding="utf-8")

    primary_section = readme.split("## 2. Current Primary Architecture Review Set", 1)[1]
    primary_section = primary_section.split("### Supporting navigation / control surfaces", 1)[0]

    expected = [
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
    ]
    positions = [primary_section.index(name) for name in expected]
    assert positions == sorted(positions)

    assert "Supporting navigation / control surfaces" in readme
    assert "Architecture/ARC_MAP.md" in readme
    assert "Architecture/_FOLDER_STATUS.md" in readme
    assert "01-System-Overview.md" in readme
    assert "earlier foundation material" in readme
    assert "physical presence does not make its historical four-layer/five-component model current Architecture authority" in readme


def test_core_closure_does_not_promote_architecture_or_registry_relationships():
    readme = README.read_text(encoding="utf-8")
    status = ARCH_STATUS.read_text(encoding="utf-8")
    registry = REP014.read_text(encoding="utf-8")
    core_status = CORE_STATUS.read_text(encoding="utf-8")

    assert "Architecture folder remains under `INTEGRITY HOLD`" in readme
    assert "INTEGRITY HOLD — RE-AUDIT IN PROGRESS / LOCAL INVENTORY VERIFIED" in status
    assert "Canonical Architecture Model alignment — OPEN" in status
    assert "BOUNDED CONSUMER ALIGNMENT PASS IN TRANSACTION S" in status
    assert "BOUNDED CONSUMER ALIGNMENT != ARCHITECTURE CERTIFICATION" in status

    forbidden_registry_markers = (
        "| ARCHITECTURE_README | CORE-000 |",
        "| ARCHITECTURE_README | CORE-003 |",
        "| ARCHITECTURE_README | ARC-011 |",
        "| CORE-000 | ARCHITECTURE_README |",
        "| CORE-003 | ARCHITECTURE_README |",
        "| ARC-011 | ARCHITECTURE_README |",
    )
    for marker in forbidden_registry_markers:
        assert marker not in registry

    assert "CORE = CLOSED_FOR_PHASE_1 / BOUNDED CORE PARTITION CERTIFIED" in core_status
    assert "Folder Certification" in core_status
    assert "🟢 CLOSED_FOR_PHASE_1" in core_status
    assert "external-domain certifications including Governance, Architecture, Runtime and Lifecycle" in core_status
