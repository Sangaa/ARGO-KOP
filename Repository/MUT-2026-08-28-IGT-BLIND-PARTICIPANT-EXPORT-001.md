# IGT Blind Participant Export Boundary — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-BLIND-PARTICIPANT-EXPORT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@45ed9275e99ea59680507e25b52f9ba4183dba47`
Working branch: `hermuz/igt-blind-participant-export-20260828`
Status: `PRE-WRITE / PARTICIPANT DELIVERY SURFACE`
Authority: `NONE`

## Entry State

Current canonical evidence:
- Experience Spine IGT harness = execution-verified;
- model-run evidence package gate = execution-verified;
- external correlation gate = execution-verified;
- governed resolver-adapter execution boundary = execution-verified;
- immutable GitHub artifact resolver mechanics = execution-verified;
- live GitHub immutable artifact acquisition = verified on isolated historical E2E branch;
- provider-native model execution receipt surface = not found after three materially different repository searches;
- B0/L1/L2 participant runs = unseen;
- cognitive effect = inconclusive.

## Problem

The repository can construct B0/L1/L2 payloads and evaluate returned evidence packages, but it lacks a governed export boundary for the exact participant-facing artifact that may later be delivered to an independent external model.

Without that boundary, a future operator could accidentally:
- copy hidden evaluator expectations into a prompt;
- add condition labels or provenance fields outside the harness-defined split;
- mutate the payload after generation;
- omit the exact repository baseline;
- change the response schema between B0/L1/L2;
- confuse participant-input identity with later execution/authenticity evidence.

## Design Law

`PARTICIPANT EXPORT IDENTITY != MODEL EXECUTION IDENTITY != PROVIDER RECEIPT != RESULT AUTHENTICITY`.

This transaction prepares controlled experiment input only. It does not invoke any model and cannot populate participant rows.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_participant_export.py` | ADD | deterministic evaluator-free sealed participant export package | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_participant_export.py` | ADD | leakage, digest, baseline, condition-isolation and schema regressions | N | N |
| C03 | `Repository/IGT_BLIND_PARTICIPANT_EXPORT_CONTRACT_2026-08-28.md` | ADD | delivery boundary and nonclaim contract | N | N |
| C04 | current integration suite | VERIFY | exact-head discovery/execution | N | N |

## Target Invariants

1. Export must be derived only through existing `build_condition_payload()`.
2. Exact 40-hex baseline SHA is mandatory.
3. Export has stable package identity derived from experiment/case/condition/baseline/payload.
4. Hidden evaluator expectations, target invariants, accepted actions/authorities, required evidence/nonclaims and scoring state must never appear.
5. Response schema is identical across B0/L1/L2.
6. B0 contains no Experience Spine material.
7. L1 contains decision view only.
8. L2 adds provenance envelope only through the existing harness materializer.
9. Package is hash-sealed; post-export mutation invalidates verification.
10. No participant evidence ref, execution context ID, provider ID, receipt ID or authenticity state is fabricated at export time.
11. Export state is `READY_FOR_EXTERNAL_DELIVERY`, not `MODEL_RUN`.
12. Successful export cannot establish cognitive effect.

## Explicit Non-Claims

- Export generation is not model execution.
- A sealed prompt/package is not evidence that a model received it.
- A GitHub commit containing an export is not proof a model consumed it.
- No B0/L1/L2 participant row becomes seen by this transaction.
- No provider authenticity or cognitive improvement is promoted.
