# HERMUZ Current-State Build Roadmap — 2026-08-28

Status: `SESSION CLOSED / RESUME-SAFE / P3 VERIFIED / P4 DISPOSITION REVIEW NEXT`
Protocol: `GOV-013 + GOV-013A + GOV-014 + GOV-015`
Observed main baseline: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Authority class: `Analysis / Execution / Transfer Evidence — NON-CANONICAL`

## 1. Session Objective

Reconstruct current ARGO-KOP state from repository evidence, reassess accumulated HERMUZ experience, remove stale/duplicated build paths, construct the smallest current-main P3/REL-009 evidence unit, verify it completely, inspect P4 semantics before creating reverse-reference debt, preserve concurrent HORUS safety, and leave one compact continuation surface.

Evidence precedence used throughout:

`Current repository + canonical authority + exact-head execution evidence > reconciliation records > historical branches > memoirs/learning > conversation memory`.

## 2. Current Priority Interpretation

Current reconciliation evidence establishes:

- `P1 = CLOSED` within inspected Ring-0 scope.
- `P2 = RECONCILED` within verified active inventory scope.
- `P3 = executable relationship proof` was the first active engineering gap at session entry.
- `P4 = OPEN / critical graph validation`.
- `P5 = EXECUTION-VERIFIED / BUILD CLOSED` within its scope.
- `P6 = EXECUTION-VERIFIED / POLICY-UNRESOLVED / NO-AUTO-PROMOTION`.

The repeated `identity_scope_reconciled=false` warning does not justify inserting the twelve Core/Knowledge artifacts into REP-001. REP-021 already classifies them as deferred authority/cross-layer scope.

## 3. Historical Workstream Cleanup

### PR #63

Final disposition:

`CLOSED WITHOUT MERGE / HISTORICAL DESIGN + EXECUTION EVIDENCE PRESERVED`.

Its divergent branch remains available for provenance, but P374 permits only reconciled design reuse. PR metadata records that clean PR #65 supersedes it as an active construction path.

### PR #64

Final disposition:

`CLOSED WITHOUT MERGE / HISTORICAL EXPERIMENT + EXECUTION EVIDENCE PRESERVED`.

Its exact historical head had successful CI, but the workstream accumulated 85 commits / 79 files and was not a clean promotion unit. Useful concepts were independently reassessed instead of merging the branch wholesale.

### Self-audit

Retained as historical analysis/evidence only. No new functional work was added to the long-lived audit branch.

Result: old P3 build doors are no longer active promotion surfaces; their history remains intact.

## 4. Clean P3 Candidate

Fresh current-main branch:

`hermuz/p3-rel009-clean-observation-20260828`

Active PR:

`#65 — P3: clean isolated REL-009 observation seam`

Current candidate head:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

Final main comparison at session end:

- `ahead_by = 4`
- `behind_by = 0`
- exactly 8 changed files
- no unexpected path
- `connected_spine_runner.py` unchanged
- `REP-014` unchanged

Mutation matrix:

`Repository/MUT-2026-08-28-P3-REL009-CLEAN-001_MUTATION_MATRIX.md`

All C01-C08 rows reached `Applied=Y / Verified=Y`.

### Clean implementation shape

- `Runtime/Execution/run010_handoff_contract.py`: pure provenance/authorization handoff; no dispatch or repository I/O.
- `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py`: existing governed adapter retained; explicit `authorization_id` now required before connector access.
- `Quality/Integration/rel009_run010_srv009_observation.py`: isolated evidence harness that composes the handoff with the existing adapter and records an attributable RUN-010 → SRV-009 dispatch observation.
- focused integration tests cover positive provenance continuity plus missing/blocked authorization fail-closed behavior.
- P3 real-provider workflow changed only to keep current consumers compatible with the authorization identity contract.

### Historical path rejected

`Runtime/Execution/run010_eng006_srv009_consumer.py` from PR #64 was not extracted because it reimplemented low-level connector dispatch beside the existing governed adapter. The clean path composes existing authority instead of creating a parallel write mechanism.

## 5. CI Failure and Architectural Correction

Initial clean-candidate head `c83683e3262412dc7015a62bae94389dfef6b020` produced:

- Full-Stack PASS
- Prototype PASS
- Integration PASS
- Integrity FAIL

First meaningful failure:

`Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py`

The first observation helper had been placed under `Runtime/Execution` and contained the deliberately protected `SRV-009` literal.

Classification:

`EVIDENCE HARNESS PLACED IN PROTECTED RUNTIME SCOPE / EXISTING GUARD CORRECT / LOCATION DEFECT`.

The guard was not weakened.

Correction commit:

`180b4c89ee51ff93f0f2ba1043bdcbccd511865b`

Correction:

- move observation harness to `Quality/Integration`;
- delete Runtime/Execution observation helper;
- keep only the pure handoff in Runtime/Execution;
- keep connected spine simulation-only.

Post-correction read-back proved the old Runtime path absent, the new Quality path present, tests bound to the relocated helper, and the final diff still limited to the declared eight files.

Session learning candidate:

`When a proof harness conflicts with a deliberate architecture guard, reassess proof placement before weakening the guard to make CI green.`

No governance promotion is implied.

## 6. Exact-Head Verification

Final candidate head:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

Runtime/Prototype/Integration run:

`33193670294 — SUCCESS`

- prototype-tests `98925253840` — SUCCESS
- integrity-tests `98925254152` — SUCCESS, `111 passed`
- integration-tests `98925254218` — SUCCESS, `295 passed / 1 expected P2 identity warning / 11 subtests`

Full-Stack Repository Audit:

`33193670090 — SUCCESS`

Therefore the final clean candidate is:

`SOURCE-VERIFIED / READ-BACK-VERIFIED / EXACT-HEAD CI-VERIFIED`.

## 7. Provider-Backed Adapter/Connector E2E

Isolated branch from exact candidate:

`e2e/runtime-srv009-p3-clean-20260828`

Trigger-only descendant:

`a5352d4b90f14387d12ad20a3f7d4676c0d80e2e`

Workflow:

`P3 Runtime GitHub E2E`

Run `33193773687` / job `98925604992`: SUCCESS.

Observed:

- create trace `TR-c9ca3ebca1e3`
- update trace `TR-1e7fe1a17e26`
- persisted SHA `d3287757b644047d6de70a548cf202e34dab1e49`
- create/update/read-back success
- cleanup success
- final missing/read-back verification success

Boundary:

This proves the reused ENG-006/SRV-009 production adapter and `GitHubRepositoryConnector` remain healthy after authorization-id dependency closure. It does not claim the new integration helper itself executed against GitHub; that helper is proven by exact-head integration CI with controlled in-memory I/O.

## 8. P3 Evidence Disposition

P374 required:

`RUN-010 origin → explicit SRV-009 target → observed callable boundary → attributable dispatch event → preserved authorization/provenance → controlled observation → exact-head CI`.

The clean candidate supplies these within its isolated integration scope, while the provider E2E independently verifies the reused real adapter/connector path.

Current technical disposition:

`B07/B08 = SATISFIED WITHIN CLEAN ISOLATED EVIDENCE SCOPE / RELATIONSHIP PROMOTION REVIEW ELIGIBLE`.

This is not automatic canonical promotion. GOV-015 explicitly separates test success from canonical promotion, and the P4 consumer matrix says satisfying B06/B07/B08 permits reconsideration rather than mandatory promotion.

PR #65 is now `Ready for Review`, open/unmerged, with no submitted review or review thread at final inspection.

## 9. P4 Semantic Reassessment

P4 remains distinct from P3 because it evaluates directional/reverse critical-edge evidence.

Three current reverse-evidence checks were performed:

1. direct canonical read of `Services/SRV-009_UPDATE_SERVICE.md`;
2. independent repository searches for RUN-010/SRV-009 reverse caller/consumer evidence;
3. Services/Architecture review using `SRV-010`, `ARC-006` and `ARC-007`.

Findings:

- SRV-009 explicitly identifies ENG-006 as its execution consumer relationship.
- SRV-009 does not independently name RUN-010 as an endpoint/caller.
- SRV-010 only recognizes RUN-010 at the broader runtime/service boundary and explicitly warns that this does not prove every service executes on every runtime path.
- ARC-006 requires dependencies to be necessary, directionally justified and free of circularity.
- ARC-007 says Runtime may consume approved service interfaces and that component ownership/interface boundaries must remain explicit.

No new direct reverse endpoint evidence was found.

### Semantic correction to the old P4 path

The absence of `SRV-009 -> RUN-010` must not automatically be treated as a document defect.

REL-009 is semantically directional:

`RUN-010 CONSUMES SRV-009`.

Forcing the service to depend on or mechanically list every runtime consumer merely to manufacture symmetry risks artificial coupling. The P4 matrix already permits an intentional-one-way disposition.

Candidate disposition for authorized review:

`REL-009 = CONSUMES / EXECUTABLE-VERIFIED WITHIN ISOLATED INTEGRATION SCOPE / INTENTIONAL ONE-WAY / NON-UNIVERSAL RUNTIME PATH / REVERSE DEPENDENCY NOT REQUIRED`.

This remains non-canonical until an applicable relationship/architecture review accepts or rejects it.

Next P4 question is therefore semantic disposition, not “add a reverse reference until the matrix becomes green.”

## 10. False Control-Plane Debt Removed

An earlier session analysis carried forward a claim that current GOV-013 referenced a missing `CONTROL_PLANE_STATUS.md` file.

Before any Governance mutation, the claim was independently rechecked:

- repository search for the filename: no result;
- direct search within current GOV-013: no occurrence;
- current GOV-013 asks for `PROJECT_BOOTSTRAP.md` plus current control-plane evidence generically;
- REP-015 exists and defines the deterministic bootstrap sequence and cross-model handoff minimum.

Disposition:

`NO CURRENT GOV-013 MISSING-FILE DEFECT ESTABLISHED`.

The proposed repair task was deleted from the roadmap. No file was invented and no Governance mutation was performed.

Classification:

`STALE PRIOR-STATE / MEMORY-DERIVED INTERPRETATION DEFECT / CURRENT REPOSITORY CORRECT`.

## 11. Concurrent HORUS / Experience Work Safety

The user explicitly warned that HORUS is working concurrently on accumulated experience.

During the session:

- `main` repeatedly remained at `09b216e403fe99a6f1a4a35e3c3038831398f6a3`;
- `horus/meta-learning-foundation-v6` was observed at `f250edd2c4ba86039941e2a2efdee6055689ecd8`;
- a new concurrent PR #66 appeared: `P375: bounded Experience Spine candidate`, head `856cc5fa842f0f79c91e79ef20512a0f30b43e51`, based on the same main.

PR #66 changed only:

- `Knowledge/Learning/EXPERIENCE_SPINE_CONTRACT.md`
- `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md`
- `Knowledge/Learning/experience_spine.py`
- `Knowledge/Learning/test_experience_spine.py`
- `Repository/REP-043_SESSION_DELTA_2026-08-28_P375.md`

PR #65 changed only its separate eight-file P3 surface.

Observed file overlap between #65 and #66:

`ZERO`.

Current classification:

`CONCURRENT / FILE-DISJOINT / NO CURRENT COLLISION`.

However, if #66 or any other agent changes `main` before #65 promotion/merge, file-disjointness alone is insufficient. The required gate remains:

`RE-READ NEW MAIN → COMPARE CANDIDATE → INSPECT OVERLAP/SEMANTIC IMPACT → RERUN REQUIRED CI → THEN DECIDE`.

No blind rebase/cherry-pick/merge is permitted from a stale base.

## 12. Tool Incidents

Several accidental PR-creation calls with nonexistent placeholder heads were rejected by GitHub with `422 Validation Failed`.

Result:

`NO PR CREATED / NO REF CHANGE / NO REPOSITORY MUTATION`.

The incidents are retained as execution traceability only.

## 13. Validated / Reapplied Knowledge

1. Repository reality outranks memory, summaries and prior HERMUZ analysis.
2. Exact-head attribution is mandatory.
3. `NO RUN`, `NO STATUS`, `PASS`, `FAIL` and `NOT OBSERVED` are distinct.
4. Successful CI does not make an accumulated branch a good promotion unit.
5. Historical work should be dependency-closed and extracted, not copied wholesale.
6. Candidate gap does not authorize mutation.
7. Test success proves only the exercised boundary.
8. Trace production is not downstream invocation.
9. Provider proof and integration-harness proof remain distinct.
10. Do not weaken deliberate architecture guards to accommodate misplaced evidence code.
11. Consolidation may be higher-value engineering than adding another test/report.
12. Concurrent agents require immediate pre-promotion synchronization.
13. Documentation/memoirs do not self-upgrade authority.
14. Bidirectional validation must not mechanically create symmetric dependencies for directional semantics.
15. A missing reverse reference may be intentional; decide semantics before mutating documentation.
16. Delete a planned work item when current repository evidence disproves its premise.

Items 14-16 remain candidate/session learning until independently validated; they are not governance rules merely because this record contains them.

## 14. Roadmap

### Priority 1 — REL-009 semantic/promotion review

Review PR #65 evidence together with the intentional-one-way P4 candidate. Determine the exact supported relationship wording without claiming universal connected-spine execution.

### Priority 2 — smallest canonical relationship mutation, only if authorized

If the disposition is accepted:

`re-read main/concurrent work → GOV-014 matrix → minimal REP-014/P4 state mutation → exact-head CI → read-back → reconciliation`.

If not accepted, keep REL-009 open with the precise unresolved semantic question rather than fabricating reverse evidence.

### Priority 3 — explicit P4 closure review

Current critical matrix contains:

- REL-005: already bidirectional/executable-verified;
- REL-061: already intentional-one-way/governance-revalidated;
- REL-009: sole remaining semantic disposition blocker.

After REL-009 disposition, perform explicit P4 closure review rather than restarting already-settled edges.

### Priority 4 — branch/workstream hygiene

PR #63 and #64 are now closed without merge; preserve their branches/history as evidence. Do not resume functional growth on those superseded paths.

Do not interfere with PR #66 unless current evidence shows a cross-impact.

### Priority 5 — broader Connected Baseline

After P3/P4 disposition, resume repository-wide relationship/domain validation before feature expansion.

Removed task:

`CONTROL_PLANE_STATUS.md / GOV-013 repair` — premise disproven by current canonical evidence.

## 15. Explicit Non-Claims

- ARGO is not globally clean.
- Connected Baseline is not complete.
- REL-009 is not canonically promoted by this record.
- Normal connected spine is not production-dispatch enabled.
- PR #65 readiness/CI is not merge authorization.
- PR #66 is not evaluated here beyond concurrency/file-overlap safety.
- HORUS outputs are not auto-promoted into HERMUZ authority.
- intentional-one-way REL-009 wording is a candidate pending authorized review.

## 16. Closure

P3 construction/evidence: `COMPLETE / VERIFIED` within declared scope.

P3 old workstream cleanup: `COMPLETE` — PR #63/#64 closed without merge; history preserved.

P4 reconnaissance: `COMPLETE / NO MUTATION` — semantic disposition identified as the next real question.

False control-plane debt: `INVALIDATED / REMOVED BEFORE MUTATION`.

Concurrent HORUS/Experience surface: `OBSERVED / ZERO FILE OVERLAP WITH PR #65 / MAIN UNCHANGED AT FINAL CHECK`.

Documentation/learning transfer: `COMPLETE`.

Final state:

`SESSION CLOSED / RESUME-SAFE / PR65 READY FOR REVIEW / P4 REL009 DISPOSITION NEXT / SUPERSEDED PR PATHS CLOSED / MAIN UNCHANGED AT FINAL OBSERVATION`.

## 17. Next Safe Entry

`Re-read main + concurrent PR/branch state → confirm PR #65 head/base/diff/CI → perform authorized REL-009 semantic disposition review → if accepted execute minimal REP-014/P4 mutation under GOV-014 → explicit P4 closure review → continue Connected Baseline`.
