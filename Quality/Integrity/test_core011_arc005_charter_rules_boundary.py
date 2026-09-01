from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE011 = ROOT / "Core" / "CORE-011_PLATFORM_CHARTER.md"
ARC005 = ROOT / "Architecture" / "ARC-005_ARCHITECTURE_RULES.md"
ARC006 = ROOT / "Architecture" / "ARC-006_DEPENDENCY_MODEL.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_arc005_core011_reference_is_bounded_and_one_way():
    registry = REP014.read_text(encoding="utf-8")
    core011 = CORE011.read_text(encoding="utf-8")
    arc005 = ARC005.read_text(encoding="utf-8")
    arc006 = ARC006.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    row = "| REL-066 | ARC-005 | CORE-011 | REFERENCES | **INTENTIONAL ONE-WAY / CHARTER-BOUNDARY-ALIGNED / NON-DEPENDENCY** |"
    assert registry.count(row) == 1

    assert "Core/CORE-011_PLATFORM_CHARTER.md" in arc005
    assert "ARC-005" not in core011

    assert "Core" in arc006 and "None" in arc006
    assert "Architecture" in arc006 and "Core" in arc006 and "Governance" in arc006

    forbidden = (
        "| CORE-011 | ARC-005 | REFERENCES |",
        "| ARC-005 | CORE-011 | DEPENDS_ON |",
        "| CORE-011 | ARC-005 | DEPENDS_ON |",
        "| ARC-005 | CORE-011 | GOVERNS |",
        "| ARC-005 | CORE-011 | IMPLEMENTS |",
        "| ARC-005 | CORE-011 | CONSUMES |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in status
    assert "Folder Certification\n\n🟢 CLOSED_FOR_PHASE_1" in status
    assert "Phase 1 remains OPEN" in registry or "broader Core cross-layer validation and certification remain open" in registry
