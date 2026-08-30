"""Evidence-only chronology classifier for H1-only two-member EJR ambiguity groups.

This module consumes current ambiguity membership from ``internal_document_id_audit``
and uses complete locally reachable Git history to classify exact-path chronology.
Chronology is evidence only: it does not determine canonical ownership and performs
no repository mutation.
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


def _pair_relation(root: Path, left: dict[str, str], right: dict[str, str]) -> str:
    if left["commit"] == right["commit"]:
        return "SAME_FIRST_SEEN_COMMIT"
    if _is_ancestor(root, left["commit"], right["commit"]):
        return "LEFT_FIRST_SEEN_ANCESTOR"
    if _is_ancestor(root, right["commit"], left["commit"]):
        return "RIGHT_FIRST_SEEN_ANCESTOR"
    return "DIVERGENT_OR_UNORDERED"


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
    relation_counts: Counter[str] = Counter()
    incomplete_groups: list[str] = []

    for document_id in sorted(ambiguous):
        if not document_id.startswith("EJR-"):
            continue
        members = ambiguous[document_id]
        if len(members) != 2:
            continue
        sources = {str(member.get("identity_source")) for member in members}
        if sources != {"FIRST_H1_FALLBACK"}:
            continue

        paths = sorted(str(member["path"]) for member in members)
        observations = []
        for path in paths:
            first = _first_seen(root, path)
            observations.append({"path": path, "first_seen": first})

        if any(item["first_seen"] is None for item in observations):
            relation = "MISSING_PATH_HISTORY"
            incomplete_groups.append(document_id)
        else:
            relation = _pair_relation(
                root, observations[0]["first_seen"], observations[1]["first_seen"]
            )
        relation_counts[relation] += 1
        groups[document_id] = {"relation": relation, "members": observations}

    return {
        "history_complete": True,
        "history_scope": "all locally reachable refs",
        "chronology_surface": "exact current path names; not ownership or rename-lineage authority",
        "classification_complete": not incomplete_groups,
        "decision": "CLASSIFIED" if not incomplete_groups else "PARTIAL",
        "group_count": len(groups),
        "counts_by_relation": dict(sorted(relation_counts.items())),
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
