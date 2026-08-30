"""Evidence-only namespace-lineage classifier for H1-only EJR ambiguity groups.

Combines exact-current-path first-seen Git ancestry with journal namespace surface to
expose provenance-direction signals. It does not assign canonical ownership, prove
rename lineage, or authorize repository mutation.
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


def _surface(path: str) -> str:
    if path.startswith("Memory/Engineering_Journal/"):
        return "MEMORY_EJR"
    if path.startswith("EJR/"):
        return "ROOT_EJR"
    return "OTHER"


def _ordered_observations(root: Path, observations: list[dict[str, Any]]) -> tuple[str, list[dict[str, Any]]]:
    commits = [item["first_seen"]["commit"] for item in observations]
    if len(set(commits)) != len(commits):
        return "SAME_FIRST_SEEN_COMMIT", []

    descendant_counts: dict[str, int] = {commit: 0 for commit in commits}
    for index, left in enumerate(commits):
        for right in commits[index + 1:]:
            left_before_right = _is_ancestor(root, left, right)
            right_before_left = _is_ancestor(root, right, left)
            if left_before_right == right_before_left:
                return "DIVERGENT_OR_UNORDERED", []
            if left_before_right:
                descendant_counts[left] += 1
            else:
                descendant_counts[right] += 1

    expected = list(range(len(commits) - 1, -1, -1))
    actual = sorted(descendant_counts.values(), reverse=True)
    if actual != expected:
        return "DIVERGENT_OR_UNORDERED", []

    ordered = sorted(
        observations,
        key=lambda item: descendant_counts[item["first_seen"]["commit"]],
        reverse=True,
    )
    return "TOTAL_ANCESTRY_CHAIN", ordered


def _collapse(surfaces: list[str]) -> list[str]:
    result: list[str] = []
    for surface in surfaces:
        if not result or result[-1] != surface:
            result.append(surface)
    return result


def _classify_sequence(sequence: list[str]) -> str:
    if "OTHER" in sequence:
        return "OTHER_SURFACE_PRESENT"
    collapsed = _collapse(sequence)
    if collapsed == ["ROOT_EJR"]:
        return "SAME_SURFACE_ROOT_EJR"
    if collapsed == ["MEMORY_EJR"]:
        return "SAME_SURFACE_MEMORY_EJR"
    if collapsed == ["MEMORY_EJR", "ROOT_EJR"]:
        return "MEMORY_TO_ROOT_EJR"
    if collapsed == ["ROOT_EJR", "MEMORY_EJR"]:
        return "ROOT_TO_MEMORY_EJR"
    return "MULTI_NAMESPACE_TRANSITION"


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
    class_counts: Counter[str] = Counter()
    surface_counts: Counter[str] = Counter()
    incomplete_groups: list[str] = []

    for document_id in sorted(ambiguous):
        if not document_id.startswith("EJR-"):
            continue
        members = ambiguous[document_id]
        if len(members) < 2:
            continue
        sources = {str(member.get("identity_source")) for member in members}
        if sources != {"FIRST_H1_FALLBACK"}:
            continue

        observations: list[dict[str, Any]] = []
        for member in members:
            path = str(member["path"])
            observations.append({
                "path": path,
                "surface": _surface(path),
                "first_seen": _first_seen(root, path),
            })

        if any(item["first_seen"] is None for item in observations):
            order_state = "MISSING_PATH_HISTORY"
            ordered: list[dict[str, Any]] = []
        else:
            order_state, ordered = _ordered_observations(root, observations)

        if order_state != "TOTAL_ANCESTRY_CHAIN":
            classification = order_state
            sequence: list[str] = []
            collapsed: list[str] = []
            incomplete_groups.append(document_id)
        else:
            sequence = [item["surface"] for item in ordered]
            collapsed = _collapse(sequence)
            classification = _classify_sequence(sequence)
            for surface in sequence:
                surface_counts[surface] += 1

        class_counts[classification] += 1
        groups[document_id] = {
            "classification": classification,
            "order_state": order_state,
            "cardinality": len(members),
            "namespace_sequence": sequence,
            "collapsed_namespace_sequence": collapsed,
            "transition_count": max(len(collapsed) - 1, 0),
            "members_in_first_seen_order": ordered,
        }

    return {
        "history_complete": True,
        "history_scope": "all locally reachable refs",
        "provenance_surface": "exact current path namespace + first-seen ancestry; not ownership or rename-lineage authority",
        "classification_complete": not incomplete_groups,
        "decision": "CLASSIFIED" if not incomplete_groups else "PARTIAL",
        "group_count": len(groups),
        "counts_by_classification": dict(sorted(class_counts.items())),
        "member_counts_by_surface": dict(sorted(surface_counts.items())),
        "incomplete_group_ids": incomplete_groups,
        "groups": groups,
    }


def current_repository_namespace_lineage(root: Path) -> dict[str, Any]:
    return classify_from_report(root, scan(root))


if __name__ == "__main__":
    import json
    import sys

    result = current_repository_namespace_lineage(Path(__file__).resolve().parents[2])
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["history_complete"]:
        sys.exit(4)
    if not result["classification_complete"]:
        sys.exit(3)
