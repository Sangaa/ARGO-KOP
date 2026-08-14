# EJR-183 — Baseline Authority Conflict Review

**Date:** 2026-08-14
**Status:** Review checkpoint recorded
**Integrity:** HOLD

## Scope

The current REP-020 matrix identified a conflict between `REP-012` declaring Development Baseline `3.3.0` and the current authoritative `Release/VERSION.md` declaring Development Baseline `3.2.1`.

## Tests performed

- **TST-015 — Direct authority read:** `Release/VERSION.md` was read from `main`. Result: PASS. It explicitly identifies itself as the authoritative reference for official release vs current development baseline and states current development baseline `3.2.1`. fileciteturn1094file0
- **TST-016 — Conflict reproduction:** `REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` was read from `main` and currently declares `3.3.0`. Result: CONFLICT CONFIRMED. fileciteturn1096file0
- **TST-017 — Root-status cross-check:** `PROJECT_STATUS.md` was read from `main`; it independently reports Active Development Baseline `3.2.1` and explicitly says `Release/VERSION.md` is authoritative. Result: SUPPORTS 3.2.1. fileciteturn1098file0
- **TST-018 — Search for competing 3.3.0 evidence:** repository search surfaced historical/older-commit artifacts carrying `3.3.0`, but search results alone are not treated as current canonical evidence. Result: INCONCLUSIVE FOR CURRENT AUTHORITY.

## Tests not performed

- No mutation was made to REP-012 because authority resolution is a governance/content decision, not a safe automatic normalization.
- No full repository-wide baseline audit was executed.
- No executable runtime test was performed.
- No automatic reconciliation program was run.

## Conclusion

Current authoritative evidence supports **Development Baseline 3.2.1**. `REP-012`'s `3.3.0` is therefore a documented conflict requiring controlled correction or an explicit governed decision if another source is intended to supersede the current authority.

The numeric value `3.3.0` was not accepted merely because it is higher.

## Matrix action

REP-020 must retain the conflict as `CONFLICT` until the authority decision is explicitly recorded. This preserves the evidence trail and prevents accidental promotion.

## Engineering learning

When a critical registry disagrees with its declared authority, the correct action is **freeze promotion → reproduce conflict → verify authority → trace impact → govern resolution → re-read all affected consumers → then reconcile**. Do not normalize by numeric comparison.
