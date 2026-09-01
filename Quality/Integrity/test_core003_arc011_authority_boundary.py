from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE003 = ROOT / "Core" / "CORE-003_CONSTITUTION.md"
ARC011 = ROOT / "Architecture" / "ARC-011_CANONICAL_ARCHITECTURE_MODEL.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_core003_arc011_authority_boundary_is_direct_and_not_overpromoted():
    registry = REP014.read_text(encoding="utf-8")
    constitution = CORE003.read_text(encoding="utf-8")
    architecture = ARC011.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    assert "The Constitution defines the highest governing rules of the ARGO Platform." in constitution
    assert "All repository components shall comply with this Constitution within the scope applicable to them." in constitution
    assert "This document defines the current canonical Architecture Model of ARGO KOP." in architecture
    assert "subordinate only to the Constitution and applicable Governance authority" in architecture
    assert "Constitution / applicable Governance authority" in architecture
    assert "Canonical Architecture Model" in architecture

    # Validation-first: source evidence supports the authority/reference candidate,
    # but REP-014 is intentionally not mutated in Transaction L.
    assert "| CORE-003 | ARC-011 | GOVERNS |" not in registry
    assert "| ARC-011 | CORE-003 | REFERENCES |" not in registry

    forbidden = (
        "| ARC-011 | CORE-003 | DEPENDS_ON |",
        "| ARC-011 | CORE-003 | GOVERNS |",
        "| ARC-011 | CORE-003 | IMPLEMENTS |",
        "| ARC-011 | CORE-003 | CONSUMES |",
        "| CORE-003 | ARC-011 | DEPENDS_ON |",
        "| CORE-003 | ARC-011 | IMPLEMENTS |",
        "| CORE-003 | ARC-011 | CONSUMES |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "CROSS-LAYER VALIDATION OPEN" in status
    assert "Folder Certification\n\n⏳ Pending" in status
