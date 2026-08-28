# IGT Binding-Aware Evidence Admission — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-BINDING-AWARE-EVIDENCE-ADMISSION-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@6a1e7f1f80d04b00ac6c2601964c3821ce0bbe9c`
Working branch: `hermuz/igt-binding-aware-evidence-admission-20260829`
Status: `SOURCE VERIFIED / READ-BACK VERIFIED / PR-CI VERIFIED / FINAL-HEAD CI PENDING`
Authority: `NONE`

## Entry Evidence
Three materially different checks established the gap on current main:
1. code search for `binding_id` under `Quality/Integration` found no existing evidence-package consumer;
2. code search for `export_package_digest` under `Quality/Integration` found no existing evidence-package consumer;
3. direct inspection of `experience_spine_igt_evidence_package.py` showed an independent payload/response/package integrity gate that does not consume or verify the newly canonical sealed-export/local-binding identity.

## Problem
The repository had two locally valid but detachable evidence chains:

`SEALED PARTICIPANT EXPORT → VERIFIED LOCAL RESPONSE BINDING`

and

`MODEL-RUN EVIDENCE PACKAGE → STRUCTURAL / INTEGRITY QUALIFICATION`.

A model-run package could therefore be valid under its own schema without establishing correlation to the exact sealed payload and locally bound response.

## Design Law
`VALID LOCAL BINDING + VALID MODEL-RUN PACKAGE != ESTABLISHED CORRELATION`.

`BINDING-AWARE ADMISSION != PROVIDER AUTHENTICITY != MODEL EXECUTION PROOF`.

## Applied Changes
| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_binding_evidence_admission.py` | composes existing verifiers and checks exact cross-artifact correlation | Y | Y source/read-back/CI |
| C02 | `Quality/Integration/test_experience_spine_igt_binding_evidence_admission.py` | positive B0/L1/L2 and adversarial detached-artifact regressions | Y | Y source/read-back/CI |
| C03 | `Repository/IGT_BINDING_AWARE_EVIDENCE_ADMISSION_CONTRACT_2026-08-29.md` | correlation, integrity, state and nonclaim contract | Y | Y source/read-back |
| C04 | Runtime/Prototype/Integrity/Integration + Full-Stack CI | exact-head validation | Y | Y on implementation head; final-head rerun pending |

## Implemented Boundaries
1. Participant export must pass canonical export verification.
2. Local response binding must pass canonical binding verification against that exact export.
3. Model-run evidence package must be `STRUCTURALLY_QUALIFIED` by the existing package validator; invalid or quarantined packages are not admitted.
4. Package participant payload must exactly equal the sealed export payload.
5. Package participant response must exactly equal the locally bound response.
6. Package case, condition, and repository baseline must equal the export identity.
7. Binding export ID/digest must still match the exact export.
8. Package payload digest must correlate with the sealed export payload.
9. Package response digest must correlate with the bound response digest.
10. Existing evidence-package validator/schema was not modified or weakened.
11. Maximum new state is `BINDING_CORRELATED_EVIDENCE_ADMISSION`.

## PR / CI Evidence

PR: `#85 — IGT: binding-aware model-run evidence admission` (non-draft).

Implementation head:
`90991bed0f0c58544995e64fbf9c724f021672ba`

Observed PR merge ref:
`c2fb3c7a51d8846005476bcd07c52ff8fc6d6150`
= `Merge 90991bed0f0c58544995e64fbf9c724f021672ba into 6a1e7f1f80d04b00ac6c2601964c3821ce0bbe9c`.

Exact-head CI:
- Prototype: SUCCESS
- Integrity: SUCCESS
- Integration: SUCCESS
- Full-Stack Repository Audit: SUCCESS
- Integration discovery: `433 passed, 1 warning, 11 subtests passed`
- Prior canonical baseline: `421 passed`
- Added discovered integration coverage: `+12 tests`

The remaining warning is the pre-existing P2 internal-ID audit warning; this mutation does not reinterpret or modify that scope.

## Diff / Concurrency Reconciliation

Exact compare from base before this documentation update:
- ahead: 4 commits;
- behind: 0;
- exactly 4 changed paths;
- all four paths declared by this transaction;
- no mutation to Runtime, Services, provider connectors, existing evidence-package validator/schema, workflows, cognition, memory, or production dispatch.

## Explicit Non-Claims
- Correlation does not prove the package came from an external model.
- Correlation does not prove the model received the sealed export.
- Correlation does not prove provider authenticity.
- Correlation does not replace the existing independence attestation gate.
- Correlation does not authenticate model execution.
- Correlation does not establish cognitive effect or authority.
- Green CI does not grant authority beyond this bounded local cross-artifact claim.

## Final Verification Plan
1. Run Runtime/Integration + Full-Stack CI on this documentation head.
2. Freeze branch if green.
3. Re-read current main, PR metadata, and exact compare for concurrency.
4. Require exact 4-path delta and behind=0.
5. Squash merge with exact expected head SHA only if clean.
6. Verify post-merge exact main with Runtime/Integration + Full-Stack (+ normal main workflows).

## Bounded Result If Final Verification Passes

`SEALED EXPORT → LOCAL RESPONSE BINDING → MODEL-RUN PACKAGE CORRELATION = EXECUTION-VERIFIED`.

while:

`EXTERNAL DELIVERY = NOT PROVEN`.

`MODEL EXECUTION AUTHENTICITY = NOT ESTABLISHED BY CORRELATION`.

`PROVIDER AUTHENTICITY = UNVERIFIED`.

`COGNITIVE EFFECT = NOT ESTABLISHED`.
