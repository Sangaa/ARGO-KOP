# EJR-182 — Test Ledger + Baseline Conflict Finding

**Date:** 2026-08-14
**Baseline used for matrix:** 3.2.1
**Integrity:** HOLD

## Work completed

- Re-read `REP-011_REVIEW_TRACEABILITY_LEDGER.md` and applied its evidence, freshness, current-fitness, cross-registry and persistence rules. fileciteturn1087file0
- Re-read `REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`.
- Detected a material baseline contradiction: REP-012 declares Development Baseline `3.3.0`, while the current version authority used by the active audit is `3.2.1`. fileciteturn1088file0
- Updated REP-020 from `0.1.4` to `0.1.5` and recorded the contradiction as `CONFLICT` instead of silently normalizing it.
- Added tests TST-010..TST-014 to the matrix and explicitly preserved NOT_PERFORMED/NOT_COMPLETED tests.

## Test evidence discipline

The matrix now separates four important states:

- PASS — the named check passed inside its stated scope.
- PARTIAL — evidence exists but is insufficient for closure.
- CONFLICT — contradictory repository evidence was detected and requires authority resolution.
- NOT_PERFORMED / NOT_COMPLETED — the test has not been established as evidence and must not be represented as a failure or success.

## Important learning

A relationship matrix without a test ledger can accidentally convert documentation inspection into perceived proof. A test ledger without explicit negative space can accidentally convert "not tested" into "passed by absence of failure." The two must therefore live together.

A second learning is that baseline metadata itself is a relationship/authority test surface. A registry carrying a different baseline cannot be treated as current merely because it is canonical or numerically newer. Authority must be resolved first.

## Next

1. Resolve 3.2.1 vs 3.3.0 through the designated canonical version authority.
2. Revalidate affected control-plane artifacts after resolution.
3. Continue runtime/repository consumer validation.
4. Perform controlled runtime/mutation tests only when the appropriate evidence environment exists.
5. Keep REP-020 test ledger synchronized during every subsequent review.

No PASS promotion.
