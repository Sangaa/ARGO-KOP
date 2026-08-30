# MUT-2026-08-30-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208 — MUTATION MATRIX

Status: PREWRITE / CORRECTIVE
Lease: `R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208`
Baseline: `912447da46af44ab0b9805e8f3d2723a524745b4`

## Authorized functional paths
- `.github/workflows/internal-id-audit.yml`
- this matrix

## Exact permitted workflow change
Add one push path filter:
- `EJR/**`

## Forbidden
- no changes to audit/analyzer/test Python semantics;
- no EJR content/path/identity mutation;
- no suppression or expected-count normalization;
- no REP-012/016/020 mutation;
- no Priority2 / Phase1 / Connected Baseline closure.

## Validation
1. compare must show only workflow + Matrix;
2. workflow must retain `fetch-depth: 0`;
3. Internal Document-ID Audit exact-head run must trigger and complete SUCCESS;
4. deterministic artifacts must be inspected for the repaired EJR-214/EJR-400 state;
5. parent Lease207 remains verification-pending until this successor supplies the missing audit evidence.
