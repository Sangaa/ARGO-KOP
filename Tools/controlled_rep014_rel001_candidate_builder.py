"""GOV-014 candidate builder scaffold for single-edge REP-014 mutation.

This builder does not decide semantic authority. A caller must supply an
explicitly authorized target state and evidence. The builder only enforces
source identity, exact single-row scope, section preservation, and candidate
validation before any future governed commit.
"""
from __future__ import annotations

import hashlib
import re

SOURCE_BLOB_SHA = "d41d84d0de7ca8dbbac8d5cc4facc78e6d187544"
REL_ID = "REL-001"

CURRENT_ROW_RE = re.compile(
    r"(?m)^\| REL-001 \| SPEC-001-KNOWLEDGE-ORGANIZATION \| MOD-001 \| DEPENDS_ON \| ([^|]+?) \|$"
)

ALLOWED_TARGET_STATES = {
    "Proposed",
    "Verified",
    "Revalidation Required",
    "Closed",
    "Rejected",
}


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


def build_candidate(
    source: str,
    *,
    target_state: str,
    authorization_evidence: str,
) -> tuple[str, dict[str, object]]:
    actual_sha = git_blob_sha1(source)
    if actual_sha != SOURCE_BLOB_SHA:
        raise RuntimeError(f"SOURCE_BLOB_SHA_MISMATCH expected={SOURCE_BLOB_SHA} actual={actual_sha}")
    if target_state not in ALLOWED_TARGET_STATES:
        raise RuntimeError(f"UNCONTROLLED_TARGET_STATE={target_state}")
    if not authorization_evidence.strip():
        raise RuntimeError("AUTHORIZATION_EVIDENCE_REQUIRED")

    matches = CURRENT_ROW_RE.findall(source)
    if len(matches) != 1:
        raise RuntimeError(f"REL001_ROW_COUNT={len(matches)}")

    current_state = matches[0].strip()
    if current_state == target_state:
        raise RuntimeError("NO_OP_TARGET_STATE")

    candidate, count = CURRENT_ROW_RE.subn(
        f"| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | {target_state} |",
        source,
        count=1,
    )
    if count != 1:
        raise RuntimeError("REL001_REPLACEMENT_COUNT != 1")

    if source.count("REL-001") != candidate.count("REL-001"):
        raise RuntimeError("REL001_IDENTITY_CHANGED")

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
        "transaction_scope": "MUT-2026-08-17-REP014-REL001",
        "relationship_id": REL_ID,
        "source_blob_sha": SOURCE_BLOB_SHA,
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "current_state": current_state,
        "target_state": target_state,
        "changed_sections": sorted(changed),
        "keep_hash_mismatches": keep_mismatches,
        "unexpected_changes": 0,
        "authorization_evidence_recorded": True,
        "status": "PRE_COMMIT_VALIDATED",
    }
