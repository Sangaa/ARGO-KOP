# IGT Blind Participant Export Boundary — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-BLIND-PARTICIPANT-EXPORT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@45ed9275e99ea59680507e25b52f9ba4183dba47`
Working branch: `hermuz/igt-blind-participant-export-20260828`
Status: `SOURCE IMPLEMENTED / READ-BACK RECONCILED / CI PENDING`
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

The repository can construct B0/L1/L2 payloads and evaluate returned evidence packages, but it lacked a governed export boundary for the exact participant-facing artifact that may later be delivered to an independent external model.

Without that boundary, a future operator could accidentally:
- copy hidden evaluator expectations into a prompt;
- add condition/provenance fields outside the harness-defined split;
- mutate the payload after generation;
- omit the exact repository baseline;
- change the response schema between B0/L1/L2;
- confuse participant-input identity with later execution/authenticity evidence.

## Design Law

`PARTICIPANT EXPORT IDENTITY != MODEL EXECUTION IDENTITY != PROVIDER RECEIPT != RESULT AUTHENTICITY`.

This transaction prepares controlled experiment input only. It does not invoke any model and cannot populate participant rows.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_participant_export.py` | deterministic evaluator-free sealed participant export + local verifier | Y | Y source/read-back |
| C02 | `Quality/Integration/test_experience_spine_igt_participant_export.py` | six-row generation plus adversarial leakage/digest/baseline/execution-boundary regressions | Y | Y source/read-back; CI pending |
| C03 | `Repository/IGT_BLIND_PARTICIPANT_EXPORT_CONTRACT_2026-08-28.md` | delivery lifecycle, blindness, response-schema, integrity and nonclaim contract | Y | Y source/read-back |
| C04 | current integration suite | exact-head discovery/execution | Y | CI pending |

## D14 — Candidate Visibility Is Not Evaluator Leakage

Pre-CI test design caught an over-restrictive first draft.

The initial hidden-value scanner treated values from evaluator fields such as `accepted_actions` as forbidden participant text. Existing IGT semantics deliberately allow candidate action labels to appear in the transformed case; what must remain hidden is which candidate the evaluator accepts.

Correction before CI:
- evaluator-only field names remain forbidden;
- target invariant values remain forbidden;
- required non-claim values remain forbidden;
- candidate action/authority/evidence labels are not rejected merely because the hidden evaluator references them.

Reusable law:

`CANDIDATE LABEL VISIBILITY != CORRECTNESS DISCLOSURE`.

A leakage guard that forbids legitimate candidate text can invalidate the experiment while appearing stricter.

## Hardened Boundaries

1. Export delegates B0/L1/L2 materialization to existing `build_condition_payload()` rather than reimplementing the split.
2. Exact 40-hex baseline SHA is mandatory.
3. Export ID is derived from experiment/case/condition/baseline/payload/response contract.
4. Package digest seals the full pre-execution package.
5. Response schema is identical across B0/L1/L2.
6. B0 contains no Experience Spine material.
7. L1 contains decision view only.
8. L2 adds provenance envelope only through the existing harness materializer.
9. Participant evidence and provider receipt remain explicit null pre-execution boundaries.
10. Execution context, independence attestation, provider IDs and authenticity state are never fabricated.
11. Verification detects post-export mutation, identity drift, premature execution claims and evaluator-field injection.
12. Maximum state is `VERIFIED_PARTICIPANT_EXPORT`.

## Read-Back / Diff Reconciliation

Compare from exact base `45ed9275e99ea59680507e25b52f9ba4183dba47` before this documentation update showed:
- ahead = 5;
- behind = 0;
- exactly 4 changed paths;
- all 4 paths declared by this transaction;
- no Runtime, Services, provider connector, cognition, memory, workflow or production dispatch mutation.

## Explicit Non-Claims

- Export generation is not external delivery.
- External delivery is not model execution.
- A sealed prompt/package is not evidence that a model received it.
- A GitHub commit containing an export is not proof a model consumed it.
- No B0/L1/L2 participant row becomes seen by this transaction.
- No provider authenticity or cognitive improvement is promoted.

## Verification Plan

1. Source implementation — PASS.
2. Read-back and exact diff reconciliation — PASS.
3. Open Draft PR from exact main.
4. Require exact-head Runtime/Integration + Full-Stack CI and inspect actual test count/merge ref.
5. Document failure/repair if any.
6. Final documentation-head CI.
7. Freeze/reconcile + expected-SHA squash merge.
8. Post-merge exact-main verification.

## Bounded Result If Verified

`BLIND PARTICIPANT EXPORT BOUNDARY = EXECUTION-VERIFIED`.

while:

`EXTERNAL DELIVERY = NOT PROVEN`.

`MODEL EXECUTION = NOT PROVEN`.

`PROVIDER AUTHENTICITY = NOT PROVEN`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
