from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_architecture_status_closes_only_exact_physical_inventory():
    status = (ROOT / "Architecture/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    required = [
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
    ]
    for item in required:
        assert item in status

    assert "15 tracked files" in status
    assert "ARCHITECTURE_EXACT_PHYSICAL_INVENTORY = CLOSED_FOR_CURRENT_INSPECTED_TREE" in status
    assert "EXACT PHYSICAL INVENTORY != ARCHITECTURE DOMAIN CERTIFICATION" in status
    assert "Layer boundary consistency — PASS FOR CURRENT PRIMARY ARC SET" in status
    assert "Dependency direction consistency — PASS FOR CURRENT PRIMARY ARC SET" in status
    assert "Architecture ↔ Runtime / Interface boundary — PASS FOR INSPECTED RUNTIME / INTERFACE SEMANTIC CONTRACT BOUNDARY" in status
    assert "BOUNDED ARCHITECTURE↔RUNTIME/INTERFACE ALIGNMENT != RUNTIME OR INTERFACE IMPLEMENTATION CERTIFICATION" in status
    assert "Architecture is **not globally certified**" in status
