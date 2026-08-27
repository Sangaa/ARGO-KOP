"""Connect the governed execution seam with cognition-state gating."""

from uuid import uuid4

from authorization_gate import authorize
from decision_pass import propose
from reasoning_packet_classifier import classify
from traceable_reasoning import reason
from execution_plan import build_plan
from execution_entrypoint import execute
from context_conflict_detector import detect
from reasoning_hold import evaluate
from decision_trace_producer import record_decision_trace
from outcome_producer import record_execution_outcome
from Runtime.Execution.run010_eng006_consumer import dispatch_run010


def run(fixture: dict) -> dict:
    reasoning_packet = {"context": fixture["context"], "knowledge": fixture["knowledge"]}
    classified = classify(reasoning_packet)
    reasoning = reason(classified)

    conflict = detect(fixture["context"])
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

    decision_trace_result = record_decision_trace(
        trace_id=f"DEC-{uuid4().hex[:12]}",
        task_id=fixture["task"]["task_id"],
        session_id=fixture["context"]["session_id"],
        evidence_map=reasoning.get("evidence_map", []),
        decision_status=proposal.get("status", "UNKNOWN"),
    )
    if decision_trace_result["status"] != "TRACE_RECORDED":
        blocked = {"status": "BLOCKED", "reason": "DECISION_TRACE_RECORDING_FAILED", "issues": decision_trace_result.get("issues", [])}
        return {
            "task_id": fixture["task"]["task_id"],
            "stages": [classified, reasoning, conflict, hold, proposal, authorization, plan, blocked],
            "final_status": "BLOCKED",
        }

    decision_trace = decision_trace_result["trace"]
    if plan.get("status") != "PLAN_READY":
        execution = {"status": "BLOCKED", "reason": "PLAN_NOT_READY"}
    elif fixture["task"]["task_id"] == "RUN-010" and authorization.get("status") == "AUTHORIZED":
        consumer = fixture.get("eng006_consumer")
        if consumer is not None:
            execution = dispatch_run010(
                candidate={
                    "task_id": "RUN-010",
                    "authorization_status": authorization.get("status"),
                    "source_trace_id": decision_trace["trace_id"],
                },
                eng006_consumer=consumer,
            )
        else:
            execution = execute(
                execution_id=f"EXEC-{uuid4().hex[:12]}",
                task_id=fixture["task"]["task_id"],
                session_id=fixture["context"]["session_id"],
                source_trace_id=decision_trace["trace_id"],
                authorized=True,
                final_status="SIMULATED",
                side_effect=False,
                stages=[
                    {"name": "decision", "status": proposal.get("status", "UNKNOWN")},
                    {"name": "authorization", "status": "AUTHORIZED"},
                    {"name": "execution", "status": "SIMULATED"},
                ],
            )
    else:
        execution = execute(
            execution_id=f"EXEC-{uuid4().hex[:12]}",
            task_id=fixture["task"]["task_id"],
            session_id=fixture["context"]["session_id"],
            source_trace_id=decision_trace["trace_id"],
            authorized=authorization.get("status") == "AUTHORIZED",
            final_status="SIMULATED",
            side_effect=False,
            stages=[
                {"name": "decision", "status": proposal.get("status", "UNKNOWN")},
                {"name": "authorization", "status": authorization.get("status", "UNKNOWN")},
                {"name": "execution", "status": "SIMULATED"},
            ],
        )

    outcome = None
    if execution.get("execution_trace_id"):
        outcome_result = record_execution_outcome(decision_id=decision_trace["trace_id"], execution=execution)
        outcome = outcome_result.get("outcome") if outcome_result["status"] == "OUTCOME_RECORDED" else {"status": "BLOCKED", "reason": "OUTCOME_RECORDING_FAILED", "issues": outcome_result.get("issues", [])}

    return {
        "task_id": fixture["task"]["task_id"],
        "stages": [classified, reasoning, conflict, hold, proposal, authorization, plan, execution],
        "decision_trace": decision_trace,
        "execution": execution,
        "outcome": outcome,
        "final_status": "SIMULATED" if execution.get("execution_trace_id") else execution.get("status"),
    }
