# IGT Sealed Export → Participant Response Binding — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-RESPONSE-BINDING-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@19805fbb948f4ae32e1c97169cc4f50b80681812`
Working branch: `hermuz/igt-response-binding-20260829`
Status: `SOURCE VERIFIED / READ-BACK VERIFIED / PR-CI VERIFIED / LIFECYCLE REPLACEMENT REQUIRED`
Authority: `NONE`

## Entry Evidence
1. `export_id` search in `Quality/Integration` returned only the participant exporter and its tests; no evidence-package/evaluator consumer.
2. Evidence-package inspection showed its own payload/response/package digests but no participant-export identity/digest binding.
3. IGT evaluator inspection showed scoring/qualification keyed from run-local `case_id`, `condition`, `response`, and evidence refs; it did not verify that the response corresponds to the sealed participant export now canonical on main.

## Problem
A structurally valid response could be evaluated against a run-local case/condition identity without a local cryptographic link to the exact sealed participant export that was prepared for that row.

## Design Law
`RESPONSE STRUCTURE != RESPONSE-TO-EXPORT BINDING`.

`LOCAL EXPORT BINDING != EXTERNAL DELIVERY != MODEL EXECUTION != PROVIDER AUTHENTICITY`.

## Applied Changes
| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_response_binding.py` | deterministic local response binding to one verified sealed export | Y | Y source/read-back/CI |
| C02 | `Quality/Integration/test_experience_spine_igt_response_binding.py` | six-row plus adversarial binding regressions | Y | Y source/read-back/CI |
| C03 | `Repository/IGT_RESPONSE_BINDING_CONTRACT_2026-08-29.md` | identity, integrity, state and nonclaim contract | Y | Y source/read-back |
| C04 | Runtime/Prototype/Integrity/Integration + Full-Stack CI | exact-head validation | Y | Y on both implementation and documentation heads |

## Implemented Boundaries
1. Input participant export must pass the canonical local export verifier.
2. Response must satisfy exactly `REQUIRED_RESPONSE_FIELDS`; extra provider/execution/transport metadata is rejected at this boundary.
3. Binding identity includes exact export ID, export package digest, experiment, case, condition, baseline SHA and response digest.
4. Bound response digest and whole binding package digest are deterministic.
5. Mutation of response content, export identity/payload, case, condition or baseline invalidates verification.
6. Export swap is detected even when the replacement export is independently valid.
7. No delivery receipt, execution context, provider ID, attestation or external authenticity is fabricated.
8. Maximum artifact state is `LOCALLY_BOUND_RESPONSE`; verifier maximum is `VERIFIED_LOCAL_BINDING`.
9. Cognitive-effect and authority claims remain absent.

## PR / CI Evidence

Initial Draft PR: `#83 — IGT: bind participant response to sealed export`.

Implementation head:
`812dc0d5ded8ad8045215a61705190c17faaf630`

Observed implementation merge ref:
`0e52c4759cc03a5c8c93f2000f9d062e182c3e07`
= `Merge 812dc0d5ded8ad8045215a61705190c17faaf630 into 19805fbb948f4ae32e1c97169cc4f50b80681812`.

Implementation-head CI:
- Prototype: SUCCESS
- Integrity: SUCCESS
- Integration: SUCCESS
- Full-Stack: SUCCESS
- Integration discovery: `421 passed, 1 warning, 11 subtests passed`
- Prior canonical baseline: `405 passed`
- Added discovered coverage: `+16 tests`

Documentation/freeze head:
`95e7161ffb2eda0fb96b5754813c1b6f1768d84a`

Documentation-head CI:
- Runtime/Prototype/Integrity/Integration workflow #1611: SUCCESS
- Full-Stack Repository Audit #1858: SUCCESS

Freeze reconciliation before lifecycle conversion attempt:
- current main remained `19805fbb948f4ae32e1c97169cc4f50b80681812`;
- PR head remained `95e7161ffb2eda0fb96b5754813c1b6f1768d84a`;
- mergeable = true;
- ahead = 5;
- behind = 0;
- exactly 4 changed files, all declared by this mutation.

The remaining integration warning is the pre-existing P2 internal-ID audit warning; this transaction does not reinterpret or mutate that scope.

## Tool / Lifecycle Incidents

### T01 — pre-branch write order
Several `create_file` attempts returned 404 because the intended branch did not yet exist. GitHub rejected every write before state change; no repository mutation occurred. The branch was then created explicitly from the exact base before the first successful matrix write.

### T02 — Draft → Ready connector schema failure
After final-head CI and clean freeze reconciliation, the connector's `markPullRequestReadyForReview` call failed on an upstream GraphQL response selection requesting non-existent Repository field `fullDatabaseId`.

A direct re-read confirmed PR #83 remained `draft=true`. A guarded REST merge attempt with exact expected head was then rejected by GitHub with HTTP 405 `Pull Request is still a draft`; no merge occurred and main remained unchanged.

Safe lifecycle disposition:
- close PR #83 without merge;
- preserve the exact branch/head;
- open a replacement non-draft PR from the same head to the same unchanged base;
- require fresh PR CI on the replacement merge ref before any merge.

Reusable laws:
`REJECTED PRECONDITION WRITE != REPOSITORY MUTATION`.

`TOOL-SURFACE LIFECYCLE FAILURE MUST NOT BE BYPASSED BY STATE ASSUMPTION`.

`SAME BRANCH + SAME BASE STILL REQUIRES FRESH REPLACEMENT-PR MERGE-REF CI AFTER LIFECYCLE RECREATION`.

## Explicit Non-Claims
- Local binding does not prove delivery or model execution.
- Local binding does not prove who produced the response.
- Local binding does not establish provider authenticity or execution independence.
- Local binding does not make an IGT participant row externally qualified.
- Local binding does not establish cognitive improvement.
- Green CI does not grant repository authority beyond the bounded local-binding claim.

## Final Verification Plan
1. Close #83 without merge after this head is re-verified.
2. Open replacement non-draft PR from the same branch/head to unchanged main.
3. Require fresh Runtime/Integration + Full-Stack CI on the replacement PR merge ref.
4. Reconcile main/head/diff again.
5. Squash merge with exact expected head SHA only if clean.
6. Verify post-merge exact main with Runtime/Integration + Full-Stack (+ normal main workflows).

## Bounded Result If Final Verification Passes

`SEALED EXPORT → RESPONSE LOCAL ATTRIBUTION = EXECUTION-VERIFIED`.

while:

`EXTERNAL DELIVERY = NOT PROVEN`.

`MODEL EXECUTION = NOT PROVEN`.

`PROVIDER AUTHENTICITY = NOT PROVEN`.

`IGT PARTICIPANT EVIDENCE QUALIFICATION = NOT ESTABLISHED BY THIS BOUNDARY`.

`COGNITIVE EFFECT = INCONCLUSIVE`.
