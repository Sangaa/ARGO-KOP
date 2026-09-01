# Priority 7 — CORE-KERNEL → RUN-009 REL-070 Reconciliation — Transaction O

Date: 2026-09-01
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-REL070-O`
Work Lease: `HERMUZ-P7-O-REL070-20260901`
Entry HEAD: `fba9db310c17f3e3745db7062ee16a32b43182b2`
Pre-write Matrix HEAD: `9699e4859d6d1e60b04ce234d542ff1322e30ba2`
Material candidate HEAD: `5714fcbebb445f12cafa4ae07965038bf5725445`

## Closed result

Transaction O reconciles the exact-head-validated Transaction-N seam into the active relationship registry:

`REL-070 | CORE-KERNEL | RUN-009 | REFERENCES | INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`.

REP-014 is now v1.2.13. The current control-plane manifest binds that version and O refresh. Core status is v1.3.10 and records the seventh bounded Priority-7 cross-layer seam while retaining Integrity Hold / Cross-Layer Validation Open / Folder Certification pending.

## Evidence boundary

Direct evidence remains unchanged:

- CORE-KERNEL says recovery follows the applicable governed recovery flow;
- CORE-KERNEL directly lists RUN-009 under Related Authority;
- CORE-KERNEL warns that a listed name does not itself establish dependency;
- RUN-009 defines governed recovery/safe resume but does not directly establish a reverse CORE-KERNEL relationship.

The focused integrity regression preserves N's exact source assertions and now requires one and only one REL-070 row while prohibiting all stronger/reverse semantics.

## Atomicity and preservation

Pre-write Matrix HEAD → material candidate:

- exactly one commit;
- exactly six authorized paths;
- unexpected path expansion `0`;
- REP-014 diff limited to version increment, REL-070 row and bounded evidence section;
- no source-authority mutation.

## Exact-head candidate CI

On `5714fcbebb445f12cafa4ae07965038bf5725445`:

- Full-Stack Repository Audit — `33523444573` — SUCCESS, including exact-SHA binding, Matrix preflight/semantic/same-change-set enforcement and repository-wide audit.
- ARGO Runtime Prototype and Integration Tests — `33523444784` — SUCCESS; integrity, prototype and integration jobs all succeeded.
- Real Mutation Matrix Regression — `33523444619` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33523444671` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred.

## Learning retained

Validation-first evidence and registry synchronization are separate controlled transactions. Once a directly proven seam becomes required by an active relationship-reconciliation obligation, leaving it absent from REP-014 is itself a local consistency gap; synchronizing it does not expand its semantics.

No new governance rule is required.

## Non-claims

No reverse edge, dependency, consumer, implementation, governance or executable-reachability promotion. No Core/Runtime certification. No Phase-1 closure. No Connected Baseline or repository-wide graph closure. No Global PASS.

## Session close / next safe entry

Work Lease CLOSED. O is resume-safe subject to closure-HEAD CI.

Any future continuation must independently rediscover live main and recompute Priority 7. No NEXT statement in this record is mutation authority.
