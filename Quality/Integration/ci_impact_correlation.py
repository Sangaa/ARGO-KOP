"""Correlate CI evidence with repository impact without guessing relationships.

P6 evaluates scope before correlation. Execution validity remains independent from
canonical mapping and relationship verification.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MATRIX = REPO_ROOT / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md"
DEFAULT_REGISTRY = REPO_ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
DEFAULT_SCOPE_REGISTRY = REPO_ROOT / "Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md"


def changed_paths(base: str, head: str) -> list[str]:
    """Return changed file paths for a commit range, failing closed on git errors."""
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}..{head}"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def _evidence_lines(path: str, text: str) -> list[str]:
    """Find exact repository-relative path mentions; never infer by basename."""
    return [
        f"L{i}: {line}"
        for i, line in enumerate(text.splitlines(), 1)
        if path in line
    ][:10]


def _parse_scope_registry(text: str) -> list[tuple[str, str]]:
    """Read the canonical eligibility table without embedding policy in code."""
    entries: list[tuple[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] == "Path Class":
            continue
        entries.append((cells[0], cells[1]))
    return entries


def scope_for_path(path: str, scope_registry_text: str) -> str:
    """Resolve eligibility from the canonical registry before correlation.

    The registry is the policy source. An unresolved or unmatched path is never
    treated as an implicit mapping failure.
    """
    entries = _parse_scope_registry(scope_registry_text)
    matches: list[tuple[int, str]] = []
    for pattern, scope in entries:
        if fnmatch.fnmatchcase(path, pattern):
            matches.append((len(pattern), scope))
    if not matches:
        return "UNRESOLVED"
    return max(matches, key=lambda item: item[0])[1]


def correlate_paths(
    paths: Iterable[str],
    matrix_text: str,
    registry_text: str,
    scope_registry_text: str | None = None,
) -> list[dict[str, object]]:
    """Correlate changed paths only after scope/eligibility evaluation."""
    if scope_registry_text is None:
        scope_registry_text = DEFAULT_SCOPE_REGISTRY.read_text(encoding="utf-8")

    records: list[dict[str, object]] = []
    for path in paths:
        eligibility = scope_for_path(path, scope_registry_text)
        matrix_hits = _evidence_lines(path, matrix_text)
        relationship_hits = _evidence_lines(path, registry_text)

        if eligibility == "UNRESOLVED":
            status = "POLICY_UNRESOLVED"
        elif eligibility == "OUT_OF_SCOPE":
            status = "NOT_APPLICABLE"
        elif eligibility == "IN_SCOPE":
            status = "MAPPED" if matrix_hits or relationship_hits else "UNMAPPED"
        else:
            status = "POLICY_UNRESOLVED"

        records.append(
            {
                "path": path,
                "eligibility": eligibility,
                "status": status,
                "matrix_evidence": matrix_hits,
                "relationship_evidence": relationship_hits,
                "promotion": "NO_AUTO_PROMOTION",
            }
        )
    return records


def classify_execution_evidence(
    baseline_sha: str,
    run_sha: str,
    artifact_sha: str,
    execution_passed: bool,
) -> str:
    """Classify execution evidence without promoting semantic authority."""
    if not execution_passed:
        return "EXECUTION_FAILED"
    if not baseline_sha or not run_sha:
        return "IDENTITY_EVIDENCE_MISSING"
    if run_sha != baseline_sha:
        return "VALID_EXECUTION_STALE_BASELINE"
    if not artifact_sha:
        return "ARTIFACT_EVIDENCE_MISSING"
    if artifact_sha != run_sha:
        return "ARTIFACT_IDENTITY_MISMATCH"
    return "VALID_CURRENT_EXECUTION"


def build_report(base: str, head: str) -> dict[str, object]:
    paths = changed_paths(base, head)
    matrix = DEFAULT_MATRIX.read_text(encoding="utf-8")
    registry = DEFAULT_REGISTRY.read_text(encoding="utf-8")
    scope_registry = DEFAULT_SCOPE_REGISTRY.read_text(encoding="utf-8")
    records = correlate_paths(paths, matrix, registry, scope_registry)
    unresolved = sum(record["status"] == "POLICY_UNRESOLVED" for record in records)
    unmapped = sum(record["status"] == "UNMAPPED" for record in records)
    not_applicable = sum(record["status"] == "NOT_APPLICABLE" for record in records)
    if not paths:
        overall = "NO_CHANGES"
    elif unresolved:
        overall = "POLICY_UNRESOLVED"
    elif unmapped:
        overall = "PARTIAL"
    elif not_applicable == len(records):
        overall = "NOT_APPLICABLE"
    else:
        overall = "MAPPED"
    return {
        "schema": "P6-CI-IMPACT-CORRELATION/v4",
        "base": base,
        "head": head,
        "changed_path_count": len(paths),
        "mapped_path_count": sum(record["status"] == "MAPPED" for record in records),
        "unmapped_path_count": unmapped,
        "policy_unresolved_path_count": unresolved,
        "not_applicable_path_count": not_applicable,
        "overall": overall,
        "promotion": "NO_AUTO_PROMOTION",
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("head")
    parser.add_argument("--output", default="ci-impact-correlation.json")
    args = parser.parse_args()

    report = build_report(args.base, args.head)
    output = Path(args.output)
    output.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
