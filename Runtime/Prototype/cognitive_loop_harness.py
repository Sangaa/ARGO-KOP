"""ARGO KOP safe cognitive-loop harness.

Deterministic, side-effect-free prototype for validating the staged pipeline.
It intentionally stops at a proposed action and never performs external I/O.
"""

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, List


class State(str, Enum):
    CANDIDATE = "CANDIDATE"
    UNDER_REVIEW = "UNDER_REVIEW"
    VALIDATED = "VALIDATED"
    AUTHORIZED = "AUTHORIZED"
    PROPOSED = "PROPOSED"
    HOLD = "HOLD"
    REJECTED = "REJECTED"


@dataclass
class Context:
    task_id: str
    session_id: str
    active_state: str
    evidence: List[str]
    knowledge: List[str]
    requested_outcome: str


@dataclass
class Trace:
    task_id: str
    state: State
    context: Dict[str, Any]
    reasoning: Dict[str, Any]
    decision: Dict[str, Any]
    validation: Dict[str, Any]
    authorization: Dict[str, Any]
    action: Dict[str, Any]
    result: Dict[str, Any]


def load_context(payload: Dict[str, Any]) -> Context:
    required = ["task_id", "session_id", "active_state", "evidence", "knowledge", "requested_outcome"]
    missing = [key for key in required if key not in payload]
    if missing:
        raise ValueError(f"missing_context:{','.join(missing)}")
    return Context(**{key: payload[key] for key in required})


def reason(context: Context) -> Dict[str, Any]:
    if not context.evidence:
        return {"status": "HOLD", "observations": [], "hypotheses": [], "reason": "no_evidence"}
    return {
        "status": "READY",
        "observations": [f"Evidence available: {len(context.evidence)}"],
        "hypotheses": [],
        "requested_outcome": context.requested_outcome,
    }


def decide(context: Context, reasoning: Dict[str, Any]) -> Dict[str, Any]:
    if reasoning.get("status") != "READY":
        return {"status": "HOLD", "candidate": None}
    return {
        "status": "CANDIDATE",
        "candidate": "produce_non_destructive_proposal",
        "basis": list(context.evidence),
    }


def validate(context: Context, decision: Dict[str, Any]) -> Dict[str, Any]:
    if decision.get("status") != "CANDIDATE":
        return {"status": "HOLD", "checks": ["decision_not_ready"]}
    checks = {
        "evidence_present": bool(context.evidence),
        "knowledge_present": bool(context.knowledge),
        "non_destructive_action": decision.get("candidate") == "produce_non_destructive_proposal",
    }
    return {"status": "VALIDATED" if all(checks.values()) else "HOLD", "checks": checks}


def authorize(validation: Dict[str, Any], approved: bool) -> Dict[str, Any]:
    if validation.get("status") != "VALIDATED":
        return {"status": "HOLD", "approved": False}
    # Lack of human authorization is a reversible HOLD, not a rejection.
    # REJECTED remains reserved for an explicit negative policy/decision path.
    return {"status": "AUTHORIZED" if approved else "HOLD", "approved": approved}


def propose(decision: Dict[str, Any], authorization: Dict[str, Any]) -> Dict[str, Any]:
    if authorization.get("status") != "AUTHORIZED":
        return {"status": "NOT_EXECUTED", "proposal": None}
    return {
        "status": "PROPOSED",
        "proposal": {
            "type": decision["candidate"],
            "side_effects": False,
        },
    }


def run(payload: Dict[str, Any], human_approved: bool = False) -> Dict[str, Any]:
    context = load_context(payload)
    reasoning = reason(context)
    decision = decide(context, reasoning)
    validation = validate(context, decision)
    authorization = authorize(validation, human_approved)
    action = propose(decision, authorization)

    if action["status"] == "PROPOSED":
        state = State.PROPOSED
    elif authorization["status"] == "REJECTED":
        state = State.REJECTED
    else:
        state = State.HOLD

    trace = Trace(
        task_id=context.task_id,
        state=state,
        context=asdict(context),
        reasoning=reasoning,
        decision=decision,
        validation=validation,
        authorization=authorization,
        action=action,
        result={"executed": False, "external_side_effect": False},
    )
    return asdict(trace)


if __name__ == "__main__":
    example = {
        "task_id": "DEMO-001",
        "session_id": "SESSION-001",
        "active_state": "awaiting_customer_response",
        "evidence": ["email:2026-08-11:001"],
        "knowledge": ["rule:customer-response-draft"],
        "requested_outcome": "prepare a response draft",
    }
    print(run(example, human_approved=True))
