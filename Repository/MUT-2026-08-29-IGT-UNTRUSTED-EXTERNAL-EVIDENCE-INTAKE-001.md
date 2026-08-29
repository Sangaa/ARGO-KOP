# IGT Untrusted External Evidence Intake — Mutation Matrix

Transaction ID: `MUT-2026-08-29-IGT-UNTRUSTED-EXTERNAL-EVIDENCE-INTAKE-001`
Base: `main@949acd74d65751786bc732a65902fbb00271d685`
Merged Main Commit: `28e3ec16f1b0e6decee6623f77f48cda74e229c7`
Branch: `hermuz/igt-untrusted-external-evidence-intake-20260829`
Protocol: `GOV-013 / applicable Governance + IGT`
Status: `CLOSED / POST-MERGE MAIN CI VERIFIED`
Authority: `NONE`

## Entry Evidence

Current canonical chain can verify and correlate:
- sealed participant export;
- locally bound participant response;
- structurally qualified model-run evidence package;
- binding-aware local evidence admission.

The canonical contract explicitly keeps `external_delivery`, `model_execution authenticity`, and `provider_authenticity` unproven.

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
| C01 | `Quality/Integration/experience_spine_igt_external_evidence_intake.py` | deterministic untrusted evidence envelope + verifier | Y | Y source/read-back/CI |
| C02 | `Quality/Integration/test_experience_spine_igt_external_evidence_intake.py` | positive/adversarial regressions | Y | Y source/read-back/CI |
| C03 | `Repository/IGT_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE_CONTRACT_2026-08-29.md` | semantic and non-claim contract | Y | Y source/read-back/CI |
| C04 | this matrix | source/read-back/CI/closure evidence | Y | Y source/read-back |

## Exact Diff Reconciliation

From exact base `949acd74d65751786bc732a65902fbb00271d685` before the final documentation commit:
- ahead = 4;
- behind = 0;
- merge base = exact canonical base;
- exactly four changed paths;
- all changed paths are declared above;
- no Runtime, Services, provider connector, workflow, cognition, memory or authority surface changed.

## PR CI Evidence

Draft PR: `#86`.

Verified candidate head before final documentation: `0c2ba2c5b24384bb0abe266c409e981177368961`.

GitHub PR merge-ref observed by integration job:
`fab50d027759d038d10d2f2c47fe947335d508df = Merge 0c2ba2c5b24384bb0abe266c409e981177368961 into 949acd74d65751786bc732a65902fbb00271d685`.

Candidate results:
- Prototype = SUCCESS;
- Integrity = SUCCESS;
- Integration = SUCCESS;
- Full-Stack Repository Audit = SUCCESS;
- integration discovery = `462 passed, 1 warning, 11 subtests passed`;
- warning remains the pre-existing P2 identity/index scope warning and is not modified by this transaction.

No CI defect was observed in this candidate cycle.

## Post-Merge Main Closure Evidence

Exact merged main commit inspected: `28e3ec16f1b0e6decee6623f77f48cda74e229c7`.

GitHub Actions observed for that exact SHA:

- `ARGO Runtime Prototype and Integration Tests` — run `33232623143` — `SUCCESS`;
- `Full-Stack Repository Audit` — run `33232623137` — `SUCCESS`;
- `M2 Multi-Channel Proposal Training` — run `33232623139` — `SUCCESS`.

The merged implementation and transaction artifacts were re-read from current repository evidence before this closure update.

Therefore the previously open `FINAL-HEAD CI PENDING` condition is now satisfied for the exact merged functional commit.

This closure remains bounded to this transaction and does not imply repository-wide integrity.

## Explicit Non-Claims

- Intake is not external delivery proof.
- Intake is not model execution proof.
- Intake is not provider authentication.
- A provider-looking request ID is still a claim until independently verified.
- A locally stored receipt is not proof the provider created it.
- Quarantine admission grants no authority and no cognitive-effect claim.

## Maximum Verified State

`VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE`

while:

`EXTERNAL DELIVERY = NOT PROVEN`

`MODEL EXECUTION AUTHENTICITY = NOT PROVEN`

`PROVIDER AUTHENTICITY = UNVERIFIED`

`AUTHORITY = NONE`

`COGNITIVE EFFECT = NOT ESTABLISHED`

## Closure

Transaction state: `CLOSED`.

Next legal continuation is downstream of quarantine only:

`QUARANTINE → INDEPENDENT RESOLUTION / PROVIDER-BACKED AUTHENTICATION → CORRELATION → BINDING → QUALIFICATION → BOUNDED AUTHORITY DECISION`.

No stage may be collapsed or inferred from receipt presence alone.
