from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SERVICES = ROOT / "Services"

EXPECTED = {
    "ENG006_SRV009_PRODUCTION_ADAPTER.py",
    "ENG006_SRV009_PRODUCTION_ADAPTER_CONTRACT.md",
    "EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py",
    "GITHUB_ACTIONS_CONNECTOR.py",
    "GITHUB_ACTIONS_CONNECTOR_INTERFACE.py",
    "GITHUB_EVIDENCE_RESOLVER_ADAPTER.py",
    "GITHUB_REPOSITORY_CONNECTOR.py",
    "README.md",
    "REPOSITORY_CONNECTOR_INTERFACE.py",
    "SRV-001_SERVICE_ARCHITECTURE.md",
    "SRV-002_REPOSITORY_SERVICE.md",
    "SRV-003_MEMORY_SERVICE.md",
    "SRV-004_KNOWLEDGE_SERVICE.md",
    "SRV-005_VALIDATION_SERVICE.md",
    "SRV-006_SEARCH_SERVICE.md",
    "SRV-007_LOGGING_SERVICE.md",
    "SRV-008_INDEX_SERVICE.md",
    "SRV-009_UPDATE_SERVICE.md",
    "SRV-010_SERVICE_REFERENCE.md",
    "_FOLDER_STATUS.md",
}


def test_services_exact_current_physical_inventory():
    observed = {p.name for p in SERVICES.iterdir()}
    assert all(p.is_file() for p in SERVICES.iterdir())
    assert observed == EXPECTED
    assert len(observed) == 20


def test_services_status_distinguishes_catalog_from_physical_tree():
    text = (SERVICES / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "Status: 🟡 INTEGRITY HOLD" in text
    assert "SERVICES EXACT PHYSICAL INVENTORY = CLOSED FOR CURRENT TREE / 20 FILES / GIT TREE NONTRUNCATED" in text
    assert "DECLARED SRV CATALOG ≠ COMPLETE CURRENT FOLDER TREE" in text
    for name in EXPECTED:
        assert f"`{name}`" in text or name == "_FOLDER_STATUS.md"
    assert "Services are **not globally certified**" in text
