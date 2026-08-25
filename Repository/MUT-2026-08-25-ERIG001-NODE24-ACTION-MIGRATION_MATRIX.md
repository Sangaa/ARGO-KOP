# MUT-2026-08-25-ERIG001 — Node24 GitHub Actions Migration

Transaction: `MUT-2026-08-25-ERIG001-001`
Authority: `GOV-013 + GOV-014`
Status: `EXECUTED / CI PENDING`

## Trigger
Repeated successful CI runs emit a Node.js 20 deprecation warning because legacy action majors (`actions/checkout@v4`, `actions/setup-python@v5`) are being forced onto Node24.

## Evidence basis
GitHub announced that hosted runners began using Node24 by default on June 16, 2026, while Node20 is scheduled for removal later in 2026. GitHub recommends updating action versions to Node24-compatible releases.

## Scope
All 13 workflow files present under `.github/workflows` in the reviewed main tree were inspected. The affected workflows used checkout v4 and setup-python v5.

## Controlled change
Migrated:
- `actions/checkout@v4` → `actions/checkout@v6`
- `actions/setup-python@v5` → `actions/setup-python@v6`

No Python runtime versions, test commands, permissions, triggers, mutation logic, or production execution behavior were intentionally changed.

## Preservation
The change is CI action-runtime modernization only. It does not change application/runtime capability claims.

## Validation required
1. Re-read all 13 workflow files.
2. Confirm no legacy checkout/setup-python references remain in the workflow corpus.
3. Correlate the post-migration commit with GitHub Actions runs.
4. Inspect warnings/errors, not only terminal PASS/FAIL.
5. Close only after CI evidence and warning state are reconciled.

## Decision boundary
A PASS with the old Node20 warning is not equivalent to a clean CI environment. Warning state is now treated as actionable environment debt, not harmless noise.
