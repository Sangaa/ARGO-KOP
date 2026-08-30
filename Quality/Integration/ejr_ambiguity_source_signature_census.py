"""Evidence-only source-signature census for ambiguous identity groups.

Consumes the member-level observability emitted by ``internal_document_id_audit``.
It does not discover identity, mutate membership, or change any audit gate semantics.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from internal_document_id_audit import scan


def _signature(sources: set[str]) -> str:
    if sources == {"DOCUMENT_ID_FIELD"}:
        return "DOCUMENT_ID_FIELD_ONLY"
    if sources == {"FIRST_H1_FALLBACK"}:
        return "FIRST_H1_FALLBACK_ONLY"
    if sources == {"DOCUMENT_ID_FIELD", "FIRST_H1_FALLBACK"}:
        return "MIXED"
    return "OTHER:" + "+".join(sorted(sources))


def summarize(report: dict[str, Any]) -> dict[str, Any]:
    groups = report.get("ambiguous_duplicate_records", {})
    details: dict[str, dict[str, Any]] = {}
    signature_counts: Counter[str] = Counter()
    cardinality_counts: Counter[str] = Counter()
    ejr_signature_counts: Counter[str] = Counter()
    ejr_cardinality_counts: Counter[str] = Counter()
    ejr_group_ids: list[str] = []

    for document_id in sorted(groups):
        members = groups[document_id]
        sources = {str(member.get("identity_source", "UNKNOWN")) for member in members}
        signature = _signature(sources)
        cardinality = len(members)
        source_counts = Counter(str(member.get("identity_source", "UNKNOWN")) for member in members)

        details[document_id] = {
            "signature": signature,
            "cardinality": cardinality,
            "source_counts": dict(sorted(source_counts.items())),
        }
        signature_counts[signature] += 1
        cardinality_counts[str(cardinality)] += 1

        if document_id.startswith("EJR-"):
            ejr_group_ids.append(document_id)
            ejr_signature_counts[signature] += 1
            ejr_cardinality_counts[str(cardinality)] += 1

    return {
        "total_ambiguous_groups": len(details),
        "counts_by_signature": dict(sorted(signature_counts.items())),
        "counts_by_cardinality": dict(sorted(cardinality_counts.items(), key=lambda item: int(item[0]))),
        "ejr": {
            "group_count": len(ejr_group_ids),
            "group_ids": ejr_group_ids,
            "counts_by_signature": dict(sorted(ejr_signature_counts.items())),
            "counts_by_cardinality": dict(
                sorted(ejr_cardinality_counts.items(), key=lambda item: int(item[0]))
            ),
        },
        "groups": details,
    }


def current_repository_census(root: Path) -> dict[str, Any]:
    return summarize(scan(root))


if __name__ == "__main__":
    import json

    print(
        json.dumps(
            current_repository_census(Path(__file__).resolve().parents[2]),
            indent=2,
            sort_keys=True,
        )
    )
