from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENTRYPOINT = ROOT / "Runtime/Execution/execution_entrypoint.py"
MOCK_EXECUTOR = ROOT / "Runtime/Execution/mock_executor.py"
AUTH_CONTRACT = ROOT / "Runtime/Execution/EXECUTION_AUTHORIZATION_HANDOFF.md"
RUN013 = ROOT / "Runtime/RUN-013_CONTROLLED_HANDOFF.md"
RUN015 = ROOT / "Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md"
STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
MATRIX = ROOT / "Repository/MUT-2026-09-03-P10-GATE15-EXECUTION-AUTHORITY-L_MUTATION_MATRIX.md"


def test_execution_authority_fails_closed_on_non_boolean_authorization_and_missing_identity():
    source = ENTRYPOINT.read_text(encoding="utf-8")
    assert "if authorized is not True:" in source
    assert "EXECUTION_NOT_EXPLICITLY_AUTHORIZED" in source
    assert "EXECUTION_IDENTITY_REQUIRED" in source


def test_mock_execution_requires_authorization_identity_and_stays_side_effect_free():
    source = MOCK_EXECUTOR.read_text(encoding="utf-8")
    contract = AUTH_CONTRACT.read_text(encoding="utf-8")
    assert "authorization identity is absent" in contract
    assert "AUTHORIZATION_REQUIRED" in source
    assert '"side_effect": False' in source


def test_gate15_hardening_does_not_promote_controlled_handoff_or_production_execution():
    run013 = RUN013.read_text(encoding="utf-8")
    run015 = RUN015.read_text(encoding="utf-8")
    status = STATUS.read_text(encoding="utf-8")
    matrix = MATRIX.read_text(encoding="utf-8")
    assert "It must not return `EXECUTED`." in run013
    assert "does not certify the full Runtime" in run015
    assert "Gate 15 is therefore boundedly verified for this tracked fail-closed seam" in status
    assert "33776295841" in matrix
    assert "no external API/email/production mutation" in matrix
