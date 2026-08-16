from pathlib import Path


def test_environment_sensing_boundary_references_current_runtime_and_integration_contracts():
    root = Path(__file__).resolve().parents[2]
    source = root / "Interfaces/INTF-006_ENVIRONMENT_SENSING.md"
    text = source.read_text(encoding="utf-8")
    for target in (
        "Interfaces/INTF-010_INTEGRATIONS.md",
        "Runtime/RUN-005_RUNTIME_WORKFLOW.md",
        "Runtime/RUN-006_AI_PROTOCOL.md",
        "Runtime/RUN-007_RUNTIME_SECURITY.md",
        "Runtime/RUN-008_RUNTIME_STATE.md",
        "Runtime/RUN-009_RECOVERY.md",
        "Architecture/ARC-007_INTEGRATION_MODEL.md",
    ):
        assert (root / target).is_file(), target
        assert Path(target).name in text, target


def test_environment_sensing_remains_proposed_until_implementation_evidence_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Interfaces/INTF-006_ENVIRONMENT_SENSING.md").read_text(encoding="utf-8")
    assert "Status: Proposed / Integrity Hold" in text
    assert "Implementation readiness and runtime availability remain separate concerns." in text
    assert "Observation → Learning Candidate is not an automatic transition" in text
