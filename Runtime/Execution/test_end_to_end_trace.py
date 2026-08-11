from end_to_end_trace import trace


def test_complete_spine_reaches_simulation():
    stages = [
        {"stage": "Runtime", "status": "READY"},
        {"stage": "Context", "status": "READY"},
        {"stage": "Knowledge", "status": "RETRIEVED"},
        {"stage": "Cognition", "status": "READY_FOR_REASONING"},
        {"stage": "Reasoning", "status": "REASONED"},
        {"stage": "Decision", "status": "PROPOSAL_READY"},
        {"stage": "Authorization", "status": "AUTHORIZED"},
        {"stage": "Execution Plan", "status": "PLAN_READY"},
        {"stage": "Mock Executor", "status": "SIMULATED_ONLY"},
    ]
    result = trace(stages)
    assert result["status"] == "COMPLETED_SIMULATION"
    assert result["side_effect"] is False
    assert result["events"][-1]["stage"] == "Mock Executor"


def test_blocked_stage_halts_spine():
    result = trace([
        {"stage": "Runtime", "status": "READY"},
        {"stage": "Authorization", "status": "BLOCKED"},
        {"stage": "Execution Plan", "status": "PLAN_READY"},
    ])
    assert result["status"] == "HALTED"
    assert len(result["events"]) == 2
