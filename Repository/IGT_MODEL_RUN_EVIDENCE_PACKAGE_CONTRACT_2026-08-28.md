# IGT Model-Run Evidence Package Contract — 2026-08-28

Status: `CONTROLLED CANDIDATE / TRANSPORT CONTRACT / NOT AUTHORITY`
Transaction: `MUT-2026-08-28-IGT-MODEL-RUN-EVIDENCE-PACKAGE-001`
Authority: `NONE`

## Purpose

Define a portable, machine-checkable evidence package for model runs produced outside the current repository CI/runtime while preserving MI-IGT independence, contamination, and evidence-boundary rules.

The package is an evidence transport artifact. It is not proof by declaration and it is not a promotion surface.

## Core Separation

`STRUCTURAL VALIDITY != INTERNAL INTEGRITY != EXTERNAL AUTHENTICITY != COGNITIVE EFFECT`.

A package may be perfectly formed and internally untampered while still failing to prove that the claimed external model execution actually occurred.

## Required Identity

Every package carries:
- `schema_version`;
- `package_id`;
- `run_id`;
- `case_id`;
- `condition` (`B0`, `L1`, or `L2`);
- `participant_kind = MODEL_RUN`;
- repository baseline SHA;
- execution context ID;
- source model label;
- source instance ID;
- execution surface;
- start/end timestamps.

Identity fields must agree with the embedded participant payload and independence attestation where applicable.

## Participant Surfaces

### Participant payload
The exact participant-visible condition input.

### Participant response
Structured response containing the IGT response fields required by the current evaluator.

Evaluator expectations, answer keys, correctness mappings, hidden invariants, or hidden non-claim keys are forbidden from participant payload/response.

## Condition Isolation

### B0
Must not contain an Experience Spine packet or provenance envelope.

### L1
Must contain the harness-derived Experience Spine decision view but must not contain:
- provenance envelope;
- packet-level `correlated_evidence_groups`;
- packet-level `evidence_boundary`;
- packet-level `authority_boundary`;
- per-item evidence/source/authority/evidence-group/consumer-route provenance fields.

### L2
Must contain the same decision view class as L1 plus the harness-derived provenance/correlation envelope.

Condition isolation is verified from the captured participant payload. A package that claims L1 while carrying L2-only fields is invalid even if its hash is correct.

## Independence Attestation

The package embeds explicit values for:
- execution independence;
- information independence;
- state/novelty independence;
- temporal independence;
- mutation independence;
- source conclusion withheld before prediction;
- leakage detection result.

It also carries an externally resolvable `independence_attestation_ref`.

An embedded attestation saying `YES` is a claim surface, not independent authentication of itself.

## External Evidence Reference

A `MODEL_RUN` package requires an externally resolvable `participant_evidence_ref` that can later be checked against the claimed execution source.

Examples of future resolvable evidence may include provider/runtime records, immutable execution artifacts, or another connector-backed execution identity. This contract does not prescribe one vendor or transport.

## Internal Integrity

The package uses deterministic SHA-256 digests for:
- participant payload;
- participant response;
- full package content excluding the package's own `package_digest` field.

Canonicalization uses stable JSON key ordering and compact separators.

Digest validation establishes only content consistency relative to the recorded digest.

`HASH MATCH != SOURCE AUTHENTICITY`.

`HASH MATCH != MODEL IDENTITY PROOF`.

## State Model

### `INVALID`
Use when structure, identity consistency, condition isolation, evaluator contamination, or digest integrity is invalid.

### `QUARANTINED`
Use when the package is structurally parseable and internally intact but a qualification requirement is not established, for example an independence dimension is `NO/UNKNOWN` or a required external evidence reference is absent.

### `STRUCTURALLY_QUALIFIED`
Use when local structure, identity, condition-isolation, contamination, integrity, and attestation-field requirements pass.

This state still carries:

`EXTERNAL_AUTHENTICITY = UNVERIFIED`.

### `EXTERNAL_AUTHENTICITY_UNVERIFIED`
Mandatory external-evidence boundary after local qualification. It is not a failure; it means no independent resolver has yet authenticated the claimed execution.

### `EXTERNALLY_VERIFIED`
Reserved for a future resolver-backed step that checks the package references against independent execution evidence. This local package gate cannot produce this state by itself.

## Duplicate Identity Rule

Multiple files are not multiple independent executions.

Duplicate `package_id`, or repeated `(run_id, case_id, condition, execution_context_id)` identity, must be surfaced and must not count as independent corroboration.

Changing only the package filename or package ID does not create a new run.

## Contamination Rule

Evaluator-only keys or answer mappings inside participant payload/response invalidate the package.

Correct digests do not rescue contaminated evidence. A perfectly hashed leaked answer remains contaminated.

## Transport Neutrality

The contract is independent of model vendor, API, chat product, file transport, or future ARGO runtime.

Transport may change without changing the semantic evidence contract.

## Resolver Boundary

A future external resolver may:
1. resolve `participant_evidence_ref`;
2. resolve `independence_attestation_ref`;
3. correlate execution identity, timestamps, baseline, context and participant material;
4. classify authenticity evidence;
5. preserve failures and ambiguities.

The resolver must not infer provider/model execution merely because the local package validates.

## Non-Claims

- package validity does not prove model learning;
- digest validity does not prove authorship;
- timestamps do not prove temporal independence by themselves;
- a new window/session label alone does not prove execution independence;
- a structurally qualified package does not populate IGT participant results until external evidence review qualifies the run;
- even externally verified bounded runs do not automatically prove broad generalization, model-weight change, or governance promotion.

## Current Boundary

`PACKAGE GATE = LOCAL STRUCTURE / INTEGRITY / CONTAMINATION / QUALIFICATION CHECK`.

`EXTERNAL AUTHENTICITY = SEPARATE FUTURE RESOLUTION STEP`.

`AUTHORITY = NONE`.
