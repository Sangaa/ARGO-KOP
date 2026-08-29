# IGT Untrusted External Evidence Intake — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-UNTRUSTED-EXTERNAL-EVIDENCE-INTAKE-001`
Base: `main@949acd74d65751786bc732a65902fbb00271d685`
Branch: `hermuz/igt-untrusted-external-evidence-intake-20260829`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT`
Status: `SOURCE IMPLEMENTED / READ-BACK RECONCILED / CI PENDING`
Authority: `NONE`

## Entry Evidence

Current canonical chain can verify and correlate:
- sealed participant export;
- locally bound participant response;
- structurally qualified model-run evidence package;
- binding-aware local evidence admission.

Current canonical contract explicitly keeps `external_delivery`, `model_execution authenticity`, and `provider_authenticity` unproven.

Three prior materially different repository searches found no implemented delivery receipt / transport ID / external-delivery observation surface. `INTF-004` defines transport capability but not observable delivery proof.

## Gap

A future real provider receipt, delivery observation, attestation, or externally supplied response had no bounded first-entry surface that could preserve the artifact while refusing to trust it.

Without such a boundary, an operator could accidentally convert `received evidence` into `authenticated evidence` merely because the artifact exists locally.

## Design Law

`RECEIVED EXTERNAL EVIDENCE != AUTHENTICATED EXTERNAL EVIDENCE`.

The intake boundary:
1. preserves raw supplied evidence without semantic rewriting;
2. seals source/channel/type/claim metadata and evidence digest;
3. assigns deterministic intake identity;
4. quarantines all external claims by default;
5. refuses pre-promoted trust/authenticity/authority states;
6. remains independent of provider-specific transport code;
7. exposes the artifact for later resolver/correlation/attestation stages without claiming those stages ran.

## Applied Paths

| ID | Target | Purpose | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_external_evidence_intake.py` | deterministic untrusted evidence envelope + verifier | Y | Y source/read-back |
| C02 | `Quality/Integration/test_experience_spine_igt_external_evidence_intake.py` | positive/adversarial regressions | Y | Y source/read-back; CI pending |
| C03 | `Repository/IGT_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE_CONTRACT_2026-08-29.md` | semantic and non-claim contract | Y | Y source/read-back |
| C04 | this matrix | source/read-back/CI/closure evidence | Y | Y source/read-back |

## Exact Diff Reconciliation

From exact base `949acd74d65751786bc732a65902fbb00271d685` before this documentation update:
- ahead = 4;
- behind = 0;
- merge base = exact canonical base;
- exactly four changed paths;
- all changed paths are declared above;
- no Runtime, Services, provider connector, workflow, cognition, memory or authority surface changed.

## Explicit Non-Claims

- Intake is not external delivery proof.
- Intake is not model execution proof.
- Intake is not provider authentication.
- A provider-looking request ID is still a claim until independently verified.
- A locally stored receipt is not proof the provider created it.
- Quarantine admission grants no authority and no cognitive-effect claim.

## Maximum Candidate State

`VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE`

while:

`EXTERNAL DELIVERY = NOT PROVEN`

`MODEL EXECUTION AUTHENTICITY = NOT PROVEN`

`PROVIDER AUTHENTICITY = UNVERIFIED`

`AUTHORITY = NONE`

`COGNITIVE EFFECT = NOT ESTABLISHED`

## Verification Plan

`SOURCE → READ-BACK → EXACT DIFF → DRAFT PR → EXACT-HEAD CI → FAILURE ANALYSIS/REPAIR → FINAL-HEAD CI → CONCURRENCY RECHECK → EXPECTED-SHA SQUASH MERGE → POST-MERGE EXACT-MAIN CI`
