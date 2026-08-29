# Baseline Authority Reconciliation — GOV-013 Decision Evidence

Date: 2026-08-14
Platform: ARGO KOP
Status: Decision Evidence / Historical Integrity-Hold Resolution
Authority boundary: evidence record under `GOV-013`; not an independent Governance Document ID.
Identity classification: `Repository/GOVERNANCE_IDENTITY_MIGRATION_MATRIX_2026-08-29.md`

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

`REP-012` was corrected to `3.2.1` in its current main content. The resulting artifact was directly re-read after mutation and its header records Version `1.0.7`, Status `Active Control / Integrity Hold / Phase 1 Population In Progress`, and Development Baseline `3.2.1`.

## Evidence Boundary

This record preserves the historical reasoning and verified decision. It does not define a second `GOV-013` authority identity and must not be treated as a substitute for the current release/baseline authority surface.
