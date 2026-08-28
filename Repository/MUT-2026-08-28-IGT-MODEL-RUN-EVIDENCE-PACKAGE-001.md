# IGT Model-Run Evidence Package — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-MODEL-RUN-EVIDENCE-PACKAGE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`
Working branch: `hermuz/igt-model-run-evidence-package-20260828`
Status: `PRE-WRITE / EVIDENCE-TRANSPORT HARDENING`
Authority: `NONE`

## Entry State

Experience Spine IGT harness is merged and post-merge verified on exact main:

- merge `eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78`;
- Full-Stack `33204445745` — SUCCESS;
- Runtime/Integration `33204445751` — SUCCESS;
- M2 `33204445740` — SUCCESS.

Participant B0/L1/L2 evidence remains `UNSEEN` and cognitive effect remains `INCONCLUSIVE`.

## Problem

The repository can now construct and evaluate IGT runs, but it does not yet define a machine-checkable portable evidence package for independently produced model runs.

A free-form file that merely declares `MODEL_RUN`, `INDEPENDENT`, or `PASS` is insufficient evidence.

Required separation:

`STRUCTURAL VALIDITY != INTERNAL INTEGRITY != EXTERNAL AUTHENTICITY != COGNITIVE EFFECT`.

## Target Invariants

1. A package cannot self-authorize or self-promote.
2. Package structure and digest integrity may be verified locally; external execution authenticity may not be inferred from them.
3. Hidden evaluator expectations/correct-answer keys are contamination and quarantine the package.
4. B0/L1/L2 information boundaries must remain inspectable in the captured participant payload.
5. Package case/condition/run identities must agree across metadata and payload.
6. Independence attestation must be explicit across execution, information, state, temporal, and mutation dimensions.
7. Source conclusion withholding and leakage clearance are mandatory for qualification.
8. A `MODEL_RUN` package requires externally resolvable participant evidence reference(s), not only embedded narrative.
9. Canonical hashing must exclude the package's own digest field and remain deterministic.
10. Duplicate package IDs or duplicate run identity cannot silently become independent evidence.
11. Validation failure must preserve reasons; it must not collapse into generic FAIL or PASS.
12. A structurally valid package remains `EXTERNAL_AUTHENTICITY_UNVERIFIED` until an independent evidence resolver validates its referenced execution source.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_evidence_package.py` | ADD | canonical package digest, structural validation, condition-isolation checks, contamination detection, qualification and external-authenticity boundary | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_evidence_package.py` | ADD | regressions for digest tampering, hidden-answer contamination, B0/L1/L2 leakage, identity mismatch, independence/quarantine, duplicate identity and non-claims | N | N |
| C03 | `Repository/IGT_MODEL_RUN_EVIDENCE_PACKAGE_CONTRACT_2026-08-28.md` | ADD | portable package contract and state transitions for external model-run evidence | N | N |
| C04 | current integration suite | VERIFY | exact-head CI discovers and executes package-gate tests | N | N |

## Intended Package Layers

### Participant payload
Exact B0/L1/L2 participant-visible input plus structured response.

### Execution provenance
Model/provider label, model instance/context ID, execution surface, timestamps, repository baseline, run/case/condition identity.

### Independence attestation
Explicit YES/NO/UNKNOWN dimensions plus source-conclusion withholding and leakage result.

### Evidence references
Externally resolvable references for participant execution evidence and independence attestation.

### Integrity
Deterministic SHA-256 over canonical JSON excluding the package digest field.

Integrity proves only that the package content did not change relative to the recorded digest. It does not prove who produced the content or that the referenced model actually executed.

## State Model

- `INVALID` — malformed, mismatched, contaminated, or digest-invalid.
- `QUARANTINED` — structurally parseable but independence/leakage/evidence-reference requirements fail.
- `STRUCTURALLY_QUALIFIED` — local structure/integrity/attestation gates pass.
- `EXTERNAL_AUTHENTICITY_UNVERIFIED` — mandatory state after local qualification until external execution evidence is independently resolved.
- `EXTERNALLY_VERIFIED` — reserved for a later resolver-backed step; this transaction does not manufacture it.

## Explicit Non-Claims

- SHA-256 is not proof of model identity.
- Embedded timestamps are not temporal independence proof by themselves.
- An attestation object is not independent evidence merely because its fields say YES.
- CI can verify the package gate, not the cognitive result.
- No B0/L1/L2 participant row will be populated by deterministic fixtures from this transaction.

## Verification Plan

1. Implement canonical package and validation helpers.
2. Test positive structural path and adversarial contamination/tampering paths.
3. Read back all changed paths and reconcile exact diff.
4. Open draft PR from exact main base.
5. Require exact-head Full-Stack + Runtime/Integration CI and inspect execution count/log evidence.
6. Document harness result separately from external authenticity and cognitive effect.

## Closure Boundary

Potential result:

`MODEL-RUN EVIDENCE PACKAGE GATE = EXECUTION-VERIFIED`

while:

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED`

and:

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
