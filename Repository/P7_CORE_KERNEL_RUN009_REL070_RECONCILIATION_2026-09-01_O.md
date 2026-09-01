# Priority 7 — CORE-KERNEL → RUN-009 REL-070 Reconciliation — Transaction O

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-REL070-O`
Work Lease: `HERMUZ-P7-O-REL070-20260901`
Entry HEAD: `fba9db310c17f3e3745db7062ee16a32b43182b2`
Pre-write Matrix HEAD: `9699e4859d6d1e60b04ce234d542ff1322e30ba2`

## Why O is legal

Transaction N already closed and exact-head-CI validated the bounded relationship:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`.

At O entry, REP-014 v1.2.12 ended at REL-069 and did not contain this proven seam. Current Core status explicitly keeps relationship reconciliation open where evidence requires. O therefore removes a validation/registry inconsistency rather than inventing a new relationship.

## Registered disposition

O adds exactly:

`REL-070 | CORE-KERNEL | RUN-009 | REFERENCES | INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

Evidence remains the direct current source pair proven by N:

- CORE-KERNEL explicitly says recovery follows the applicable governed recovery flow;
- CORE-KERNEL directly lists `Runtime/RUN-009_RECOVERY.md` under Related Authority;
- CORE-KERNEL explicitly warns that a listed name does not establish dependency merely by appearing;
- RUN-009 defines canonical governed recovery and safe-resume behavior but does not directly establish a reverse CORE-KERNEL relationship.

## Synchronized surfaces

- REP-014 v1.2.12 → v1.2.13, REL-070 only.
- Current REP-020 manifest updated to bind REP-014 v1.2.13 and O refresh while retaining all open/hold boundaries.
- Core status v1.3.9 → v1.3.10 and records the seventh bounded seam while retaining CROSS-LAYER VALIDATION OPEN / Folder Certification pending.
- N focused test now enforces exact unique REL-070 while preserving all original source assertions and forbidden stronger/reverse semantics.

## Non-claims

No CORE-KERNEL or RUN-009 source mutation. No reverse edge. No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, `GOVERNS` or executable proof. No Core/Runtime certification. No Phase-1, Connected Baseline, repository-wide graph or Global PASS closure.

## Candidate verification

Pending exact-head atomic diff, registry preservation check and four required workflows. Failure remains evidence under GOV-016 and cannot be repaired by semantic weakening.
