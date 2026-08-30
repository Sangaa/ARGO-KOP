"""Evidence-only chronology classifier for H1-only multi-member EJR ambiguity groups.

Consumes current ambiguity membership from ``internal_document_id_audit`` and uses
complete locally reachable Git history to classify exact-path first-seen ancestry.
Chronology is evidence only: it does not determine canonical ownership, rename
lineage, or authorize repository mutation.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any
import subprocess

from internal_document_id_audit import scan


def _git(root: Path, *args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=root, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False
    )
    if check and completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "git command failed")
    return completed.stdout.strip()


def history_complete(root: Path) -> bool:
    return _git(root, "rev-parse", "--is-shallow-repository").lower() == "false"


def _first_seen(root: Path, path: str) -> dict[str, str] | None:
    output = _git(root, "log", "--all", "--format=%H%x09%cI", "--", path)
    lines = [line for line in output.splitlines() if line.strip()]
    if not lines:
        return None
    commit, committed_at = lines[-1].split("\t", 1)
    return {"commit": commit, "committed_at": committed_at}


def _is_ancestor(root: Path, older: str, newer: str) -> bool:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", older, newer], cwd=root,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
    )
    if completed.returncode == 0:
        return True
    if completed.returncode == 1:
        return False
    raise RuntimeError("unable to determine ancestry")


def _relation(root: Path, left: dict[str, str], right: dict[str, str]) -> str:
    if left["commit"] == right["commit"]:
        return "SAME_FIRST_SEEN_COMMIT"
    if _is_ancestor(root, left["commit"], right["commit"]):
        return "LEFT_FIRST_SEEN_ANCESTOR"
    if _is_ancestor(root, right["commit"], left["commit"]):
        return "RIGHT_FIRST_SEEN_ANCESTOR"
    return "DIVERGENT_OR_UNORDERED"


def _classify_group(root: Path, observations: list[dict[str, Any]]) -> tuple[str, dict[str, int]]:
    pair_counts: Counter[str] = Counter()
    for index, left in enumerate(observations):
        for right in observations[index + 1:]:
            relation = _relation(root, left["first_seen"], right["first_seen"])
            pair_counts[relation] += 1

    if pair_counts.get("DIVERGENT_OR_UNORDERED", 0):
        classification = "DIVERGENT_PARTIAL_ORDER"
    elif pair_counts.get("SAME_FIRST_SEEN_COMMIT", 0):
        classification = "SAME_FIRST_SEEN_COLLISION"
    else:
        classification = "TOTAL_ANCESTRY_CHAIN"
    return classification, dict(sorted(pair_counts.items()))


def classify_from_report(root: Path, report: dict[str, Any]) -> dict[str, Any]:
    root = Path(root)
    if not history_complete(root):
        return {
            "history_complete": False,
            "history_scope": "all locally reachable refs",
            "classification_complete": False,
            "decision": "HISTORY_INCOMPLETE",
            "group_count": 0,
            "groups": {},
        }

    ambiguous = report.get("ambiguous_duplicate_records", {})
    groups: dict[str, Any] = {}
    classification_counts: Counter[str] = Counter()
    cardinality_counts: Counter[int] = Counter()
    incomplete_groups: list[str] = []

    for document_id in sorted(ambiguous):
        if not document_id.startswith("EJR-"):
            continue
        members = ambiguous[document_id]
        if len(members) <= 2:
            continue
        sources = {str(member.get("identity_source")) for member in members}
        if sources != {"FIRST_H1_FALLBACK"}:
            continue

        paths = sorted(str(member["path"]) for member in members)
        observations: list[dict[str, Any]] = []
        for path in paths:
            observations.append({"path": path, "first_seen": _first_seen(root, path)})

        if any(item["first_seen"] is None for item in observations):
            classification = "MISSING_PATH_HISTORY"
            pair_counts: dict[str, int] = {}
            incomplete_groups.append(document_id)
        else:
            classification, pair_counts = _classify_group(root, observations)

        classification_counts[classification] += 1
        cardinality_counts[len(members)] += 1
        groups[document_id] = {
            "classification": classification,
            "cardinality": len(members),
            "pair_counts": pair_counts,
            "members": observations,
        }

    return {
        "history_complete": True,
        "history_scope": "all locally reachable refs",
        "chronology_surface": "exact current path names; not ownership or rename-lineage authority",
        "classification_complete": not incomplete_groups,
        "decision": "CLASSIFIED" if not incomplete_groups else "PARTIAL",
        "group_count": len(groups),
        "counts_by_classification": dict(sorted(classification_counts.items())),
        "counts_by_cardinality": {str(k): cardinality_counts[k] for k in sorted(cardinality_counts)},
        "incomplete_group_ids": incomplete_groups,
        "groups": groups,
    }


def current_repository_chronology(root: Path) -> dict[str, Any]:
    return classify_from_report(root, scan(root))


if __name__ == "__main__":
    import json
    import sys

    result = current_repository_chronology(Path(__file__).resolve().parents[2])
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["history_complete"]:
        sys.exit(4)
    if not result["classification_complete"]:
        sys.exit(3)
