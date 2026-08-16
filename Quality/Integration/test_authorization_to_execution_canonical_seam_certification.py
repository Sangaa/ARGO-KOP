import json
from pathlib import Path

from canonical_spine_integration_audit import audit
from canonical_spine_gap_map import SEAMS
from execution_entrypoint import ExecutionDenied, execute


def test_authorization_to_execution_registry_record_is_material_and_verified():
    root = Path(__file__).resolve().parents[2]
    registry_path = root / "Quality/Integration/evidence/runtime/authorization_to_execution_verified_registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    result = audit(root, registry)
    assert len(SEAMS) == 11
    assert result["evidence"]["Authorization -> Execution"] == "CONNECTED"
    assert result["verified_connection_count"] == 1


def test_authorized_execution_reaches_trace_without_side_effect():
    result = execute(
        execution_id="EXEC-AUTH-EXEC-CANONICAL-001",
        task_id="TASK-AUTH-EXEC-CANONICAL-001",
        session_id="SESSION-AUTH-EXEC-CANONICAL-001",
        source_trace_id="DECISION-TRACE-AUTHORIZATION-EXECUTION-CANONICAL-001",
        authorized=True,
        final_status="SIMULATED",
        side_effect=False,
        stages=[
            {"name": "authorization", "status": "AUTHORIZED"},
            {"name": "execution", "status": "SIMULATED"},
        ],
    )
    assert result["execution_trace_id"] == result["trace"]["trace_id"]
    assert result["trace"]["record_type"] == "EXECUTION_TRACE"
    assert result["trace"]["side_effect"] is False


def test_unauthorized_execution_remains_blocked():
    try:
        execute(
            execution_id="EXEC-AUTH-EXEC-CANONICAL-BLOCKED",
            task_id="TASK-AUTH-EXEC-CANONICAL-BLOCKED",
            session_id="SESSION-AUTH-EXEC-CANONICAL-BLOCKED",
            source_trace_id="DECISION-TRACE-AUTHORIZATION-EXECUTION-CANONICAL-BLOCKED",
            authorized=False,
            final_status="SIMULATED",
            side_effect=False,
            stages=[{"name": "execution", "status": "SIMULATED"}],
        )
    except ExecutionDenied as exc:
        assert str(exc) == "EXECUTION_NOT_AUTHORIZED"
    else:
        raise AssertionError("unauthorized execution must remain blocked")
