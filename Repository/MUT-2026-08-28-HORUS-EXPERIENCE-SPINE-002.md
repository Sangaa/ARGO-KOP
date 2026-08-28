# Experience Spine Multi-Instance Reconciliation Mutation Matrix

Transaction ID: `MUT-2026-08-28-HORUS-EXPERIENCE-SPINE-002`
Date: 2026-08-28
Branch: `feature/experience-spine-p375`
Pre-mutation HEAD: `856cc5fa842f0f79c91e79ef20512a0f30b43e51`
Base main: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Status: `PRE-WRITE / OPEN`

## Trigger

Concurrent-work enumeration found that PR #64 independently owns the path
`Repository/REP-043_SESSION_DELTA_2026-08-28_P375.md` with different content.
Open PRs #59, #63, #64, and #65 do not modify the Experience Spine code paths.
Diverged HORUS branches contain transferable lineage/routing concepts but are
not current-main authority and must not be merged wholesale.

## Preservation Boundary

- Do not modify `main`.
- Do not modify Runtime, Engine, Services, REL-009, or any open PR branch.
- Preserve the verified Experience Spine behavior unless a declared row changes it.
- Do not promote the candidate to canonical authority.
- Do not import the divergent HORUS directory/history into this branch.

## Mutation Matrix

| Change ID | Path | Source identity | Action | Expected result | Applied | Verified |
|---|---|---|---|---|---|---|
| MI-001 | `Repository/REP-043_SESSION_DELTA_2026-08-28_P375.md` | blob `3ed26ecea6b74686d320d98c5a32e7af0b460638` | REMOVE | Conflicting numeric session path absent from this branch | N | N |
| MI-002 | `Repository/HORUS_EXPERIENCE_SPINE_SESSION_DELTA_2026-08-28_P375.md` | MI-001 preserved content | ADD | Same checkpoint under collision-resistant path plus reconciliation evidence | N | N |
| MI-003 | `Knowledge/Learning/EXPERIENCE_SPINE_CONTRACT.md` | blob `a0b3972ad6e56553fd053efe141d11ded46295ae` | UPDATE | Add execution identity, lineage/routing and duplicate-identity HOLD rules | N | N |
| MI-004 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | current-main/branch blob to be re-read | UPDATE | Add backward-compatible retrieval profile fields; no lifecycle redefinition | N | N |
| MI-005 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | blob `d01372d563fdfb073c7e6ffa2a9f53331215dcef` | UPDATE | Add execution identity, consumer route and repository/concurrent-ref context | N | N |
| MI-006 | `Knowledge/Learning/experience_spine.py` | blob `6d9e978606f8aed622ff57cfea535641903060bc` | UPDATE | Preserve source lineage, enforce routing, HOLD on duplicate selected identity | N | N |
| MI-007 | `Knowledge/Learning/test_experience_spine.py` | blob `d05517461c96600f1792eea8e7d8e9d49d914092` | UPDATE | Add lineage, routing, duplicate-ID and multi-instance context tests | N | N |

## Pre-Write Validation

- Current main re-read: PASS at `09b216e403fe99a6f1a4a35e3c3038831398f6a3`.
- PR #66 head re-read: PASS at `856cc5fa842f0f79c91e79ef20512a0f30b43e51`.
- Open-PR filename comparison: PASS; only MI-001 is a direct collision.
- Diverged HORUS review: TRANSFERABLE concepts only; no path or authority reuse.
- Unexpected target paths: 0.
- Destructive main mutation: 0.
- Pre-write disposition: `AUTHORIZED FOR DECLARED BRANCH-ONLY MUTATION`.

## Required Closure

`MATRIX PERSISTED → RE-READ SOURCE BLOBS → BUILD CANDIDATE → LOCAL TEST →
ATOMIC COMMIT → BRANCH RE-READ → SHA/DIFF VERIFY → CI → MATRIX RECONCILE → CLOSE`
