# IGT Model-Run Evidence Package — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-MODEL-RUN-EVIDENCE-PACKAGE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`
Working branch: `hermuz/igt-model-run-evidence-package-20260828`
PR: `#78`
Status: `PACKAGE GATE EXECUTION-VERIFIED ON REPAIR HEAD / FINAL DOC-HEAD CI REQUIRED / EXTERNAL AUTHENTICITY UNVERIFIED`
Authority: `NONE`

## Entry State

Experience Spine IGT harness entered this transaction merged and post-merge verified:
- main `eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`;
- Full-Stack `33204445745` — SUCCESS;
- Runtime/Integration `33204445751` — SUCCESS;
- M2 `33204445740` — SUCCESS.

Participant B0/L1/L2 evidence remains `UNSEEN`; cognitive effect remains `INCONCLUSIVE`.

## Core Separation

`STRUCTURAL VALIDITY != INTERNAL INTEGRITY != EXTERNAL AUTHENTICITY != COGNITIVE EFFECT`.

A free-form file that declares `MODEL_RUN`, `INDEPENDENT`, or `PASS` is not proof of those claims.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_evidence_package.py` | canonical sealing/digests, structural/integrity/contamination/condition/independence validation, duplicate identity detection | Y | Y |
| C02 | `Quality/Integration/test_experience_spine_igt_evidence_package.py` | 15 discovered regressions for B0/L1/L2, tampering, contamination, identity, quarantine, duplicate evidence and authenticity non-claims | Y | Y |
| C03 | `Repository/IGT_MODEL_RUN_EVIDENCE_PACKAGE_CONTRACT_2026-08-28.md` | portable evidence contract, state model, transport/resolver/authenticity boundaries | Y | Y |
| C04 | `Quality/Integration/experience_spine_igt.py` | D07 repair: remove packet-level `authority_boundary` from L1 decision view while preserving it in L2 provenance envelope | Y | Y |
| C05 | current integration suite | exact-head discovery/execution of package regressions and D07 boundary | Y | Y |

## D07 — L1 Authority-Boundary Leakage Found During Reuse

Reinspection of merged `materialize_experience_views()` found an unasserted condition-isolation defect:
- per-item provenance, `correlated_evidence_groups`, and `evidence_boundary` were removed from L1;
- `authority_boundary` was copied into L2 provenance correctly;
- but the same packet-level `authority_boundary` still remained in L1.

Smallest repair:

`decision.pop("authority_boundary", None)`.

Permanent regression now proves:
1. harness-generated L1 excludes `authority_boundary`;
2. a resealed L1 package that reintroduces it is `INVALID` while `internal_integrity` can still be `PASS`.

Learning:

`CI PASS PROVES TESTED BOUNDARIES; IT DOES NOT PROVE AN UNASSERTED FIELD WAS ABSENT`.

`INTERNAL INTEGRITY CAN COEXIST WITH SEMANTIC INVALIDITY`.

## D08 — Structural Missing vs Qualification Missing

Initial PR CI exposed a state-classification defect.

Head: `93bd512104c35dbb8ecf9f9aeac4d4c63c438651`.

Evidence:
- Full-Stack `33204958898` — SUCCESS;
- Runtime `33204958917` — FAILURE;
- integration job `98963543715` checked out PR merge ref `28057387547f352bfeb8c5695995d0348586a7c4`, explicitly `Merge 93bd5121... into eea81fb5...`;
- result: `330 passed, 1 failed, 1 warning, 11 subtests passed`;
- only failure: `test_l2_requires_provenance_envelope`;
- observed classifier state: `QUARANTINED`;
- required state: `INVALID`.

Root cause: the generic classifier distinguished `MISSING_*` structural keys but did not explicitly classify condition-specific reasons ending in `_MISSING`. Expanding all `_MISSING` to INVALID would have incorrectly converted missing external evidence references—qualification incompleteness—into structural invalidity.

Repair introduced an explicit structural-condition set:
- `L1_EXPERIENCE_PACKET_MISSING`;
- `L1_EXPERIENCE_ITEMS_NOT_LIST`;
- `L2_EXPERIENCE_PACKET_MISSING`;
- `L2_PROVENANCE_ENVELOPE_MISSING`.

Meanwhile missing external participant/attestation evidence references remain `QUARANTINED` when the fields exist but are empty.

Reusable law:

`MISSING CONDITION-DEFINING SURFACE = INVALID`.

`MISSING EXTERNAL QUALIFICATION EVIDENCE = QUARANTINED`.

## Repair-Head CI

Repair head: `8edb9ef2cfdd45dd7535861d775341b2a4757e6a`.

- Full-Stack `33205064015` — SUCCESS;
- Runtime/Integration `33205064000` — SUCCESS;
- integration job `98963898554` — SUCCESS;
- actual GitHub checkout = PR merge ref `0450d672989ba88b1685a817a2c4716ba54724cd`, explicitly `Merge 8edb9ef2... into eea81fb5...`;
- command = `python -m pytest -q Quality/Integration`;
- result = `331 passed, 1 warning, 11 subtests passed in 8.37s`.

Current exact-main baseline before this transaction = `316` integration tests.

Therefore the package-gate transaction contributes exactly `15` discovered integration regressions.

## Package State Model

- `INVALID` — malformed, identity-mismatched, evaluator-contaminated, condition-isolation-invalid, or digest-invalid.
- `QUARANTINED` — structurally parseable/intact but independence or required external qualification evidence is incomplete.
- `STRUCTURALLY_QUALIFIED` — all local structure/integrity/attestation-field gates pass.
- `external_authenticity = UNVERIFIED` remains mandatory after local qualification.
- `EXTERNALLY_VERIFIED` is reserved for a future resolver-backed transaction.

## Integrity / Authenticity Boundary

The package carries SHA-256 digests for participant payload, participant response, and canonical package content excluding only `package_digest` from its own hash.

`HASH MATCH != SOURCE AUTHENTICITY`.

`HASH MATCH != MODEL IDENTITY`.

`STRUCTURALLY_QUALIFIED != EXTERNALLY_VERIFIED`.

Correct digests never rescue evaluator contamination or condition leakage.

## Duplicate Evidence Boundary

Duplicate `package_id` or repeated `(run_id, case_id, condition, execution_context_id)` identity is surfaced and never counted as independent corroboration.

Changing only package filename/package ID does not create a new execution event.

## Non-Claims

- No provider/model execution was authenticated by this transaction.
- No deterministic test package populates B0/L1/L2 participant evidence.
- External model-run authenticity remains `UNVERIFIED`.
- Experience Spine cognitive effect remains `INCONCLUSIVE`.
- Package-gate CI does not establish learning, broad generalization, model-weight change, or promotion authority.

## Remaining Closure Gates

1. Run exact-head Full-Stack + Runtime/Integration after this evidence documentation commit.
2. Freeze if PASS.
3. Re-read main, #78, open PR surface and exact five-path diff.
4. Mark ready and squash merge only with expected frozen head SHA.
5. Require post-merge exact-main Full-Stack + Runtime/Integration verification.
6. External resolver/authenticity verification remains a separate future transaction.

## Bounded Result

`MODEL-RUN EVIDENCE PACKAGE GATE = EXECUTION-VERIFIED ON REPAIR HEAD`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
