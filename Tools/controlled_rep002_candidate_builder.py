"""GOV-014 controlled candidate builder for REP-002 synchronization."""
from __future__ import annotations

import hashlib
import re

SOURCE_BLOB_SHA = "386308c528cdb80c48b2aad7208753e864728a1f"
TX_ID = "MUT-2026-08-17-REP002-001"

REP_OLD = """- `Repository/REP-001_MASTER_INDEX.md`\n- `Repository/REP-002_REPOSITORY_MAP.md`\n- `Repository/REP-003_REPOSITORY_STANDARDS.md`\n- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`\n- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`\n"""
REP_NEW = """- `Repository/REP-001_MASTER_INDEX.md`\n- `Repository/REP-002_REPOSITORY_MAP.md`\n- `Repository/REP-003_REPOSITORY_STANDARDS.md`\n- `Repository/REP-004_REPOSITORY_NAVIGATION.md`\n- `Repository/REP-005_REPOSITORY_COMPONENTS.md`\n- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`\n- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`\n- `Repository/REP-008_REPOSITORY_BASELINE.md`\n- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`\n"""
GOV_OLD = """- `Governance/GOV-010_GOVERNANCE_MODEL.md`\n- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`\n- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`\n- `Governance/_FOLDER_STATUS.md`\n"""
GOV_NEW = """- `Governance/GOV-010_GOVERNANCE_MODEL.md`\n- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`\n- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`\n- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`\n- `Governance/_FOLDER_STATUS.md`\n"""

def git_blob_sha1(text: str) -> str:
    payload = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()

def parse_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^## (.+)$", text))
    out: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1).strip(), text[m.start():end]))
    return out

def build_candidate(source: str) -> tuple[str, dict[str, object]]:
    actual = git_blob_sha1(source)
    if actual != SOURCE_BLOB_SHA:
        raise RuntimeError(f"SOURCE_BLOB_SHA_MISMATCH expected={SOURCE_BLOB_SHA} actual={actual}")
    if source.count(REP_OLD) != 1:
        raise RuntimeError("REP_REPOSITORY_ANCHOR_COUNT != 1")
    if source.count(GOV_OLD) != 1:
        raise RuntimeError("GOVERNANCE_ANCHOR_COUNT != 1")
    candidate = source.replace(REP_OLD, REP_NEW, 1).replace(GOV_OLD, GOV_NEW, 1)
    trailing = [i for i, line in enumerate(candidate.splitlines(), 1) if line.rstrip() != line]
    if trailing:
        raise RuntimeError(f"TRAILING_WHITESPACE_LINES={trailing}")
    src = dict(parse_sections(source))
    cand = dict(parse_sections(candidate))
    if list(src) != list(cand):
        raise RuntimeError("SECTION_ORDER_OR_IDENTITY_CHANGED")
    changed = {k for k in src if src[k] != cand[k]}
    expected = {"4. Repository Layer", "5. Governance Layer"}
    if changed != expected:
        raise RuntimeError(f"UNEXPECTED_CHANGED_SECTIONS={sorted(changed)}")
    keep = [k for k in src if k not in expected and hashlib.sha256(src[k].encode()).hexdigest() != hashlib.sha256(cand[k].encode()).hexdigest()]
    if keep:
        raise RuntimeError(f"KEEP_HASH_MISMATCHES={keep}")
    required = [
        "Repository/REP-004_REPOSITORY_NAVIGATION.md",
        "Repository/REP-005_REPOSITORY_COMPONENTS.md",
        "Repository/REP-007_REPOSITORY_GOVERNANCE.md",
        "Repository/REP-008_REPOSITORY_BASELINE.md",
        "Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md",
    ]
    missing = [x for x in required if x not in candidate]
    if missing:
        raise RuntimeError(f"EXPECTED_CHANGES_MISSING={missing}")
    return candidate, {
        "transaction_id": TX_ID,
        "source_blob_sha": SOURCE_BLOB_SHA,
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "changed_sections": sorted(changed),
        "keep_hash_mismatches": keep,
        "unexpected_changes": 0,
        "required_changes_present": 5,
        "status": "PRE_COMMIT_VALIDATED",
    }
