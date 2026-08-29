from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_core_canonical_inventory_is_discoverable_across_control_surfaces():
    rep001 = (ROOT / "Repository" / "REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    rep002 = (ROOT / "Repository" / "REP-002_REPOSITORY_MAP.md").read_text(encoding="utf-8")
    status = (ROOT / "Core" / "_FOLDER_STATUS.md").read_text(encoding="utf-8")

    paths = (
        "Core/CORE-000A_PLATFORM_GLOSSARY.md",
        "Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md",
        "Core/ARGO_KERNEL.md",
    )

    for path in paths:
        assert path in rep001, f"REP-001 missing canonical Core discoverability: {path}"
        assert path in rep002, f"REP-002 missing canonical Core mapping: {path}"

    assert "CORE-000A_PLATFORM_GLOSSARY.md" in status
    assert "CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md" in status
    assert "ARGO_KERNEL.md" in status

    # Inventory synchronization is deliberately bounded; it must not erase the hold.
    assert "INTEGRITY HOLD" in status
    assert "Cross-Layer Review" in status
    assert "In Progress" in status
