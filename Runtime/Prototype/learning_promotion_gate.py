"""Side-effect-free learning promotion gate for the ARGO prototype."""

from typing import Any, Dict


def candidate_from_trace(
    trace: Dict[str, Any],
    *,
    observed_result: Any,
    pattern: str,
    confidence: float,
    promotion_authority: bool,
    governing_conflict: bool,
) -> Dict[str, Any]:
    """Build a promotion candidate without inferring learning authority.

    A RUN-011 action authorization is deliberately not reused as promotion
    authority. Callers must supply the learning decision and observed outcome
    explicitly after the cognitive run.
    """
    context = trace.get("context") if isinstance(trace.get("context"), dict) else {}
    validation = trace.get("validation") if isinstance(trace.get("validation"), dict) else {}

    return {
        "task_id": trace.get("task_id"),
        "session_id": context.get("session_id"),
        "evidence": list(context.get("evidence") or []),
        "observed_result": observed_result,
        "pattern": pattern,
        "confidence": confidence,
        "validation": validation.get("status"),
        "promotion_authority": promotion_authority,
        "governing_conflict": governing_conflict,
    }


def evaluate(candidate: Dict[str, Any]) -> Dict[str, Any]:
    required = (
        "task_id",
        "session_id",
        "evidence",
        "observed_result",
        "pattern",
        "confidence",
        "validation",
        "promotion_authority",
        "governing_conflict",
    )
    missing = [key for key in required if key not in candidate]
    if missing:
        return {"status": "HOLD", "reason": "CANDIDATE_INCOMPLETE", "missing": missing}

    blank = [
        key
        for key in ("task_id", "session_id", "pattern")
        if not isinstance(candidate[key], str) or not candidate[key].strip()
    ]
    if blank:
        return {"status": "HOLD", "reason": "CANDIDATE_INCOMPLETE", "invalid": blank}

    if not candidate["evidence"]:
        return {"status": "HOLD", "reason": "NO_EVIDENCE"}

    if candidate["observed_result"] is None:
        return {"status": "HOLD", "reason": "RESULT_NOT_OBSERVED"}

    if candidate["validation"] != "VALIDATED":
        return {"status": "HOLD", "reason": "VALIDATION_FAILED"}

    if candidate["governing_conflict"] is not False:
        return {"status": "HOLD", "reason": "GOVERNING_CONFLICT"}

    if candidate["promotion_authority"] is not True:
        return {"status": "HOLD", "reason": "PROMOTION_AUTHORITY_MISSING"}

    if not isinstance(candidate["confidence"], (int, float)) or not 0 <= candidate["confidence"] <= 1:
        return {"status": "HOLD", "reason": "INVALID_CONFIDENCE"}

    if candidate["confidence"] < 0.8:
        return {"status": "HOLD", "reason": "LOW_CONFIDENCE"}

    return {"status": "PROMOTION_ELIGIBLE", "promote": True}
