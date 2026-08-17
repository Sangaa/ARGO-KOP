"""GOV-014 transaction 002 candidate builder for REP-001."""
from __future__ import annotations

import hashlib
import re

SOURCE_BLOB_SHA = "2093074e3cde57a3cb9d1d51140598279ca390a7"
TX_ID = "MUT-2026-08-17-REP001-002"

GOVERNANCE_OLD = """- `Governance/GOV-010_GOVERNANCE_MODEL.md`\n- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`\n- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`\n- `Governance/_FOLDER_STATUS.md`\n"""
GOVERNANCE_NEW = """- `Governance/GOV-010_GOVERNANCE_MODEL.md`\n- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`\n- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`\n- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`\n- `Governance/_FOLDER_STATUS.md`\n"""


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


def build_candidate(source: str) -> tuple[str, dict[str, object]]:
    if git_blob_sha1(source) != SOURCE_BLOB_SHA:
        raise RuntimeError(
            f"SOURCE_BLOB_SHA_MISMATCH expected={SOURCE_BLOB_SHA} actual={git_blob_sha1(source)}"
        )
    if source.count(GOVERNANCE_OLD) != 1:
        raise RuntimeError("GOVERNANCE_ANCHOR_COUNT != 1")
    candidate = source.replace(GOVERNANCE_OLD, GOVERNANCE_NEW, 1)
    trailing = [n for n, line in enumerate(candidate.splitlines(), 1) if line.rstrip() != line]
    if trailing:
        raise RuntimeError(f"TRAILING_WHITESPACE_LINES={trailing}")

    source_sections = parse_sections(source)
    candidate_sections = parse_sections(candidate)
    if [x[0] for x in source_sections] != [x[0] for x in candidate_sections]:
        raise RuntimeError("SECTION_ORDER_OR_IDENTITY_CHANGED")

    source_map = dict(source_sections)
    candidate_map = dict(candidate_sections)
    changed = {k for k in source_map if source_map[k] != candidate_map[k]}
    if changed != {"5. Governance Layer"}:
        raise RuntimeError(f"UNEXPECTED_CHANGED_SECTIONS={sorted(changed)}")

    keep_mismatches = [
        k for k in source_map
        if k != "5. Governance Layer"
        and hashlib.sha256(source_map[k].encode()).hexdigest()
        != hashlib.sha256(candidate_map[k].encode()).hexdigest()
    ]
    if keep_mismatches:
        raise RuntimeError(f"KEEP_HASH_MISMATCHES={keep_mismatches}")

    required = "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md"
    if required not in candidate:
        raise RuntimeError("GOV014_EXPECTED_ENTRY_MISSING")

    return candidate, {
        "transaction_id": TX_ID,
        "source_blob_sha": SOURCE_BLOB_SHA,
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "section_count_source": len(source_sections),
        "section_count_candidate": len(candidate_sections),
        "changed_sections": sorted(changed),
        "keep_hash_mismatches": keep_mismatches,
        "unexpected_changes": 0,
        "required_changes_present": 1,
        "status": "PRE_COMMIT_VALIDATED",
    }
