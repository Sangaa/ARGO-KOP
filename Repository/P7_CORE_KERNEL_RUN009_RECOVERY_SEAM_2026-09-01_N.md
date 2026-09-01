# Priority 7 — CORE-KERNEL → RUN-009 Recovery Seam — Transaction N

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / VALIDATION-FIRST / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-VALIDATION-N`
Work Lease: `HERMUZ-P7-N-CORE-KERNEL-RUN009-20260901`
Entry HEAD: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
Pre-write Matrix HEAD: `a940b5b526e17517b54669a904e78d87b96e13cf`

## Direct current evidence

`Core/ARGO_KERNEL.md` is the canonical Core/Runtime coordination contract. It explicitly states that recovery follows the applicable governed recovery flow and lists `Runtime/RUN-009_RECOVERY.md` under `Related Authority`.

The same Kernel source explicitly warns that a name appearing in the document does not establish a dependency merely by being listed.

`Runtime/RUN-009_RECOVERY.md` is the canonical Runtime recovery mechanism. It defines repository/authority/dependency validation and safe-resume conditions, but does not directly identify CORE-KERNEL as a reverse dependency, consumer, implementation or governing source.

Current `REP-014` v1.2.12 does not register this pair.

## Validated candidate under test

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

This is a documentary/authority handoff alignment only. N does not claim executable reachability or dependency.

## Prior learning applied

- Transaction E is directly applicable: the same CORE-KERNEL source already proved that explicit Runtime Related Authority can justify a bounded one-way `REFERENCES` relationship while the Kernel dependency warning blocks automatic `DEPENDS_ON` promotion.
- Transactions J/L supply validation-first discipline.
- Transaction M supplies the rule to preserve proven source wording and treat any gate failure as evidence rather than rewriting semantics to pass a test.

## Material unit

N creates only:

1. `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py`
2. this transaction record
3. same-change-set update of the N Mutation Matrix

No Core, Runtime, REP-014, REP-020 or folder-status source mutation occurs in N.

## Non-claims

- no reverse `RUN-009 → CORE-KERNEL` edge;
- no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES` or `GOVERNS` relationship;
- no runtime reachability claim;
- no Core or Runtime certification;
- no Phase-1 closure;
- no Connected Baseline/repository-wide graph closure;
- no Global PASS.

## Candidate verification

Pending exact-head diff/read-back and the four required workflows. If all pass, N may close validation-only and a future fresh recomputation may consider REP-014 reconciliation. N itself does not authorize that future mutation.
