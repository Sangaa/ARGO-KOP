import json
from pathlib import Path

from canonical_spine_integration_audit import audit


def test_trace_to_outcome_seam_accepts_only_complete_verified_evidence():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Execution Trace -> Outcome Evaluation": {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/OUTCOME_EVALUATION_CONTRACT.md",
            "test": "Quality/Integration/test_execution_trace_to_outcome_evaluation.py",
            "trace": "Quality/Integration/evidence/runtime/execution_trace_to_outcome_evaluation_certification.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Execution Trace -> Outcome Evaluation"] == "CONNECTED"
    assert result["verified_connection_count"] == 1

    payload = json.loads(
        (root / evidence["Execution Trace -> Outcome Evaluation"]["trace"]).read_text(encoding="utf-8")
    )
    assert payload["record_type"] == "EXECUTION_TRACE"
    assert payload["final_status"] == "SIMULATED"
    assert payload["outcome_result"] == "INCONCLUSIVE"
    assert payload["execution_trace_ids"] == [payload["trace_id"]]
    assert payload["evidence_trace_ids"] == [payload["trace_id"]]
    assert payload["side_effect"] is False


def test_trace_to_outcome_certification_does_not_promote_other_seams():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Execution Trace -> Outcome Evaluation": {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/OUTCOME_EVALUATION_CONTRACT.md",
            "test": "Quality/Integration/test_execution_trace_to_outcome_evaluation.py",
            "trace": "Quality/Integration/evidence/runtime/execution_trace_to_outcome_evaluation_certification.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Execution -> Execution Trace"] != "CONNECTED"
