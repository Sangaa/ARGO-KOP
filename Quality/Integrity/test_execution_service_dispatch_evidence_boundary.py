from pathlib import Path


def test_execution_engine_declares_update_service_dispatch_boundary():
    root = Path(__file__).resolve().parents[2]
    engine = (root / "Engine/ENG-006_EXECUTION_ENGINE.md").read_text(encoding="utf-8")
    runtime = (root / "Runtime/RUN-010_RUNTIME_REFERENCE.md").read_text(encoding="utf-8")
    service = (root / "Services/SRV-009_UPDATE_SERVICE.md").read_text(encoding="utf-8")
    assert "Operations on repository state MUST route through `Services/SRV-009_UPDATE_SERVICE.md`" in engine
    assert "ENG-006 Execution → SRV-009 Controlled Mutation" in runtime
    assert "Technical write completion is not equivalent to governed acceptance" in service


def test_execution_service_dispatch_is_not_promoted_to_proven_runtime_coupling_without_evidence():
    root = Path(__file__).resolve().parents[2]
    matrix = (root / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(encoding="utf-8")
    assert "RUN-E03" in matrix
    assert "SERVICE_DISPATCH" in matrix
    assert "PARTIALLY_VERIFIED" in matrix
