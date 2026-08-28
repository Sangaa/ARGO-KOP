# IGT Trusted Resolver Adapter Contract — 2026-08-28

Status: `CONTROLLED CANDIDATE / ADAPTER EXECUTION BOUNDARY / NOT AUTHORITY`
Transaction: `MUT-2026-08-28-IGT-TRUSTED-RESOLVER-ADAPTER-001`
Authority: `NONE`

## Purpose

Define the governed execution boundary between the pure external-evidence correlation layer and future provider-specific evidence acquisition adapters.

The boundary exists to ensure that trusted-path correlation is produced by an adapter invocation controlled by the gate rather than by caller-supplied observation dictionaries.

## Core Separation

`ADAPTER INTERFACE != APPROVED ADAPTER IDENTITY != ADAPTER EXECUTION != PROVIDER-BACKED AUTHENTICITY`.

An adapter can be registered and successfully invoked without proving that its upstream provider is authentic.

## Package Precondition

The gate first executes the existing package validator.

Only:

`STRUCTURALLY_QUALIFIED`

packages may trigger external acquisition.

Invalid or quarantined packages return before adapter identity inspection or acquisition calls.

Required law:

`INVALID PACKAGE -> ZERO EXTERNAL ACQUISITION SIDE EFFECTS`.

## Adapter Identity

Every adapter exposes immutable canonical identity:
- `adapter_id`;
- `adapter_kind`;
- `implementation_id`.

The gate snapshots identity before acquisition, after participant acquisition, and after attestation acquisition.

Any change produces:

`ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION`.

## Approved Registry

The gate accepts an explicit registry mapping adapter ID to the expected canonical identity tuple.

Registry checks reject:
- unknown adapter ID;
- adapter-kind mismatch;
- implementation-ID mismatch;
- non-canonical registry record.

Registry membership establishes only:

`APPROVED PATH ELIGIBILITY`.

It does not establish provider authenticity or authority.

## Acquisition Records

Participant and attestation acquisitions are separate immutable records carrying:
- adapter ID;
- adapter kind;
- acquisition ID;
- acquisition surface;
- start/end timestamps;
- exact requested reference;
- observation payload.

Participant and attestation acquisition IDs must be distinct.

Acquisition time order must be valid.

## Reserved Identity Rule

Observation payloads may not provide:
- `resolver_id`;
- `resolution_id`;
- `requested_ref`.

Those fields are injected only by the governed gate from adapter identity and acquisition records.

Required law:

`OBSERVATION CONTENT MAY NOT SELF-ASSIGN RESOLVER IDENTITY`.

## Correlation Reuse

The trusted-adapter gate does not reimplement external evidence semantics.

After acquisition normalization it delegates to the existing pure correlation layer.

Therefore:
- reference mismatch remains mismatch;
- payload/response digest mismatch remains mismatch;
- unavailable/partial semantics remain unchanged;
- receipt binding semantics remain unchanged.

## Gate Result States

### `PACKAGE_NOT_ELIGIBLE`
Package failed local qualification. Adapter not invoked.

### `ADAPTER_IDENTITY_REJECTED`
Adapter identity surface is non-canonical/incomplete. Adapter not invoked.

### `ADAPTER_NOT_APPROVED`
Adapter identity does not match registry. Adapter not invoked.

### `ADAPTER_EXECUTION_FAILED`
Acquisition raised an error or violated acquisition invariants.

### `APPROVED_ADAPTER_PATH_MISMATCH`
Approved adapter path executed but acquired evidence contradicts package content.

### `APPROVED_ADAPTER_PATH_INCONCLUSIVE`
Approved adapter path executed but pure correlation remained unavailable/partial/inconclusive.

### `APPROVED_ADAPTER_PATH_CORRELATED`
Approved adapter path executed, both acquisition channels correlated, and exact acquisition-bound receipts were passed to the pure correlation layer.

This is the maximum positive state of this transaction.

## No Authenticity Promotion Rule

The gate MUST still report:

`external_authenticity = INCONCLUSIVE`

and:

`provider_backed_authenticity = NOT_ESTABLISHED`.

It MUST NOT return:

`EXTERNAL_AUTHENTICITY_VERIFIED`.

A provider-specific adapter requires its own production validation transaction and independently inspectable acquisition evidence before any later authenticity promotion can be considered.

## Deterministic Test Boundary

A fake adapter may implement the protocol and be registered in test fixtures.

Such a fixture may prove:
- call ordering;
- zero-side-effect preconditions;
- identity stability checks;
- registry matching;
- acquisition normalization;
- semantic delegation to correlation;
- fail-closed behavior.

It cannot prove external provider authenticity.

## Reused Architectural Principle

This contract reuses the existing connector law already present in ARGO repository services:

`NO AUTHORITY INFERENCE FROM TECHNICAL ACCESS`.

The same law applies to evidence acquisition:

`NO AUTHENTICITY INFERENCE FROM ADAPTER INVOCATION ALONE`.

## Current Boundary

`TRUSTED RESOLVER ADAPTER EXECUTION BOUNDARY = CANDIDATE`.

`PROVIDER-SPECIFIC RESOLVER = NOT IMPLEMENTED / NOT VERIFIED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`AUTHORITY = NONE`.
