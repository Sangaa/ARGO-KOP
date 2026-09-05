from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
MOD001 = ROOT / "Models" / "MOD-001_KNOWLEDGE_MODEL.md"
SRV004 = ROOT / "Services" / "SRV-004_KNOWLEDGE_SERVICE.md"


def test_rel002_stable_id_has_current_source_direction_and_type() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    current = "| REL-002 | SRV-004 | MOD-001 | DEPENDS_ON |"
    stale = "| REL-002 | MOD-001 | SRV-004 | CONSUMES |"
    assert current in registry
    assert stale not in registry
    assert registry.count("| REL-002 |") == 1


def test_rel002_current_contract_is_directly_supported() -> None:
    srv004 = SRV004.read_text(encoding="utf-8")
    mod001 = MOD001.read_text(encoding="utf-8")
    assert "Models / MOD-001 Knowledge Domain Model" in srv004
    assert "Models/MOD-001_KNOWLEDGE_MODEL.md" in srv004
    assert "SRV-004_KNOWLEDGE_SERVICE.md" in mod001


def test_rel002_correction_does_not_claim_executable_consumption() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    assert "REL-002 = SRV-004 → MOD-001 = DEPENDS_ON" in registry
    assert "no executable consumption" in registry.lower()
    assert "stable relationship id" in registry.lower()
