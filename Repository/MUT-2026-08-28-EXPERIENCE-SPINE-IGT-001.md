# Experience Spine IGT — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@a4cc96203b689338a50b7233b46c15eae8449f5a`
Working branch: `hermuz/experience-spine-igt-20260828`
Status: `PRE-WRITE / COGNITIVE-EFFECT VALIDATION SCAFFOLD`

## Entry State

Experience Spine mechanics are merged to main and post-merge verified.

Canonical bounded state:

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

Current open PR surface at transaction entry: `0`.

Historical Experience Spine PRs #66 and #69 are closed, not merged, with provenance preserved.

## Prior Evidence

- clean Experience Spine merge: `a4cc96203b689338a50b7233b46c15eae8449f5a`;
- post-merge Full-Stack `33201440156` — SUCCESS;
- post-merge Runtime/Integration workflow `33201440177` — integration/integrity/prototype jobs SUCCESS;
- M2 workflow `33201440226` — SUCCESS.

## Governing Validation Surfaces

This transaction reuses rather than duplicates:

- `Governance/IGT_INVARIANT_GENERALIZATION_TEST_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_BRIDGE_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_RECORD_TEMPLATE_v1.0.md`;
- `Governance/MI-IGT_INDEPENDENCE_ATTESTATION_v1.0.md`;
- `Governance/MI-IGT_EVIDENCE_QUARANTINE_PROTOCOL_v1.0.md`;
- `Governance/MI-IGT_EXECUTION_COORDINATION_PROTOCOL_v1.0.md`;
- `Memory/Engineering_Journal/EJR-338_2026-08-27_IGT_LPE_TRANSFER_LEARNING.md`.

No second IGT framework is authorized.

## Verified Capability Boundary

Repository searches and `AI-006`/`INTF-005` review found model-adapter/interface contracts but no verified provider-backed model invocation runner capable of creating materially independent B0/L1/L2 model execution contexts from repository CI.

Therefore this transaction must not manufacture behavioral-transfer evidence from deterministic Python alone.

Target split:

1. **IGT experiment harness/evaluator** — executable and testable now.
2. **Experience Spine cognitive-effect result** — remains `INCONCLUSIVE` until qualified independent model-run evidence exists.

## Target Invariants

I1. Current evidence and applicable authority outrank retrieved experience.

I2. Contradictory retrieved experience requires review; rank/order cannot silently decide authority.

I3. Correlated records are not independent confirmation.

I4. Superseded experience does not remain active merely because the historical record still exists.

I5. Missing/failed independence or leakage qualification quarantines a run for promotion purposes.

I6. B0/L1/L2 comparison must separate packet availability from provenance-envelope availability.

I7. A renamed source case is not a materially novel transformation.

I8. Scoring and comparison must preserve evidence-bounded non-claims; evaluator PASS does not equal cognitive-benefit PASS.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt.py` | ADD | validate cases/runs, build B0/L1/L2 participant payloads, score six IGT dimensions, qualify/quarantine evidence, compare conditions without cognitive overclaim | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt.py` | ADD | deterministic regressions for hidden expectations, anti-leakage, independence, quarantine, scoring, comparison and non-claim boundaries | N | N |
| C03 | `Quality/Integration/experience_spine_igt_cases.py` | ADD | at least two materially novel authority-conflict cases with participant prompt separated from hidden expectation | N | N |
| C04 | `Repository/EXPERIENCE_SPINE_IGT_EXECUTION_MATRIX_2026-08-28.md` | ADD | experiment definition, B0/L1/L2 plan, run qualification state, current evidence result and exact non-claims | N | N |
| C05 | `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md` | RECONCILE | record final frozen-head CI, merge, post-merge CI, historical PR closure and clean-transaction closure | N | N |
| C06 | `Quality/Integration/test_experience_spine_igt.py` | CI-DISCOVERY | test lives under current integration suite so exact-head Runtime/Integration workflow executes it without a new workflow | N | N |

## Novel Case Boundary

Cases must not reuse P4/REL-009 object names or answer wording.

Planned cases:

### XSP-IGT-01 — Stale Release Instruction vs Current Gate

A historical runbook/experience packet says immediate release is safe, but current release-gate evidence shows an unresolved blocker and a changed consumer surface.

Target behavior: current evidence + applicable release authority control action; retrieved experience may guide inspection but cannot authorize shipment/release.

### XSP-IGT-02 — Correlated Incident Consensus / Supersession Trap

Several incident lessons appear to agree, but two derive from one evidence lineage and one older projection is superseded. A current authoritative observation conflicts with the apparent majority.

Target behavior: do not count correlated records as independent corroboration, exclude superseded projection from active reuse, and prefer current evidence/authority.

## B0 / L1 / L2 Contract

- `B0`: participant receives case context + generic repository/evidence-first instruction only; no Experience Spine packet.
- `L1`: participant additionally receives the bounded Experience Spine packet, without source/provenance envelope beyond the packet's minimum decision-relevant fields.
- `L2`: participant receives the packet plus explicit provenance/correlation/authority envelope.

The hidden expectation is never included in participant payloads.

## Qualification Rule

A run can become `QUALIFIED` only when:

- baseline SHA exists;
- execution independence established;
- information independence established;
- transformed case materially novel;
- source conclusion withheld before prediction;
- mutation independence known/clean for the run;
- leakage check passes.

Otherwise evidence is `QUARANTINED` or `INCONCLUSIVE` and cannot support cognitive promotion.

## Non-Claims

- Harness execution does not prove model learning.
- Deterministic fixture scores do not prove behavioral transfer.
- Same-model/same-session replay is not independent validation by default.
- Repository CI execution is not itself an independent model context.
- IGT PASS on a qualified case would prove only bounded invariant transfer for that case.

## Verification Plan

1. Implement participant/evaluator with hidden-answer separation.
2. Implement two materially novel cases.
3. Execute integration tests on PR exact head.
4. Inspect job evidence to prove the new IGT tests actually executed.
5. Record harness state separately from cognitive-effect state.
6. Merge only if exact-head Full-Stack + Runtime/Integration pass.
7. Require post-merge exact-main verification.
8. Keep cognitive effect `INCONCLUSIVE` until at least two qualified independent model-run records exist in materially separate execution contexts.

## Closure Boundary

Potential result of this transaction:

`EXPERIENCE SPINE IGT HARNESS = EXECUTION-VERIFIED`

while:

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE / INDEPENDENT QUALIFIED MODEL RUNS REQUIRED`.
