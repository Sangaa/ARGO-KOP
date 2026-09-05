from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOD004 = ROOT / "Models" / "MOD-004_MEMORY_MODEL.md"
EVIDENCE = ROOT / "Repository" / "REP-014_PRIORITY12_MOD004_RIPPLE_EVIDENCE_2026-09-05_G.tsv"
TARGETS = {
    "RUN-004": ROOT / "Runtime" / "RUN-004_CONTEXT_LOADING.md",
    "RUN-008": ROOT / "Runtime" / "RUN-008_RUNTIME_STATE.md",
    "RUN-009": ROOT / "Runtime" / "RUN-009_RECOVERY.md",
    "ENG-007": ROOT / "Engine" / "ENG-007_LEARNING_ENGINE.md",
}


def test_mod004_separates_semantic_dependencies_from_ripple_targets():
    text = MOD004.read_text(encoding="utf-8")
    assert "The Memory Model depends semantically on the current model contracts" in text
    assert "downstream" in text.lower()
    for target in TARGETS:
        assert target in text


def test_runtime_engine_targets_are_not_registered_relationship_candidates():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    for target in TARGETS:
        assert f"MOD-004\t{target}\tNONE\tRIPPLE_ONLY" in evidence
        assert f"{target}\tMOD-004\tNONE\tNO_REVERSE_EDGE_PROVEN" in evidence
    assert evidence.count("\tDO_NOT_REGISTER") == 8


def test_current_reverse_sources_do_not_name_mod004():
    for target, path in TARGETS.items():
        text = path.read_text(encoding="utf-8")
        assert "MOD-004" not in text, f"{target} now names MOD-004; Unit-9 evidence requires revalidation"


def test_historical_p65_cannot_override_current_source_contract():
    evidence = EVIDENCE.read_text(encoding="utf-8")
    assert "RIPPLE_ONLY" in evidence
    assert "NO_REVERSE_EDGE_PROVEN" in evidence
    assert "DEPENDS_ON" not in evidence
    assert "CONSUMES" not in evidence
