"""Correlate a CI commit range with repository impact/relationship evidence.

This tool is intentionally conservative: changed paths are mapped to evidence only
when the current matrix/registry text contains direct path evidence. An unmapped
path is reported as UNMAPPED rather than inferred into a relationship.
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
    """Find direct path mentions, preferring exact path before basename matches."""
    lines = text.splitlines()
    exact = [f"L{i}: {line}" for i, line in enumerate(lines, 1) if path in line]
    if exact:
        return exact[:10]
    basename = Path(path).name
    return [f"L{i}: {line}" for i, line in enumerate(lines, 1) if basename in line][:10]


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
        "schema": "P6-CI-IMPACT-CORRELATION/v1",
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
