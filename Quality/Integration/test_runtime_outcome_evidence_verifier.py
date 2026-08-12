from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence


def test_verifies_exact_runtime_trace_to_outcome_lineage():
    result = {
        "execution": {
            "execution_trace_id": "TR-1",
            "task_id": "TASK-1",
            "trace": {"trace_id": "TR-1"},
        },
        "outcome": {
            "status": "INCONCLUSIVE",
            "execution_trace_ids": ["TR-1"],
            "evidence_trace_ids": ["TR-1"],
        },
    }

    verified = verify_runtime_outcome_evidence(result)

    assert verified["status"] == "VERIFIED"
    assert verified["execution_trace_id"] == "TR-1"


def test_holds_on_trace_identity_mismatch():
    result = {
        "execution": {
            "execution_trace_id": "TR-1",
            "trace": {"trace_id": "TR-2"},
        },
        "outcome": {
            "execution_trace_ids": ["TR-1"],
            "evidence_trace_ids": ["TR-1"],
        },
    }

    assert verify_runtime_outcome_evidence(result) == {
        "status": "HOLD",
        "reason": "TRACE_ID_MISMATCH",
    }


def test_holds_when_outcome_does_not_reference_runtime_trace():
    result = {
        "execution": {
            "execution_trace_id": "TR-1",
            "trace": {"trace_id": "TR-1"},
        },
        "outcome": {
            "execution_trace_ids": ["TR-2"],
            "evidence_trace_ids": ["TR-2"],
        },
    }

    assert verify_runtime_outcome_evidence(result) == {
        "status": "HOLD",
        "reason": "OUTCOME_TRACE_LINEAGE_MISSING",
    }
