# Priority 7 — CORE-KERNEL → RUN-009 Recovery Seam — Transaction N

Date: 2026-09-01
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-VALIDATION-N`
Work Lease: `HERMUZ-P7-N-CORE-KERNEL-RUN009-20260901`
Entry HEAD: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
Pre-write Matrix HEAD: `a940b5b526e17517b54669a904e78d87b96e13cf`
Material candidate HEAD: `dc21040815434219933cae974cf79d61812904bb`

## Closed result

Direct current evidence validates:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

`Core/ARGO_KERNEL.md` explicitly states that recovery follows the applicable governed recovery flow and directly lists `Runtime/RUN-009_RECOVERY.md` under Related Authority. The same source explicitly warns that a name appearing in the Kernel document does not establish dependency merely by being listed.

`Runtime/RUN-009_RECOVERY.md` defines the governed Runtime recovery mechanism and safe-resume gates, but does not directly establish a reverse relationship to CORE-KERNEL.

## Validation-first boundary

N deliberately did not mutate REP-014. The focused regression proves current source semantics and asserts absence of the pair in REP-014 during this transaction while forbidding stronger or reverse semantics.

Material candidate comparison from the pre-write Matrix HEAD proved:

- exactly one commit;
- exactly three authorized paths;
- unexpected path expansion `0`.

## Exact-head CI

On `dc21040815434219933cae974cf79d61812904bb`:

- Full-Stack Repository Audit — `33522126057` — SUCCESS; exact-SHA binding, Matrix preflight/semantics/same-change-set enforcement and repository-wide audit succeeded.
- ARGO Runtime Prototype and Integration Tests — `33522126161` — SUCCESS; integrity, prototype and integration jobs all succeeded.
- Real Mutation Matrix Regression — `33522126125` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33522126025` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred.

## Learning retained

Transaction E's rule transfers directly to recovery: an explicit Runtime authority/handoff reference may be a real one-way documentary seam without being an architectural dependency. Related Authority and lifecycle handoff are evidence for `REFERENCES`, not automatic evidence for `DEPENDS_ON` or executable reachability.

No new Governance rule is required; existing relationship discipline already governs this case.

## Non-claims

No mutation to CORE-KERNEL, RUN-009, REP-014, REP-020 or Core status. No reverse edge. No dependency/consumer/implementation/governing/executable promotion. No Core or Runtime certification. No Phase-1, Connected Baseline, repository-wide graph or Global PASS claim.

## Session close / next safe entry

Work Lease CLOSED. Transaction N is resume-safe.

A future continuation must independently rediscover live main and recompute the Priority-7 queue. REP-014 reconciliation of this pair may be evaluated only after that recomputation; this record is evidence, not future mutation authority.
