"""Connect the experimental stage contracts with cognition-state gating."""

from authorization_gate import authorize
from decision_pass import propose
from reasoning_packet_classifier import classify
from traceable_reasoning import reason
from execution_plan import build_plan
from mock_executor import execute
from context_conflict_detector import detect
from reasoning_hold import evaluate


def run(fixture: dict) -> dict:
    cognition_context = fixture["context"] | {"knowledge": fixture["knowledge"]}
    classified = classify(cognition_context)
    reasoning = reason(classified)

    conflict = detect(cognition_context)
    hold = evaluate(conflict)
    if hold["status"] == "HOLD":
        blocked = {"status": "BLOCKED", "reason": hold["reason"]}
        return {
            "task_id": fixture["task"]["task_id"],
            "stages": [classified, reasoning, conflict, hold, blocked, blocked, blocked],
            "final_status": "HOLD",
        }

    proposal = propose(reasoning, rules=fixture["rules"])
    authorization = authorize(proposal, fixture["authorization"])
    plan = build_plan(authorization, action="SIMULATED_REVIEW", target=fixture["task"]["task_id"])
    execution = execute(plan)
    return {
        "task_id": fixture["task"]["task_id"],
        "stages": [classified, reasoning, conflict, hold, proposal, authorization, plan, execution],
        "final_status": execution["status"],
    }
