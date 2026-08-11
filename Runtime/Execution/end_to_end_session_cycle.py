"""Small synthetic end-to-end cycle across two sessions.

This is intentionally a prototype harness: it proves state/provenance continuity
without invoking external side effects.
"""

from Cognition.session_context_rehydrator import rehydrate
from Cognition.context_memory_selector import select
from Decision.authorization_gate import authorize
from Runtime.Execution.mock_executor import execute


def run_cycle(session_1: dict, session_2: dict) -> dict:
    historical = session_1["historical_record"]
    context = rehydrate(
        current_task_id=session_2["task_id"],
        current_project_id=session_2.get("project_id"),
        current_facts=session_2.get("current_facts", []),
        historical_records=[historical],
    )

    proposal = {
        "status": "PROPOSAL_READY" if context["historical_evidence"] else "REVIEW_REQUIRED",
        "task_id": session_2["task_id"],
        "project_id": session_2.get("project_id"),
        "evidence": context["historical_evidence"],
    }
    authorization = authorize(proposal, session_2.get("authorization"))

    if authorization["status"] != "AUTHORIZED":
        return {
            "status": "BLOCKED",
            "context": context,
            "authorization": authorization,
        }

    plan = {
        "status": "PLAN_READY",
        "execution_status": "NOT_STARTED",
        "task_id": session_2["task_id"],
        "authorization_id": authorization["authorization_id"],
    }
    execution = execute(plan)
    return {
        "status": "COMPLETE",
        "context": context,
        "authorization": authorization,
        "execution": execution,
    }
