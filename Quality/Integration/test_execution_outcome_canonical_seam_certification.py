from canonical_spine_integration_audit import audit


def test_execution_to_outcome_accepts_complete_verified_evidence():
    root = __import__("pathlib").Path(__file__).resolve().parents[2]
    evidence = {
        "Execution -> Outcome": {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/OUTCOME_EVALUATION_CONTRACT.md",
            "test": "Quality/Integration/test_execution_outcome_registry_evidence.py",
            "trace": "Quality/Integration/canonical_evidence/EXECUTION_TO_OUTCOME_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Execution -> Outcome"] == "CONNECTED"
    assert result["verified_connection_count"] >= 1


def test_execution_to_outcome_certification_does_not_promote_unrelated_seams():
    root = __import__("pathlib").Path(__file__).resolve().parents[2]
    evidence = {
        "Execution -> Outcome": {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/OUTCOME_EVALUATION_CONTRACT.md",
            "test": "Quality/Integration/test_execution_outcome_registry_evidence.py",
            "trace": "Quality/Integration/canonical_evidence/EXECUTION_TO_OUTCOME_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Authorization -> Execution"] != "CONNECTED"
