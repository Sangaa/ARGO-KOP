# Experience Spine IGT — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Working branch: `hermuz/experience-spine-igt-20260828`
PR: `#77`
Status: `HARNESS EXECUTION-VERIFIED ON HARDENED SOURCE HEAD / FINAL DOC-HEAD CI REQUIRED / PARTICIPANT RUNS UNSEEN / COGNITIVE EFFECT INCONCLUSIVE`

## Entry State

Experience Spine mechanics were already merged and post-merge verified on main.

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

Open PR surface at transaction entry was `0`.

## Governing Surfaces

This transaction reuses the existing IGT / MI-IGT system, including the invariant generalization test, execution bridge, execution record template, independence attestation, evidence quarantine, execution coordination, GOV-018 evidence reasoning, and EJR-338 transfer-learning evidence.

No replacement IGT framework is introduced.

## Capability Boundary

Repository review found model-adapter/interface contracts but no verified provider-backed model invocation runner capable of generating materially independent B0/L1/L2 model contexts from repository CI.

Therefore:

`IGT HARNESS / EVALUATOR` may be execution-verified now.

`COGNITIVE EFFECT` remains `INCONCLUSIVE` until qualified independent model-run evidence exists.

CI, deterministic fixtures, and evaluator regressions are never counted as participant/model-learning evidence.

## Implemented Invariants

1. Current direct factual evidence and applicable authority outrank advisory retrieved experience for the claim layer they legitimately govern.
2. Contradictory experience requires review; ordering cannot create authority.
3. Correlated records are not independent confirmation.
4. Revised/superseded experience does not remain active guidance merely because history is preserved.
5. Failed/unknown independence or leakage qualification quarantines evidence.
6. B0/L1/L2 information separation is produced by the harness, not trusted to caller convention.
7. Novel cases must require fresh reasoning rather than merely rename source objects or narrate the answer.
8. Six-dimension scoring preserves non-claims; evaluator PASS is not cognitive-benefit PASS.
9. Duplicate qualified runs for one case/condition fail closed instead of silently shadowing.
10. `MODEL_RUN` is insufficient without participant evidence and independence-attestation references.
11. Missing response fields and explicit empty/wrong answers are distinct evidence states.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt.py` | deterministic condition materialization, scoring, qualification/quarantine, duplicate protection, bounded readiness | Y | Y |
| C02 | `Quality/Integration/test_experience_spine_igt.py` | 17 discovered integration regressions covering novelty, leakage, condition isolation, immutability, scoring, missing-vs-empty, quarantine, attestation, duplicate runs and non-claims | Y | Y |
| C03 | `Quality/Integration/experience_spine_igt_cases.py` | two materially novel authority-conflict cases with hidden evaluator expectations | Y | Y |
| C04 | `Repository/EXPERIENCE_SPINE_IGT_EXECUTION_MATRIX_2026-08-28.md` | experiment state and participant UNSEEN matrix | Y | Y |
| C05 | `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md` | prior clean transaction reconciled to CLOSED/MERGED/POST-MERGE VERIFIED | Y | Y |
| C06 | CI discovery | current `Quality/Integration` workflow executes the IGT harness regressions | Y | Y |

## Design Corrections Learned During Construction

### D01 — Candidate visibility is not answer leakage
Candidate action labels may be visible. Leakage is the hidden correctness mapping, evaluator invariants, or evaluator-only non-claims.

### D02 — Duplicate qualified runs must not shadow
Multiple qualified results for one `case/condition` produce `AMBIGUOUS_MULTIPLE_QUALIFIED_RUNS`; no score delta is computed until aggregation policy exists.

### D03 — Self-declared model identity is not model evidence
`MODEL_RUN` requires evidence and independence-attestation references, and those references still require external verification.

### D04 — Missing field is not empty/wrong answer
Initial CI exposed a truthiness bug. Correct semantics:
- absent key → structural `INVALID_RESPONSE`;
- present but empty/wrong → scoreable observation with zero on the affected dimension.

`MISSING FIELD != PRESENT BUT EMPTY/WRONG`.

### D05 — L1/L2 separation is a harness responsibility
The real Experience Spine packet includes source/provenance/correlation data. The harness now derives an L1 decision view with those fields stripped and an L2 provenance envelope from the same immutable source packet.

### D06 — A novel case must not narrate its target invariant
XSP-IGT-02 now exposes raw historical records with lineage/revision links; the participant must infer correlation and revision meaning rather than receive the evaluator conclusion in prose.

## CI Evidence Chain

### Initial head
`959e499383d244d27e03adf7c36b69f3a3c52e92`
- Full-Stack `33202452134` — SUCCESS.
- Runtime `33202452007` — FAILURE.
- integration job `98955011597` — `312 passed / 1 failed / 11 subtests`.
- failure exposed D04.

### Repair head
`45a899b49f2217605b0ff9b947489f91b016c7c5`
- Runtime push run `33202559265` — SUCCESS.

### Hardened source head
`40397fce03b3481765971b06f48a4004847f679d`
- Full-Stack `33203060544` — SUCCESS.
- Runtime/Integration `33203060557` — SUCCESS.
- integration job `98957084303` — SUCCESS.
- GitHub checked out PR merge ref `c9a4cff828d912c6afee7470336d9f633e7a13f0`, explicitly `Merge 40397fce... into a4cc9620...`.
- command: `python -m pytest -q Quality/Integration`.
- result: `316 passed, 1 warning, 11 subtests passed in 8.46s`.

The verified pre-IGT Experience Spine main baseline was `299` integration tests. The hardened candidate therefore contributes `17` discovered integration regressions.

This establishes both head-associated PR CI and compatibility of the hardened head with the exact current base through GitHub's generated merge ref. It does not convert CI into independent model evidence.

## Novel Cases

- `XSP-IGT-01 / ORBIT-SIGNAL / RS-42`: stale release instruction versus current blocked compatibility gate.
- `XSP-IGT-02 / NORTH-HARBOR / NH-31`: raw historical lineage/revision records versus current queue-saturation evidence and current change authority.

No P4/REL-009 source identities are reused in participant cases.

## Condition Contract

- `B0`: transformed case + generic evidence/authority-first instruction.
- `L1`: B0 + harness-derived decision view of a usable Experience Spine packet.
- `L2`: L1 + harness-derived provenance/correlation envelope from that same packet.

The source packet is immutable. Unusable/HOLD packets are rejected.

## Participant Evidence State

All B0/L1/L2 participant rows remain `UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

No workflow, fixture, or evaluator result is inserted into participant outcome rows.

## Remaining Closure Gates

1. Run exact-head Full-Stack + Runtime/Integration after this evidence-documentation commit.
2. Freeze if PASS.
3. Re-read main, PR #77, open PR surface and changed-path set.
4. Squash merge only with expected frozen head SHA.
5. Require post-merge exact-main verification.
6. A later workstream may ingest independently qualified model-run packages and populate B0/L1/L2 evidence.

## Bounded Result

`EXPERIENCE SPINE IGT HARNESS = EXECUTION-VERIFIED ON HARDENED SOURCE HEAD`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE / INDEPENDENT QUALIFIED MODEL RUNS REQUIRED`.
