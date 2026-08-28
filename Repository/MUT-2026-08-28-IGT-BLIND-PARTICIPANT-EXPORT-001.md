# IGT Blind Participant Export Boundary — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-BLIND-PARTICIPANT-EXPORT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@45ed9275e99ea59680507e25b52f9ba4183dba47`
Working branch: `hermuz/igt-blind-participant-export-20260828`
Status: `SOURCE + READ-BACK + ADVERSARIAL PR-CI VERIFIED / FINAL DOC-HEAD CI PENDING`
Authority: `NONE`

## Entry State

- Experience Spine IGT harness = execution-verified.
- Model-run evidence package gate = execution-verified.
- External correlation gate = execution-verified.
- Governed resolver-adapter execution boundary = execution-verified.
- Immutable GitHub artifact resolver = execution-verified.
- Live GitHub immutable artifact acquisition = verified on isolated historical E2E branch.
- Provider-native model execution receipt surface = not found after three materially different repository searches.
- B0/L1/L2 participant runs = unseen.
- Cognitive effect = inconclusive.

## Problem / Law

A governed exact participant-facing export surface was missing.

`PARTICIPANT EXPORT IDENTITY != MODEL EXECUTION IDENTITY != PROVIDER RECEIPT != RESULT AUTHENTICITY`.

This transaction prepares controlled experiment input only.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_participant_export.py` | deterministic sealed participant export + local verifier | Y | Y source/read-back/PR-CI |
| C02 | `Quality/Integration/test_experience_spine_igt_participant_export.py` | B0/L1/L2 + adversarial leakage/digest/baseline/execution tests | Y | Y source/read-back/PR-CI |
| C03 | `Repository/IGT_BLIND_PARTICIPANT_EXPORT_CONTRACT_2026-08-28.md` | lifecycle/blindness/integrity/nonclaim contract | Y | Y source/read-back/PR-CI |
| C04 | current integration suite | exact-head discovery/execution | Y | Y — 405 passed |

## D14 — Candidate Visibility Is Not Correctness Disclosure

Pre-CI review found the first leakage concept too broad: evaluator `accepted_actions` values may legitimately occur as participant-visible candidate labels.

Correction:
- evaluator-only field names remain forbidden;
- candidate labels are not forbidden merely because the evaluator references them.

Law:
`CANDIDATE LABEL VISIBILITY != CORRECTNESS DISCLOSURE`.

## D15 — Generic `score` Key Has Multiple Semantics

First PR-CI head `866762205c300674f0b61398714b38e8d0091c2a`:
- Runtime run `33210784270`;
- merge ref `5c762eca377cf1a6c626b88e28237adfff5309e9` = merge candidate into exact base;
- Prototype PASS;
- Integrity PASS;
- Integration FAIL: `390 passed / 10 failed` out of 400 discovered tests.

All failures were `FORBIDDEN_EXPORT_KEYS:score`.

Root cause: L1/L2 Experience Spine items intentionally contain retrieval/ranking `score`; this is not evaluator result scoring.

Correction: generic `score` removed from global forbidden-key set; evaluator-specific result surfaces remain forbidden.

Law:
`FIELD NAME EQUALITY != SEMANTIC EQUALITY`.

## D16 — Legitimate L2 Provenance Can Equal an Evaluator Non-Claim

Second PR-CI head `f40dababd0cede83ac11ca53b628277873d2594c`:
- Runtime run `33210916885`;
- merge ref `90749e9548d4f9340fe6fa00336c28f6abce0c84`;
- Prototype PASS;
- Integrity PASS;
- Integration FAIL: `397 passed / 3 failed`.

The phrase `CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION` is deliberately exposed by the L2 provenance envelope and also appears in evaluator expectations.

Correction attempt: make evaluator-value leakage path-aware for nonclaims.

## D17 — The Same L2 Provenance Value Can Also Be a Target Invariant

Third PR-CI head `33ca602a3d39b344fa552b8f512203dbb2b842c2`:
- Runtime run `33211090728`;
- merge ref `ae298ec2ba7e169b6d6020d431a7b03833cf7553`;
- Prototype PASS;
- Integrity PASS;
- Integration FAIL: `398 passed / 5 failed`.

The same phrase was present in both evaluator target/nonclaim expectations and the intentionally exposed L2 provenance boundary.

Final correction:
- hidden evaluator **field names** remain globally forbidden;
- evaluator target/nonclaim **values** are permitted only under the existing harness-created path `participant_payload/provenance_envelope`;
- the same values anywhere else fail closed;
- B0/L1 remain free of those hidden values;
- adversarial tests inject the same value outside provenance and require rejection.

Law:
`VALUE EQUALITY != EVALUATOR LEAKAGE; ORIGIN / PATH + CONDITION DETERMINE AUTHORIZED DISCLOSURE`.

This preserves the experimental meaning of L2 instead of accidentally censoring the provenance signal being tested.

## Successful Repair-Head Evidence

Head: `17c360f4b04ee2a6b70e926b8ad6b757e406251c`.

Runtime/Prototype/Integration run: `33211294596` — SUCCESS.
- prototype = SUCCESS;
- integrity = SUCCESS;
- integration job `98984857466` = SUCCESS;
- integration result = `405 passed, 1 warning, 11 subtests passed`;
- prior canonical baseline = 383 tests;
- net new discovered tests = 22.

PR merge-ref checkout:
`4bc3a6114c70c8638a4cf5aa44c4c8dc4296f158 = Merge 17c360f4... into 45ed9275...`.

Full-Stack run `33211294563` — SUCCESS.

Expected P2 identity warning remains unchanged and is not treated as an index defect.

## Hardened Boundary

- Export delegates condition materialization to existing `build_condition_payload()`.
- Exact 40-hex baseline SHA mandatory.
- Stable deterministic export ID; no timestamp/random identity.
- Full package SHA-256 digest.
- Response contract identical across B0/L1/L2.
- B0 = no Experience Spine material.
- L1 = decision view only.
- L2 = same decision view + governed provenance envelope.
- Evaluator field surfaces fail closed.
- Overlapping evaluator values are accepted only in the authorized L2 provenance path.
- Experience-item `score` remains legitimate retrieval metadata.
- Participant evidence/provider receipt remain null before execution.
- Premature execution/authenticity claims fail.

## Read-Back / Diff Boundary

Initial exact-base reconciliation showed exactly 4 declared paths, zero behind, and no Runtime, Services, provider connector, cognition, memory, workflow, or production-dispatch mutation.

## Explicit Non-Claims

- Export generation is not external delivery.
- External delivery is not model execution.
- Sealed export is not evidence that a model received it.
- GitHub storage is not evidence that a model consumed it.
- No B0/L1/L2 participant row becomes seen.
- No provider authenticity or cognitive-effect claim is promoted.

## Final Gate

The successful repair-head CI is pre-documentation evidence. This documentation commit changes the candidate head, therefore it must receive fresh exact-head Runtime/Integration + Full-Stack CI before freeze/merge.

Potential bounded result after that gate:

`BLIND PARTICIPANT EXPORT BOUNDARY = EXECUTION-VERIFIED`.

while:
`EXTERNAL DELIVERY = NOT PROVEN`;
`MODEL EXECUTION = NOT PROVEN`;
`PROVIDER AUTHENTICITY = NOT PROVEN`;
`IGT PARTICIPANT EVIDENCE = UNSEEN`;
`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
