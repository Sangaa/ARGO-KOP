# Experience Spine IGT Execution Matrix — 2026-08-28

Status: `HARNESS EXECUTION-VERIFIED / PARTICIPANT RUNS UNSEEN / COGNITIVE EFFECT INCONCLUSIVE`
Baseline: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Transaction: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
PR: `#77`
Authority: `NONE`

## Purpose

Measure whether bounded Experience Spine input later supports invariant transfer in materially novel decision conflicts, while refusing to confuse deterministic harness mechanics with cognitive improvement.

The existing IGT / MI-IGT system is reused unchanged as the governing experiment framework.

## Verified Harness State

Hardened source head:
`40397fce03b3481765971b06f48a4004847f679d`.

Evidence:
- Full-Stack `33203060544` — SUCCESS;
- Runtime/Integration `33203060557` — SUCCESS;
- integration job `98957084303` — SUCCESS;
- actual checkout = PR merge ref `c9a4cff828d912c6afee7470336d9f633e7a13f0`, representing `40397fce...` merged into exact base `a4cc9620...`;
- `python -m pytest -q Quality/Integration` → `316 passed, 1 warning, 11 subtests passed`.

Verified pre-IGT main baseline = `299` integration tests; IGT harness contribution = `17` discovered integration regressions.

This establishes harness execution and current-base compatibility. It does not establish participant behavior or model learning.

## Information Conditions

| Condition | Participant Receives | Explicitly Excluded | Purpose |
|---|---|---|---|
| B0 | transformed case + generic evidence/authority-first instruction | Experience Spine packet, provenance envelope, evaluator expectations | baseline reasoning |
| L1 | B0 + harness-derived Experience Spine decision view | source/evidence/authority/correlation provenance envelope, evaluator expectations | experience-availability comparison |
| L2 | identical L1 decision view + harness-derived provenance/correlation envelope from same immutable source packet | evaluator expectations | provenance-aware comparison |

The harness, not caller convention, produces the L1/L2 split.

Score deltas are descriptive only.

## XSP-IGT-01 — ORBIT-SIGNAL / RS-42

Participant sees a stale launch instruction, current blocked compatibility gate, green smoke evidence, and absence of a successful current-build consumer-compatibility result.

Hidden evaluator target class:
- current factual evidence must be evaluated directly;
- applicable release authority controls release authorization;
- historical experience cannot manufacture missing execution evidence.

| Condition | Run State | Independence | Leakage | Score | Transfer | Evidence State |
|---|---|---|---|---:|---|---|
| B0 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L1 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L2 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |

## XSP-IGT-02 — NORTH-HARBOR / NH-31

Participant sees raw historical records carrying lineage/revision links, current queue-saturation trace, normal cache health, and current change authority. The participant text does not state which records are correlated or which revision is active; that meaning must be inferred.

Hidden evaluator target class:
- correlated representations are not independent corroboration;
- revised/superseded experience is not automatically active guidance;
- factual evidence and normative authority remain separate claim layers.

| Condition | Run State | Independence | Leakage | Score | Transfer | Evidence State |
|---|---|---|---|---:|---|---|
| B0 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L1 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |
| L2 | UNSEEN | UNSEEN | UNSEEN | — | INCONCLUSIVE | UNSEEN |

## Qualification Gate

A run may become structurally `QUALIFIED` only when all applicable evidence is explicit:
- baseline SHA;
- execution independence;
- information independence;
- state/novelty independence;
- temporal independence;
- mutation independence;
- source conclusion withheld before prediction;
- leakage cleared;
- execution context identity;
- independence-attestation reference;
- participant evidence reference for `MODEL_RUN`.

Any critical `NO` or `UNKNOWN` → `QUARANTINED / INCONCLUSIVE`.

Structural qualification does not authenticate an external reference by itself.

## Six-Dimension Scoring

1. invariant identification;
2. authority selection;
3. scope preservation;
4. action selection;
5. evidence quality;
6. explanation fidelity / non-overclaim.

Absent required response key = `INVALID_RESPONSE`.

Present but empty/wrong answer = scoreable evidence with zero on the affected dimension.

## Evidence Separation Rule

`HARNESS PASS != PARTICIPANT PASS`.

`PARTICIPANT PASS != BROAD GENERALIZATION`.

`MULTIPLE PASSING RUNS != AUTOMATIC PROMOTION`.

`CI != INDEPENDENT MODEL CONTEXT`.

## Current Result

`EXPERIENCE SPINE IGT HARNESS = EXECUTION-VERIFIED ON HARDENED SOURCE HEAD`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

`PROMOTION = NONE`.

## Next Evidence Gate

After final documentation-head CI and merge/post-merge verification, a separate workstream may ingest independently produced model-run packages, verify their evidence/attestation references, populate the six participant rows, and only then perform bounded B0/L1/L2 transfer interpretation.
