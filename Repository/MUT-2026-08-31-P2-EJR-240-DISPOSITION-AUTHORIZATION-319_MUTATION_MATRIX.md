# MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 319-01 | `Repository/MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319.md` | CREATE | evidence-only disposition; retain earlier Memory allocation and classify later root allocation as displacement candidate | N | N |
| 319-02 | EJR-240 member files | KEEP | no rename/delete/reassignment/allocation under disposition lease | Y | Y |
| 319-03 | Priority queue | KEEP | Priority 2 remains OPEN; 317/318 do not promote REP-016 ordering | Y | Y |

## KEEP REQUIREMENT
Preserve both current EJR-240 member files byte-for-byte during this disposition action. Do not allocate a successor, rename, delete, rewrite consumers, change the MEMORY_TO_ROOT baseline, reopen 317/318, or promote Priority 2.

## Pre-write evidence
- Live re-entry HEAD before this action: `e75f2399b6f9c692027ec2a0933c2db3898194db`.
- REP-016 Priority 2: `RELATIONSHIP_VALIDATION / GLOBAL SCOPE OPEN` with closure authority `REP-011/014 + explicit identity decisions`.
- Current deterministic census remains 7/7 because the exact 316→current compare contains no classifier, EJR member, or Memory member changes.
- Current targets: EJR-165, EJR-237, EJR-240, EJR-293, EJR-294, EJR-295, EJR-296.
- EJR-240 census: two distinct members, zero exact-member-path consumers, eight external exact-ID reference paths.
- Memory allocation first appears at `693e9ec40d2a06ced4ebda41d8f94bf6cdb21360` / 2026-08-15T06:00:39Z.
- Root allocation first appears at `2afb2374cc446ffb2e315bc70cb0106a6fe7a5d9` / 2026-08-17T17:48:28Z.
- No evidence reviewed invalidates the earlier Memory allocation.

## Queue-reconstruction learning
Session-local `NEXT` text is not queue authority. A valid bounded side repair or runtime proof may be preserved without promoting REP-016 ordering. After such out-of-order bounded work, HERMUZ must reconstruct the active queue from live REP-016/control-plane authority before selecting the next build target.

Classification: `CANDIDATE REUSABLE LEARNING / CURRENT SESSION EVIDENCE` — no governance promotion is implied by this matrix alone.

## Closure
Close only after the disposition record is created, re-read, and current evidence still supports the earlier Memory allocation as retained identity. The next legal action, if closed, is successor candidate discovery plus a separate complete-history vacancy proof.