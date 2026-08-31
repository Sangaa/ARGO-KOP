# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-209 — MUTATION MATRIX

Status: FUNCTIONAL / CORRECTIVE
Lease: `R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-209`
Baseline: `19ff6beeae781627fd6d41be997c998ebf8fe1dc`

## Authorized functional paths
- `Quality/Integration/ejr_memory_to_root_provenance_census.py`
- this matrix

## Exact functional change
- `EXPECTED_GROUP_COUNT = 36` → `EXPECTED_GROUP_COUNT = 35`

## Evidence basis
- Lease202 established a dynamic classifier plus fail-on-drift guard at a verified cohort of 36.
- Lease207 deliberately removed the displaced root EJR-214 ambiguity member by re-identifying it as EJR-400.
- Lease208 exact-head run `33329835211` proves all test execution passes; only census emission failed.
- emitted census artifact `9737318158` proves observed=35 and sole incompleteness=`__COHORT_COUNT_DRIFT__`.

## Preserved semantics
- dynamic target selection remains classifier-derived;
- count drift still fails PARTIAL;
- incomplete history still fails closed;
- identity-source/cardinality checks unchanged;
- evidence-only/no-authority boundary unchanged;
- no EJR record changed.

## Required postwrite validation
- compare limited to census baseline constant + Matrix;
- Internal Document-ID Audit exact-head SUCCESS;
- deterministic census expected=35 / observed=35 / CENSUSED;
- repaired EJR-214 ambiguity absent and EJR-400 unique/not ambiguous;
- applicable Full-Stack / Runtime / M2 / Real Matrix PASS.
