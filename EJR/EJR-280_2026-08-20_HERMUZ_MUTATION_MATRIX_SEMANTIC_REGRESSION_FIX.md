# EJR-280 — HERMUZ Mutation Matrix Semantic Regression Fix

**Date:** 2026-08-20  
**Protocol:** GOV-013 HERMUZ Session Build Protocol  
**Status:** CLOSED — MINIMAL VALIDATOR REPAIR / READ-BACK VERIFIED / EXECUTION PENDING

## 1. Trigger

GitHub Actions run `fix CI YAML syntax in mutation matrix regression #1285` parsed successfully after the YAML repair, but `repository-audit` failed in the `Run Mutation Matrix semantic regression` step with:

`AssertionError: Repository/MUT-2026-08-17-REP001-001_MUTATION_MATRIX.md`

## 2. Root Cause

The semantic validator assumed that every Mutation Matrix used the newest six-column schema and the newest section naming. The historical REP-001 transaction matrices are governed artifacts but use compatible legacy forms:

- REP001-001 has eight table columns, including `Section ID` and `Authority Evidence`.
- REP001-002 has eight table columns, including `Section ID` and `Authority`.
- Historical matrices use `Post-Commit Reconciliation` and `Boundary` instead of requiring the newer `Execution Evidence` / `Closure` headings.
- REP001-001 does not contain an explicit `Protocol: GOV-014` line but contains the governed legacy evidence/boundary structure.
- REP001-001 records unexpected additions/deletions rather than the exact phrase `Unexpected Changes`.

The failure was therefore a **validator compatibility defect**, not evidence that the historical matrices were semantically invalid.

## 3. Controlled Repair

Updated only `Quality/Integration/check_mutation_matrix_semantics.py`.

The validator now:

1. Locates required columns by header name instead of requiring exactly six columns.
2. Accepts additional governed columns while still validating `Change ID`, `Target`, `Action`, `Expected Content`, `Applied`, and `Verified`.
3. Accepts case variation in governed section headings.
4. Recognizes the legacy governed shape when explicit GOV-014 declaration predates the artifact.
5. Accepts `Post-Commit Reconciliation` as execution/read-back evidence.
6. Accepts explicit unexpected-addition/deletion controls as equivalent preservation evidence.
7. Does not weaken the Y/N controls for `Applied` and `Verified`.

## 4. Evidence

Initial validator repair commit:
`e77fb7fb4dfe441e91031e691017d74e9915d3d1`

Follow-up compatibility refinement:
`80c5dea5ad6af247bd2b8d6e38d58468ffcf1c1a`

Post-write validator blob SHA:
`f8a774ff18c2b2753d2b8fe32a829bd0ca2e1774`

The current repository files were read back after each mutation.

## 5. Scope Boundary

No Mutation Matrix content was rewritten. No historical transaction state was promoted. No Runtime semantics, relationship state, P6 classification, or production execution path was changed.

The repair changes only the **test oracle** so that it validates both the current governed schema and explicitly recognized historical governed representations.

## 6. Learning

**Validator Compatibility Rule:** A repository-wide semantic regression must validate the governed semantic contract, not accidentally require one historical serialization format. When legacy artifacts are intentionally retained, the validator must map required semantic fields by name and explicitly model compatible legacy representations.

**Anti-weakening Rule:** Backward compatibility must not remove core safety checks. Required identity fields, action fields, expected content, and `Applied/Verified ∈ {Y,N}` remain mandatory.

## 7. Closure

- [x] CI failure inspected.
- [x] Failing historical artifact identified.
- [x] Root cause isolated to validator schema assumptions.
- [x] Minimal validator repair applied.
- [x] Follow-up compatibility gap corrected.
- [x] Current validator read-back completed.
- [x] No historical matrix mutation performed.
- [x] No runtime/relationship/P6 promotion performed.
- [x] Learning documented directly in repository.
- [ ] Authoritative Actions execution on the new current HEAD verified.
- [ ] P6 promotion authorized.

**Next checkpoint:** current-HEAD Actions execution → semantic regression result → identity/SHA verification → P6 correlation artifact read-back → classification → closure.
