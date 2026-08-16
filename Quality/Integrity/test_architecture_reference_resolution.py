from pathlib import Path


ARCHITECTURE_REFS = [
    "Architecture/ARC_MAP.md",
    "Architecture/ARC-001_PLATFORM_ARCHITECTURE.md",
    "Architecture/ARC-002_COMPONENT_ARCHITECTURE.md",
    "Architecture/ARC-003_INFORMATION_FLOW.md",
    "Architecture/ARC-004_LAYER_MODEL.md",
    "Architecture/ARC-005_ARCHITECTURE_RULES.md",
    "Architecture/ARC-006_DEPENDENCY_MODEL.md",
    "Architecture/ARC-007_INTEGRATION_MODEL.md",
    "Architecture/ARC-008_REPOSITORY_LAYOUT.md",
    "Architecture/ARC-009_ARCHITECTURE_DECISIONS.md",
    "Architecture/ARC-010_EVOLUTION_MODEL.md",
    "Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md",
]


def test_promoted_architecture_review_set_is_materialized():
    root = Path(__file__).resolve().parents[2]
    for relative in ARCHITECTURE_REFS:
        assert (root / relative).is_file(), relative


def test_architecture_map_and_status_retain_integrity_hold_boundary():
    root = Path(__file__).resolve().parents[2]
    map_text = (root / "Architecture/ARC_MAP.md").read_text(encoding="utf-8")
    status_text = (root / "Architecture/_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "This file is a **map artifact**, not `ARC-001`." in map_text
    assert "INTEGRITY HOLD" in status_text
    assert "Architecture is **not globally certified**." in status_text
