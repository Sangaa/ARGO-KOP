import json

from canonical_spine_integration_audit import audit


def test_outcome_feedback_quality_seam_is_canonically_certifiable(tmp_path):
    contract = "Quality/Integration/canonical_evidence/OUTCOME_EVALUATION_TO_FEEDBACK_QUALITY.md"
    test = "Quality/Integration/test_outcome_evaluation_to_feedback_quality.py"
    trace = "Quality/Integration/canonical_evidence/OUTCOME_EVALUATION_TO_FEEDBACK_QUALITY_TRACE.json"

    (tmp_path / contract).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / contract).write_text("verified evidence", encoding="utf-8")
    (tmp_path / test).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / test).write_text("verified evidence", encoding="utf-8")
    (tmp_path / trace).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / trace).write_text(
        json.dumps({
            "record_type": "EXECUTION_TRACE",
            "trace_id": "TRACE-OUTCOME-FEEDBACK-QUALITY-001",
            "task_id": "TASK-OUTCOME-FEEDBACK-QUALITY-001",
            "session_id": "SESSION-OUTCOME-FEEDBACK-QUALITY-001",
            "final_status": "SUCCESS",
        }),
        encoding="utf-8",
    )

    result = audit(
        tmp_path,
        {
            "Outcome Evaluation -> Feedback Quality": {
                "state": "CONNECTED",
                "contract": contract,
                "test": test,
                "trace": trace,
                "verification_status": "VERIFIED",
            }
        },
    )

    assert result["evidence"]["Outcome Evaluation -> Feedback Quality"] == "CONNECTED"
    assert result["verified_connection_count"] == 1
    assert all(
        gap["seam"] != "Outcome Evaluation -> Feedback Quality"
        for gap in result["gap_map"]["gaps"]
    )
