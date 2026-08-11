"""Persistable, inspectable representation of one ARGO execution trace."""

from datetime import datetime, timezone


def build_trace_record(result: dict, *, session_id: str) -> dict:
    if "task_id" not in result or "stages" not in result:
        return {"status": "HOLD", "reason": "TRACE_RESULT_INCOMPLETE"}

    return {
        "trace_id": f"TRACE-{result['task_id']}-{session_id}",
        "task_id": result["task_id"],
        "session_id": session_id,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "final_status": result.get("final_status"),
        "side_effect": result["stages"][-1].get("side_effect", False),
        "stages": result["stages"],
        "record_type": "EXECUTION_TRACE",
    }
