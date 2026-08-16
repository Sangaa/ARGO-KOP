from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SERVICES = {
    f"SRV-{index:03d}": ROOT / "Services" / name
    for index, name in {
        1: "SRV-001_SERVICE_ARCHITECTURE.md",
        2: "SRV-002_REPOSITORY_SERVICE.md",
        3: "SRV-003_MEMORY_SERVICE.md",
        4: "SRV-004_KNOWLEDGE_SERVICE.md",
        5: "SRV-005_VALIDATION_SERVICE.md",
        6: "SRV-006_SEARCH_SERVICE.md",
        7: "SRV-007_LOGGING_SERVICE.md",
        8: "SRV-008_INDEX_SERVICE.md",
        9: "SRV-009_UPDATE_SERVICE.md",
        10: "SRV-010_SERVICE_REFERENCE.md",
    }.items()
}
FOLDER_STATUS = ROOT / "Services/_FOLDER_STATUS.md"
SERVICE_REFERENCE = ROOT / "Services/SRV-010_SERVICE_REFERENCE.md"


def test_active_service_artifacts_match_filename_identity():
    for service_id, path in SERVICES.items():
        assert path.is_file(), f"missing active service artifact: {path}"
        text = path.read_text(encoding="utf-8")
        assert re.search(rf"(?m)^#\s+{re.escape(service_id)}\s*$", text)
        assert re.search(rf"(?m)^Document ID\s*:?\s*$\n\s*{re.escape(service_id)}\s*$", text) or re.search(
            rf"(?m)^Document ID\s*:\s*{re.escape(service_id)}\s*$", text
        )
        assert re.search(r"(?m)^Canonical\s*$\n\s*Yes\s*$", text) or re.search(
            r"(?m)^Canonical\s*:\s*Yes\s*$", text
        )


def test_service_inventory_declares_the_same_active_service_set():
    folder_status = FOLDER_STATUS.read_text(encoding="utf-8")
    reference = SERVICE_REFERENCE.read_text(encoding="utf-8")
    assert "`SRV-001` through `SRV-010`" in folder_status
    for service_id in SERVICES:
        assert service_id in reference


def test_services_identity_guard_does_not_certify_implementation():
    folder_status = FOLDER_STATUS.read_text(encoding="utf-8")
    assert "INTEGRITY HOLD" in folder_status
    assert "Canonical: Pending consolidated validation" in folder_status
    assert "Physical existence of a service artifact does not prove implementation or runtime execution." in folder_status
