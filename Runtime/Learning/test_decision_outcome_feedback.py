from decision_outcome_feedback import evaluate_outcome


def test_evaluated_outcome_can_be_learning_eligible():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "evaluation_status": "EVALUATED",
            "learning_eligible": True,
        },
    )
    assert result["status"] == "OUTCOME_RECORDED"
    assert result["learning_eligible"] is True


def test_unassessed_outcome_cannot_enter_learning():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={
            "outcome_id": "OUT-1",
            "evaluation_status": "UNASSESSED",
            "learning_eligible": True,
        },
    )
    assert result["status"] == "OUTCOME_RECORDED"
    assert result["learning_eligible"] is False


def test_missing_provenance_rejects_feedback():
    result = evaluate_outcome(
        decision_id="",
        execution_id="EXEC-1",
        outcome={"outcome_id": "OUT-1", "evaluation_status": "EVALUATED"},
    )
    assert result["status"] == "FEEDBACK_REJECTED"
    assert "DECISION_ID_REQUIRED" in result["issues"]


def test_invalid_evaluation_status_rejects_feedback():
    result = evaluate_outcome(
        decision_id="DEC-1",
        execution_id="EXEC-1",
        outcome={"outcome_id": "OUT-1", "evaluation_status": "GUESS"},
    )
    assert result["status"] == "FEEDBACK_REJECTED"
    assert "INVALID_EVALUATION_STATUS" in result["issues"]
