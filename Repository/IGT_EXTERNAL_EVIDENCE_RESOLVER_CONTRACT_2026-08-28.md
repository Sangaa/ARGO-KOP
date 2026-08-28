# IGT External Evidence Resolver Contract — 2026-08-28

Status: `CONTROLLED CANDIDATE / CORRELATION CONTRACT / NOT AUTHORITY`
Transaction: `MUT-2026-08-28-IGT-EXTERNAL-EVIDENCE-RESOLVER-001`
Authority: `NONE`

## Purpose

Define the evidence-correlation boundary between a locally qualified IGT model-run package and observations later retrieved from an external execution/attestation source.

This contract does not implement a provider connector and cannot authenticate external execution by declaration.

## Core Separation

`PACKAGE QUALIFICATION != RESOLVER CORRELATION != RESOLVER TRUST != EXTERNAL AUTHENTICITY`.

The pure correlation layer may establish compatibility or incompatibility between a package and resolver observations. It cannot establish that those observations themselves came from a trusted production adapter.

Therefore the pure correlation layer has **no state transition to `EXTERNAL_AUTHENTICITY_VERIFIED`**.

## Eligibility Precondition

External correlation begins only when the package gate returns:

`STRUCTURALLY_QUALIFIED`.

`INVALID` or `QUARANTINED` packages are not resolver-eligible.

## Separate Evidence Channels

### Participant execution observation
Must bind, where the external source exposes them:
- requested and observed participant evidence reference;
- run ID;
- case ID;
- condition;
- execution-context ID;
- repository baseline SHA;
- source model;
- source instance;
- execution surface;
- execution start/end timestamps;
- participant payload digest;
- participant response digest.

### Independence-attestation observation
Must bind:
- requested and observed attestation reference;
- run ID;
- execution-context ID;
- repository baseline SHA;
- full attestation digest;
- full attestation content.

The participant and attestation channels remain separately observable and separately classifiable.

## Resolver Observation States

Every resolver observation declares one of:

- `FOUND` — a target observation was retrieved and can be compared;
- `UNAVAILABLE` — the resolver could not obtain the referenced target;
- `PARTIAL` — some evidence exists but is insufficient for complete comparison.

Even `UNAVAILABLE` and `PARTIAL` are resolver events and therefore require `resolver_id`, `resolution_id`, and the exact `requested_ref`.

`UNAVAILABLE != MISMATCH`.

A missing result from an identified resolver is unresolved evidence, not direct contradiction.

## Correlation Classification

### `CORRELATED`
The requested/observed reference and applicable identity/content bindings match the package.

### `MISMATCH`
Direct incompatible evidence exists, such as:
- requested/observed reference mismatch;
- run/case/condition/context/baseline mismatch;
- model/instance mismatch;
- execution-surface or time mismatch;
- payload/response digest mismatch;
- attestation digest/content mismatch.

### `UNAVAILABLE`
An identified resolver event reports it could not retrieve the target.

### `INCONCLUSIVE`
Partial/ambiguous evidence prevents complete comparison.

## Observation Digest vs Evidence Fingerprint

Two different hashes serve different claims.

### Observation digest
`observation_digest` hashes the complete resolver record, including `resolver_id` and `resolution_id`.

Purpose: bind a receipt to one exact resolver event.

### Evidence fingerprint
`evidence_fingerprint` hashes the observed evidence after excluding resolver-event metadata:
- `resolver_id`;
- `resolution_id`.

Purpose: detect when multiple resolver records are merely repeated representations of the same underlying evidence.

Required law:

`RESOLUTION EVENT IDENTITY != UNDERLYING EVIDENCE IDENTITY`.

Changing only resolver/resolution IDs does not create independent corroboration.

## Resolver Receipt Binding

A receipt may bind:
- resolver ID;
- resolution ID;
- source reference;
- exact observation digest.

Pure correlation may classify such a receipt as `RECEIPT_BOUND` or `RECEIPT_MISMATCH`.

But:

`RECEIPT_BOUND != RESOLVER TRUSTED`.

A caller-supplied receipt cannot authenticate itself.

The pure correlation layer always reports:

`resolver_trust = UNAUTHENTICATED_BY_PURE_CORRELATION`.

## Final Pure-Correlation States

### `PACKAGE_NOT_ELIGIBLE`
Package is not structurally qualified.

### `EXTERNAL_EVIDENCE_MISMATCH`
At least one external observation directly contradicts the package identity/content.

### `EXTERNAL_EVIDENCE_UNAVAILABLE`
Required external evidence could not be retrieved.

### `EXTERNAL_EVIDENCE_INCONCLUSIVE`
Evidence is partial/ambiguous.

### `CORRELATED_UNTRUSTED`
Participant and attestation observations correlate, but trusted receipt/adaptor provenance is absent.

### `CORRELATED_AWAITING_TRUSTED_ADAPTER`
Both observations correlate and receipts bind to the exact observations, but the correlation layer still cannot authenticate the resolver adapter itself.

This is the maximum positive state of this transaction.

## No Pure-Function Verification Rule

The pure module MUST NOT return:

`EXTERNAL_AUTHENTICITY_VERIFIED`.

That state is reserved for a future connector/adapter boundary that can establish how the observations were actually retrieved and bind its trusted execution identity independently of package-supplied content.

## Duplicate Resolver Evidence

The resolver layer detects:
- duplicate `(resolver_id, resolution_id)` events;
- duplicate complete observation digests;
- duplicate underlying evidence fingerprints.

Any such multiplicity must not be interpreted as independent corroboration.

`NEW RESOLUTION_ID != NEW EVIDENCE`.

`NEW RESOLVER_ID != NEW EVIDENCE` when the underlying evidence fingerprint is unchanged.

## Claim Boundaries

A later trusted resolver may establish only the authenticity of the exact external evidence event/package binding.

It does not by itself establish:
- IGT transfer PASS;
- broad generalization;
- model-weight change;
- learning promotion;
- governance authority.

## Current Boundary

`EXTERNAL EVIDENCE CORRELATION GATE = LOCAL/DETERMINISTIC`.

`PRODUCTION TRUSTED RESOLVER ADAPTER = NOT IMPLEMENTED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`AUTHORITY = NONE`.
