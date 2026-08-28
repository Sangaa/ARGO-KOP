"""Build a bounded advisory experience packet from promoted knowledge.

The Experience Spine is a semantic projection over existing promoted knowledge.
It does not persist, promote, demote, authorize, or rewrite knowledge records.
"""
from __future__ import annotations

from collections import Counter, defaultdict


BLOCKED_EVIDENCE_STATES = {"INVALIDATED", "REJECTED", "HOLD", "UNPROVEN"}
MATCH_WEIGHTS = {
    "artifact_ids": 8,
    "failure_classes": 4,
    "problem_types": 2,
    "domains": 1,
}
REQUIRED_CONTEXT = (
    "task_id",
    "execution_identity",
    "domain",
    "problem_types",
    "allowed_scopes",
    "consumer_route",
)
REQUIRED_PROFILE = (
    "source_identity",
    "source_type",
    "evidence_state",
    "authority_state",
    "consumer_routes",
    "evidence_group",
)


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


def _required_missing(mapping: dict, fields: tuple[str, ...]) -> list[str]:
    return [field for field in fields if not mapping.get(field)]


def build_experience_packet(records: list[dict], context: dict) -> dict:
    """Return a deterministic, scope-bounded advisory experience packet."""
    missing = _required_missing(context, REQUIRED_CONTEXT)
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
    consumer_route = str(context["consumer_route"])
    task_keys = {
        "domains": _values(context["domain"]),
        "problem_types": _values(context["problem_types"]),
        "artifact_ids": _values(context.get("artifact_ids")),
        "failure_classes": _values(context.get("failure_classes")),
    }

    excluded = Counter()
    selected: list[dict] = []

    for record in records:
        record_id = _identity(record)
        if not record_id:
            excluded["IDENTITY_MISSING"] += 1
            continue

        # Lifecycle and validation stay independent. Experience retrieval does
        # not invent lifecycle meanings beyond the current promotion contract.
        if record.get("status") != "PROMOTED":
            excluded["LIFECYCLE_NOT_PROMOTED"] += 1
            continue
        if record.get("validation") != "VALIDATED":
            excluded["VALIDATION_NOT_VALIDATED"] += 1
            continue
        if not record.get("evidence") or not record.get("provenance_preserved"):
            excluded["PROMOTION_PROVENANCE_INCOMPLETE"] += 1
            continue
        if record.get("knowledge_scope") not in allowed_scopes:
            excluded["OUT_OF_SCOPE"] += 1
            continue

        profile = record.get("experience_profile")
        if not isinstance(profile, dict):
            excluded["EXPERIENCE_PROFILE_MISSING"] += 1
            continue
        if _required_missing(profile, REQUIRED_PROFILE):
            excluded["EXPERIENCE_PROFILE_INCOMPLETE"] += 1
            continue
        if str(profile["evidence_state"]) in BLOCKED_EVIDENCE_STATES:
            excluded["EVIDENCE_STATE_BLOCKED"] += 1
            continue
        if _values(profile.get("superseded_by")):
            excluded["SUPERSEDED"] += 1
            continue

        routes = _values(profile["consumer_routes"])
        if consumer_route not in routes and "SHARED" not in routes:
            excluded["CONSUMER_ROUTE_MISMATCH"] += 1
            continue

        reasons: dict[str, list[str]] = {}
        score = 0
        for field, weight in MATCH_WEIGHTS.items():
            overlap = sorted(task_keys[field] & _values(profile.get(field)))
            if overlap:
                reasons[field] = overlap
                score += weight * len(overlap)
        if not reasons:
            excluded["NO_EXPLICIT_STRUCTURAL_MATCH"] += 1
            continue

        selected.append(
            {
                "knowledge_id": record_id,
                "pattern": record.get("pattern"),
                "knowledge_scope": record.get("knowledge_scope"),
                "lifecycle_state": record.get("status"),
                "validation_state": record.get("validation"),
                "evidence": record.get("evidence"),
                "evidence_state": profile["evidence_state"],
                "authority_state": profile["authority_state"],
                "source_identity": profile["source_identity"],
                "source_type": profile["source_type"],
                "evidence_group": str(profile["evidence_group"]),
                "consumer_routes": sorted(routes),
                "applicability_boundaries": sorted(
                    _values(profile.get("applicability_boundaries"))
                ),
                "counterindications": sorted(_values(profile.get("counterindications"))),
                "contradicts": sorted(_values(profile.get("contradicts"))),
                "match_reasons": reasons,
                "score": score,
            }
        )

    # Two promoted projections claiming the same knowledge identity cannot be
    # resolved by retrieval order or source preference.
    identity_counts = Counter(item["knowledge_id"] for item in selected)
    duplicate_ids = sorted(
        identity for identity, count in identity_counts.items() if count > 1
    )
    if duplicate_ids:
        return {
            "status": "HOLD",
            "reason": "DUPLICATE_KNOWLEDGE_IDENTITY",
            "duplicate_knowledge_ids": duplicate_ids,
            "task_id": context["task_id"],
            "execution_identity": context["execution_identity"],
            "experience_items": [],
            "excluded_summary": dict(sorted(excluded.items())),
            "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        }

    selected.sort(key=lambda item: (-item["score"], item["knowledge_id"]))
    selected = selected[:limit]
    selected_ids = {item["knowledge_id"] for item in selected}

    conflicts = sorted(
        {
            tuple(sorted((item["knowledge_id"], target)))
            for item in selected
            for target in item["contradicts"]
            if target in selected_ids and target != item["knowledge_id"]
        }
    )

    evidence_groups: dict[str, list[str]] = defaultdict(list)
    for item in selected:
        evidence_groups[item["evidence_group"]].append(item["knowledge_id"])
    correlated = [
        {
            "evidence_group": group,
            "knowledge_ids": sorted(ids),
            "independence": "CORRELATED_NOT_INDEPENDENT",
        }
        for group, ids in sorted(evidence_groups.items())
        if len(ids) > 1
    ]

    status = "REVIEW_REQUIRED" if conflicts else "READY"
    result = {
        "status": status,
        "task_id": context["task_id"],
        "execution_identity": context["execution_identity"],
        "execution_context": {
            "repository_ref": context.get("repository_ref"),
            "repository_head": context.get("repository_head"),
            "concurrent_work_refs": sorted(_values(context.get("concurrent_work_refs"))),
            "consumer_route": consumer_route,
        },
        "experience_items": selected,
        "conflicts": [list(pair) for pair in conflicts],
        "correlated_evidence_groups": correlated,
        "excluded_summary": dict(sorted(excluded.items())),
        "reasoning_start": [
            "CURRENT_EVIDENCE",
            "APPLICABLE_AUTHORITY",
            "RELEVANT_EXPERIENCE",
            "CONFLICT_AND_CORRELATION_CHECK",
            "ASSUMPTIONS",
            "OPTIONS",
            "TESTABLE_DECISION",
        ],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }
    if conflicts:
        result["reason"] = "CONFLICTING_EXPERIENCE_REQUIRES_CURRENT_EVIDENCE_REVIEW"
    return result
