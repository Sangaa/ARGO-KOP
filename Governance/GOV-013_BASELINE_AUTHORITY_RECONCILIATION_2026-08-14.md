# GOV-013 — BASELINE AUTHORITY RECONCILIATION

Date: 2026-08-14
Platform: ARGO KOP
Status: Decision Evidence / Integrity Hold

## Question

Which Development Baseline is authoritative for the current repository?

## Evidence

- `Release/VERSION.md` declares Current Development Baseline `3.2.1` and identifies itself as the official reference for development baseline identification.
- `PROJECT_STATUS.md` reports Active Development Baseline `3.2.1` and states that `Release/VERSION.md` is authoritative for the release/baseline distinction.
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` currently declares `3.3.0`.

## Decision

**Authoritative current Development Baseline = 3.2.1.**

The `3.3.0` declaration in REP-012 is treated as a **CONFLICTING STALE DECLARATION** until REP-012 is explicitly reconciled through a controlled document replacement.

The numerically higher value does not override an explicit authority declaration.

## Required mutation

`REP-012` must be reconciled to `3.2.1` through the normal mutation protocol, with complete-file replacement safety and post-write re-read.

This decision does not itself perform that mutation.

## Test / Evidence Ledger

| TEST-ID | Result | Evidence |
|---|---|---|
| BASELINE-003 | PASS | `Release/VERSION.md` current main |
| BASELINE-004 | PASS | `PROJECT_STATUS.md` current main |
| BASELINE-005 | CONFLICT CONFIRMED | `REP-012` current main says 3.3.0 |
| BASELINE-006 | PASS | Authority precedence established |
| BASELINE-007 | NOT_PERFORMED | REP-012 controlled correction pending |

## Integrity

Repository remains **INTEGRITY HOLD** until the stale declaration is corrected and re-read.
