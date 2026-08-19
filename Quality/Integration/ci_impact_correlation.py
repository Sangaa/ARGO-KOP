"""Correlate CI evidence with repository impact without guessing relationships.

P6 distinguishes execution validity from evidence freshness. A successful historical
run is valid execution evidence, but it is not current-HEAD evidence when its SHA
chain is stale. Stale evidence must be classified, not treated as a test failure.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MATRIX = REPO_ROOT / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md"
DEFAULT_REGISTRY = REPO_ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


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
    """Find only exact repository-relative path mentions; never infer by basename."""
    return [
        f"L{i}: {line}"
        for i, line in enumerate(text.splitlines(), 1)
        if path in line
    ][:10]


def correlate_paths(
    paths: Iterable[str], matrix_text: str, registry_text: str
) -> list[dict[str, object]]:
    """Correlate changed paths without guessing relationships."""
    records: list[dict[str, object]] = []
    for path in paths:
        matrix_hits = _evidence_lines(path, matrix_text)
        registry_hits = _evidence_lines(path, registry_text)
        status = "MAPPED" if matrix_hits or registry_hits else "UNMAPPED"
        records.append(
            {
                "path": path,
                "status": status,
                "matrix_evidence": matrix_hits,
                "relationship_evidence": registry_hits,
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
    """Classify each evidence boundary without collapsing distinct failures.

    A successful run whose run SHA differs from the current baseline is valid
    historical execution evidence. A run that is current but whose artifact SHA
    differs is an artifact-integrity failure, not stale execution. Missing identity
    values are invalid evidence rather than an execution result.
    """
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
    records = correlate_paths(paths, matrix, registry)
    unmapped = sum(record["status"] == "UNMAPPED" for record in records)
    if not paths:
        overall = "NO_CHANGES"
    elif unmapped:
        overall = "PARTIAL"
    else:
        overall = "MAPPED"
    return {
        "schema": "P6-CI-IMPACT-CORRELATION/v3",
        "base": base,
        "head": head,
        "changed_path_count": len(paths),
        "mapped_path_count": len(paths) - unmapped,
        "unmapped_path_count": unmapped,
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
