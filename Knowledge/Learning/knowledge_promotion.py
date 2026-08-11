"""Governed state transition from promotion eligibility to a knowledge record."""

from copy import deepcopy
from datetime import datetime, timezone


def promote(candidate: dict, *, authority: bool = False) -> dict:
    """Create a governed knowledge record only when the candidate is eligible."""
    if not authority:
        return {"status": "HOLD", "reason": "PROMOTION_AUTHORITY_MISSING"}

    required = ("task_id", "session_id", "evidence", "pattern", "confidence", "validation")
    missing = [key for key in required if not candidate.get(key)]
    if missing:
        return {"status": "HOLD", "reason": "REQUIRED_FIELD_MISSING", "missing": missing}

    if candidate.get("validation") != "VALIDATED":
        return {"status": "HOLD", "reason": "VALIDATION_REQUIRED"}

    if float(candidate.get("confidence", 0)) < 0.8:
        return {"status": "HOLD", "reason": "CONFIDENCE_BELOW_THRESHOLD"}

    record = deepcopy(candidate)
    record["status"] = "PROMOTED"
    record["promoted_at"] = datetime.now(timezone.utc).isoformat()
    record["knowledge_scope"] = "tested_claim_only"
    record["provenance_preserved"] = True
    return record
