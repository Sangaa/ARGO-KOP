# IGT Sealed Export → Participant Response Binding — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-RESPONSE-BINDING-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@19805fbb948f4ae32e1c97169cc4f50b80681812`
Working branch: `hermuz/igt-response-binding-20260829`
Status: `PLANNED / SOURCE NOT YET IMPLEMENTED`
Authority: `NONE`

## Entry Evidence
1. `export_id` search in `Quality/Integration` returns only the participant exporter and its tests; no evidence-package/evaluator consumer.
2. Evidence-package inspection shows its own payload/response/package digests but no participant-export identity/digest binding.
3. IGT evaluator inspection shows scoring/qualification keyed from run-local `case_id`, `condition`, `response`, and evidence refs; it does not verify that the response corresponds to the sealed participant export now canonical on main.

## Problem
A structurally valid response may be evaluated against a run-local case/condition identity without a local cryptographic link to the exact sealed participant export that was prepared for that row.

## Design Law
`RESPONSE STRUCTURE != RESPONSE-TO-EXPORT BINDING`.

`LOCAL EXPORT BINDING != EXTERNAL DELIVERY != MODEL EXECUTION != PROVIDER AUTHENTICITY`.

## Planned Changes
| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_response_binding.py` | deterministic local response binding to one verified sealed export | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_response_binding.py` | positive + adversarial binding regressions | N | N |
| C03 | `Repository/IGT_RESPONSE_BINDING_CONTRACT_2026-08-29.md` | identity, integrity, state and nonclaim contract | N | N |
| C04 | current Runtime/Integration + Full-Stack CI | exact-head validation | N | N |

## Required Boundaries
1. Input participant export must pass the canonical local export verifier.
2. Response must satisfy `REQUIRED_RESPONSE_FIELDS` before binding.
3. Binding identity includes exact export ID, export package digest, case, condition and baseline SHA.
4. Bound response digest is deterministic.
5. Mutation of export identity/payload or response after binding invalidates verification.
6. No delivery receipt, execution context, provider ID, attestation or external authenticity is fabricated.
7. Maximum local state: `LOCALLY_BOUND_RESPONSE`.
8. Cognitive-effect and authority claims remain absent.

## Explicit Non-Claims
- Local binding does not prove delivery or model execution.
- Local binding does not prove who produced the response.
- Local binding does not establish provider authenticity or execution independence.
- Local binding does not make an IGT participant row externally qualified.
- Local binding does not establish cognitive improvement.

## Tool Incident
Several pre-branch `create_file` attempts returned 404 because the intended branch did not yet exist. GitHub rejected every write before state change; no repository mutation occurred. The branch was then created explicitly from the exact base before this matrix write.

## Verification Plan
Implement smallest binding helper → adversarial regressions → read-back/diff reconciliation → Draft PR → exact-head Runtime/Integration + Full-Stack CI → semantic failure diagnosis → documentation → final-head CI → freeze/reconcile → expected-head squash merge → post-merge exact-main verification.
