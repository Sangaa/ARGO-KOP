# IGT Untrusted External Evidence Intake Contract

Date: `2026-08-29`
State: `CANDIDATE / QUARANTINE ENTRY ONLY`
Authority: `NONE`

## Purpose

Define the first governed entry boundary for externally supplied IGT evidence before any provider authentication, independent resolution, cross-artifact correlation, or authority decision.

The intake boundary exists so that a future real delivery receipt, model-execution receipt, provider attestation, participant response, or other external artifact can be preserved without being believed merely because it was received.

## Required Semantic Separation

`RECEIVED ARTIFACT != AUTHENTICATED ARTIFACT`

`PROVIDER-LOOKING IDENTIFIER != PROVIDER-VERIFIED IDENTIFIER`

`SUCCESS-LIKE STATUS != VERIFIED EXECUTION`

`LOCAL STORAGE != EXTERNAL DELIVERY PROOF`

`SEALED QUARANTINE != AUTHORITY`

## Intake Responsibilities

The intake boundary SHALL:
- preserve the supplied raw evidence value without semantic rewriting;
- bind it to an exact repository baseline SHA;
- record a non-empty source channel and source reference;
- classify the external artifact type;
- preserve separately supplied external claims as claims;
- compute a digest over the raw evidence;
- derive a deterministic intake identity from source/type/claims/evidence digest/baseline;
- seal the full quarantine envelope with an envelope digest;
- retain `UNTRUSTED_QUARANTINED` as the only successful trust state;
- declare the next required stage as independent resolution or provider-backed authentication.

## Supported Artifact Classes

- `DELIVERY_RECEIPT`
- `MODEL_EXECUTION_RECEIPT`
- `PROVIDER_ATTESTATION`
- `PARTICIPANT_RESPONSE`
- `OTHER_EXTERNAL_EVIDENCE`

Artifact class describes what the supplied object claims or appears to represent. It does not authenticate the claim.

## Fail-Closed Rules

The builder/verifier SHALL reject or invalidate:
- invalid/non-full repository baseline identities;
- missing source channel or source reference;
- unsupported artifact types;
- absent raw evidence;
- non-mapping external claim containers;
- pre-promoted external claim states such as `AUTHENTICATED`, `VERIFIED_PROVIDER`, `EXTERNAL_AUTHENTICITY_VERIFIED`, `EXECUTION_VERIFIED`, `DELIVERY_VERIFIED`, `AUTHORIZED`, or `PROMOTED`;
- post-intake mutation of raw evidence;
- source/type/claim identity drift;
- trust-state promotion inside the intake envelope;
- claim-boundary promotion;
- envelope digest mismatch.

## Provider Identifier Rule

Fields such as `provider_request_id`, `provider_response_id`, provider name, model name, signatures, or status text may be preserved verbatim inside raw evidence or external claims.

Their presence is not evidence that the provider created them.

The intake boundary therefore MUST keep:
- `external_delivery = NOT_PROVEN`;
- `model_execution_authenticity = NOT_PROVEN`;
- `provider_authenticity = UNVERIFIED`;
- `independence = UNVERIFIED`;
- `authority = NONE`;
- `cognitive_effect = NOT_ESTABLISHED`.

## Relationship to Existing IGT Evidence Chain

The intake boundary is earlier than trust establishment.

Possible later flow:

`EXTERNAL ARTIFACT`
→ `UNTRUSTED QUARANTINE INTAKE`
→ `INDEPENDENT ACQUISITION / PROVIDER-BACKED AUTHENTICATION`
→ `CORRELATION / ATTESTATION CHECKS`
→ `BINDING-AWARE EVIDENCE ADMISSION`
→ `EVALUATION`

The exact later order may depend on artifact class, but intake itself cannot skip any trust-establishing stage.

## Maximum State

`VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE`

This state proves only that ARGO preserved and sealed a supplied external artifact under quarantine semantics without silently promoting its claims.
