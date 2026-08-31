# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-213 — MUTATION MATRIX

Status: PREWRITE / CORRECTIVE
Lease: `R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-213`
Baseline: `89c51d6aff95f86652a01153f2d842f4db0e7960`

## Authorized functional paths
- `Quality/Integration/ejr_memory_to_root_provenance_census.py`
- this Matrix

## Exact permitted change
- `EXPECTED_GROUP_COUNT = 35` → `EXPECTED_GROUP_COUNT = 34`

## Evidence basis
- Lease212 repaired one displaced MEMORY_TO_ROOT_EJR ambiguity group.
- Internal-ID run `33354350722`: all tests and prior analyzers PASS; memory-to-root census only failure.
- census artifact `9744650333`: expected=35, observed=34, history_complete=true, sole incomplete=`__COHORT_COUNT_DRIFT__`.
- audit artifact `9744649112`: EJR-211 and EJR-401 are not ambiguous.

## Preserved semantics
- dynamic target selection classifier-derived;
- count drift still fails PARTIAL;
- incomplete history still fails closed;
- identity-source/cardinality checks unchanged;
- evidence-only/no-authority boundary unchanged;
- no EJR record changed.

## Validation
- compare limited to baseline constant + Matrix;
- exact-head Internal-ID SUCCESS;
- deterministic census 34/34 CENSUSED;
- EJR-211/EJR-401 remain non-ambiguous;
- standard regression workflows PASS.
