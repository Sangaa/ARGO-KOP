# GOV-013 — BASELINE AUTHORITY RECONCILIATION

Date: 2026-08-14
Platform: ARGO KOP
Status: Decision Evidence / Integrity Hold

## Question

Which Development Baseline is authoritative for the current repository?

## Evidence

- `Release/VERSION.md` declares Current Development Baseline `3.2.1` and identifies itself as the official reference for development baseline identification.
- `PROJECT_STATUS.md` reports Active Development Baseline `3.2.1` and states that `Release/VERSION.md` is authoritative for the release/baseline distinction.
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` has now been re-read on current `main` and declares `3.2.1`.
- `Repository/REP-001_MASTER_INDEX.md`, `Repository/REP-002_REPOSITORY_MAP.md`, and `Runtime/RUN-001_BOOT_SEQUENCE.md` independently align with `3.2.1` within the inspected control-plane scope.

## Decision

**Authoritative current Development Baseline = 3.2.1.**

The former `3.3.0` declaration in REP-012 was a **CONFLICTING STALE DECLARATION**. It has now been reconciled to `3.2.1` through the repository's normal mutation protocol and verified by post-write re-read.

The numerically higher value does not override an explicit authority declaration.

## Mutation / Verification Result

`REP-012` was corrected to `3.2.1` in its current main content. The resulting artifact was directly re-read after mutation and its header now records Version `1.0.7`, Status `Active Control / Integrity Hold / Phase 1 Population In Progress`, and Development Baseline `3.2.1`.

## Test / Evidence Ledger

| TEST-ID | Result | Evidence |
|---|---|---|
| BASELINE-003 | PASS | `Release/VERSION.md` current main |
| BASELINE-004 | PASS | `PROJECT_STATUS.md` current main |
| BASELINE-005 | CONFLICT CONFIRMED → RESOLVED | Historical REP-012 declaration of 3.3.0 was replaced |
| BASELINE-006 | PASS | Authority precedence established |
| BASELINE-007 | PASS | REP-012 corrected to 3.2.1 and directly re-read |
| BASELINE-008 | PASS | REP-001 / REP-002 / RUN-001 cross-check aligns to 3.2.1 within inspected scope |

## Remaining Scope

This reconciliation closes the specific REP-012 baseline conflict. It does **not** prove that every repository artifact declares 3.2.1, and any remaining 3.3.0 declaration must be evaluated independently for authority, history, or stale state.

Repository remains **INTEGRITY HOLD** for other unresolved integrity blockers.
