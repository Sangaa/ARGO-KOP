# IGT Quarantine Resolution Contract

Date: `2026-08-29`
State: `CANDIDATE / RESOLUTION BOUNDARY`
Authority: `NONE`

## Purpose

Define the first downstream trust-state transition after a verified untrusted external-evidence intake.

The boundary permits ARGO to distinguish:

`I preserved a supplied artifact`

from:

`an approved technical resolver path re-acquired the exact same JSON value from the exact same source reference`.

It deliberately stops before provider/model/source authenticity.

## Required Semantic Separation

`QUARANTINE != RESOLUTION`

`RESOLUTION != PROVIDER AUTHENTICATION`

`APPROVED RESOLVER IMPLEMENTATION != APPROVED EVIDENCE CLAIM`

`EXACT CONTENT MATCH != EXTERNAL DELIVERY PROOF`

`IMMUTABLE GITHUB SOURCE IDENTITY != PROVIDER / MODEL IDENTITY`

`RESOLVED_UNAUTHENTICATED != AUTHORIZED`

## Entry Requirement

The input MUST pass the existing untrusted external-evidence intake verifier at:

`VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE`

with trust state:

`UNTRUSTED_QUARANTINED`.

An invalid, mutated, promoted or otherwise ineligible intake MUST prevent resolver invocation.

## Resolver Requirement

A successful path requires the governed gate itself to invoke a resolver whose immutable identity matches an explicit approved registry record.

Generic quarantine evidence uses a dedicated `acquire_external(evidence_ref)` protocol and MUST NOT be routed through participant or attestation channels merely because those interfaces already exist.

Approval proves only that the local resolver implementation identity is permitted for this technical acquisition path.

It does not prove upstream provider authenticity.

## Acquisition Requirement

The acquisition MUST provide:

- stable canonical adapter identity;
- non-empty acquisition identity;
- non-empty acquisition surface;
- ordered start/end timestamps;
- exact requested-reference equality with the sealed intake `source_ref`;
- a mapping observation with an allowed status;
- no injection of resolver/trust/authority control keys.

Allowed resolution observation states:

- `FOUND`
- `UNAVAILABLE`
- `PARTIAL`

## FOUND Gate

`FOUND` may advance only when:

1. `observed_ref == intake.source_ref`;
2. `evidence_content` is present;
3. canonical SHA-256 of acquired content equals the sealed `raw_evidence_digest`;
4. acquired JSON value exactly matches the sealed `raw_evidence`.

Successful state:

`RESOLVED_UNAUTHENTICATED`

The original intake envelope is not mutated.

## UNAVAILABLE Gate

`UNAVAILABLE` remains:

`UNTRUSTED_QUARANTINED`

and returns:

`RESOLUTION_UNAVAILABLE`.

It means only:

`UNAVAILABLE_BY_THIS_APPROVED_ADAPTER_PATH`.

It MUST NOT be interpreted as global proof that the evidence does not exist.

An `UNAVAILABLE` observation that also supplies evidence content is contradictory and MUST fail closed as a mismatch.

## PARTIAL Gate

`PARTIAL` returns:

`RESOLUTION_INCONCLUSIVE`

and remains:

`UNTRUSTED_QUARANTINED`.

## Mismatch / Failure

Reference mismatch, content mismatch, canonical digest mismatch, malformed acquisition, unstable adapter identity, unapproved adapter identity, reserved-control injection, invalid time ordering or adapter execution failure MUST NOT advance trust.

Representative states:

- `ADAPTER_IDENTITY_REJECTED`
- `ADAPTER_NOT_APPROVED`
- `RESOLUTION_EXECUTION_FAILED`
- `RESOLUTION_MISMATCH`

## Maximum Claim Boundary

A successful resolution result MUST retain:

- `provider_authenticity = UNVERIFIED`
- `external_authenticity = NOT_ESTABLISHED_BY_RESOLUTION`
- `external_delivery = NOT_PROVEN`
- `model_execution_authenticity = NOT_PROVEN`
- `independence = UNVERIFIED`
- `authority = NONE`
- `cognitive_effect = NOT_ESTABLISHED`

Next required stage:

`PROVIDER_BACKED_AUTHENTICATION_OR_OTHER_GOVERNED_AUTHENTICITY_EVIDENCE`

## GitHub Immutable Resolver Boundary

The current GitHub resolver may re-acquire an exact JSON value from:

`github+artifact://owner/repo@FULL_COMMIT_SHA/path`

through the read-only Contents API path.

For generic quarantine acquisition, the external JSON is nested under `evidence_content`; external keys are not copied into resolver control state.

GitHub repository/commit/path/blob identity proves technical artifact location only. It does not authenticate provider/model claims stored in the artifact.

## Maximum State

`RESOLVED_UNAUTHENTICATED`

This state proves bounded technical resolution/correlation only.
