from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_interfaces_status_matches_current_inventory_and_identity_boundary():
    status = (ROOT / "Interfaces/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    required = [
        "INTF-001_INTERFACE_SPEC.md",
        "INTF-002_GITHUB.md",
        "INTF-003_DATABASE.md",
        "INTF-004_API.md",
        "INTF-005_LLM.md",
        "INTF-006_ENVIRONMENT_SENSING.md",
        "INTF-006_WEB.md",
        "INTF-007_USER_INTERFACE.md",
        "INTF-008_CONNECTORS.md",
        "INTF-009_IMPORT_EXPORT.md",
        "INTF-010_INTEGRATIONS.md",
        "_FOLDER_STATUS.md",
    ]
    for item in required:
        assert item in status

    assert "12 tracked files" in status
    assert "INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER AND EXTERNAL-TRUST VALIDATION OPEN" in status
    assert "INTF006_FILENAME_DUPLICATION != ACTIVE_AUTHORITY_COLLISION" in status
    assert "INTF-006_WEB = LEGACY NONCANONICAL PROVENANCE / INTERNAL ID INT-006" in status
    assert "INTERFACE CONTRACT != CONNECTOR IMPLEMENTATION" in status
    assert "TECHNICAL ACCESS != AUTHORIZATION" in status
    assert "EXTERNAL DATA != CANONICAL TRUTH" in status
