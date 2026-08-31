# MUT-2026-08-31-P2-EJR-211-IDENTITY-REPAIR-212 — MUTATION MATRIX

Status: FUNCTIONAL / ONE-RECORD REPAIR
Lease: `R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212`
Baseline: `9211f7accd89ab1a597e0651fde909d0b6fcca20`

## Authorized functional paths
- `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` — removed
- `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` — added
- this Matrix

## Exact functional identity mutation
- complete record body preserved;
- only first H1 identity changed `EJR-211` → `EJR-401`;
- filename suffix and chronology preserved.

## Proven replacement vacancy
Lease211 artifact `9744595264`: EJR-401 VACANT; history_complete=true; current_claims=[]; historical_claims=[].

## Preserved boundaries
- retained Memory EJR-211 unchanged;
- no analyzer/test/workflow semantics changed;
- no preemptive census baseline normalization;
- no unrelated consumer or authority mutation.

## Required postwrite validation
1. compare exactly old path + new path + Matrix;
2. semantic body equality except first H1;
3. Internal-ID trigger/run inspected;
4. ambiguity evidence proves displaced root EJR-211 removed and EJR-401 unique;
5. standard regression workflows PASS;
6. any cohort drift is successor-only work.
