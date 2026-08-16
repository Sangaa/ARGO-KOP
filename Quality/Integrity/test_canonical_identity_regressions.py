from pathlib import Path


def test_architecture_map_and_platform_architecture_keep_distinct_identity():
    root = Path(__file__).resolve().parents[2]
    arc_map = (root / "Architecture/ARC_MAP.md").read_text(encoding="utf-8")
    platform_architecture = (root / "Architecture/ARC-001_PLATFORM_ARCHITECTURE.md").read_text(encoding="utf-8")

    header = arc_map.split("# Purpose", 1)[0]
    assert "not `ARC-001`" in arc_map
    assert "Document ID:" not in header
    assert "`ARC-001` is reserved for `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`." in header
    assert "Document ID" in platform_architecture
    assert "ARC-001" in platform_architecture


def test_lifecycle_identity_migration_removes_active_gov_005_collision():
    root = Path(__file__).resolve().parents[2]
    lifecycle = root / "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md"
    governance = root / "Governance/GOV-005_REVIEW_STANDARD.md"
    retired = root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md"

    lifecycle_text = lifecycle.read_text(encoding="utf-8")
    governance_text = governance.read_text(encoding="utf-8")

    assert "Document ID" in lifecycle_text
    assert "LIF-001" in lifecycle_text
    assert "Document ID: GOV-005" in governance_text
    assert not retired.exists()
