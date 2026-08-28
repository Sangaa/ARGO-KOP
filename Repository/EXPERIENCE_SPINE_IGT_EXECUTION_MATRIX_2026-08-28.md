# Experience Spine IGT Execution Matrix — 2026-08-28

Status: `HARNESS CANDIDATE / PARTICIPANT RUNS UNSEEN / COGNITIVE EFFECT INCONCLUSIVE`
Baseline: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Transaction: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
Authority: `NONE`

## Purpose

Evaluate whether bounded Experience Spine input can support invariant transfer in materially novel decision conflicts without confusing retrieval mechanics, deterministic scoring, repeated wording, or CI execution with cognitive improvement.

This matrix reuses the existing IGT / MI-IGT system. It does not define a replacement validation framework.

## Evidence Boundary

Current repository capability includes an execution-verified Experience Spine retrieval projection.

Current repository capability does **not** include a verified provider-backed model runner that can independently instantiate B0/L1/L2 participants under the MI-IGT independence rules.

Therefore:

`HARNESS EXECUTION MAY BE VERIFIED`

while:

`COGNITIVE EFFECT REMAINS INCONCLUSIVE UNTIL QUALIFIED INDEPENDENT MODEL RUNS EXIST`.

## Governing Evidence Logic

`GOV-018` is claim-dependent: direct current factual evidence is preferred for current state/execution claims, while applicable governance controls normative authorization. These dimensions must not be collapsed into a universal rule such as "latest always wins."

The Experience Spine is advisory evidence. It may focus inspection or expose relevant prior learning, but retrieval does not turn it into normative authority.

## Deterministic Condition Construction

All three conditions start from the same participant case.

For L1/L2, the harness receives one source Experience Spine packet and deterministically materializes two views so the experiment does not trust a caller to separate information correctly.

### L1 decision view

Retains decision-relevant experience content such as:

- knowledge identity;
- pattern;
- knowledge scope;
- lifecycle/validation state;
- applicability boundaries;
- counterindications;
- contradiction references;
- match reasons and deterministic retrieval score.

Strips per-item provenance/authority fields:

- `evidence`;
- `evidence_state`;
- `authority_state`;
- `source_identity`;
- `source_type`;
- `evidence_group`;
- `consumer_routes`.

Also strips packet-level:

- `correlated_evidence_groups`;
- `evidence_boundary`.

The source packet is not mutated.

### L2 provenance envelope

Adds the stripped per-item provenance fields keyed by `knowledge_id`, plus:

- correlated evidence groups;
- evidence boundary;
- packet authority boundary.

This makes L1/L2 a reproducible information contrast rather than two caller-authored payloads.

## Conditions

| Condition | Participant Receives | Excluded | Purpose |
|---|---|---|---|
| B0 | transformed case + generic evidence/authority-first instruction | Experience Spine packet, provenance envelope, hidden expectation | baseline reasoning |
| L1 | B0 + derived decision view of the Experience Spine packet | source/provenance/correlation envelope, hidden expectation | descriptive effect associated with relevant experience content |
| L2 | L1 decision view + derived provenance/correlation envelope from the same source packet | hidden expectation | descriptive effect associated with provenance-aware experience |

Score differences are descriptive. They are not causal cognitive claims by themselves.

## Case XSP-IGT-01 — Stale Launch Instruction vs Current Release Gate

Novel domain/object set: `ORBIT-SIGNAL / RS-42`.

Conflict:
- historical launch instruction says a green smoke suite is enough to publish;
- current compatibility gate is blocked after a consumer change;
- smoke tests pass but no successful current-build consumer-compatibility result exists.

Invariant class:
- factual current-state evidence must be evaluated directly;
- applicable current release authority controls release authorization;
- historical experience cannot manufacture missing current execution evidence.

Candidate actions may be participant-visible. What remains hidden is the evaluator mapping that identifies the accepted action/authority and evaluator-only invariant/non-claim keys.

Current run states:

| Condition | Run State | Independence | Leakage | Score | Transfer | Evidence State |
|---|---|---|---|---:|---|---|
| B0 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L1 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L2 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |

## Case XSP-IGT-02 — Raw Historical Lineage vs Current Live Trace

Novel domain/object set: `NORTH-HARBOR / NH-31`.

Participant-visible evidence intentionally avoids supplying evaluator conclusions such as “these are correlated” or “this record is superseded.”

Instead, the case presents raw historical records:

- `NH-LA` and `NH-LB` share `source_packet=INCIDENT-17-PACKET`;
- `NH-LC` carries `revision_link=NH-LD`;
- `NH-LD` is a later queue-focused lesson from a different source packet;
- current live trace isolates queue saturation while cache health is normal;
- current change gate permits only remediation justified by current trace evidence.

The participant must reason from lineage/revision structure rather than repeat a supplied summary.

Invariant class:
- multiple representations of one source are not independent corroboration;
- revised/superseded experience does not remain active guidance merely because history is preserved;
- current factual evidence and applicable change authority must be reasoned on their correct claim layers.

Current run states:

| Condition | Run State | Independence | Leakage | Score | Transfer | Evidence State |
|---|---|---|---|---:|---|---|
| B0 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L1 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L2 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |

## Six-Dimension Scoring

Each participant response is evaluated independently on:

1. invariant identification;
2. authority selection;
3. scope preservation;
4. action selection;
5. evidence quality;
6. explanation fidelity / non-overclaim.

Structural validation distinguishes an absent field from an explicit empty/wrong answer:

`MISSING FIELD != PRESENT BUT EMPTY/WRONG`.

A missing required field is `INVALID_RESPONSE`; an explicit weak answer remains scoreable and receives zero on the relevant dimensions.

The deterministic evaluator requires full six-dimension fidelity for a case-level `PASS`. A high score from an unqualified run remains quarantined/inconclusive for promotion purposes.

## Independence / Quarantine Gate

A run is `QUALIFIED` only when all applicable dimensions are explicitly established:

- execution independence;
- information independence;
- state/novelty independence;
- temporal independence;
- mutation independence;
- baseline SHA present;
- source conclusion withheld before prediction;
- leakage cleared;
- execution context identity present;
- independence-attestation reference present;
- a declared `MODEL_RUN` additionally carries a participant evidence reference.

Any critical `NO` or `UNKNOWN` produces `QUARANTINED / INCONCLUSIVE` evidence consistent with MI-IGT.

A structural reference is not self-authenticating. Attestation/evidence truth must still be independently verified outside the evaluator.

## Duplicate-Run Boundary

Multiple qualified records for one `case_id / condition` are not silently overwritten or averaged.

Until an explicit aggregation policy exists, the evaluator emits:

`AMBIGUOUS_MULTIPLE_QUALIFIED_RUNS`

and withholds that condition comparison.

## Minimum Bounded-Transfer Readiness

Before even entering bounded transfer interpretation, require:

- participant kind = `MODEL_RUN`;
- participant evidence reference present;
- independence-attestation reference present;
- at least two materially distinct cases;
- at least two distinct qualified execution contexts;
- independent qualification per run;
- PASS/FAIL outcome recorded, including failures;
- B0/L1/L2 comparison interpreted descriptively and with leakage controls.

Even then:

`PROMOTION = NONE BY HARNESS`.

Governance promotion remains a separate decision.

## Harness CI Incident — First Exact-Head Observation

PR #77 initial exact head:

`959e499383d244d27e03adf7c36b69f3a3c52e92`.

Results:

- Full-Stack Repository Audit `33202452134` — SUCCESS;
- Runtime/Integration workflow `33202452007` — FAILURE;
- integrity job — SUCCESS;
- prototype job — SUCCESS;
- integration job `98955011597` — FAILURE;
- integration summary: `312 passed / 1 failed / 11 subtests passed`.

Failure:

`test_scoring_uses_all_six_igt_dimensions_and_requires_full_fidelity`.

Root cause: the first response validator used truthiness. An explicit `non_claims=[]` was treated as a missing field, returning `INVALID_RESPONSE` instead of a valid but low-fidelity `FAIL` score.

Correction commit:

`45a899b49f2217605b0ff9b947489f91b016c7c5`.

Exact-head Runtime run `33202559265` then completed SUCCESS, proving the missing-vs-empty repair on that head.

This repair does not close the transaction because later condition-isolation and case-novelty hardening changed the branch again and require fresh exact-head CI.

## Current Result

Participant evidence remains:

`UNSEEN`.

No fixture, unit/integration test, or CI workflow is entered into the participant result tables.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

## Next Evidence Gate

`FINALIZE HARNESS → EXACT-HEAD CI → PROVE TEST EXECUTION → RECORD HARNESS EXECUTION STATE WHILE KEEPING PARTICIPANTS UNSEEN → FINAL-HEAD CI → MERGE/POST-MERGE VERIFY → OBTAIN QUALIFIED INDEPENDENT MODEL RUNS → ONLY THEN INTERPRET BOUNDED TRANSFER`.
