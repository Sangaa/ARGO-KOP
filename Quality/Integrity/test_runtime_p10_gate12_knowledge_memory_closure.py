from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
LEARNING_CONTRACT = ROOT / "Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md"
RUN014 = ROOT / "Runtime/RUN-014_LEARNING_PROMOTION_TEST.md"
G_MATRIX = ROOT / "Repository/MUT-2026-09-03-P10-RUNTIME-MEMORY-PERSISTENCE-G_MUTATION_MATRIX.md"
H_MATRIX = ROOT / "Repository/MUT-2026-09-03-P10-RUNTIME-KNOWLEDGE-CORRECTION-H_MUTATION_MATRIX.md"


def test_gate12_requires_closed_runtime_memory_and_knowledge_transactions():
    for matrix in (G_MATRIX, H_MATRIX):
        text = matrix.read_text(encoding="utf-8")
        assert "CLOSED / VERIFIED / RESUME-SAFE" in text


def test_runtime_learning_boundary_stops_before_knowledge_promotion():
    contract = LEARNING_CONTRACT.read_text(encoding="utf-8")
    run014 = RUN014.read_text(encoding="utf-8")
    assert "This integration MUST NOT promote knowledge itself." in contract
    assert "A readiness report is not a promotion action." in contract
    assert "no candidate becomes learned knowledge unless the promotion gate is satisfied" in run014


def test_folder_status_closes_only_bounded_gate12_and_preserves_independent_holds():
    status = RUNTIME_STATUS.read_text(encoding="utf-8")
    assert "Runtime ↔ Knowledge / Memory integration — BOUNDED VERIFIED" in status
    assert "Runtime ↔ Interfaces / external connectors — BOUNDED VERIFIED FOR PROVIDER-NEUTRAL HANDOFF" in status
    assert "LIVE PROVIDER AUTHENTICITY, AUTHORIZATION AND AVAILABILITY HOLD" in status
    assert "EXECUTABLE PROMOTION HOLD" in status
    assert "production/provider authenticity" in status
