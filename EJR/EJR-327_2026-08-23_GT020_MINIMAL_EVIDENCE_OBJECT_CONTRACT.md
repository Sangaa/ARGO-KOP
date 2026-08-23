# EJR-327 — GT-020 Minimal Evidence Object Contract

Date: 2026-08-23
Status: COMPLETED / CANDIDATE CONTRACT / NO NEW MODEL
Protocol: GOV-013 + GOV-018 Candidate + Model Creation Gate
Parent: EJR-326

## Objective

Determine the smallest structured representation ENG-001 needs to reason over competing evidence without creating a new canonical Model prematurely.

## Prior-learning gate

Three materially different retrieval paths were used before mutation:

1. exact/semantic search for evidence-object, claim, provenance and confidence structures;
2. direct inspection of `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`;
3. direct inspection of `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md` plus related Runtime/Engine search results.

Relevant prior learning was found and classified as **DIRECTLY APPLICABLE / TRANSFERABLE**.

`MOD-011` already defines source identity, scope, timestamp, evidence scope, authority scope, provenance policy and source-claim/evidence/knowledge states. It also explicitly requires source claims to remain distinguishable from ARGO interpretation. `KNW-008` already requires knowledge traceability from source → evidence → validation → repository integration → operational use. Therefore a new canonical Evidence Model is not yet justified.

## Gap identified

Existing models describe the provenance and lifecycle of knowledge and sources, but GT-018 requires a **minimal runtime reasoning envelope** that can carry the dimensions needed for one evidence observation during comparison.

This is a contract/data shape gap, not yet a proven semantic-model gap.

## Minimal Evidence Object

The smallest sufficient reasoning envelope is:

```text
EvidenceObservation {
  evidence_id
  claim {
    claim_id
    claim_type
    proposition
  }
  target_id
  scope
  temporal_context
  evidence_layer
  source_ref
  provenance_ref
  authority_scope
  claim_fitness
  identity_confidence
  evidence_independence
  completeness
  observed_value
  semantic_status
}
```

### Field rules

- `evidence_id` — stable identity for the observation/evidence record.
- `claim_id` — groups observations addressing the same claim.
- `claim_type` — `NORMATIVE | IDENTITY | STATE | EXECUTION | DERIVED_RESULT | HISTORICAL | PROVENANCE`.
- `proposition` — the explicit statement being evaluated; prevents text-only comparison errors.
- `target_id` — object/run/file/entity to which the proposition applies.
- `scope` — repository, workflow, environment, path, component or other applicable boundary.
- `temporal_context` — timestamp, version, commit, run or other time anchor required for comparison.
- `evidence_layer` — repository state, run metadata, job/step execution, artifact metadata, artifact payload, correlation/audit, governance/promotion, or a validated equivalent.
- `source_ref` — pointer to the source record or evidence-producing surface.
- `provenance_ref` — pointer to transport/origin/derivation evidence.
- `authority_scope` — authority applicable to this claim, kept separate from confidence.
- `claim_fitness` — how directly this observation can establish the stated claim.
- `identity_confidence` — confidence that the observation belongs to the target claimed.
- `evidence_independence` — whether corroboration is materially independent or derived from the same evidence chain.
- `completeness` — whether the evidence surface is complete enough for the intended comparison.
- `observed_value` — the actual observed state/result; never silently normalized into a preferred conclusion.
- `semantic_status` — producer/evidence status such as `OBSERVED`, `CORROBORATED`, `CONTRADICTION`, `UNRESOLVED`, `SUPERSEDED`, without granting canonical authority.

## Deliberate omissions

The object does **not** contain:

- a global authority score;
- a global confidence score;
- a final ARGO decision;
- automatic PASS/FAIL promotion;
- model-specific storage fields;
- database-specific fields;
- an embedded resolution rule.

Those are intentionally kept outside the observation object because they belong to claim-dependent reasoning, governance and decision stages.

## Comparison contract

Two `EvidenceObservation` records may be compared only after ENG-001 evaluates:

`claim_id/proposition → target_id → scope → temporal_context → provenance → evidence_layer`

Then:

- compatible same proposition → `CONSISTENT / CORROBORATED`;
- different proposition/layer → `DIFFERENT EVIDENCE LAYERS`;
- same proposition with mutually exclusive values → `CONTRADICTION`;
- insufficient alignment/completeness or unresolved conflict → `UNRESOLVED`.

Resolution is a downstream operation and MUST NOT mutate the original observation into the winning conclusion.

## Model Creation Gate Result

**NO NEW MODEL CREATED.**

Reason:

`MOD-011 + KNW-008 + ENG-001 + GOV-018` already provide the necessary semantic surfaces. The missing element is a bounded reasoning envelope, which can be treated as a contract/implementation shape until runtime integration proves a persistent canonical model is actually required.

This explicitly satisfies the HERMUZ Model Creation Gate:

`Existing Models → Current Relationships → Consumer Proof → Repository Reconciliation → Verified Gap Assessment`

## Integration impact

Potential consumers to verify at the next integration checkpoint:

- `Engine/ENG-001_REASONING_ENGINE.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`
- `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- Runtime cognitive-loop artifacts
- applicable evidence/learning registries

No consumer contract was mutated in this checkpoint. This is intentional: the contract is first recorded and tested conceptually before cross-layer implementation.

## Controlled test vectors

### Vector A — same claim, different value

Same `claim_id`, `target_id`, `scope`, `temporal_context`; values `3.2.1` and `3.3.0`; authoritative evidence exists.

Expected:

`CONTRADICTION → RESOLVED BY AUTHORITY`

### Vector B — same event, different layer

Same target/run; one observation is `RUN_METADATA`, another is `ARTIFACT_PAYLOAD`; propositions are compatible.

Expected:

`DIFFERENT EVIDENCE LAYERS / CORROBORATED`

### Vector C — incomplete evidence

Same intended claim but identity or scope cannot be established and retrieval is incomplete.

Expected:

`UNRESOLVED / EVIDENCE GAP`

### Vector D — explicit producer unresolved result

Producer observation contains `observed_value=POLICY_UNRESOLVED` and `semantic_status=UNRESOLVED`.

Expected:

`UNRESOLVED`; transport, digest or artifact existence cannot promote it.

## Knowledge Delta

**KD-026 — Evidence is an observation contract before it is a decision.**

ARGO should preserve the raw/observed evidence dimensions independently from later reasoning and decision outcomes.

**KD-027 — No new Model without a proven semantic gap.**

The current GT-020 gap is satisfied by a minimal reasoning envelope; persistent model creation remains unjustified until integration evidence proves otherwise.

**KD-028 — Resolution must not overwrite evidence.**

The winning conclusion is a derived reasoning result; the underlying competing observations remain traceable.

## Closure

`Execute → Prior-Learning Retrieval → Gap Assessment → Contract Definition → Document → Read-back → Verify → Close`

Next safe continuation:

`GT-021 — recover existing ENG-004 / Runtime cognitive-loop integration tests and determine whether the EvidenceObservation contract can be exercised through an existing test seam before any new runtime implementation is created.`
