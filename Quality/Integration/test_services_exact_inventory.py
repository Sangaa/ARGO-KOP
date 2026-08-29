from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SERVICES = ROOT / "Services"

EXPECTED = {
    "Services/ENG006_SRV009_PRODUCTION_ADAPTER.py",
    "Services/ENG006_SRV009_PRODUCTION_ADAPTER_CONTRACT.md",
    "Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py",
    "Services/GITHUB_ACTIONS_CONNECTOR.py",
    "Services/GITHUB_ACTIONS_CONNECTOR_INTERFACE.py",
    "Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py",
    "Services/GITHUB_REPOSITORY_CONNECTOR.py",
    "Services/README.md",
    "Services/REPOSITORY_CONNECTOR_INTERFACE.py",
    "Services/SRV-001_SERVICE_ARCHITECTURE.md",
    "Services/SRV-002_REPOSITORY_SERVICE.md",
    "Services/SRV-003_MEMORY_SERVICE.md",
    "Services/SRV-004_KNOWLEDGE_SERVICE.md",
    "Services/SRV-005_VALIDATION_SERVICE.md",
    "Services/SRV-006_SEARCH_SERVICE.md",
    "Services/SRV-007_LOGGING_SERVICE.md",
    "Services/SRV-008_INDEX_SERVICE.md",
    "Services/SRV-009_UPDATE_SERVICE.md",
    "Services/SRV-010_SERVICE_REFERENCE.md",
    "Services/_FOLDER_STATUS.md",
}


def _tracked_services() -> set[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "Services"], cwd=ROOT, text=True
    )
    return {line.strip() for line in output.splitlines() if line.strip()}


def test_services_exact_current_tracked_inventory():
    observed = _tracked_services()
    assert observed == EXPECTED
    assert len(observed) == 20


def test_services_status_distinguishes_catalog_from_physical_tree():
    text = (SERVICES / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "Status: 🟡 INTEGRITY HOLD" in text
    assert "`SRV-001` through `SRV-010`" in text
    assert "SERVICES EXACT PHYSICAL INVENTORY = CLOSED FOR CURRENT TREE / 20 FILES / GIT TREE NONTRUNCATED" in text
    assert "DECLARED SRV CATALOG ≠ COMPLETE CURRENT FOLDER TREE" in text
    assert "Physical existence of a service artifact does not prove implementation or runtime execution." in text
    assert "Services are **not globally certified**" in text
