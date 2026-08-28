"""Controlled full-content mutation builder for P4 REL-009 registry closure.

The builder accepts the complete current REP-014 text, requires its exact Git
blob SHA, and changes only:

1. the REL-009 registry State cell; and
2. the REL-009 current review-cycle reconciliation block.

Everything else is preserved by construction and guarded by neighboring
canonical relationship rows/section boundaries.
"""
from __future__ import annotations

import hashlib

EXPECTED_TARGET = "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"

OLD_ROW = "| REL-009 | RUN-010 | SRV-009 | CONSUMES | **REVALIDATION REQUIRED** |"
NEW_ROW = (
    "| REL-009 | RUN-010 | SRV-009 | CONSUMES | "
    "**INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL** |"
)

REL005_GUARD = (
    "| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | "
    "**BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E** |"
)
REL061_GUARD = (
    "| REL-061 | GOV-013A | GOV-013 | REFERENCES | "
    "**INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED** |"
)

SECTION_START = "### REL-009 executable boundary reconciliation\n"
SECTION_END = "### REL-061 governance bootstrap relationship\n"

NEW_SECTION = """### REL-009 executable boundary reconciliation

`REL-009` retains its canonical identity and controlled relationship type:

```text
RUN-010 → SRV-009 = CONSUMES
```

Current evidence now supports a bounded intentional-directional disposition:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`

Evidence basis:

- `Runtime/RUN-010_RUNTIME_REFERENCE.md` describes the governed execution relationship ending in `SRV-009 Controlled Mutation` while explicitly stating that the sequence is not a claim that every runtime operation follows that exact path.
- current main contains a pure RUN-010 handoff contract plus an integration-only observation harness that composes the existing governed ENG-006/SRV-009 production adapter;
- the observation preserves execution/task/session/source-trace identity and authorization identity and records an attributable SRV-009-targeted dispatch with post-read verification;
- exact-main Full-Stack and Runtime/Integration CI verify the positive isolated observation and the negative normal connected-spine boundary together;
- the normal connected spine remains simulation-oriented and contains no direct `SRV-009` dispatch;
- provider-backed ENG-006/SRV-009 E2E evidence remains a separate evidence class from the isolated RUN-010 observation.

Directionality boundary:

- no `SRV-009 → RUN-010` dependency is created;
- no reverse dependency is required merely to manufacture graph symmetry;
- this state does not mean every RUN-010 operation invokes SRV-009;
- this state does not convert the normal connected spine to production dispatch;
- repository-wide graph closure is not implied.

Current evidence checkpoints include:

- P3 clean proof merged to main: `a538325bcde36d3a45f19583ca20d72d8f591e0a`;
- P3 exact-main Full-Stack: `33196013636` — SUCCESS;
- P3 exact-main Runtime/Integration: `33196013609` — SUCCESS;
- P4 semantic reconciliation merged to main: `94a9bbb43432f3e098854571130778a498f76299`;
- P4 exact-main Full-Stack: `33196750118` — SUCCESS;
- P4 exact-main Runtime/Integration: `33196750113` — SUCCESS.

Historical records that state executable consumer evidence was absent remain valid for their original checkpoint and are superseded only for current operational interpretation within this bounded relationship scope.

"""


def git_blob_sha(content: str) -> str:
    raw = content.encode("utf-8")
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def build_candidate(content: str, expected_blob_sha: str) -> str:
    actual = git_blob_sha(content)
    if actual != expected_blob_sha:
        raise ValueError(
            f"SOURCE_BLOB_SHA_MISMATCH expected={expected_blob_sha} actual={actual}"
        )

    if content.count(OLD_ROW) != 1:
        raise ValueError("REL009_OLD_ROW_EXPECTED_EXACTLY_ONCE")
    if content.count(NEW_ROW) != 0:
        raise ValueError("REL009_NEW_ROW_ALREADY_PRESENT")
    if content.count(REL005_GUARD) != 1:
        raise ValueError("REL005_PRESERVATION_GUARD_FAILED")
    if content.count(REL061_GUARD) != 1:
        raise ValueError("REL061_PRESERVATION_GUARD_FAILED")
    if content.count(SECTION_START) != 1 or content.count(SECTION_END) != 1:
        raise ValueError("REL009_SECTION_BOUNDARY_UNSAFE")

    source_start = content.index(SECTION_START)
    source_end = content.index(SECTION_END, source_start)
    if source_end <= source_start:
        raise ValueError("REL009_SECTION_ORDER_INVALID")

    prefix_before_row, suffix_after_row = content.split(OLD_ROW, 1)
    candidate = prefix_before_row + NEW_ROW + suffix_after_row

    candidate_start = candidate.index(SECTION_START)
    candidate_end = candidate.index(SECTION_END, candidate_start)
    candidate = candidate[:candidate_start] + NEW_SECTION + candidate[candidate_end:]

    if candidate.count(NEW_ROW) != 1 or candidate.count(OLD_ROW) != 0:
        raise ValueError("REL009_ROW_REPLACEMENT_FAILED")
    if candidate.count(REL005_GUARD) != 1:
        raise ValueError("REL005_CHANGED_UNEXPECTEDLY")
    if candidate.count(REL061_GUARD) != 1:
        raise ValueError("REL061_CHANGED_UNEXPECTEDLY")
    if candidate.count(NEW_SECTION) != 1:
        raise ValueError("REL009_NEW_SECTION_NOT_EXACTLY_ONCE")

    # Everything after the next relationship section boundary must be byte-identical.
    source_tail = content[source_end:]
    candidate_tail = candidate[candidate.index(SECTION_END):]
    if candidate_tail != source_tail:
        raise ValueError("POST_REL009_CONTENT_CHANGED_UNEXPECTEDLY")

    # Everything before the old row must remain byte-identical.
    if not candidate.startswith(prefix_before_row):
        raise ValueError("PRE_REL009_ROW_CONTENT_CHANGED_UNEXPECTEDLY")

    return candidate
