"""Governed correction and demotion primitives for promoted knowledge."""


def assess_contradiction(record: dict, *, evidence: list[str], contradiction: bool) -> dict:
    """Return a proposed state change; never silently mutate knowledge."""
    if not contradiction:
        return {"status": "NO_CHANGE", "record": record}
    return {
        "status": "DEMOTION_REVIEW_REQUIRED",
        "record_id": record.get("task_id"),
        "evidence": evidence,
        "reason": "NEW_EVIDENCE_CONTRADICTS_PROMOTED_CLAIM",
    }
