"""Governed correction and demotion primitives for promoted knowledge."""


def _hold(record, reason: str) -> dict:
    """Fail closed without mutating the supplied record."""
    return {"status": "HOLD", "reason": reason, "record": record}


def assess_contradiction(record: dict, *, evidence: list[str], contradiction: bool) -> dict:
    """Return a governed review proposal only after minimum proof is satisfied."""
    if not isinstance(record, dict):
        return _hold(record, "INVALID_RECORD")

    task_id = record.get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        return _hold(record, "MISSING_STABLE_TASK_ID")

    if record.get("status") != "PROMOTED":
        return _hold(record, "SOURCE_NOT_PROMOTED")

    if (
        not isinstance(evidence, list)
        or not evidence
        or any(not isinstance(item, str) or not item.strip() for item in evidence)
    ):
        return _hold(record, "INVALID_EVIDENCE")

    if type(contradiction) is not bool:
        return _hold(record, "INVALID_CONTRADICTION_SIGNAL")

    if contradiction is False:
        return {"status": "NO_CHANGE", "record": record}

    return {
        "status": "DEMOTION_REVIEW_REQUIRED",
        "record_id": task_id,
        "evidence": list(evidence),
        "reason": "NEW_EVIDENCE_CONTRADICTS_PROMOTED_CLAIM",
    }
