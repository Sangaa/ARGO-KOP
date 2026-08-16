from pathlib import Path


def test_core_index_inventory_files_exist_without_promoting_folder_status():
    root = Path(__file__).resolve().parents[2]
    index = (root / "Core/Core.md").read_text(encoding="utf-8")
    status = (root / "Core/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    expected = [
        "ARGO_KERNEL.md",
        "CORE-000_PLATFORM_ARCHITECTURE.md",
        "CORE-000A_PLATFORM_GLOSSARY.md",
        "CORE-001_ARGO_MANIFEST.md",
        "CORE-002_ARGO_IDENTITY.md",
        "CORE-003_CONSTITUTION.md",
        "CORE-004_CORE_PRINCIPLES.md",
        "CORE-005_COGNITIVE_MODEL.md",
        "CORE-006_SYSTEM_PHILOSOPHY.md",
        "CORE-007_DESIGN_PRINCIPLES.md",
        "CORE-008_ARCHITECTURAL_LAWS.md",
        "CORE-009_PLATFORM_LIFECYCLE.md",
        "CORE-010_PLATFORM_ROADMAP.md",
        "CORE-011_PLATFORM_CHARTER.md",
    ]

    for name in expected:
        assert name in index, name
        assert (root / "Core" / name).is_file(), name

    assert "INTEGRITY HOLD" in status
    assert "Folder Certification" in status
    assert "Pending" in status
