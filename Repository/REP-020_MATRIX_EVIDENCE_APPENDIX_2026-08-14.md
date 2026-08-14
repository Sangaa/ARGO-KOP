# REP-020 Evidence Appendix — Baseline Authority Conflict Review

**Parent Matrix:** REP-020 v0.1.5  
**Date:** 2026-08-14  
**Integrity:** HOLD

This appendix is part of the REP-020 evidence surface and records checks discovered while populating/revalidating the matrix. It does not replace REP-020 or any authority source.

## New test ledger entries

| Test ID | Check | Result | Evidence | Matrix consequence |
|---|---|---|---|---|
| TST-015 | Direct read of authoritative version source | PASS | `Release/VERSION.md` | Keep matrix baseline 3.2.1 |
| TST-016 | Reproduce REP-012 baseline claim | CONFLICT CONFIRMED | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | Preserve CONFLICT; no normalization |
| TST-017 | Cross-check root status against version authority | SUPPORTS 3.2.1 | `PROJECT_STATUS.md` | Strengthens 3.2.1 authority finding |
| TST-018 | Search for competing 3.3.0 evidence | INCONCLUSIVE | Search surfaced historical/older-commit artifacts | Do not promote search results to current authority |

## Not performed

| Test ID | Check | State |
|---|---|---|
| TST-119 | Controlled correction/reconciliation of REP-012 | NOT_PERFORMED — governance decision required |
| TST-120 | Exhaustive repository-wide baseline audit | NOT_PERFORMED |
| TST-121 | Executable runtime baseline test | NOT_PERFORMED |
| TST-122 | Automated cross-registry reconciliation | NOT_PERFORMED |

## Authority finding

`Release/VERSION.md` explicitly identifies itself as the authoritative source for release/baseline distinction and reports Development Baseline `3.2.1`. `PROJECT_STATUS.md` independently reports Active Development Baseline `3.2.1` and points back to `Release/VERSION.md` as authoritative. fileciteturn1094file0 fileciteturn1098file0

`REP-012` currently declares `3.3.0`, so the conflict is real and must remain visible until governed resolution. fileciteturn1096file0

## Required next action

Trace every affected control-plane artifact that declares `3.3.0`, determine whether the value is historical, stale, or evidence of a governed baseline transition, then reconcile only after authority is explicitly established.

**Rule:** highest numeric version ≠ authoritative version.
