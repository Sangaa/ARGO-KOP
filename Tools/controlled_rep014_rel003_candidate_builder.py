"""GOV-014 candidate builder for single-edge REP-014 REL-003 correction.

The builder resolves only relationship direction/type representation. It does not
promote semantic state to Verified and does not authorize mutation by itself.
"""
from __future__ import annotations

import hashlib
import re

SOURCE_BLOB_SHA = "d41d84d0de7ca8dbbac8d5cc4facc78e6d187544"
REL_ID = "REL-003"
CURRENT_ROW_RE = re.compile(
    r"(?m)^\| REL-003 \| ENG-004 \| SRV-005 \| PRODUCES \| Revalidated within inspected scope \|$"
)
EXPECTED_ROW = (
    "| REL-003 | SRV-005 | ENG-004 | CONSUMES | "
    "Revalidation Required |"
)


def git_blob_sha1(text: str) -> str:
    payload = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def parse_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^## (.+)$", text))
    sections: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[match.start():end]))
    return sections


def build_candidate(source: str, *, authorization_evidence: str) -> tuple[str, dict[str, object]]:
    actual_sha = git_blob_sha1(source)
    if actual_sha != SOURCE_BLOB_SHA:
        raise RuntimeError(f"SOURCE_BLOB_SHA_MISMATCH expected={SOURCE_BLOB_SHA} actual={actual_sha}")
    if not authorization_evidence.strip():
        raise RuntimeError("AUTHORIZATION_EVIDENCE_REQUIRED")

    matches = CURRENT_ROW_RE.findall(source)
    if len(matches) != 1:
        raise RuntimeError(f"REL003_ROW_COUNT={len(matches)}")

    candidate, count = CURRENT_ROW_RE.subn(EXPECTED_ROW, source, count=1)
    if count != 1:
        raise RuntimeError("REL003_REPLACEMENT_COUNT != 1")
    if source.count("REL-003") != candidate.count("REL-003"):
        raise RuntimeError("REL003_IDENTITY_CHANGED")

    source_sections = parse_sections(source)
    candidate_sections = parse_sections(candidate)
    if [x[0] for x in source_sections] != [x[0] for x in candidate_sections]:
        raise RuntimeError("SECTION_ORDER_OR_IDENTITY_CHANGED")

    source_map = dict(source_sections)
    candidate_map = dict(candidate_sections)
    changed = {key for key in source_map if source_map[key] != candidate_map[key]}
    if changed != {"Relationship Record"}:
        raise RuntimeError(f"UNEXPECTED_CHANGED_SECTIONS={sorted(changed)}")

    keep_mismatches = [
        key
        for key in source_map
        if key != "Relationship Record"
        and hashlib.sha256(source_map[key].encode()).hexdigest()
        != hashlib.sha256(candidate_map[key].encode()).hexdigest()
    ]
    if keep_mismatches:
        raise RuntimeError(f"KEEP_HASH_MISMATCHES={keep_mismatches}")

    return candidate, {
        "transaction_scope": "MUT-2026-08-17-REP014-REL003",
        "relationship_id": REL_ID,
        "source_blob_sha": SOURCE_BLOB_SHA,
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "changed_sections": sorted(changed),
        "keep_hash_mismatches": keep_mismatches,
        "unexpected_changes": 0,
        "target_state": "Revalidation Required",
        "status": "PRE_COMMIT_VALIDATED",
    }
