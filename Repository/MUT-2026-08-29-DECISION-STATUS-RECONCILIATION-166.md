# MUT-2026-08-29 — DECISION STATUS RECONCILIATION — 166

State: FINALIZED / AWAITING EXACT-HEAD VERIFICATION
Role: HERMUZ via Room71
Prewrite baseline: `a34902b1317bc265d6431b83235c06817dfde1ba`
Prewrite commit: `cd06d506e73f15c2056080ef8f1f3edd13be1f3b`

## Final Change

- create `Decision/_FOLDER_STATUS.md` from exact recursive Git-tree evidence (`truncated:false`, 22 tracked files, no subdirectories);
- preserve DEC-001..010 as the Decision document/navigation family while separately representing boundary contracts, executable/support artifacts and tests;
- update DEC-010 from stale `Module Status: Completed` to `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN`;
- replace DEC-010 placeholder `Last Updated: YYYY-MM-DD` with the actual semantic-review date `2026-08-29`;
- preserve DEC-010 Document ID, Version and Owner;
- preserve the Decision-versus-Decision-Memory authority boundary established in lease 144;
- add a bounded regression in the same final change set.

## Authority / Claim Boundary

`EXACT PHYSICAL INVENTORY != DECISION DOMAIN CERTIFICATION`

`DECISION_MEMORY != DECISION AUTHORITY`

`TEST PRESENCE != TEST EXECUTION`

Cross-layer, consumer and global Connected Baseline validation remain open.

## Regression

`Quality/Integrity/test_decision_folder_status_reconciliation.py` guards:
- current Decision physical inventory representation;
- 22-file exact-tree count;
- bounded Integrity Hold language;
- Decision-Memory authority separation;
- removal of stale `Completed` and placeholder date from DEC-010.

## Close Gate

Final state becomes `CLOSED / EXECUTION-VERIFIED` only after status + DEC-010 + regression + this Matrix enter one final Git tree/commit, exact read-back succeeds, and applicable exact-head CI succeeds.
