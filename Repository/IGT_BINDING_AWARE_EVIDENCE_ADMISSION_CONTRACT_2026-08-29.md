# IGT Binding-Aware Evidence Admission Contract

Date: `2026-08-29`
State: `CANDIDATE / LOCAL CORRELATION ONLY`
Authority: `NONE`

## Purpose

Close the local attribution gap between the canonical sealed participant export / response-binding chain and the existing independently supplied model-run evidence package gate.

The admission gate does not replace either existing verifier. It composes them and then verifies exact semantic correlation across their artifacts.

## Required Chain

`VERIFIED PARTICIPANT EXPORT`
→ `VERIFIED LOCAL RESPONSE BINDING`
→ `STRUCTURALLY QUALIFIED MODEL-RUN EVIDENCE PACKAGE`
→ `BINDING-CORRELATED EVIDENCE ADMISSION`

## Correlation Requirements

The model-run package must carry exactly the same:
- participant payload as the sealed export;
- participant response as the local response binding;
- case ID;
- condition;
- repository baseline SHA.

The package payload digest must match the sealed export payload. The package response digest must match the response digest already sealed by the local binding.

The response binding must still point to the exact export ID and export package digest supplied to admission.

## Existing Verifier Authority

The admission gate delegates:
- participant export integrity/blindness to `verify_participant_export()`;
- local export-response identity to `verify_response_binding()`;
- model-run package structural/integrity/independence-attestation qualification to `validate_package()`.

It must not duplicate or weaken these validators merely to make cross-artifact correlation pass.

## Maximum State

`BINDING_CORRELATED_EVIDENCE_ADMISSION`

This state means only:

> the locally verified sealed participant export, locally verified response binding, and structurally qualified model-run evidence package are semantically correlated to the same payload/response/case/condition/baseline artifacts.

## Explicit Separations

`VALID ARTIFACTS != CORRELATED ARTIFACTS`

`CORRELATED ARTIFACTS != EXTERNAL DELIVERY PROOF`

`CORRELATED ARTIFACTS != MODEL EXECUTION AUTHENTICITY`

`CORRELATED ARTIFACTS != PROVIDER AUTHENTICITY`

`CORRELATED ARTIFACTS != INDEPENDENT CONFIRMATION`

`CORRELATED ARTIFACTS != COGNITIVE EFFECT`

## Failure Semantics

Fail closed when:
- export verification fails;
- local binding verification fails;
- evidence package is invalid or quarantined rather than structurally qualified;
- package payload differs from the sealed export;
- package response differs from the bound response;
- case, condition, or baseline differs;
- binding export ID/digest differs from the supplied export;
- package payload/response digests do not correlate with the exact semantic artifacts.

A package may remain valid under its own schema yet fail this admission gate because local cross-artifact attribution is a separate claim.

## Authenticity Boundary

Even a successful admission result must retain:
- `external_delivery = NOT_PROVEN`;
- `model_execution = NOT_AUTHENTICATED_BY_CORRELATION`;
- `provider_authenticity = UNVERIFIED`;
- `authority = NONE`;
- `cognitive_effect = NOT_ESTABLISHED`.

Provider/execution authenticity requires separately observed external evidence and must not be inferred from digest consistency or artifact agreement.
