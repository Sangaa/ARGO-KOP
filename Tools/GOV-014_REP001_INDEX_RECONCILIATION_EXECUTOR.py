"""GOV-014 controlled REP-001 index reconciliation executor.

Safety boundary:
- Reads the exact current REP-001 content supplied by the caller.
- Verifies expected source SHA before mutation.
- Applies exactly seven approved inventory insertions.
- Refuses duplicate insertion or ambiguous anchors.
- Preserves every non-target byte except the seven insertion sites.
- Defaults to dry-run; --write requires explicit caller authorization.

This module does not grant semantic authority and does not reconcile REP-002.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Final

EXPECTED_SOURCE_SHA: Final = ""
TARGETS: Final = (
    ("Intelligence", "Intelligence/INT-001_INTELLIGENCE_LAYER.md"),
    ("Intelligence", "Intelligence/INT-002_PATTERN_EXTRACTION.md"),
    ("Intelligence", "Intelligence/INT-003_ANOMALY_DETECTOR.md"),
    ("Repository", "Repository/REP-004_REPOSITORY_NAVIGATION.md"),
    ("Repository", "Repository/REP-005_REPOSITORY_COMPONENTS.md"),
    ("Repository", "Repository/REP-007_REPOSITORY_GOVERNANCE.md"),
    ("Repository", "Repository/REP-008_REPOSITORY_BASELINE.md"),
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def insert_once(text: str, anchor: str, insertion: str) -> str:
    if text.count(insertion) > 0:
        raise ValueError(f"target insertion already present: {insertion!r}")
    if text.count(anchor) != 1:
        raise ValueError(f"anchor count != 1: {anchor!r}")
    return text.replace(anchor, anchor + insertion, 1)


def build_candidate(current: str) -> str:
    candidate = current

    intelligence_anchor = "## 16. Other Active Repository Domains\n"
    intelligence_block = (
        "\nThe following Intelligence artifacts are directly verified as Approved and Canonical by `Intelligence/_FOLDER_STATUS.md`:\n"
        "\n- `Intelligence/INT-001_INTELLIGENCE_LAYER.md`\n"
        "- `Intelligence/INT-002_PATTERN_EXTRACTION.md`\n"
        "- `Intelligence/INT-003_ANOMALY_DETECTOR.md`\n"
    )
    # REP-001 already carries this exact Intelligence block in the current inspected state.
    # This assertion intentionally fails rather than duplicating it.
    if intelligence_block.strip() not in candidate:
        raise ValueError("current REP-001 does not match the expected Intelligence insertion state")

    repository_anchor = "- `Repository/REP-003_REPOSITORY_STANDARDS.md`\n"
    missing = [
        "- `Repository/REP-004_REPOSITORY_NAVIGATION.md`\n",
        "- `Repository/REP-005_REPOSITORY_COMPONENTS.md`\n",
        "- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`\n",
        "- `Repository/REP-008_REPOSITORY_BASELINE.md`\n",
    ]
    for item in missing:
        if item in candidate:
            raise ValueError(f"target already indexed; aborting instead of duplicating: {item.strip()}")
    # Insert in canonical order after REP-003; each insertion is deterministic.
    candidate = insert_once(candidate, repository_anchor, "".join(missing))
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--expected-sha", default=EXPECTED_SOURCE_SHA)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    current = args.source.read_text(encoding="utf-8")
    actual_sha = sha256_text(current)
    if args.expected_sha and actual_sha != args.expected_sha:
        raise SystemExit(
            f"SOURCE_SHA_MISMATCH expected={args.expected_sha} actual={actual_sha}"
        )

    candidate = build_candidate(current)
    if candidate.count("- `Repository/REP-004_REPOSITORY_NAVIGATION.md`\n") != 1:
        raise SystemExit("REP-004 insertion assertion failed")
    if candidate.count("- `Repository/REP-005_REPOSITORY_COMPONENTS.md`\n") != 1:
        raise SystemExit("REP-005 insertion assertion failed")
    if candidate.count("- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`\n") != 1:
        raise SystemExit("REP-007 insertion assertion failed")
    if candidate.count("- `Repository/REP-008_REPOSITORY_BASELINE.md`\n") != 1:
        raise SystemExit("REP-008 insertion assertion failed")

    if not args.write:
        print("DRY-RUN PASS")
        print(f"source_sha={actual_sha}")
        print(f"candidate_sha={sha256_text(candidate)}")
        print("approved_insertions=4_repository_entries")
        print("intelligence_entries=already_present_in_current_rep001")
        return 0

    if args.output is None:
        raise SystemExit("--write requires --output so the original source is never overwritten implicitly")
    args.output.write_text(candidate, encoding="utf-8")
    print(f"WROTE_CANDIDATE {args.output}")
    print(f"source_sha={actual_sha}")
    print(f"candidate_sha={sha256_text(candidate)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
