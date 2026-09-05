from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Interfaces/_FOLDER_STATUS.md"
CLOSURE = ROOT / "Repository/P11_INTERFACES_EXPLICIT_BOUNDED_CLOSURE_2026-09-05_S.md"
REP011 = ROOT / "Repository/REP-011_PRIORITY11_INTERFACES_CLOSURE_ADDENDUM_2026-09-05_S.md"
MATRIX = ROOT / "Repository/MUT-2026-09-05-P11-INTERFACES-BOUNDED-CLOSURE-S_MUTATION_MATRIX.md"
DIGEST = "81e052fe0ae6cf61f6a70b15acafa4cd07e5372ef168a1228790db314c8eaae9"


def texts():
    return [path.read_text(encoding="utf-8") for path in (STATUS, CLOSURE, REP011, MATRIX)]


def test_p11_bounded_closure_is_synchronized_without_global_or_provider_overclaim():
    surfaces = texts()
    for text in surfaces:
        assert "BOUNDED INTERFACES PARTITION" in text
    combined = "\n".join(surfaces)
    assert "provider authenticity" in combined.lower()
    assert "Global Connected Baseline" in combined
    assert "Global Integrity" in combined
    assert "does not start Priority 12" in combined


def test_closure_binds_exact_inventory_and_non_authoritative_allocation():
    combined = "\n".join(texts())
    assert DIGEST in combined
    assert "12" in STATUS.read_text(encoding="utf-8")
    assert "NONE_BY_ALLOCATION" in combined
    assert "03b65d4ccbb0527da2f3fcbd8f0f050b23d0c774" in combined


def test_deferred_work_does_not_become_p11_reopen_by_itself():
    combined = "\n".join(texts()).lower()
    assert "reopen conditions" in combined
    assert "optional hardening" in combined
    assert "deferred documentation" in combined
    assert "alone do not reopen priority 11" in combined


def test_horus_and_authority_boundaries_are_preserved():
    combined = "\n".join(texts())
    assert "HORUS" in combined
    assert "no HORUS documentation work" in combined or "No HORUS analytical finding is promoted" in combined
    assert "Governance" in combined
    assert "learning" in combined.lower()
