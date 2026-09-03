from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
README = ROOT / "Runtime/README.md"
CLOSURE = ROOT / "Repository/P10_RUNTIME_EXPLICIT_BOUNDED_CLOSURE_2026-09-03_O.md"
REP011 = ROOT / "Repository/REP-011_PRIORITY10_RUNTIME_CLOSURE_ADDENDUM_2026-09-03_O.md"
REP012 = ROOT / "Repository/REP-012_PRIORITY10_RUNTIME_CLOSURE_ADDENDUM_2026-09-03_O.md"
REP013 = ROOT / "Repository/REP-013_PRIORITY10_RUNTIME_CLOSURE_ADDENDUM_2026-09-03_O.md"
REP016 = ROOT / "Repository/REP-016_PRIORITY10_RUNTIME_CLOSURE_ADDENDUM_2026-09-03_O.md"
DIGEST = "a5db51a6d6cbf7dbf22bdb971fc0d2238d2bdef6627caadc4ee2b1933dad4438"


def texts():
    return [path.read_text(encoding="utf-8") for path in (STATUS, README, CLOSURE, REP011, REP012, REP013, REP016)]


def test_runtime_bounded_closure_is_synchronized_without_global_overclaim():
    surfaces = texts()
    for text in surfaces:
        assert "CLOSED_FOR_PHASE_1" in text
    combined = "\n".join(surfaces)
    assert "BOUNDED RUNTIME PARTITION CERTIFIED" in combined
    assert "Phase 1 = OPEN" in combined
    assert "Global Connected Baseline = OPEN" in combined
    assert "Global Integrity PASS = NOT CLAIMED" in combined
    assert "does not start Priority 11" in combined


def test_closure_binds_exact_inventory_allocation_and_all_four_gates():
    status = STATUS.read_text(encoding="utf-8")
    closure = CLOSURE.read_text(encoding="utf-8")
    rep012 = REP012.read_text(encoding="utf-8")
    rep013 = REP013.read_text(encoding="utf-8")
    assert DIGEST in status and DIGEST in rep013
    assert "118 / 118 RECONCILED" in rep012
    assert "118 / 118 RECONCILED" in rep013
    assert "NONE_BY_ALLOCATION" in closure and "NONE_BY_ALLOCATION" in rep012
    for gate in range(12, 16):
        assert f"{gate}. Runtime ↔" in status


def test_candidate_provider_and_production_authority_remain_unpromoted():
    combined = "\n".join(texts())
    assert "EXECUTABLE PROMOTION HOLD" in combined
    assert "provider authenticity" in combined
    assert "production execution" in combined
    assert "allocation does not grant authority" in combined.lower()
    assert "Priority 10 reopens only if new Runtime-specific evidence" in combined
