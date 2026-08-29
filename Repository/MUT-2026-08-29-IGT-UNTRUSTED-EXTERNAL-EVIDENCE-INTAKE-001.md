# IGT Untrusted External Evidence Intake — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-UNTRUSTED-EXTERNAL-EVIDENCE-INTAKE-001`
Base: `main@949acd74d65751786bc732a65902fbb00271d685`
Branch: `hermuz/igt-untrusted-external-evidence-intake-20260829`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT`
Status: `MATRIX OPEN / SOURCE MUTATION PENDING`
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

A future real provider receipt, delivery observation, attestation, or externally supplied response currently has no bounded first-entry surface that can preserve the artifact while refusing to trust it.

Without such a boundary, an operator may accidentally convert `received evidence` into `authenticated evidence` merely because the artifact exists locally.

## Design Law

`RECEIVED EXTERNAL EVIDENCE != AUTHENTICATED EXTERNAL EVIDENCE`.

The intake boundary must:
1. preserve raw supplied evidence without semantic rewriting;
2. seal source/channel/type/claim metadata and evidence digest;
3. assign deterministic intake identity;
4. quarantine all external claims by default;
5. refuse pre-promoted trust/authenticity/authority states;
6. remain independent of provider-specific transport code;
7. expose the artifact for later resolver/correlation/attestation stages without claiming those stages ran.

## Planned Paths

| ID | Target | Purpose | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_external_evidence_intake.py` | deterministic untrusted evidence envelope + verifier | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_external_evidence_intake.py` | positive/adversarial regressions | N | N |
| C03 | `Repository/IGT_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE_CONTRACT_2026-08-29.md` | semantic and non-claim contract | N | N |
| C04 | this matrix | source/read-back/CI/closure evidence | Y | source only |

## Explicit Non-Claims

- Intake is not external delivery proof.
- Intake is not model execution proof.
- Intake is not provider authentication.
- A provider-looking request ID is still a claim until independently verified.
- A locally stored receipt is not proof the provider created it.
- Quarantine admission grants no authority and no cognitive-effect claim.

## Verification Plan

`SOURCE → READ-BACK → EXACT DIFF → DRAFT PR → EXACT-HEAD CI → FAILURE ANALYSIS/REPAIR → FINAL-HEAD CI → CONCURRENCY RECHECK → EXPECTED-SHA SQUASH MERGE → POST-MERGE EXACT-MAIN CI`
