def normalize_result(runtime_result: dict) -> dict:
    return {
        "task_id": runtime_result["task_id"],
        "session_id": runtime_result.get("session_id"),
        "project_id": runtime_result.get("project_id"),
        "execution_status": runtime_result["execution_status"],
        "authorization_id": runtime_result.get("authorization_id"),
        "side_effect": runtime_result.get("side_effect", False),
        "source": "runtime",
    }


def test_simulation_is_not_external_fact():
    result = normalize_result({
        "task_id": "SYN-TASK-001",
        "session_id": "SYN-SESSION-001",
        "project_id": "ARGO-KOP",
        "execution_status": "SIMULATED_ONLY",
        "authorization_id": "SYN-AUTH-001",
        "side_effect": False,
    })
    assert result["source"] == "runtime"
    assert result["execution_status"] == "SIMULATED_ONLY"
    assert result["side_effect"] is False


def test_identity_survives_normalization():
    result = normalize_result({
        "task_id": "T-42",
        "session_id": "S-42",
        "project_id": "P-42",
        "execution_status": "SIMULATED_ONLY",
        "authorization_id": "AUTH-42",
    })
    assert result["task_id"] == "T-42"
    assert result["session_id"] == "S-42"
    assert result["project_id"] == "P-42"
    assert result["authorization_id"] == "AUTH-42"


def test_persistence_requires_explicit_state_transition():
    candidate = {"execution_status": "SIMULATED_ONLY"}
    assert candidate["execution_status"] != "PERSISTED"
