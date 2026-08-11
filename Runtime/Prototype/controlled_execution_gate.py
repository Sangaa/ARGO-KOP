"""Controlled execution gate for the ARGO cognitive-loop prototype.

This module does not execute external actions. It verifies that a proposed
action has the minimum traceable conditions before a future executor could
accept it.
"""

from typing import Any, Dict


REQUIRED_TRACE_FIELDS = (
    "task_id",
    "context",
    "reasoning",
    "decision",
    "validation",
    "authorization",
    "action",
    "result",
)


def evaluate(trace: Dict[str, Any]) -> Dict[str, Any]:
    missing = [field for field in REQUIRED_TRACE_FIELDS if field not in trace]
    if missing:
        return {"status": "HOLD", "reason": "TRACE_INCOMPLETE", "missing": missing}

    validation = trace["validation"]
    authorization = trace["authorization"]
    action = trace["action"]

    if validation.get("status") != "VALIDATED":
        return {"status": "HOLD", "reason": "VALIDATION_FAILED"}

    if authorization.get("status") != "AUTHORIZED":
        return {"status": "HOLD", "reason": "AUTHORIZATION_MISSING"}

    proposal = action.get("proposal")
    if not proposal or proposal.get("side_effects") is not False:
        return {"status": "HOLD", "reason": "UNSAFE_ACTION"}

    return {"status": "READY_FOR_CONTROLLED_HANDOFF", "side_effects": False}
