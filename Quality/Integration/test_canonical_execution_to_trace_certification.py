import json
from pathlib import Path

from canonical_spine_integration_audit import audit
from canonical_spine_gap_map import SEAMS


ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "Quality" / "Integration" / "evidence" / "runtime" / "execution_to_trace_verified_registry.json"


def test_controlled_execution_to_trace_seam_is_canonically_certifiable():
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    result = audit(ROOT, registry)

    assert len(SEAMS) == 11
    assert result["evidence"]["Execution -> Execution Trace"] == "CONNECTED"
    assert result["verified_connection_count"] == 1

    trace = json.loads(
        (ROOT / registry["Execution -> Execution Trace"]["trace"]).read_text(encoding="utf-8")
    )
    assert trace["record_type"] == "EXECUTION_TRACE"
    assert trace["evidence_mode"] == "CONTROLLED_SYNTHETIC"
    assert trace["side_effect"] is False


def test_controlled_fixture_does_not_certify_another_seam():
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    result = audit(ROOT, registry)

    assert result["evidence"]["Decision -> Authorization"] != "CONNECTED"
    assert result["verified_connection_count"] == 1
