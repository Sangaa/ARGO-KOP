# MUTATION MATRIX — P7 CORE-KERNEL → RUN-009 VALIDATION — N

Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-VALIDATION-N`
Work Lease: `HERMUZ-P7-N-CORE-KERNEL-RUN009-20260901`
Priority: `7 — Core cross-layer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
Pre-write Matrix HEAD: `a940b5b526e17517b54669a904e78d87b96e13cf`
Material candidate HEAD: `dc21040815434219933cae974cf79d61812904bb`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Closed finding

Direct current evidence validates only:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

The Kernel explicitly hands recovery to the applicable governed recovery flow and lists RUN-009 as Related Authority, while its dependency boundary explicitly prohibits treating a listed name as dependency proof. RUN-009 does not provide direct reverse CORE-KERNEL dependency/consumer/implementation/governance evidence.

## Material change set

| Change ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| N-01 | `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py` | CREATE | Y | Y |
| N-02 | `Repository/P7_CORE_KERNEL_RUN009_RECOVERY_SEAM_2026-09-01_N.md` | CREATE | Y | Y |
| N-03 | this Matrix | UPDATE IN SAME CHANGE SET | Y | Y |

Candidate comparison from pre-write Matrix HEAD to material candidate proved exactly one commit and exactly three authorized paths. Unexpected path expansion = `0`.

## Exact-head verification

Required workflows on `dc21040815434219933cae974cf79d61812904bb`:

- Full-Stack Repository Audit — `33522126057` — SUCCESS. Repository-audit job and all reported steps succeeded, including exact checkout SHA binding, Mutation Matrix preflight, Matrix semantic regression, same-change-set enforcement, repository-wide audit and evidence emission.
- ARGO Runtime Prototype and Integration Tests — `33522126161` — SUCCESS. Integrity, prototype and integration jobs all succeeded.
- Real Mutation Matrix Regression — `33522126125` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33522126025` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred in N.

## KEEP / non-authority

- CORE-KERNEL and RUN-009 source content unchanged.
- REP-014 unchanged by N; no relationship row is registered yet.
- REP-020 and Core status unchanged by N.
- No reverse RUN-009 → CORE-KERNEL edge.
- No DEPENDS_ON, IMPLEMENTS, CONSUMES, GOVERNS or executable-reachability promotion.
- No Core/Runtime certification.
- No Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Learning assessment

The useful lesson is an application of already-validated Transaction-E discipline: an explicit runtime recovery handoff plus Related Authority can justify a bounded documentary reference while the source's own dependency warning blocks automatic dependency promotion. This does not warrant a new governance rule.

Work Lease: `CLOSED / RESUME-SAFE`.

A future continuation must rediscover live main and recompute Priority 7. REP-014 synchronization of this validated seam is only a candidate and receives no mutation authority from this record.
