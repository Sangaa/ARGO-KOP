# MUTATION MATRIX — P7 CORE-KERNEL → RUN-009 REL-070 RECONCILIATION — O

Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-REL070-O`
Work Lease: `HERMUZ-P7-O-REL070-20260901`
Priority: `7 — Core cross-layer validation / relationship reconciliation`
State: `PRE-WRITE / LEASE ACTIVE`
Entry HEAD: `fba9db310c17f3e3745db7062ee16a32b43182b2`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Re-entry proof

- Live `main` independently rediscovered at `fba9db310c17f3e3745db7062ee16a32b43182b2` immediately before this write.
- Transaction N is closed/resume-safe and its closure HEAD passed all four required workflows.
- `REP-014` is live at v1.2.12, ending at REL-069, and has no CORE-KERNEL→RUN-009 row.
- `Core/_FOLDER_STATUS.md` is v1.3.9 and still requires REP-014 reconciliation where evidence requires while retaining `CROSS-LAYER VALIDATION OPEN` and pending Folder Certification.
- Current control-plane manifest binds REP-014 v1.2.12 and preserves Phase 1 OPEN / Integrity HOLD / Global PASS NOT CLAIMED.

## Highest-value legal action

N directly and exact-head-CI validates only:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

Because the active Core status explicitly requires relationship reconciliation where evidence requires, leaving a directly proven bounded seam absent from REP-014 would leave the local validation/registry surfaces inconsistent. O therefore synchronizes N's proven seam before unrelated Core exploration.

## Prior-learning classification

- Transaction N CORE-KERNEL→RUN-009 validation — `DIRECTLY APPLICABLE`.
- Transaction K ARC-006→CORE-003 registry reconciliation — `DIRECTLY APPLICABLE` synchronization pattern.
- Transaction M CORE-003↔ARC-011 reconciliation — `DIRECTLY APPLICABLE` manifest/status/test synchronization pattern.
- Transaction E CORE-KERNEL→RUN-001 — `DIRECTLY APPLICABLE` semantic precedent.
- M/R1 assertion-drift recovery — `DIRECTLY APPLICABLE`: preserve N's already-proven source assertions exactly; change only the registry expectation.
- Historical broad runtime coupling assumptions — `STALE / NON-AUTHORITY` for this bounded seam.

## Authorized atomic material change set

Exactly six paths after this pre-write Matrix:

1. `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
   - v1.2.12 → v1.2.13;
   - append exactly `REL-070 | CORE-KERNEL | RUN-009 | REFERENCES` with bounded one-way/non-dependency state;
   - add bounded evidence text without unrelated registry cleanup.
2. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
   - synchronize REP-014 row to v1.2.13;
   - refresh current binding to O while preserving all open/hold boundaries.
3. `Core/_FOLDER_STATUS.md`
   - v1.3.9 → v1.3.10;
   - add the registered CORE-KERNEL→RUN-009 seam to current bounded evidence;
   - preserve CROSS-LAYER VALIDATION OPEN and Folder Certification pending.
4. `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py`
   - preserve N's exact source assertions;
   - replace validation-first absence with exact REL-070 registration assertion and uniqueness check;
   - preserve all forbidden stronger/reverse semantics.
5. `Repository/P7_CORE_KERNEL_RUN009_REL070_RECONCILIATION_2026-09-01_O.md`
   - transaction evidence.
6. This Matrix — rebound in the same atomic material change set.

## KEEP / non-authority

- No mutation to `Core/ARGO_KERNEL.md`.
- No mutation to `Runtime/RUN-009_RECOVERY.md`.
- No reverse RUN-009→CORE-KERNEL relationship.
- No DEPENDS_ON, IMPLEMENTS, CONSUMES, GOVERNS or executable-reachability promotion.
- No unrelated REP-014 row changes.
- No Core or Runtime certification.
- No Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Verification contract

`PRE-WRITE MATRIX → ONE ATOMIC SIX-PATH MATERIAL COMMIT → EXACT-HEAD READ-BACK → DIFF/REGISTRY PRESERVATION CHECK → FOUR REQUIRED WORKFLOWS → LEARNING ASSESSMENT → LEASE CLOSE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Unexpected path expansion, main divergence, failed required gate, source contradiction, duplicate/incorrect relation registration or semantic overpromotion stops O and is preserved as evidence under GOV-016.
