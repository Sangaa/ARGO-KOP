# MUT-2026-08-30-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208 — MUTATION MATRIX

Status: FUNCTIONAL / CORRECTIVE SUCCESSOR
Lease: `R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208`
Baseline: `10f14c11a4f4d1d0ba42eab56aa3a85fa04eabfe`

## Authorized functional paths
- `.github/workflows/internal-id-audit.yml`
- this matrix

## Exact workflow change
Added exactly one push path filter:
- `EJR/**`

## Reason
The audit already scans EJR identities and runs EJR-specific chronology/provenance analyzers, but direct EJR mutations did not trigger the workflow. The parent Lease207 repair therefore lacked the required automatic Internal-ID evidence.

## Preserved behavior
- `workflow_dispatch` retained;
- complete-history checkout retained (`fetch-depth: 0`);
- all tests/analyzers/artifact steps retained unchanged;
- no Python audit/test semantics changed;
- no EJR content changed in this successor.

## Required verification
1. compare limited to workflow + Matrix;
2. exact-head Internal Document-ID Audit triggers and passes;
3. deterministic audit and ambiguity-census evidence proves the already repaired current state;
4. root displaced EJR-214 member absent;
5. EJR-400 not ambiguous;
6. parent Lease207 may close only after this evidence and its other applicable checks are reconciled.
