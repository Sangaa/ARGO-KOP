# IGT Sealed Export → Participant Response Binding Contract

Date: `2026-08-29`
State: `CANDIDATE / LOCAL BINDING ONLY`
Authority: `NONE`

## Purpose

Prevent a structured IGT participant response from being scored or carried forward as though it belonged to an arbitrary run-local case/condition identity when no local link to the exact prepared participant export has been established.

This contract binds one response to one already-verified `IGT-PARTICIPANT-EXPORT-1` package. It does not authenticate the origin of the response.

## Identity Boundary

A valid local binding is defined by:
- participant `export_id`;
- participant export package digest;
- experiment ID;
- case ID;
- condition (`B0`, `L1`, or `L2`);
- exact repository baseline SHA;
- deterministic response digest.

The derived binding ID therefore changes if the export identity, condition, case, baseline or response content changes.

## Input Gate

Before binding:
1. the participant export must pass `verify_participant_export()`;
2. the participant response must be a mapping;
3. every `REQUIRED_RESPONSE_FIELDS` field must be present;
4. no extra response fields are accepted by this local boundary.

The exact-schema rule prevents execution/provider/transport metadata from being mixed into the semantic participant response.

## Integrity Gate

The binding stores:
- `response_digest` for response integrity;
- `binding_id` for export-response identity;
- `binding_package_digest` for whole-artifact integrity.

Verification also requires the supplied participant export itself to remain locally valid and checks the binding's export ID, export digest, experiment, case, condition and baseline against that export.

## Maximum State

`LOCALLY_BOUND_RESPONSE`

Verification result:

`VERIFIED_LOCAL_BINDING`

means only:

> the local response artifact is deterministically attributable to the exact locally verified participant export supplied to the verifier.

## Explicit Separations

`RESPONSE STRUCTURE != RESPONSE-TO-EXPORT BINDING`

`LOCAL EXPORT BINDING != EXTERNAL DELIVERY`

`LOCAL EXPORT BINDING != MODEL EXECUTION`

`LOCAL EXPORT BINDING != PROVIDER AUTHENTICITY`

`LOCAL EXPORT BINDING != INDEPENDENCE ATTESTATION`

`LOCAL EXPORT BINDING != COGNITIVE EFFECT`

## Forbidden Promotion

This boundary must not populate or infer:
- delivery receipt;
- provider request/response/execution IDs;
- execution context identity;
- independence attestation;
- external authenticity;
- participant evidence qualification;
- cognitive-effect promotion;
- repository authority.

Those require their own evidence surfaces.

## Consumer Rule

A later evidence-package or evaluator adapter may consume a verified local binding, but must not reinterpret local binding as proof of external execution. Provider/execution evidence must remain separately established and correlated.

## Failure Semantics

Fail closed on:
- invalid/tampered participant export;
- missing or unexpected response fields;
- response digest drift;
- export swap;
- case/condition/baseline mismatch;
- binding ID drift;
- binding package digest drift.

No failed binding may be upgraded by multiplicity or by a valid-looking response payload.
