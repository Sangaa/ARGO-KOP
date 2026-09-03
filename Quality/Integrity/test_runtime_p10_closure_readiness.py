from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
RUN013 = ROOT / "Runtime/RUN-013_CONTROLLED_HANDOFF.md"
RUN015 = ROOT / "Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md"
H = ROOT / "Repository/MUT-2026-09-03-P10-RUNTIME-KNOWLEDGE-CORRECTION-H_MUTATION_MATRIX.md"
I = ROOT / "Repository/MUT-2026-09-03-P10-GATE12-KNOWLEDGE-MEMORY-CLOSURE-I_MUTATION_MATRIX.md"
J = ROOT / "Repository/MUT-2026-09-03-P10-GATE13-RUNTIME-CONNECTOR-HANDOFF-J_MUTATION_MATRIX.md"


def test_bounded_runtime_transactions_are_closed_before_readiness_hold():
    for matrix in (H, I, J):
        text = matrix.read_text(encoding="utf-8")
        assert "CLOSED / VERIFIED / RESUME-SAFE" in text


def test_gate15_contracts_still_forbid_executable_promotion_claim():
    run013 = RUN013.read_text(encoding="utf-8")
    run015 = RUN015.read_text(encoding="utf-8")
    assert "It must not return `EXECUTED`." in run013
    assert "It does not authorize production execution." in run013
    assert "does not certify the full Runtime" in run015
    assert "executable promotion and consolidated cross-layer Runtime validation remain on HOLD" in run015


def test_runtime_status_closes_gate15_boundedly_and_keeps_p10_open_on_exact_inventory():
    status = STATUS.read_text(encoding="utf-8")
    assert "🟡 VALIDATED / CROSS-LAYER INTEGRATION HOLD" in status
    assert "15. Runtime ↔ Engine cognitive-loop prototype seam — BOUNDED VERIFIED" in status
    assert "Therefore Priority 10 is not closure-ready while exact Runtime physical inventory/allocation remains unreconciled." in status
    assert "Proceed to exact Runtime physical inventory/allocation reconciliation" in status
    assert "118` paths" in status
    assert "global Runtime certification remains intentionally capped" in status
