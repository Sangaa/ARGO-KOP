from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
RUN011 = ROOT / "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md"
ENG014 = ROOT / "Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md"


def test_rel056_follows_the_current_direct_reference_source():
    registry = REGISTRY.read_text(encoding="utf-8")
    run011 = RUN011.read_text(encoding="utf-8")
    eng014 = ENG014.read_text(encoding="utf-8")

    assert "Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md" not in run011
    assert "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md" in eng014
    assert registry.count(
        "| REL-056 | ENG-014 | RUN-011 | REFERENCES | "
        "**RUNTIME VALIDATION CONTRACT / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY** |"
    ) == 1
    assert "| REL-056 | RUN-011 | ENG-014 | REFERENCES |" not in registry


def test_rel056_is_not_promoted_beyond_documentary_evidence():
    registry = REGISTRY.read_text(encoding="utf-8")
    for stronger_type in ("DEPENDS_ON", "CONSUMES", "IMPLEMENTS", "VALIDATES", "GOVERNS"):
        assert f"| REL-056 | ENG-014 | RUN-011 | {stronger_type} |" not in registry

    assert "This is **not** a complete graph." in registry
