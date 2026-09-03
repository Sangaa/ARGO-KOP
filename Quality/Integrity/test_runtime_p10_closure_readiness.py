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


def test_runtime_status_closes_p10_boundedly_after_exact_inventory():
    status = STATUS.read_text(encoding="utf-8")
    assert "🟢 CLOSED_FOR_PHASE_1 / BOUNDED RUNTIME PARTITION CERTIFIED / GLOBAL HOLDS REMAIN" in status
    assert "15. Runtime ↔ Engine cognitive-loop prototype seam — BOUNDED VERIFIED" in status
    assert "Priority 10 is `CLOSED_FOR_PHASE_1 / BOUNDED RUNTIME PARTITION CERTIFIED / GLOBAL HOLDS REMAIN`." in status
    assert "BOUNDED RUNTIME PARTITION CLOSURE != GLOBAL RUNTIME CERTIFICATION" in status
    assert "After exact-head verification of Transaction O, rediscover live `main`" in status
    assert "118` paths" in status
    assert "live provider trust is not inferred" in status
    assert "EXECUTABLE PROMOTION HOLD" in status
