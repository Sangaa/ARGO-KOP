# MUT-2026-08-31-P2-EJR-211-IDENTITY-REPAIR-212 — MUTATION MATRIX

Status: PREWRITE / ONE-RECORD REPAIR
Lease: `R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212`
Baseline: `88c1e90a6c6ddad5bd021c8a6a1fb1ac58b9e05b`

## Authorized functional paths
- `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` — remove
- `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` — add
- this Matrix

## Exact permitted identity mutation
- preserve the complete record body;
- change only first H1 identity `EJR-211` → `EJR-401`;
- preserve filename suffix and chronology.

## Proven replacement vacancy
Lease211 artifact `9744595264`: EJR-401 VACANT; history_complete=true; current_claims=[]; historical_claims=[].

## Preserved boundaries
- retained Memory EJR-211 unchanged;
- no analyzer/test/workflow semantics changed;
- no preemptive census baseline normalization;
- no unrelated consumer or authority mutation.

## Validation
1. compare exactly old path + new path + Matrix;
2. semantic body equality except first H1;
3. Internal-ID trigger/run inspected;
4. ambiguity evidence proves EJR-211 displaced root removed and EJR-401 unique;
5. standard regression workflows PASS;
6. any cohort drift is successor-only work.
