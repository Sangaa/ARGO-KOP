"""Controlled mutation builder for P4 REL-005 closure.

The builder is deliberately narrow: it accepts the current REP-014 content,
requires the exact expected Git blob SHA, and changes only the REL-005 row and
its current review-cycle reconciliation block. All other content must remain
byte-for-byte identical.
"""
from __future__ import annotations

import hashlib

EXPECTED_TARGET = "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
OLD_ROW = "| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | **REVALIDATION REQUIRED** |"
NEW_ROW = "| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E** |"

SECTION_START = "### REL-005 executable boundary reconciliation\n"
SECTION_END = "### REL-009 executable boundary reconciliation\n"

NEW_SECTION = """### REL-005 executable boundary reconciliation

`REL-005` is now revalidated as a bidirectional relationship using current endpoint authority plus isolated production-runtime evidence.

Current evidence establishes both directions:

```text
ENG-006 → SRV-009 = DOCUMENTED / CONTRACTUAL + EXECUTABLE-VERIFIED IN ISOLATED E2E
SRV-009 → ENG-006 = CONTROLLED MUTATION SERVICE CONSUMED BY ENG-006
```

The Runtime production adapter executed the relationship through the governed write dispatcher and the concrete GitHub repository connector in an isolated non-canonical branch. The successful E2E run created and updated a probe artifact, performed mandatory post-write read-back, emitted governed execution traces, and removed the probe after validation.

Runtime evidence:

- Workflow run: `32021524046`
- Successful HEAD: `702f73b113ce9074ad090ba320867e1dc1eeb3c1`
- Create trace: `TR-6e94cc825acc`
- Update trace: `TR-3d0dd3df6ce3`
- Final persisted SHA before cleanup: `d3287757b644047d6de70a548cf202e34dab1e49`

Therefore the registry may now classify `REL-005` as:

`BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E`

Boundary:

- this promotion applies only to the validated ENG-006 ↔ SRV-009 relationship;
- it does not promote `REL-009` or `REL-061`;
- it does not authorize arbitrary canonical mutation;
- repository-wide graph closure remains open.

Historical P303 evidence is preserved below in repository history; this section supersedes its current-state interpretation for the present review cycle.

"""


def git_blob_sha(content: str) -> str:
    raw = content.encode("utf-8")
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def build_candidate(content: str, expected_blob_sha: str) -> str:
    actual = git_blob_sha(content)
    if actual != expected_blob_sha:
        raise ValueError(f"SOURCE_BLOB_SHA_MISMATCH expected={expected_blob_sha} actual={actual}")

    if content.count(OLD_ROW) != 1:
        raise ValueError("REL005_ROW_EXPECTED_EXACTLY_ONCE")
    if content.count(NEW_ROW) != 0:
        raise ValueError("REL005_ALREADY_PROMOTED")
    if content.count(SECTION_START) != 1 or content.count(SECTION_END) != 1:
        raise ValueError("REL005_SECTION_BOUNDARY_UNSAFE")

    start = content.index(SECTION_START)
    end = content.index(SECTION_END, start)
    if end <= start:
        raise ValueError("REL005_SECTION_ORDER_INVALID")

    candidate = content.replace(OLD_ROW, NEW_ROW, 1)
    start = candidate.index(SECTION_START)
    end = candidate.index(SECTION_END, start)
    candidate = candidate[:start] + NEW_SECTION + candidate[end:]

    if candidate.count(NEW_ROW) != 1:
        raise ValueError("REL005_NEW_ROW_NOT_EXACTLY_ONCE")
    if candidate.count(OLD_ROW) != 0:
        raise ValueError("REL005_OLD_ROW_REMAINS")
    if candidate.count("| REL-009 | RUN-010 | SRV-009 | CONSUMES | **REVALIDATION REQUIRED** |") != 1:
        raise ValueError("REL009_GUARD_FAILED")
    if candidate.count("| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |") != 1:
        raise ValueError("REL061_GUARD_FAILED")

    return candidate
