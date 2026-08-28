"""Build a bounded, provenance-preserving prior-experience packet."""

from collections import Counter


ELIGIBLE_STATES = {"PROMOTED", "REUSABLE", "VERIFIED", "CANONICAL"}
INELIGIBLE_EVIDENCE = {"INVALIDATED", "REJECTED", "HOLD", "UNPROVEN"}
MATCH_WEIGHTS = {
    "artifact_ids": 8,
    "failure_classes": 4,
    "problem_types": 2,
    "domains": 1,
}


def _values(value) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {value}
    return {str(item) for item in value}


def _identity(record: dict) -> str | None:
    if record.get("knowledge_id"):
        return str(record["knowledge_id"])
    if record.get("task_id") and record.get("session_id"):
        return f"{record['task_id']}:{record['session_id']}"
    return None


def build_experience_packet(records: list[dict], context: dict) -> dict:
    """Select explicit, scope-compatible experience without changing authority."""
    required = ("task_id", "domain", "problem_types", "allowed_scopes")
    missing = [field for field in required if not context.get(field)]
    if missing:
        return {
            "status": "HOLD",
            "reason": "TASK_CONTEXT_INCOMPLETE",
            "missing": missing,
            "experience_items": [],
        }

    try:
        requested_limit = int(context.get("max_records", 5))
    except (TypeError, ValueError):
        requested_limit = 5
    limit = min(max(requested_limit, 1), 10)
    allowed_scopes = _values(context["allowed_scopes"])
    task_keys = {
        "domains": _values(context["domain"]),
        "problem_types": _values(context["problem_types"]),
        "artifact_ids": _values(context.get("artifact_ids")),
        "failure_classes": _values(context.get("failure_classes")),
    }

    excluded = Counter()
    selected = []
    for record in records:
        record_id = _identity(record)
        if not record_id:
            excluded["IDENTITY_MISSING"] += 1
            continue
        if record.get("status") not in ELIGIBLE_STATES:
            excluded["LIFECYCLE_STATE_INELIGIBLE"] += 1
            continue
        if record.get("evidence_state") in INELIGIBLE_EVIDENCE:
            excluded["EVIDENCE_STATE_INELIGIBLE"] += 1
            continue
        if record.get("knowledge_scope") not in allowed_scopes:
            excluded["OUT_OF_SCOPE"] += 1
            continue
        if not record.get("evidence") or not record.get("authority_state"):
            excluded["PROVENANCE_OR_AUTHORITY_MISSING"] += 1
            continue

        reasons = {}
        score = 0
        for field, weight in MATCH_WEIGHTS.items():
            overlap = sorted(task_keys[field] & _values(record.get(field)))
            if overlap:
                reasons[field] = overlap
                score += weight * len(overlap)
        if not reasons:
            excluded["NO_EXPLICIT_MATCH"] += 1
            continue

        selected.append({
            "knowledge_id": record_id,
            "pattern": record.get("pattern"),
            "knowledge_scope": record.get("knowledge_scope"),
            "evidence": record.get("evidence"),
            "evidence_state": record.get("evidence_state", "REPORTED"),
            "authority_state": record["authority_state"],
            "match_reasons": reasons,
            "score": score,
            "contradicts": sorted(_values(record.get("contradicts"))),
        })

    selected.sort(key=lambda item: (-item["score"], item["knowledge_id"]))
    selected = selected[:limit]
    selected_ids = {item["knowledge_id"] for item in selected}
    conflicts = sorted({
        tuple(sorted((item["knowledge_id"], target)))
        for item in selected
        for target in item["contradicts"]
        if target in selected_ids and target != item["knowledge_id"]
    })

    return {
        "status": "READY",
        "task_id": context["task_id"],
        "experience_items": selected,
        "conflicts": [list(pair) for pair in conflicts],
        "excluded_summary": dict(sorted(excluded.items())),
        "reasoning_start": [
            "CURRENT_EVIDENCE",
            "APPLICABLE_AUTHORITY",
            "RELEVANT_EXPERIENCE",
            "CONFLICT_CHECK",
            "ASSUMPTIONS",
            "OPTIONS",
            "TESTABLE_DECISION",
        ],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
    }


