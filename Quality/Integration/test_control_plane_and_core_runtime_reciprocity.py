from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (_root() / relative).read_text(encoding="utf-8")


def test_core003_run001_reciprocity_is_explicit():
    boot = _read("Runtime/RUN-001_BOOT_SEQUENCE.md")
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "CORE-003_CONSTITUTION.md" in boot
    assert "REL-037 | CORE-003 | RUN-001" in registry
    assert "REL-038 | RUN-001 | CORE-003" in registry


def test_control_plane_pairs_have_explicit_registry_edges():
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    required_pairs = (
        ("REL-022 | REP-001 | REP-002", "REL-023 | REP-002 | REP-001"),
        ("REL-029 | REP-016 | REP-012", None),
        ("REL-033 | REP-015 | REP-016", "REL-034 | REP-016 | REP-015"),
    )
    for forward, reverse in required_pairs:
        assert forward in registry
        if reverse:
            assert reverse in registry
