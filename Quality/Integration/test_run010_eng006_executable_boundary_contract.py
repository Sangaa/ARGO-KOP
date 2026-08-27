"""P302 contract tests for the open RUN-010 -> ENG-006 boundary.

These tests are intentionally non-invasive: they prove the current boundary is
not executable-verified and establish the acceptance contract for a future
implementation. They must not promote REL-009 or mutate production authority.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "Runtime" / "Execution"
sys.path.insert(0, str(RUNTIME))

import connected_spine_runner


def _fixture():
    return {
        "context": {"session_id": "P302-CONTRACT", "signal": "clean"},
        "knowledge": {"facts": ["fixture"]},
        "rules": {"mode": "governed"},
        "authorization": {"approved": True},
        "task": {"task_id": "RUN-010"},
    }


def test_c1_authorization_is_present_before_boundary():
    result = connected_spine_runner.run(_fixture())
    assert result["execution"]["status"] == "SIMULATED"
    assert any(s.get("status") == "AUTHORIZED" for s in result["stages"] if isinstance(s, dict))


def test_c2_current_runner_does_not_claim_callable_eng006_consumer():
    result = connected_spine_runner.run(_fixture())
    assert result["final_status"] == "SIMULATED"
    assert result["execution"]["final_status"] == "SIMULATED"
    assert result["execution"]["side_effect"] is False


def test_c3_trace_continuity_exists_only_for_simulated_execution():
    result = connected_spine_runner.run(_fixture())
    assert result["decision_trace"]["trace_id"] == result["execution"]["source_trace_id"]


def test_c4_validation_evidence_is_preserved():
    result = connected_spine_runner.run(_fixture())
    assert result["decision_trace"]["evidence_map"] is not None


def test_c5_simulation_cannot_close_rel009():
    result = connected_spine_runner.run(_fixture())
    assert result["final_status"] != "EXECUTABLE-VERIFIED"


def test_c6_downstream_boundary_is_not_implicitly_reclassified():
    probe = (ROOT / "Quality" / "Integration" / "ENG006_SRV009_EXECUTABLE_CONSUMER_PROBE.md").read_text()
    assert "ENG-006 → SRV-009 = EXECUTABLE-VERIFIED" in probe
    assert "RUN-010 → ENG-006 = NOT EXECUTABLE-VERIFIED" in probe


def test_c7_contract_does_not_mutate_runtime_or_registry():
    runtime = (RUNTIME / "connected_spine_runner.py").read_text()
    registry = (ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text()
    assert "SIMULATED_REVIEW" in runtime
    assert "REL-009" in registry
