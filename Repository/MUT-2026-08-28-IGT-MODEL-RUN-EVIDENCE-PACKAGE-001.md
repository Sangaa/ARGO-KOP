# IGT Model-Run Evidence Package — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-MODEL-RUN-EVIDENCE-PACKAGE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`
Working branch: `hermuz/igt-model-run-evidence-package-20260828`
Status: `SOURCE IMPLEMENTED / READ-BACK AND CI PENDING / EXTERNAL AUTHENTICITY UNVERIFIED`
Authority: `NONE`

## Entry State

Experience Spine IGT harness entered this transaction merged and post-merge verified:
- main `eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`;
- Full-Stack `33204445745` — SUCCESS;
- Runtime/Integration `33204445751` — SUCCESS;
- M2 `33204445740` — SUCCESS.

Participant B0/L1/L2 evidence remains `UNSEEN`; cognitive effect remains `INCONCLUSIVE`.

## Problem

The repository can construct and evaluate IGT conditions but had no machine-checkable portable evidence package for externally produced model runs.

A file that merely declares `MODEL_RUN`, `INDEPENDENT`, or `PASS` is not evidence of those claims.

Core separation:

`STRUCTURAL VALIDITY != INTERNAL INTEGRITY != EXTERNAL AUTHENTICITY != COGNITIVE EFFECT`.

## Target Invariants

1. Package content cannot self-authorize or self-promote.
2. Local structure/digest integrity never imply external execution authenticity.
3. Hidden evaluator keys or answer mappings are contamination.
4. B0/L1/L2 information boundaries remain inspectable from captured participant payload.
5. Package/run/case/condition/context/baseline identity must reconcile.
6. MI-IGT independence dimensions are explicit and fail closed.
7. Source-conclusion withholding and leakage clearance are mandatory.
8. `MODEL_RUN` requires external participant-evidence and attestation references.
9. Canonical hashing excludes only the package's own digest field and is deterministic.
10. Duplicate package/run identity cannot become independent corroboration by multiplicity.
11. Failure reasons remain explicit.
12. Local success ends at `STRUCTURALLY_QUALIFIED / EXTERNAL_AUTHENTICITY_UNVERIFIED`.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_evidence_package.py` | canonical sealing/digests, structural/integrity/contamination/condition/independence validation, duplicate identity detection | Y | source pending read-back |
| C02 | `Quality/Integration/test_experience_spine_igt_evidence_package.py` | adversarial + positive regressions for B0/L1/L2, tampering, contamination, identity, quarantine, duplicate evidence and authenticity non-claims | Y | source pending read-back |
| C03 | `Repository/IGT_MODEL_RUN_EVIDENCE_PACKAGE_CONTRACT_2026-08-28.md` | portable evidence contract, state model, transport/resolver/authenticity boundaries | Y | source pending read-back |
| C04 | `Quality/Integration/experience_spine_igt.py` | D07 repair: remove `authority_boundary` from L1 decision view while preserving it in L2 provenance envelope | Y | source pending read-back |
| C05 | current integration suite | exact-head execution/discovery of package regressions and D07 boundary | Y | CI pending |

## D07 — Post-Merge IGT Condition-Isolation Defect Found During Reuse

While building the evidence-package gate, reinspection of merged `materialize_experience_views()` found a bounded defect not covered by #77's tests:

- L1 removed per-item provenance, `correlated_evidence_groups`, and `evidence_boundary`;
- L2 correctly received `authority_boundary` in its provenance envelope;
- but L1's decision view still retained the packet-level `authority_boundary`.

This contradicted the intended condition contract: L1 is decision experience without provenance/authority envelope; L2 is the provenance-aware condition.

Smallest repair:

`decision.pop("authority_boundary", None)`.

The package regression now verifies both directions:
1. harness-generated L1 contains no `authority_boundary`;
2. any resealed L1 package that reintroduces `authority_boundary` is `INVALID` even when all digests are internally correct.

Learning:

`CI PASS PROVES TESTED BOUNDARIES; IT DOES NOT PROVE AN UNASSERTED FIELD WAS ABSENT`.

`INTERNAL INTEGRITY CAN COEXIST WITH SEMANTIC INVALIDITY`.

## Package Layers

### Participant material
Exact condition payload + structured response.

### Execution provenance
Model/source/context/surface/timestamps/repository baseline and run identity.

### Independence attestation
Execution, information, state, temporal and mutation independence plus source-conclusion withholding and leakage result.

### External references
`participant_evidence_ref` and `independence_attestation_ref` are required before a model package can enter external resolution.

### Integrity
SHA-256 over canonical JSON for payload, response and package excluding only `package_digest` from the package-level hash.

`HASH MATCH != SOURCE AUTHENTICITY`.

## Local State Model

- `INVALID` — malformed, identity-mismatched, contaminated, condition-leaking, or digest-invalid.
- `QUARANTINED` — structurally parseable/intact but independence or external-reference qualification is incomplete.
- `STRUCTURALLY_QUALIFIED` — all local gates pass.
- external authenticity remains `UNVERIFIED` after local qualification.
- `EXTERNALLY_VERIFIED` is reserved for a later resolver-backed transaction.

## Explicit Non-Claims

- SHA-256 does not authenticate a model/provider.
- Embedded timestamps do not prove temporal independence.
- Embedded `YES` attestation values do not authenticate themselves.
- CI verifies the gate, not an external model run.
- Deterministic fixtures never populate B0/L1/L2 participant results.
- Experience Spine cognitive effect remains `INCONCLUSIVE`.

## Verification Gates

1. Read back all implementation/doc paths.
2. Compare branch against exact base and confirm only declared paths changed.
3. Open draft PR.
4. Require exact-head Full-Stack + Runtime/Integration CI.
5. Inspect integration execution/count evidence.
6. Record any failures and repair only demonstrated defects.
7. Final documentation-head CI, freeze/reconcile, expected-SHA merge, post-merge exact-main verification.

## Closure Boundary

Potential result:

`MODEL-RUN EVIDENCE PACKAGE GATE = EXECUTION-VERIFIED`

while:

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED`

and:

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
