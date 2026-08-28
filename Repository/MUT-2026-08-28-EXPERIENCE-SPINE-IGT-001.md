# Experience Spine IGT — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Working branch: `hermuz/experience-spine-igt-20260828`
PR: `#77`
Status: `HARNESS HARDENED / SOURCE-READBACK VERIFIED / FINAL EXACT-HEAD CI PENDING / PARTICIPANT RUNS UNSEEN / COGNITIVE EFFECT INCONCLUSIVE`

## Entry State

Experience Spine mechanics are merged to main and post-merge verified:

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

Open PR surface at transaction entry: `0`.

Historical PRs #66/#69 are closed, not merged, provenance preserved.

Prior verified main evidence:

- clean merge `a4cc96203b689338a50b7233b46c15eae8449f5a`;
- Full-Stack `33201440156` — SUCCESS;
- Runtime workflow `33201440177` — integration/integrity/prototype jobs SUCCESS;
- M2 `33201440226` — SUCCESS.

## Governing Surfaces Reused

No second IGT framework is introduced. This transaction consumes:

- `Governance/IGT_INVARIANT_GENERALIZATION_TEST_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_BRIDGE_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_RECORD_TEMPLATE_v1.0.md`;
- `Governance/MI-IGT_INDEPENDENCE_ATTESTATION_v1.0.md`;
- `Governance/MI-IGT_EVIDENCE_QUARANTINE_PROTOCOL_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_COORDINATION_PROTOCOL_v1.0.md`;
- `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md`;
- `Memory/Engineering_Journal/EJR-338_2026-08-27_IGT_LPE_TRANSFER_LEARNING.md`.

## Capability Boundary

Repository search plus `AI-006` / `INTF-005` review found model-adapter/interface contracts but no verified provider-backed model invocation runner capable of creating materially independent B0/L1/L2 model contexts from repository CI.

Therefore:

1. `IGT HARNESS / EVALUATOR` may be execution-verified now.
2. `COGNITIVE EFFECT` remains `INCONCLUSIVE` until qualified independent model-run evidence exists.

Deterministic fixtures, evaluator regressions, and GitHub Actions are not participant/model-learning evidence.

## Target Invariants

I1. Current direct factual evidence and applicable authority outrank advisory retrieved experience for the claim layer they legitimately govern.

I2. Contradictory experience requires review; rank/order cannot silently decide authority.

I3. Correlated records are not independent confirmation.

I4. Revised/superseded experience does not remain active guidance merely because history is preserved.

I5. Failed/unknown independence or leakage qualification quarantines evidence.

I6. B0/L1/L2 must be deterministically separated rather than trusted to caller discipline.

I7. A renamed source case is not materially novel; transformed cases must require fresh reasoning.

I8. Scoring/comparison preserves non-claims; evaluator PASS does not equal cognitive-benefit PASS.

I9. Multiple qualified runs for one case/condition may not silently shadow one another.

I10. A self-declared `MODEL_RUN` label is insufficient without participant evidence and independence-attestation references.

I11. Missing response fields and explicit empty/wrong answers are different evidence states.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt.py` | deterministic B0/L1/L2 materialization, six-dimension scoring, MI-IGT qualification/quarantine, duplicate-run fail-closed comparison, model-evidence readiness boundary | Y | Y source/read-back |
| C02 | `Quality/Integration/test_experience_spine_igt.py` | regressions for novelty, hidden keys, condition isolation, source immutability, six scores, missing-vs-empty, quarantine, attestation/evidence refs, duplicate runs, fixtures and non-claims | Y | Y source/read-back |
| C03 | `Quality/Integration/experience_spine_igt_cases.py` | two materially novel authority-conflict cases with evaluator expectations separated; second case uses raw lineage/revision records | Y | Y source/read-back |
| C04 | `Repository/EXPERIENCE_SPINE_IGT_EXECUTION_MATRIX_2026-08-28.md` | deterministic condition contract, cases, qualification, CI incident, current UNSEEN/INCONCLUSIVE participant state | Y | Y source/read-back |
| C05 | `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md` | prior transaction reconciled to CLOSED/MERGED/POST-MERGE VERIFIED | Y | Y source/read-back |
| C06 | `Quality/Integration/test_experience_spine_igt.py` | integration-suite discovery surface; final exact-head execution proof required | Y | CI PENDING |

## Current Read-Back Identities

- evaluator blob: `2bbbc03179831faea2b5fd3724369637b9bc3b95`;
- test blob: `25d13218b277b1905a9cf4ea73f90a06c2ce560b`;
- case blob: `173fcf8d3b4d385f37ed72e483f9e020f179f26b`;
- execution matrix blob: `a830088ffd2d6192c18e31dee005b13d8cd0dca1`;
- reconciled clean-transaction blob: `e913f4dd71c3f491b8dcc161e53201ae92b0251c`.

Pre-PR/early branch comparison established:

- base exactly `a4cc9620...`;
- `behind_by=0`;
- changed paths = six declared paths;
- unexpected paths = `0`;
- no Runtime, Engine, Memory, Services, Interface/provider, workflow, or Governance-authority mutation.

Fresh compare is still required at final frozen head.

## Design Corrections / Learning

### D01 — Candidate choice visibility is not answer leakage

The first leakage detector treated a participant-visible candidate action label as leaked merely because the same label appears in evaluator expectations.

Correction: candidate labels may be visible; what remains hidden is the correctness mapping plus evaluator-only invariant/non-claim keys.

### D02 — Duplicate qualified condition runs must not shadow

The first comparison map could let a later qualified run overwrite an earlier run for the same `case_id/condition`.

Correction: multiple qualified runs for one condition produce `AMBIGUOUS_MULTIPLE_QUALIFIED_RUNS`; no delta is calculated until an explicit aggregation policy exists.

### D03 — Model label is not model evidence

A `MODEL_RUN` now requires participant evidence reference and independence-attestation reference before it can count toward bounded-transfer readiness. Those references are still not self-authenticating; external verification remains required.

`SELF-DECLARED MODEL LABEL != QUALIFIED MODEL EVIDENCE`.

### D04 — Missing field is not an empty/wrong answer

Initial CI exposed that truthiness-based response validation converted explicit `non_claims=[]` into `INVALID_RESPONSE`.

Correct semantics:

- required key absent → structural `INVALID_RESPONSE`;
- key present but empty/wrong → valid observation, scored zero on the relevant dimension.

`MISSING FIELD != PRESENT BUT EMPTY/WRONG`.

### D05 — L1/L2 information separation must be produced by the harness

The real Experience Spine packet contains source/provenance/correlation fields. Passing the full packet directly into L1 would contaminate the intended L1/L2 contrast.

Correction: `materialize_experience_views()` derives both conditions from one immutable source packet:

- L1 decision view strips per-item evidence/source/authority/evidence-group/route fields and packet-level correlation/evidence-boundary surfaces;
- L2 receives the exact same decision view plus a deterministic provenance/correlation envelope.

`CONDITION ISOLATION = HARNESS RESPONSIBILITY`, not caller convention.

### D06 — Novel case must not narrate the target invariant

The first XSP-IGT-02 participant summary explicitly described same-lineage and supersession conclusions.

Correction: participant now receives raw historical records with `source_packet` and `revision_link`; correlation/revision meaning must be inferred. Hidden evaluator expectations retain the target invariants.

## CI Incident / Repair Evidence

### Initial PR exact head

Head:
`959e499383d244d27e03adf7c36b69f3a3c52e92`

- Full-Stack `33202452134` — SUCCESS;
- Runtime workflow `33202452007` — FAILURE;
- integrity job — SUCCESS;
- prototype job — SUCCESS;
- integration job `98955011597` — FAILURE;
- integration summary: `312 passed / 1 failed / 11 subtests passed`.

Failure:
`test_scoring_uses_all_six_igt_dimensions_and_requires_full_fidelity`.

Root cause = D04.

### D04 repair observation

Repair head:
`45a899b49f2217605b0ff9b947489f91b016c7c5`

Runtime push run:
`33202559265` — SUCCESS.

This proves the D04 repair on that head only. It is not final transaction verification because D05/D06 and expanded tests changed the branch afterward.

## Novel Cases

### XSP-IGT-01 — ORBIT-SIGNAL / RS-42

Historical launch instruction conflicts with current blocked compatibility gate. Smoke tests are green but current-build consumer compatibility is unproven.

### XSP-IGT-02 — NORTH-HARBOR / NH-31

Participant receives four raw historical records. Shared `source_packet` and `revision_link` relationships must be interpreted alongside current queue-saturation trace and current change authority. Participant text no longer supplies the evaluator conclusions as prose.

No P4/REL-009 object identities are reused in participant cases.

## B0 / L1 / L2 Contract

- `B0`: transformed participant case + generic evidence/authority-first instruction only.
- `L1`: B0 + harness-derived decision view of a usable Experience Spine packet.
- `L2`: L1 decision view + harness-derived provenance/correlation envelope from that same source packet.

The source packet is not mutated.

`HOLD`/unusable packets are rejected rather than silently treated as learning input.

## Qualification Rule

A run becomes structurally `QUALIFIED` only when baseline, execution/information/state/temporal/mutation independence, source-conclusion withholding, leakage clearance, execution context, and independence-attestation reference are all present/positive. A `MODEL_RUN` also requires participant evidence reference.

Any critical `NO` or `UNKNOWN` is quarantined/inconclusive.

Structural qualification does not authenticate external evidence by itself.

## Non-Claims

- Harness execution does not prove model learning.
- Fixture scores do not prove behavioral transfer.
- Repository CI is not an independent model context.
- Separate windows alone are not independence.
- A case PASS, if later independently qualified, is bounded to that case.
- Two-case readiness is readiness for analysis, not promotion.
- Broad generalization and model-weight change remain unproven.

## Current Participant State

All B0/L1/L2 participant rows remain:

`UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

No CI run or deterministic fixture is written into participant outcome rows.

## Remaining Gates

1. Obtain exact-head Full-Stack + Runtime/Integration CI after D05/D06 hardening and expanded tests.
2. Inspect integration log and establish final discovered-test count relative to the verified 299-test pre-IGT main baseline.
3. Record `IGT HARNESS` execution state while participant state stays UNSEEN.
4. Perform final docs-only reconciliation, then final-head CI.
5. Freeze branch; re-read main, PR #77, open PR surface and six-path diff.
6. Squash merge only with expected frozen head SHA.
7. Require post-merge exact-main Full-Stack + Runtime/Integration verification.
8. Only a later workstream may ingest independently qualified model-run packages and populate B0/L1/L2 participant rows.

## Closure Boundary

Potential transaction result:

`EXPERIENCE SPINE IGT HARNESS = EXECUTION-VERIFIED`

while:

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE / INDEPENDENT QUALIFIED MODEL RUNS REQUIRED`.
