# MUTATION MATRIX — P7 CORE-KERNEL → RUN-009 VALIDATION — N

Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-VALIDATION-N`
Work Lease: `HERMUZ-P7-N-CORE-KERNEL-RUN009-20260901`
Priority: `7 — Core cross-layer validation`
State: `MATERIAL-CANDIDATE / CI-PENDING / LEASE ACTIVE / VALIDATION-FIRST`
Entry HEAD: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
Pre-write Matrix HEAD: `a940b5b526e17517b54669a904e78d87b96e13cf`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Boot-proof and legal action

Current `main`, bootstrap, control-plane, Core status and exact-head CI were re-proven before the first write. Priority 7 remains open. Direct source evidence supports only:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

Transaction E is directly applicable prior learning; J/L validation-first discipline and M failure/test-drift learning are transferable.

## Material change set

| Change ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| N-01 | `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py` | CREATE | Y | PENDING CI |
| N-02 | `Repository/P7_CORE_KERNEL_RUN009_RECOVERY_SEAM_2026-09-01_N.md` | CREATE | Y | PENDING CI |
| N-03 | this Matrix | UPDATE IN SAME CHANGE SET | Y | PENDING CI |

Candidate must be exactly one commit from the pre-write Matrix HEAD and exactly these three paths. Unexpected path expansion must equal `0`.

## Required evidence boundary

The focused regression preserves exact current source assertions:

- Kernel recovery-handoff wording and RUN-009 Related Authority entry;
- Kernel warning that listed names do not themselves establish dependency;
- RUN-009 canonical recovery identity and safe-resume semantics;
- REP-014 absence of this pair during validation-first N;
- prohibition on reverse edge and stronger dependency/consumer/implementation/governance semantics;
- Core status remains cross-layer validation open / certification pending.

## KEEP / non-authority

No mutation to CORE-KERNEL, RUN-009, REP-014, REP-020 or Core status. No executable/dependency promotion. No certification, Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Verification contract

`EXACT-HEAD READ-BACK → DIFF SCOPE = 3 AUTHORIZED PATHS / ONE COMMIT → FOUR REQUIRED WORKFLOWS → LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Failure is preserved and governed under GOV-016; test/source semantics are not weakened to manufacture PASS.
