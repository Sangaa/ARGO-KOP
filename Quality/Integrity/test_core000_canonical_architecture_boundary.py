from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_core000_uses_current_nine_boundary_model():
    core = read_text("Core/CORE-000_PLATFORM_ARCHITECTURE.md")
    labels = [
        "1. Identity / Core",
        "2. Governance",
        "3. Architecture",
        "4. Repository",
        "5. Knowledge / Specifications / Standards",
        "6. Memory",
        "7. Cognition / Engine",
        "8. Runtime / Services / AI",
        "9. Projects / Applied Artifacts",
    ]
    positions = [core.index(label) for label in labels]
    assert positions == sorted(positions)
    assert "Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md" in core


def test_core000_preserves_archive_boundary():
    core = read_text("Core/CORE-000_PLATFORM_ARCHITECTURE.md")
    normalized = " ".join(core.split())
    assert "repository preservation domain and is not an active dependency layer" in normalized
    assert "eight primary architectural components" not in normalized
    assert "Layer 8 Archive" not in normalized


def test_core_status_keeps_priority7_open():
    status = read_text("Core/_FOLDER_STATUS.md")
    assert "CORE-000 Canonical-Architecture Reconciliation" in status
    assert "Priority 7 remains OPEN" in status
    assert "Folder Certification" in status
    assert "Pending" in status
