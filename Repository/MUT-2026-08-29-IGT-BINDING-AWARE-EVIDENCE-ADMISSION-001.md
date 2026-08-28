# IGT Binding-Aware Evidence Admission — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-BINDING-AWARE-EVIDENCE-ADMISSION-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@6a1e7f1f80d04b00ac6c2601964c3821ce0bbe9c`
Working branch: `hermuz/igt-binding-aware-evidence-admission-20260829`
Status: `PLANNED / SOURCE NOT YET IMPLEMENTED`
Authority: `NONE`

## Entry Evidence

Three materially different checks established the gap on current main:
1. code search for `binding_id` under `Quality/Integration` found no existing evidence-package consumer;
2. code search for `export_package_digest` under `Quality/Integration` found no existing evidence-package consumer;
3. direct inspection of `experience_spine_igt_evidence_package.py` showed an independent payload/response/package integrity gate that does not consume or verify the newly canonical sealed-export/local-binding identity.

## Problem

The repository now has two locally valid evidence chains:

`SEALED PARTICIPANT EXPORT → VERIFIED LOCAL RESPONSE BINDING`

and

`MODEL-RUN EVIDENCE PACKAGE → STRUCTURAL / INTEGRITY QUALIFICATION`.

They can currently remain detached. A model-run package may carry a valid-looking payload/response/case/condition/baseline set without proving that those exact semantic artifacts are the ones already sealed and locally bound.

## Design Law

`VALID LOCAL BINDING + VALID MODEL-RUN PACKAGE != ESTABLISHED CORRELATION`.

and:

`BINDING-AWARE ADMISSION != PROVIDER AUTHENTICITY != MODEL EXECUTION PROOF`.

## Planned Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_binding_evidence_admission.py` | verify exact export/binding/package semantic correlation before downstream admission | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_binding_evidence_admission.py` | positive and adversarial correlation regressions | N | N |
| C03 | `Repository/IGT_BINDING_AWARE_EVIDENCE_ADMISSION_CONTRACT_2026-08-29.md` | correlation, integrity, state and nonclaim contract | N | N |
| C04 | Runtime/Integration + Full-Stack CI | exact-head validation | N | N |

## Required Boundaries

1. Participant export must pass canonical export verification.
2. Local response binding must pass canonical binding verification against that exact export.
3. Model-run evidence package must pass its existing local package validator; this transaction does not weaken or replace it.
4. Package `participant_payload` must exactly equal the sealed export payload.
5. Package `participant_response` must exactly equal the locally bound response.
6. Package case, condition and repository baseline must equal the export/binding identity.
7. Package payload/response digests must therefore correlate with the already sealed semantic artifacts.
8. No provider receipt, execution authenticity or independence claim is inferred merely from correlation.
9. Maximum new state: `BINDING_CORRELATED_EVIDENCE_ADMISSION`.

## Explicit Non-Claims

- Correlation does not prove the package came from an external model.
- Correlation does not prove the model received the sealed export.
- Correlation does not prove provider authenticity.
- Correlation does not replace the existing independence attestation gate.
- Correlation does not establish cognitive effect or authority.

## Verification Plan

Implement smallest adapter → adversarial regressions → exact read-back/diff → Draft PR → exact-head Runtime/Integration + Full-Stack CI → semantic repair only if evidence requires it → documentation-head CI → freeze/concurrency reconciliation → lifecycle-safe expected-head squash merge → exact-main post-merge CI.
