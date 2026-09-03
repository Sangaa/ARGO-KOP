# P10 Runtime — REP-013 Candidate Inventory Reconciliation — Transaction A

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REP013-INVENTORY-A`
Priority: `10 — Runtime`
State: `CORRECTIVE MATERIAL CANDIDATE / EXACT-HEAD CI PENDING / RESUME-SAFE`
Entry HEAD: `337786f736b21f449acf1e879e5f83f3a67ed00d`
Pre-write HEAD: `15b5b69588efb057fbf93cfc29e8df2cf96ad9a5`
Initial Material HEAD: `1000364723f378111aeba3316bd164c8a65fc39f`
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
| P10-A-01 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | replace only the five non-existent RUN-011..015 inventory filenames with the five exact tracked paths | all non-Runtime content; Runtime scope/non-promotion wording; document identity and ordering | PASS | CONTENT PASS / CI HOLD |
| P10-A-02 | `Quality/Integrity/test_control_plane_runtime_inventory_alignment.py` | UPDATE | include REP-013 in current-path and stale-path assertions | current REP-001/REP-002 guards; physical-file guard; Runtime hold/non-promotion guards | PASS | CONTENT PASS / CI HOLD |
| P10-A-C1-01 | this Matrix | UPDATE IN SAME CHANGE SET | preserve the initial failure and satisfy enforced same-change-set evidence | original queue/gap/scope evidence | PASS | PENDING |
| P10-A-C1-02 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | add explicit current/stale candidate-path boundary without changing the five-file correction | all other REP-013 content and non-exhaustive/non-promotion boundaries | PASS | PENDING |
| P10-A-C1-03 | `Quality/Integrity/test_control_plane_runtime_inventory_alignment.py` | UPDATE | name the expanded REP-001/002/013 coverage accurately | all assertions and failure strength | PASS | PENDING |

## Non-claims

- No Runtime document identity or implementation is renamed or promoted.
- This transaction repairs five known inventory rows only; it does not claim exhaustive Runtime/Prototype inventory, cross-layer closure, executable authority, Phase-1 closure, repository-wide graph completion, Global Connected Baseline closure or Global Integrity PASS.
- Any heterogeneous failure is isolated from this cohort.

Validation:
`pre-write matrix → bounded REP-013 + consumer-guard repair → read-back → targeted tests → exact-head CI → close or HOLD`.

## Preserved first failure and corrective rule

- Initial material Runtime/Integration `33741725724` — SUCCESS.
- Initial material M2 `33741725577` — SUCCESS.
- Initial material Full-Stack `33741725592` — FAILURE at `Enforce Mutation Matrix on current change set` only: `protected_changes=1`, `PROTECTED: Repository/REP-013_REPOSITORY_CONTENT_TREE.md`, `MUTATION_MATRIX_PREFLIGHT=FAIL`.
- The content/test repair itself remains valid; the failure is a transaction-packaging defect.
- Current enforced repository learning is stronger than matrix-before-write alone: a protected target and its applicable Matrix must also be present in the same current change set.
- Corrective packaging therefore changes this Matrix, REP-013 and its guard atomically. It does not revert the inventory correction, weaken enforcement or disguise the failed head.
