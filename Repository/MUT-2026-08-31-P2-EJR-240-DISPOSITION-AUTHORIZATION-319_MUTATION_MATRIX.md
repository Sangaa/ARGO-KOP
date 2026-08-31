# MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 319-01 | `Repository/MUT-2026-08-31-P2-EJR-240-DISPOSITION-AUTHORIZATION-319.md` | CREATE | evidence-only disposition; retain earlier Memory allocation and classify later root allocation as displacement candidate | Y | Y |
| 319-02 | EJR-240 member files | KEEP | no rename/delete/reassignment/allocation under disposition lease | Y | Y |
| 319-03 | Priority queue | KEEP | Priority 2 remains OPEN; 317/318 do not promote REP-016 ordering | Y | Y |

## KEEP REQUIREMENT
Both current EJR-240 member files were preserved byte-for-byte during disposition. No successor was allocated; no rename/delete/consumer rewrite/baseline change occurred; 317/318 were not reopened; Priority 2 was not promoted.

## Execution Evidence
- Re-entry authority: REP-016 current queue keeps Priority 2 `RELATIONSHIP_VALIDATION / GLOBAL SCOPE OPEN`.
- Current deterministic cohort: 7 groups; 316→re-entry exact compare contains no classifier or EJR/Memory member changes.
- EJR-240 current census: 2 distinct members, zero exact-member-path consumers, eight external exact-ID reference paths.
- Earlier Memory allocation: `693e9ec40d2a06ced4ebda41d8f94bf6cdb21360` / 2026-08-15T06:00:39Z.
- Later root allocation: `2afb2374cc446ffb2e315bc70cb0106a6fe7a5d9` / 2026-08-17T17:48:28Z.
- Lease319 was created and re-read successfully at current main.

## Queue-reconstruction learning
Session-local `NEXT` text is not queue authority. A valid bounded side repair or runtime proof may be preserved without promoting REP-016 ordering. After such out-of-order bounded work, HERMUZ must reconstruct the active queue from live REP-016/control-plane authority before selecting the next build target.

Classification: `CANDIDATE REUSABLE LEARNING / CURRENT SESSION EVIDENCE`; no governance promotion.

## Closure
PASS. EJR-240 disposition is explicitly authorized: retain the earlier Memory allocation; later root record is the bounded displacement candidate. Next legal action is successor candidate discovery plus separate complete-history vacancy proof. Priority 2 remains OPEN.