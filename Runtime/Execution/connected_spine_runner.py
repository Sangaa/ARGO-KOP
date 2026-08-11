"""Connect the experimental stage contracts using a synthetic fixture."""

from authorization_gate import authorize
from decision_pass import propose
from reasoning_packet_classifier import classify
from traceable_reasoning import reason
from execution_plan import build_plan
from mock_executor import execute


def run(fixture: dict) -> dict:
    classified = classify(fixture["context"] | {"knowledge": fixture["knowledge"]})
    reasoning = reason(classified)
    proposal = propose(reasoning, rules=fixture["rules"])
    authorization = authorize(proposal, fixture["authorization"])
    plan = build_plan(authorization, action="SIMULATED_REVIEW", target=fixture["task"]["task_id"])
    execution = execute(plan)
    return {
        "task_id": fixture["task"]["task_id"],
        "stages": [classified, reasoning, proposal, authorization, plan, execution],
        "final_status": execution["status"],
    }
