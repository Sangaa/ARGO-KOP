"""GOV-014 candidate builder for REP-001.

Builds a candidate from the current repository source and a fixed mutation specification.
It never writes REP-001 directly. The caller receives a complete candidate plus a
reconciliation report and the operation aborts on unexpected preservation drift.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

SOURCE_BLOB_SHA = "067adc90433e5435df220b46882e8c1888fffd2d"
TX_ID = "MUT-2026-08-17-REP001-001"

REPOSITORY_LAYER_OLD = """- `Repository/REP-001_MASTER_INDEX.md`\n- `Repository/REP-002_REPOSITORY_MAP.md`\n- `Repository/REP-003_REPOSITORY_STANDARDS.md`\n- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`\n- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`\n"""
REPOSITORY_LAYER_NEW = """- `Repository/REP-001_MASTER_INDEX.md`\n- `Repository/REP-002_REPOSITORY_MAP.md`\n- `Repository/REP-003_REPOSITORY_STANDARDS.md`\n- `Repository/REP-004_REPOSITORY_NAVIGATION.md`\n- `Repository/REP-005_REPOSITORY_COMPONENTS.md`\n- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`\n- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`\n- `Repository/REP-008_REPOSITORY_BASELINE.md`\n- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`\n"""

INTELLIGENCE_ANCHOR = "The repository contains additional physical domains shown by the current `SYSTEM_MAP.md`, including Knowledge, Memory, Decision, AI, Services, Intelligence, Quality, Projects, Release, Logs, Examples and Future.\n"
INTELLIGENCE_INSERT = INTELLIGENCE_ANCHOR + "\nThe following Intelligence artifacts are directly verified as Approved and Canonical by `Intelligence/_FOLDER_STATUS.md`:\n\n- `Intelligence/INT-001_INTELLIGENCE_LAYER.md`\n- `Intelligence/INT-002_PATTERN_EXTRACTION.md`\n- `Intelligence/INT-003_ANOMALY_DETECTOR.md`\n"

@dataclass(frozen=True)
class Section:
    key: str
    start: int
    end: int
    text: str


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_blob_sha1(text: str) -> str:
    payload = text.encode("utf-8")
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def parse_sections(text: str) -> list[Section]:
    matches = list(re.finditer(r"(?m)^## (.+)$", text))
    sections: list[Section] = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        key = match.group(1).strip()
        sections.append(Section(key=key, start=match.start(), end=end, text=text[match.start():end]))
    return sections


def assert_no_trailing_whitespace(text: str) -> None:
    bad_lines = [line_no for line_no, line in enumerate(text.splitlines(), 1) if line.rstrip() != line]
    if bad_lines:
        raise RuntimeError(f"TRAILING_WHITESPACE_LINES={bad_lines}")


def build_candidate(source: str) -> tuple[str, dict[str, object]]:
    original_blob_sha = git_blob_sha1(source)
    original_sha256 = sha256_text(source)
    if original_blob_sha != SOURCE_BLOB_SHA:
        raise RuntimeError(f"SOURCE_BLOB_SHA_MISMATCH expected={SOURCE_BLOB_SHA} actual={original_blob_sha}")

    if source.count(REPOSITORY_LAYER_OLD) != 1:
        raise RuntimeError("REPOSITORY_LAYER_ANCHOR_COUNT != 1")
    if source.count(INTELLIGENCE_ANCHOR) != 1:
        raise RuntimeError("INTELLIGENCE_ANCHOR_COUNT != 1")

    candidate = source.replace(REPOSITORY_LAYER_OLD, REPOSITORY_LAYER_NEW, 1)
    candidate = candidate.replace(INTELLIGENCE_ANCHOR, INTELLIGENCE_INSERT, 1)
    assert_no_trailing_whitespace(candidate)

    original_sections = parse_sections(source)
    candidate_sections = parse_sections(candidate)
    if [s.key for s in original_sections] != [s.key for s in candidate_sections]:
        raise RuntimeError("SECTION_ORDER_OR_IDENTITY_CHANGED")

    original_map = {s.key: s.text for s in original_sections}
    candidate_map = {s.key: s.text for s in candidate_sections}

    changed_sections = {key for key in original_map if original_map[key] != candidate_map[key]}
    expected_changed = {
        "4. Repository Layer",
        "16. Other Active Repository Domains",
    }
    if changed_sections != expected_changed:
        raise RuntimeError(f"UNEXPECTED_CHANGED_SECTIONS={sorted(changed_sections)}")

    keep_hash_mismatches: list[str] = []
    for key in original_map:
        if key not in expected_changed:
            if sha256_text(original_map[key]) != sha256_text(candidate_map[key]):
                keep_hash_mismatches.append(key)
    if keep_hash_mismatches:
        raise RuntimeError(f"KEEP_HASH_MISMATCHES={keep_hash_mismatches}")

    required = [
        "Repository/REP-004_REPOSITORY_NAVIGATION.md",
        "Repository/REP-005_REPOSITORY_COMPONENTS.md",
        "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
        "Repository/REP-008_REPOSITORY_BASELINE.md",
        "Intelligence/INT-001_INTELLIGENCE_LAYER.md",
        "Intelligence/INT-002_PATTERN_EXTRACTION.md",
        "Intelligence/INT-003_ANOMALY_DETECTOR.md",
    ]
    missing = [item for item in required if item not in candidate]
    if missing:
        raise RuntimeError(f"EXPECTED_CHANGES_MISSING={missing}")

    report = {
        "transaction_id": TX_ID,
        "source_blob_sha": original_blob_sha,
        "source_sha256": original_sha256,
        "candidate_sha256": sha256_text(candidate),
        "section_count_source": len(original_sections),
        "section_count_candidate": len(candidate_sections),
        "changed_sections": sorted(changed_sections),
        "keep_hash_mismatches": keep_hash_mismatches,
        "unexpected_changes": 0,
        "required_changes": len(required),
        "required_changes_present": len(required),
        "trailing_whitespace_lines": [],
        "status": "PRE_COMMIT_VALIDATED",
    }
    return candidate, report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--candidate", type=Path, default=None)
    args = parser.parse_args()

    source_path = args.repo / "Repository" / "REP-001_MASTER_INDEX.md"
    source = source_path.read_text(encoding="utf-8")
    candidate, report = build_candidate(source)

    if args.candidate:
        args.candidate.parent.mkdir(parents=True, exist_ok=True)
        args.candidate.write_text(candidate, encoding="utf-8")

    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
