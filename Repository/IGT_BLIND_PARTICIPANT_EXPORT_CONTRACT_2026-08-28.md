# IGT Blind Participant Export Contract — 2026-08-28

Status: `CANDIDATE / PRE-CI`
Authority: `NONE`

## Purpose

Define the exact participant-facing artifact boundary for later independent Experience Spine IGT model runs.

The export exists to prevent experiment operators from hand-assembling B0/L1/L2 prompts in a way that leaks evaluator expectations, changes response requirements, loses baseline identity, or fabricates execution evidence.

## Lifecycle

`CANONICAL IGT CASE + CONDITION + EXACT BASELINE + OPTIONAL EXPERIENCE PACKET`

→ `HARNESS CONDITION MATERIALIZATION`

→ `BLIND PARTICIPANT EXPORT`

→ `EXTERNAL DELIVERY (FUTURE / SEPARATE EVIDENCE)`

→ `MODEL EXECUTION (FUTURE / SEPARATE EVIDENCE)`

→ `MODEL-RUN EVIDENCE PACKAGE`

→ `EXTERNAL RESOLVER / AUTHENTICITY GATES`

→ `BOUNDED EVALUATION`.

No arrow may be skipped by inference.

## Export Identity

Each export contains:
- export format version;
- experiment ID;
- case ID;
- condition (`B0`, `L1`, `L2`);
- exact 40-hex repository baseline SHA;
- harness-generated participant payload;
- invariant response contract;
- export ID derived from canonical identity material;
- package SHA-256 digest;
- explicit pre-execution evidence boundary;
- claim boundary `PARTICIPANT_INPUT_ONLY`.

The export is deterministic. No random ID or generation timestamp is used to create artificial identity differences.

## Blindness Boundary

The export must not contain evaluator-only field names such as:
- `target_invariants`;
- `accepted_authorities`;
- `accepted_actions`;
- `required_scope`;
- `required_evidence`;
- `required_non_claims`;
- scoring dimensions/results;
- transfer or promotion outcomes.

The evaluator's target invariant values and required non-claim values must not appear in participant-visible serialization.

Candidate action/authority labels may remain visible when they are part of the transformed case by design. Visibility of a candidate label is not equivalent to disclosure that it is correct.

## Condition Isolation

`B0` receives no Experience Spine packet.

`L1` receives the harness-derived decision view only.

`L2` receives the same decision view plus the harness-derived provenance/correlation envelope.

The export boundary does not independently reimplement the B0/L1/L2 split. It delegates to the already-governed `build_condition_payload()` surface.

## Response Contract

Every condition receives the same structured response schema:
- `prediction`;
- `identified_invariants`;
- `selected_authority`;
- `scope`;
- `action`;
- `evidence_refs`;
- `non_claims`.

Changing response requirements between conditions would contaminate the experiment and is not permitted.

## Execution-Evidence Boundary

At export time:

`execution_evidence.state = NOT_YET_EXECUTED`.

The following must remain null/unpopulated:
- participant evidence reference;
- provider receipt.

The export must not fabricate:
- execution context ID;
- independence attestation;
- provider request/response/execution ID;
- delivery receipt;
- external authenticity state.

## Integrity Boundary

`EXPORT DIGEST MATCH = LOCAL PACKAGE INTEGRITY ONLY`.

It does not prove:
- external delivery;
- model receipt;
- model execution;
- provider identity;
- independence;
- response authenticity;
- cognitive effect.

Any mutation of condition, baseline, participant payload, experiment identity or response contract must invalidate the original export identity and/or digest.

## Claim Ladder

Maximum state established by this boundary:

`VERIFIED_PARTICIPANT_EXPORT`.

Explicit non-states:

`EXTERNAL DELIVERY = NOT PROVEN`.

`MODEL EXECUTION = NOT PROVEN`.

`PROVIDER AUTHENTICITY = NOT PROVEN`.

`B0/L1/L2 PARTICIPANT RUN = UNSEEN`.

`COGNITIVE EFFECT = INCONCLUSIVE`.

## Reusable Law

`PREPARED INPUT != DELIVERED INPUT != EXECUTED INPUT != AUTHENTICATED OUTPUT`.

A later provider-specific transaction must supply real evidence for each additional transition rather than inheriting trust from this export package.
