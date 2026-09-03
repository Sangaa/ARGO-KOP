from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_INTEGRATION = ROOT / "Runtime/Integration"
sys.path.insert(0, str(RUNTIME_INTEGRATION))

from runtime_connector_handoff import dispatch_connector_request  # noqa: E402

INTF010 = ROOT / "Interfaces/INTF-010_INTEGRATIONS.md"
RUNTIME_STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
INTERFACE_STATUS = ROOT / "Interfaces/_FOLDER_STATUS.md"
HANDOFF_SOURCE = RUNTIME_INTEGRATION / "runtime_connector_handoff.py"


def valid_request():
    return {
        "request_id": "REQ-P10-J-GUARD",
        "operation": "update",
        "target": "provider-neutral-target",
        "payload": {"content": "guard"},
        "authorized": True,
    }


def test_intf010_outbound_semantics_are_bound_to_runtime_handoff():
    contract = INTF010.read_text(encoding="utf-8")
    assert "Intent → Authorization Check → Payload Validation → Connector → External System → Result → Evidence/Log" in contract
    assert "A requested action is not equivalent to a completed action." in contract
    assert "execution status unknown" in contract

    result = dispatch_connector_request(valid_request(), executor=lambda payload: {"status": "executed"})
    assert result["status"] == "RESULT_REPORTED"
    assert result["connector_status"] == "executed"


def test_runtime_handoff_is_provider_neutral_and_does_not_claim_authenticity():
    source = HANDOFF_SOURCE.read_text(encoding="utf-8")
    assert "GITHUB_REPOSITORY_CONNECTOR" not in source
    assert "ENG006_SRV009_PRODUCTION_ADAPTER" not in source
    assert "caller-supplied executor" in source

    runtime = RUNTIME_STATUS.read_text(encoding="utf-8")
    interfaces = INTERFACE_STATUS.read_text(encoding="utf-8")
    assert "13. Runtime ↔ Interfaces / external connectors — BOUNDED VERIFIED FOR PROVIDER-NEUTRAL HANDOFF" in runtime
    assert "LIVE PROVIDER AUTHENTICITY, AUTHORIZATION AND AVAILABILITY HOLD" in runtime
    assert "provider authentication capability and trust-anchor acquisition" in interfaces
    assert "provider authenticity" in interfaces


def test_gate15_and_global_runtime_hold_remain_independent():
    runtime = RUNTIME_STATUS.read_text(encoding="utf-8")
    assert "EXECUTABLE PROMOTION HOLD" in runtime
    assert "🟡 VALIDATED / CROSS-LAYER INTEGRATION HOLD" in runtime
    assert "global Runtime certification remains intentionally capped" in runtime
