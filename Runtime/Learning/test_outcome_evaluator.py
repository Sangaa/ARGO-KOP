from outcome_evaluator import evaluate_outcome


def base_outcome(result):
    return {
        "outcome_id": "OUT-1",
        "result": result,
        "evidence_trace_ids": ["TR-1"],
        "execution_trace_ids": ["TR-1"],
    }


def test_success_is_evaluated_and_learning_eligible():
    result = evaluate_outcome(
        decision_id="DEC-1", execution_id="EXEC-1", outcome=base_outcome("SUCCESS")
    )
    assert result["status"] == "EVALUATED"
    assert result["learning_eligible"] is True


def test_partial_is_evaluated_and_learning_eligible():
    result = evaluate_outcome(
        decision_id="DEC-1", execution_id="EXEC-1", outcome=base_outcome("PARTIAL")
    )
    assert result["learning_eligible"] is True


def test_failure_is_evaluated_and_learning_eligible_for_review():
    result = evaluate_outcome(
        decision_id="DEC-1", execution_id="EXEC-1", outcome=base_outcome("FAILURE")
    )
    assert result["status"] == "EVALUATED"
    assert result["learning_eligible"] is True


def test_inconclusive_is_not_learning_eligible():
    result = evaluate_outcome(
        decision_id="DEC-1", execution_id="EXEC-1", outcome=base_outcome("INCONCLUSIVE")
    )
    assert result["status"] == "EVALUATED"
    assert result["learning_eligible"] is False


def test_invalid_result_is_rejected():
    result = evaluate_outcome(
        decision_id="DEC-1", execution_id="EXEC-1", outcome=base_outcome("GUESS")
    )
    assert result["status"] == "EVALUATION_REJECTED"
    assert "INVALID_OUTCOME_RESULT" in result["issues"]


def test_missing_outcome_evidence_is_rejected():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "result": "SUCCESS",
            "evidence_trace_ids": [],
            "execution_trace_ids": ["TR-1"],
        },
    )
    assert result["status"] == "EVALUATION_REJECTED"
    assert "OUTCOME_EVIDENCE_REQUIRED" in result["issues"]


def test_missing_execution_trace_is_rejected():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={"outcome_id": "OUT-1", "result": "SUCCESS", "evidence_trace_ids": ["TR-1"]},
    )
    assert result["status"] == "EVALUATION_REJECTED"
    assert "EXECUTION_TRACE_REQUIRED" in result["issues"]


def test_outcome_evidence_not_in_execution_trace_is_rejected():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "result": "SUCCESS",
            "evidence_trace_ids": ["TR-1"],
            "execution_trace_ids": ["TR-2"],
        },
    )
    assert result["status"] == "EVALUATION_REJECTED"
    assert "OUTCOME_PROVENANCE_BROKEN" in result["issues"]
