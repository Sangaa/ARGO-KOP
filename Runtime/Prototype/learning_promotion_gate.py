"""Side-effect-free learning promotion gate for the ARGO prototype."""

from typing import Any, Dict


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
    )
    missing = [key for key in required if key not in candidate]
    if missing:
        return {"status": "HOLD", "reason": "CANDIDATE_INCOMPLETE", "missing": missing}

    if not candidate["evidence"]:
        return {"status": "HOLD", "reason": "NO_EVIDENCE"}

    if candidate["observed_result"] is None:
        return {"status": "HOLD", "reason": "RESULT_NOT_OBSERVED"}

    if candidate["validation"] != "VALIDATED":
        return {"status": "HOLD", "reason": "VALIDATION_FAILED"}

    if candidate["promotion_authority"] is not True:
        return {"status": "HOLD", "reason": "PROMOTION_AUTHORITY_MISSING"}

    if not isinstance(candidate["confidence"], (int, float)) or not 0 <= candidate["confidence"] <= 1:
        return {"status": "HOLD", "reason": "INVALID_CONFIDENCE"}

    if candidate["confidence"] < 0.8:
        return {"status": "HOLD", "reason": "LOW_CONFIDENCE"}

    return {"status": "PROMOTION_ELIGIBLE", "promote": True}
