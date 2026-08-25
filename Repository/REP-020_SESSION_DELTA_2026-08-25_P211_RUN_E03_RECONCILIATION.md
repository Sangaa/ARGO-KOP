# REP-020 — SESSION DELTA — 2026-08-25 — P211 RUN-E03 RECONCILIATION

Platform: ARGO KOP  
Protocol: GOV-013 HERMUZ Session Build Protocol  
Status: Active / Integrity Hold  
Predecessor: P210 / Control-Plane Version Reconciliation

## Trigger

The first Runtime Prototype execution after P210 was bound to `main` commit `11216b0744ed5b12b1539fd13ba8a2f60a1a7118` and workflow run `32829282329`.

Integration tests completed successfully. Prototype tests completed successfully. The integrity-tests job failed with exactly two assertions requiring the current `REP-020` matrix to retain the explicit `RUN-E03` evidence row and classify it as `PARTIALLY_VERIFIED`.

## Evidence Recovered

The repository contains authoritative P3 isolated E2E evidence for:

`ENG-006 → SRV-009 = EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E`

The P3 reconciliation addendum explicitly states that the legacy `RUN-E03` entry in `REP-020` must be reconciled to `VERIFIED` for the isolated-E2E scope, while the ordinary `RUN-010` runtime service coupling remains unproven.

Therefore the correct current matrix representation is not a simple `VERIFIED` runtime relationship. It is an explicit evidence-boundary row:

`RUN-E03 | ENG-006 → SRV-009 | isolated E2E proof | PARTIALLY_VERIFIED | runtime-service coupling unproven`

This preserves both facts without collapsing the evidence layers.

## Root Cause

P205 changed `REP-020` to version `0.2.1` while the RUN-E03 row was absent from the current canonical matrix. The absence was not caught by the control-plane version gate because the version remained internally consistent. The later integrity regression correctly detected the semantic evidence-boundary omission.

This is a distinct class of defect from the P210 version mismatch:

`Version consistency ≠ Evidence completeness.`

## Corrective Mutation

`REP-020` was updated to version `0.2.2` and now contains an explicit RUN-E03 evidence-boundary section. The row is intentionally `PARTIALLY_VERIFIED` because isolated P3 execution proof does not establish ordinary RUN-010 runtime-service coupling.

No relationship was promoted to runtime-verified. No authority changed. Connected Baseline and global Integrity Hold remain unchanged.

## Post-Write Verification

The updated matrix was written from its exact pre-write blob SHA and returned content SHA:

`c4756644f70b02c7732ee97d5b32df5bac48d361`

The matrix must be re-read after the corrective commit and a fresh Runtime Prototype run must bind the result to the new main SHA.

## Learning

This checkpoint adds a stronger rule to HERMUZ's evidence discipline:

`A relationship can have verified evidence in one execution boundary while remaining partial in a broader consumer/runtime boundary.`

Therefore registries and matrices must preserve the boundary of proof rather than selecting the strongest status globally.

## Next Safe Action

Run fresh CI on the corrected main SHA. If the two RUN-E03 integrity assertions pass, classify that surface as reconciled and inspect the next independent integrity failure, if any. Do not promote RUN-010 → SRV-009 to runtime-verified without new direct runtime evidence.

## Closure Classification

`P211 / RUN-E03-EVIDENCE-BOUNDARY-RECONCILED / RUNTIME-COUPLING-STILL-OPEN / INTEGRITY-HOLD`
