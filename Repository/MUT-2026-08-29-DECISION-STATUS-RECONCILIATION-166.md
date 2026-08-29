# MUT-2026-08-29 — DECISION STATUS RECONCILIATION — 166

State: PREWRITE / NOT CLOSED
Role: HERMUZ via Room71
Baseline: `a34902b1317bc265d6431b83235c06817dfde1ba`
Scope: Decision folder status construction + DEC-010 stale module-status repair + bounded regression

## Evidence

Current Decision Git tree `d0b5c8b2eba1ba057a96ba1f52c603723beadab0` returned `truncated:false` and contains exactly 22 tracked files with no subdirectories.

The tree contains:
- canonical/navigation document family `DEC-001..DEC-010`;
- authorization/decision contracts;
- Python execution/support artifacts;
- tests.

`Decision/DEC-010_DECISION_INDEX.md` currently lists DEC-001..010 and declares `Module Status: Completed`, while lease 144 established that Decision has no current folder status and cross-layer validation remains open. DEC-010 also retains `Last Updated: YYYY-MM-DD`.

## Intended Mutation

- create `Decision/_FOLDER_STATUS.md` from exact current physical inventory;
- preserve separation between DEC-001..010 document family and support/contracts/tests;
- mark current Decision state `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN`;
- update DEC-010 module status from stale `Completed` to the same bounded current state;
- replace placeholder last-updated date with the actual semantic review date 2026-08-29;
- preserve DEC-010 identity/version/owner;
- add regression preventing future return of unbounded `Completed` while cross-layer holds remain.

## Non-Claims

No global Decision certification, no authority transfer to Decision Memory, no execution proof for every Decision test/artifact, no Core136 mutation, no Room71 JSON rewrite, no Connected Baseline global closure.

## Close Gate

Final status + repaired DEC-010 + regression + finalized Matrix must enter one Git tree/commit, followed by exact read-back and applicable exact-head CI.
