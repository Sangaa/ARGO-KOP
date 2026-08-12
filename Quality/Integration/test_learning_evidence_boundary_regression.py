from learning_pipeline_integration import assess_for_promotion


def test_learning_never_reaches_readiness_without_evidence_trace():
    result = assess_for_promotion(
        decision_id="DEC-EVIDENCE-1",
        execution_id="EXEC-EVIDENCE-1",
        outcome={
            "outcome_id": "OUT-EVIDENCE-1",
            "result": "SUCCESS",
            "evidence_trace_ids": [],
            "execution_trace_ids": [],
            "confidence": "HIGH",
        },
    )

    assert result["status"] == "NOT_READY"
    assert result["stage"] == "EVALUATION"


def test_learning_never_reaches_readiness_with_mismatched_evidence_lineage():
    result = assess_for_promotion(
        decision_id="DEC-EVIDENCE-2",
        execution_id="EXEC-EVIDENCE-2",
        outcome={
            "outcome_id": "OUT-EVIDENCE-2",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TRACE-A"],
            "execution_trace_ids": ["TRACE-B"],
            "confidence": "HIGH",
        },
    )

    assert result["status"] == "NOT_READY"
    assert result["stage"] == "EVALUATION"
    assert "OUTCOME_PROVENANCE_BROKEN" in result["evaluation"]["issues"]
