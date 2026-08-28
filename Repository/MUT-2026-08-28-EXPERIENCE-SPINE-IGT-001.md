# Experience Spine IGT — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Working branch: `hermuz/experience-spine-igt-20260828`
Status: `SOURCE/READ-BACK VERIFIED / EXACT-HEAD CI PENDING / COGNITIVE EFFECT INCONCLUSIVE`

## Entry State

Experience Spine mechanics are merged to main and post-merge verified.

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

Open PR surface at transaction entry: `0`.

Historical PRs #66/#69 are closed, not merged, provenance preserved.

## Prior Evidence

- clean merge: `a4cc96203b689338a50b7233b46c15eae8449f5a`;
- post-merge Full-Stack `33201440156` — SUCCESS;
- post-merge Runtime workflow `33201440177` — integration/integrity/prototype jobs SUCCESS;
- M2 `33201440226` — SUCCESS.

## Governing Validation Surfaces

Reused, not duplicated:

- `Governance/IGT_INVARIANT_GENERALIZATION_TEST_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_BRIDGE_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_RECORD_TEMPLATE_v1.0.md`;
- `Governance/MI-IGT_INDEPENDENCE_ATTESTATION_v1.0.md`;
- `Governance/MI-IGT_EVIDENCE_QUARANTINE_PROTOCOL_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_COORDINATION_PROTOCOL_v1.0.md`;
- `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md`;
- `Memory/Engineering_Journal/EJR-338_2026-08-27_IGT_LPE_TRANSFER_LEARNING.md`.

No second IGT framework is introduced.

## Verified Capability Boundary

Repository search plus `AI-006` / `INTF-005` review found model-adapter/interface contracts but no verified provider-backed model invocation runner that can create materially independent B0/L1/L2 model contexts from repository CI.

Therefore deterministic Python may verify harness behavior but cannot establish cognitive improvement.

Target split:

1. `IGT HARNESS / EVALUATOR` — executable and testable now.
2. `COGNITIVE EFFECT` — `INCONCLUSIVE` until qualified independent model-run evidence exists.

## Target Invariants

I1. Current direct factual evidence and applicable authority outrank advisory retrieved experience for the claim layer they legitimately govern.

I2. Contradictory experience requires review; rank/order cannot silently decide authority.

I3. Correlated records are not independent confirmation.

I4. Superseded experience does not remain active guidance merely because history is preserved.

I5. Failed/unknown independence or leakage qualification quarantines evidence.

I6. B0/L1/L2 separate generic context, packet availability, and provenance-envelope availability.

I7. A renamed source case is not materially novel.

I8. Scoring/comparison preserves non-claims; evaluator PASS does not equal cognitive-benefit PASS.

I9. Multiple qualified runs for one case/condition may not silently shadow one another.

I10. A self-declared `MODEL_RUN` label is insufficient without participant evidence and independence-attestation references.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt.py` | B0/L1/L2 payloads, six-dimension scoring, MI-IGT qualification/quarantine, duplicate-run fail-closed comparison, model-evidence readiness boundary | Y | Y source/read-back |
| C02 | `Quality/Integration/test_experience_spine_igt.py` | regressions for novelty, hidden reasoning keys, B0/L1/L2 boundaries, six scores, quarantine, attestation, duplicate runs, fixture/model-evidence and non-claim gates | Y | Y source/read-back |
| C03 | `Quality/Integration/experience_spine_igt_cases.py` | two materially novel authority-conflict cases; participant-visible data separated from evaluator expectation mapping | Y | Y source/read-back |
| C04 | `Repository/EXPERIENCE_SPINE_IGT_EXECUTION_MATRIX_2026-08-28.md` | B0/L1/L2 plan, cases, qualification and current UNSEEN/INCONCLUSIVE participant evidence state | Y | Y source/read-back |
| C05 | `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md` | prior transaction reconciled to CLOSED/MERGED/POST-MERGE VERIFIED | Y | Y source/read-back |
| C06 | `Quality/Integration/test_experience_spine_igt.py` | current integration-suite discovery surface; exact-head execution proof required | Y | CI PENDING |

## Source / Diff Reconciliation

Read-back verified current source for:

- evaluator blob: `3084074a5be9f51b4cbf0d5f5e828def7093b0fe`;
- test blob: `4533a2d1e9d3d03e3f935a9c4af7368be52d6833`;
- case blob: `feadb541ed308c4e966b1e6be949f2e9057984a9`.

Branch compare against exact base after C01-C05:

- `ahead_by = 8`;
- `behind_by = 0`;
- changed paths = `6`;
- unexpected paths = `0`.

Changed-path set:

1. `Quality/Integration/experience_spine_igt.py`;
2. `Quality/Integration/experience_spine_igt_cases.py`;
3. `Quality/Integration/test_experience_spine_igt.py`;
4. `Repository/EXPERIENCE_SPINE_IGT_EXECUTION_MATRIX_2026-08-28.md`;
5. `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md`;
6. `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001.md`.

No Runtime, Engine, Memory, Services, Interface, provider, or Governance authority mutation is included.

## Design Corrections Found During Read-Back

### D01 — Candidate choice visibility is not answer leakage

The first leakage detector treated the mere presence of an action option as leaked expected answer because that option also appears in evaluator expectations.

Correction: action labels may be participant-visible; what remains hidden is the evaluator mapping that identifies which option satisfies the invariant, plus evaluator-only invariant/non-claim keys.

### D02 — Duplicate qualified condition runs must not shadow

The first condition-comparison implementation indexed one result per `case_id/condition`, allowing a later qualified run to overwrite an earlier one silently.

Correction: group runs per case/condition; if more than one qualified run exists for the same condition, emit `AMBIGUOUS_MULTIPLE_QUALIFIED_RUNS` and do not calculate a descriptive delta until aggregation policy is explicitly defined.

### D03 — Model label is not model evidence

Readiness now requires `participant_kind=MODEL_RUN` plus participant evidence reference and independence-attestation reference. Structural presence still does not verify the truth of those references; external evidence review remains required.

Reusable rule:

`SELF-DECLARED MODEL LABEL != QUALIFIED MODEL EVIDENCE`.

## Novel Cases

### XSP-IGT-01 — ORBIT-SIGNAL / RS-42

Historical launch instruction conflicts with current blocked compatibility gate. Smoke tests are green but current-build consumer compatibility is unproven.

Target: factual current evidence + applicable release authority; no execution overclaim.

### XSP-IGT-02 — NORTH-HARBOR / NH-31

Historical lessons appear to agree, but some share one lineage and an older projection is superseded; current trace identifies queue saturation and current change authority requires evidence-bound remediation.

Target: correlation/supersession reasoning + current factual evidence + applicable normative authority.

No P4/REL-009 object names are reused in participant cases.

## B0 / L1 / L2

- `B0`: transformed case + generic evidence/authority-first instruction only.
- `L1`: B0 + Experience Spine packet.
- `L2`: L1 + provenance/correlation/authority envelope.

Hidden evaluator reasoning keys are never attached to participant payloads.

## Qualification Rule

A run becomes `QUALIFIED` only when baseline, execution/information/state/temporal/mutation independence, source-conclusion withholding, leakage clearance, execution context, and independence-attestation reference are all present/positive.

Any critical `NO` or `UNKNOWN` is quarantined/inconclusive for promotion purposes.

## Non-Claims

- Harness execution does not prove model learning.
- Fixture scores do not prove behavioral transfer.
- Repository CI is not an independent model context.
- Different windows alone are not independence.
- A case PASS proves only that qualified case if/when the participant evidence itself is independently verified.
- Two-case readiness is only readiness for bounded transfer analysis, not promotion.

## Verification Gates Still Open

1. Open draft PR from this six-path transaction.
2. Require exact-head Full-Stack + Runtime/Integration CI.
3. Inspect integration job evidence and establish that the new IGT test module executed.
4. Record harness result separately from cognitive-effect result.
5. Freeze final head, re-read current main/open PR surface, merge only with expected SHA.
6. Require post-merge exact-main CI.
7. Keep participant rows in execution matrix `UNSEEN` until real independent runs exist.

## Closure Boundary

Potential transaction result:

`EXPERIENCE SPINE IGT HARNESS = EXECUTION-VERIFIED`

while:

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE / INDEPENDENT QUALIFIED MODEL RUNS REQUIRED`.
