# Experience Spine Multi-Instance Reconciliation Mutation Matrix

Transaction ID: `MUT-2026-08-28-HORUS-EXPERIENCE-SPINE-002`
Date: 2026-08-28
Branch: `feature/experience-spine-p375`
Pre-mutation HEAD: `856cc5fa842f0f79c91e79ef20512a0f30b43e51`
Matrix persistence commit: `6aaf42d42ddb53858044e650b25819e74986cefb`
Base main: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Status: `IMPLEMENTATION WRITTEN / READ-BACK PASS / CI COVERAGE GAP IDENTIFIED / MI-008 PRE-WRITE`

## Trigger

Concurrent-work enumeration found that PR #64 independently owns the path `Repository/REP-043_SESSION_DELTA_2026-08-28_P375.md` with different content. Open PRs #59, #63, #64, and #65 do not modify the Experience Spine code paths. Diverged HORUS branches contain transferable lineage/routing concepts but are not current-main authority and must not be merged wholesale.

## Preservation Boundary

- Do not modify `main`.
- Do not modify Runtime, Engine, Services, REL-009, or any open PR branch.
- Preserve verified Experience Spine behavior unless a declared row changes it.
- Do not promote the candidate to canonical authority.
- Do not import the divergent HORUS directory/history into this branch.

## Mutation Matrix

| Change ID | Path | Source identity | Action | Expected result | Applied | Verified |
|---|---|---|---|---|---|---|
| MI-001 | `Repository/REP-043_SESSION_DELTA_2026-08-28_P375.md` | blob `3ed26ecea6b74686d320d98c5a32e7af0b460638` | REMOVE | Conflicting numeric session path absent from this branch | Y | PENDING BRANCH READ-BACK |
| MI-002 | `Repository/HORUS_EXPERIENCE_SPINE_SESSION_DELTA_2026-08-28_P375.md` | MI-001 preserved content | ADD | Same checkpoint under collision-resistant path plus reconciliation evidence | Y | PENDING BRANCH READ-BACK |
| MI-003 | `Knowledge/Learning/EXPERIENCE_SPINE_CONTRACT.md` | blob `a0b3972ad6e56553fd053efe141d11ded46295ae` | UPDATE | Add execution identity, lineage/routing and duplicate-identity HOLD rules | Y | PENDING BRANCH READ-BACK |
| MI-004 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | blob `92a6338c35af14594dabcc9bf71cbf1c0b28ffab` | UPDATE | Add backward-compatible retrieval profile fields; no lifecycle redefinition | Y | PENDING BRANCH READ-BACK |
| MI-005 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | blob `d01372d563fdfb073c7e6ffa2a9f53331215dcef` | UPDATE | Add execution identity, consumer route and repository/concurrent-ref context | Y | PENDING BRANCH READ-BACK |
| MI-006 | `Knowledge/Learning/experience_spine.py` | blob `6d9e978606f8aed622ff57cfea535641903060bc` | UPDATE | Preserve source lineage, enforce routing, HOLD on duplicate selected identity | Y | LOCAL TEST PASS / BRANCH READ-BACK PENDING |
| MI-007 | `Knowledge/Learning/test_experience_spine.py` | blob `d05517461c96600f1792eea8e7d8e9d49d914092` | UPDATE | Add lineage, routing, duplicate-ID and multi-instance context tests | Y | 8 FOCUSED TESTS PASS / CI PENDING |
| MI-008 | `Quality/Integration/test_experience_spine_integration.py` | new unique path | ADD | Exercise ready packet and duplicate-identity HOLD in existing integration CI suite | N | N |

## Pre-Write Validation

- Current main re-read: PASS at `09b216e403fe99a6f1a4a35e3c3038831398f6a3`.
- PR #66 head re-read: PASS before matrix at `856cc5fa842f0f79c91e79ef20512a0f30b43e51`.
- Matrix persisted and re-read at `6aaf42d42ddb53858044e650b25819e74986cefb`.
- Open-PR filename comparison: PASS; only MI-001 is a direct collision.
- Diverged HORUS review: TRANSFERABLE concepts only; no path or authority reuse.
- Unexpected target paths: 0.
- Destructive main mutation: 0.

## Local Verification

- Experience Spine focused tests: `8 PASSED`.
- Adjacent retrieval regression tests: `4 PASSED`.
- Combined assertion tests: `12 PASSED`.
- Python compilation: `PASS`.

## Post-Write Read-Back / CI Coverage Finding

- Implementation commit: `0279f5c81c69ca6708811676271f9bc1565836dd`.
- All seven intended implementation blobs matched after GitHub read-back.
- The conflicting numeric session path returned `NOT_FOUND` on the branch.
- PR #66 vs PR #64 exact changed-file overlap after correction: `0`.
- Full-Stack run `33195645857`: `SUCCESS`.
- Runtime/Integration run `33195645852`: `SUCCESS`.
- Workflow command inspection proved that neither workflow directly collects `Knowledge/Learning/test_experience_spine.py`; the green runs therefore verify repository compatibility, not focused Experience Spine execution.
- MI-008 is added before its write to close that explicit CI coverage gap through the existing `Quality/Integration` pytest suite without workflow mutation.

## Required Closure

`PERSIST MI-008 ROW → ADD INTEGRATION BRIDGE → BRANCH RE-READ → EXACT-HEAD CI → MATRIX RECONCILE → CLOSE`

