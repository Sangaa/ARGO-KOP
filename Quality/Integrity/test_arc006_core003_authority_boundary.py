from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE003 = ROOT / "Core" / "CORE-003_CONSTITUTION.md"
ARC006 = ROOT / "Architecture" / "ARC-006_DEPENDENCY_MODEL.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_arc006_core003_authority_reference_is_direct_bounded_and_not_promoted():
    registry = REP014.read_text(encoding="utf-8")
    core003 = CORE003.read_text(encoding="utf-8")
    arc006 = ARC006.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    row = "| REL-067 | ARC-006 | CORE-003 | REFERENCES | **INTENTIONAL ONE-WAY / CONSTITUTION-AUTHORITY-ALIGNED / NON-DEPENDENCY** |"
    assert registry.count(row) == 1

    assert "Core/CORE-003_CONSTITUTION.md" in arc006
    assert "ARC-006" not in core003

    assert "## Core" in arc006
    assert "Depends on: None at the architectural layer level." in arc006
    assert "## Architecture" in arc006
    assert "May depend on: Core, Governance." in arc006
    assert "A textual reference to a file path does not by itself establish an architectural dependency." in arc006

    forbidden = (
        "| ARC-006 | CORE-003 | DEPENDS_ON |",
        "| CORE-003 | ARC-006 | DEPENDS_ON |",
        "| ARC-006 | CORE-003 | GOVERNS |",
        "| ARC-006 | CORE-003 | IMPLEMENTS |",
        "| ARC-006 | CORE-003 | CONSUMES |",
        "| CORE-003 | ARC-006 | REFERENCES |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in status
    assert "Folder Certification\n\n🟢 CLOSED_FOR_PHASE_1" in status
    assert "ARC-006 → CORE-003" in status
