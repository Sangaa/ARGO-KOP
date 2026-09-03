# P10 Runtime — REP-013 Candidate Inventory Reconciliation — Transaction A

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REP013-INVENTORY-A`
Priority: `10 — Runtime`
State: `PRE-WRITE / OPEN / RESUME-SAFE`
Entry HEAD: `337786f736b21f449acf1e879e5f83f3a67ed00d`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-011..016`

## Legal queue entry

- Current operational REP-016 addenda close Priorities 2 through 9 for their bounded Phase-1 scopes; the base queue already records Priority 1 closed.
- No later mutation or current evidence establishes a higher-priority reopen.
- Priority 9 Transaction T plus T-C1 is exact-head verified and `CLOSED_FOR_PHASE_1 / RESUME-SAFE`.
- The base queue's first successor is Priority 10 — Runtime; its required entry surfaces exist and are readable: `Runtime/_FOLDER_STATUS.md` plus REP-013, with Runtime authority and REP-011/014 evidence available.
- Runtime is not closed. Its `CROSS-LAYER INTEGRATION HOLD` is the bounded work state to reconcile, not a prohibition on entering the partition.

Decision:
`PRIORITY 10 — RUNTIME = FIRST LEGAL OPEN SUCCESSOR / ENTERED`.

## Verified gap

The current tracked Runtime tree, `Runtime/README.md`, `RUN-010`, REP-001, REP-002 and existing Runtime identity tests agree on these five candidate paths:

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`

REP-013 alone records five different, non-existent filenames for RUN-011..015. This is a current control-plane inventory defect. Existing `test_control_plane_runtime_inventory_alignment.py` checks REP-001/REP-002 but omits REP-013, allowing the drift to remain green.

## Authorized bounded cohort

| Change ID | Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-A-01 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | replace only the five non-existent RUN-011..015 inventory filenames with the five exact tracked paths | all non-Runtime content; Runtime scope/non-promotion wording; document identity and ordering | PASS | PENDING |
| P10-A-02 | `Quality/Integrity/test_control_plane_runtime_inventory_alignment.py` | UPDATE | include REP-013 in current-path and stale-path assertions | current REP-001/REP-002 guards; physical-file guard; Runtime hold/non-promotion guards | PASS | PENDING |

## Non-claims

- No Runtime document identity or implementation is renamed or promoted.
- This transaction repairs five known inventory rows only; it does not claim exhaustive Runtime/Prototype inventory, cross-layer closure, executable authority, Phase-1 closure, repository-wide graph completion, Global Connected Baseline closure or Global Integrity PASS.
- Any heterogeneous failure is isolated from this cohort.

Validation:
`pre-write matrix → bounded REP-013 + consumer-guard repair → read-back → targeted tests → exact-head CI → close or HOLD`.
