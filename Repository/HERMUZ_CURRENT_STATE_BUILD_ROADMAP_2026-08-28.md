# HERMUZ Current-State Build Roadmap — 2026-08-28

Status: `SESSION CLOSED / P3 CLEAN BUILD VERIFIED / PROMOTION REVIEW NEXT`
Protocol: `GOV-013 + GOV-013A + GOV-014 + GOV-015`
Base branch observed: `main`
Base HEAD observed at final synchronization: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Roadmap branch: `hermuz/current-state-roadmap-20260828`
Authority class: `Analysis / Recovery / Execution / Transfer Evidence — NON-CANONICAL`

## 1. Purpose

Reconstruct ARGO-KOP from current repository evidence before further construction; reconcile accumulated HERMUZ experience with current authority; remove stale branch/promotion assumptions; identify the actual priority chain; construct the smallest dependency-closed P3/REL-009 evidence candidate; verify it through governed CI and real provider execution where applicable; preserve concurrent-agent safety; and leave one compact resume-safe transfer surface rather than another sequence of checkpoint files.

This record does not itself promote a relationship, governance rule, branch or runtime capability.

## 2. Evidence Precedence Applied

`Current main + Canonical Authority + Exact-HEAD CI/Runtime Evidence > Current Reconciliation Records > Historical Branch Evidence > Memoirs/Learning > Conversation Narrative`

Key current authority/evidence read during the session:

- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md`
- `Repository/REP-021_P2_INDEX_SCOPE_RECONCILIATION_2026-08-17.md`
- `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md`
- `Repository/REP-042_SESSION_DELTA_2026-08-28_P374.md`
- current branch/PR/workflow evidence.

Historical/self-audit/HORUS material was treated as evidence or learning according to its actual authority state, never auto-promoted by documentation.

## 3. Reconstructed Current Priority State

Current reconciliation evidence establishes:

- `P1 = CLOSED` within inspected Ring-0 control-plane scope.
- `P2 = RECONCILED` within verified active inventory scope.
- `P3 = OPEN / EXECUTABLE RELATIONSHIP PROOF` at session entry.
- `P4 = OPEN / BIDIRECTIONAL CRITICAL GRAPH VALIDATION`.
- `P5 = EXECUTION-VERIFIED / BUILD CLOSED` within its harness scope.
- `P6 = EXECUTION-VERIFIED / POLICY-UNRESOLVED / NO-AUTO-PROMOTION`.

The older P2-open language retained in REP-016 is historical/current-state layering and does not override REP-021/REP-022.

The recurring `identity_scope_reconciled=false` CI warning does not authorize blind index mutation. REP-021 already classifies the twelve Core/Knowledge canonical-unindexed records as deferred authority/cross-layer scope rather than direct active-index defects.

## 4. Historical Workstream Reconciliation

### PR #63

Classified as:

`HISTORICAL DESIGN + EXECUTION EVIDENCE SOURCE / NOT A WHOLESALE PROMOTION UNIT`.

Its branch is materially diverged from current main. P374 explicitly permits design reuse only after current-main reconciliation. PR metadata was corrected accordingly.

### PR #64

Classified as:

`EVIDENCE-RICH EXPERIMENTAL WORKSTREAM / NOT A CLEAN PROMOTION UNIT`.

Its current exact head had successful Runtime/Integration and Full-Stack pull-request CI, superseding the stale historical `NO RUN` narrative. Its 85-commit/79-file accumulated surface was deliberately not promoted wholesale. PR metadata was corrected accordingly.

### Self-audit branch

Classified as:

`HISTORICAL ANALYSIS + EVIDENCE SOURCE`.

The branch itself demonstrates that an audit branch can become accumulation debt. No further functional work was added to it in this session.

## 5. Clean P3 Extraction

Fresh branch created directly from current main:

`hermuz/p3-rel009-clean-observation-20260828`

Draft PR:

`#65 — P3: clean isolated REL-009 observation seam`

Final observed candidate head:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

Final diff against main:

- 4 commits;
- exactly 8 changed files;
- no unexpected path;
- `connected_spine_runner.py` unchanged;
- canonical REL-009 registry state unchanged.

Mutation control:

`Repository/MUT-2026-08-28-P3-REL009-CLEAN-001_MUTATION_MATRIX.md`

All rows C01-C08 reached:

`Applied = Y / Verified = Y`.

### Included design

1. `Runtime/Execution/run010_handoff_contract.py`
   - pure handoff builder;
   - no repository I/O;
   - no SRV-009 literal/dispatch;
   - validates execution trace, authorization state and authorization identity.

2. `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py`
   - retains the existing governed dispatcher path;
   - now requires explicit `authorization_id` before connector access;
   - fails closed when authorization identity is absent.

3. `Quality/Integration/rel009_run010_srv009_observation.py`
   - integration-only evidence harness;
   - composes the pure handoff contract with the existing governed production adapter;
   - emits an attributable observation containing RUN-010 origin, explicit SRV-009 target, callable boundary, execution/task/session/source-trace identity, authorization identity, downstream execution trace, dispatch status and post-read verification.

4. Focused integration regressions preserve positive and fail-closed paths.

5. Existing P3 provider E2E workflow was updated only for `authorization_id` dependency closure.

### Explicitly rejected historical path

Historical PR #64 contains `Runtime/Execution/run010_eng006_srv009_consumer.py`, which performs lower-level connector read/create/update/read-back directly.

It was deliberately NOT extracted because it would create a parallel dispatch implementation beside the already governed ENG-006/SRV-009 production adapter. The clean candidate composes the existing governed adapter instead.

## 6. CI Failure, Root Cause and Correction

Initial clean-candidate head:

`c83683e3262412dc7015a62bae94389dfef6b020`

Observed results:

- Full-Stack Repository Audit: PASS.
- Prototype job: PASS.
- Integration job: PASS.
- Integrity job: FAIL.

First meaningful failure:

`Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py`

The existing guard intentionally prohibits the literal `SRV-009` inside `Runtime/Execution/*.py`. The initial observation helper had been placed at:

`Runtime/Execution/run010_srv009_observation.py`

Root classification:

`NEW EVIDENCE SEAM PLACED IN PROTECTED RUNTIME SCOPE / EXISTING INTEGRITY RULE CORRECT / DESIGN LOCATION DEFECT`.

The guard was NOT weakened, bypassed or rewritten.

Correction:

- relocated the evidence helper to `Quality/Integration/rel009_run010_srv009_observation.py`;
- removed the initial Runtime/Execution helper;
- kept Runtime/Execution's negative consumer boundary intact;
- kept connected spine simulation-only.

Correction commit:

`180b4c89ee51ff93f0f2ba1043bdcbccd511865b`.

Post-correction read-back confirmed the old Runtime path absent, the new Quality path present, the focused test importing the new path, and the final diff still limited to eight files.

This failure is retained as useful execution evidence: when a proof harness conflicts with a deliberate architecture guard, first reassess the proof's placement rather than weakening the guard to make CI green.

Learning level:

`SESSION-LEARNING / TRANSFERABLE CANDIDATE`.

It is not promoted to governance by this record.

## 7. Exact-HEAD Governed CI

Final clean candidate head:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

### Runtime / Prototype / Integration workflow

Run: `33193670294` — `SUCCESS`

Jobs:

- prototype-tests `98925253840` — SUCCESS;
- integrity-tests `98925254152` — SUCCESS;
- integration-tests `98925254218` — SUCCESS.

Integration result:

`295 passed / 1 expected P2 identity warning / 11 subtests passed`.

Integrity result:

`111 passed`.

The unchanged Runtime/Execution negative REL-009 guard therefore passed after relocation of the evidence harness.

### Full-Stack Repository Audit

Run: `33193670090` — `SUCCESS` on the same candidate head.

Classification:

`SOURCE-VERIFIED + READ-BACK-VERIFIED + EXACT-HEAD PULL-REQUEST CI VERIFIED`.

## 8. Provider-Backed E2E Revalidation

Isolated E2E branch created from exact clean candidate `499c3cfd...`:

`e2e/runtime-srv009-p3-clean-20260828`

A single trigger-only descendant commit was created:

`a5352d4b90f14387d12ad20a3f7d4676c0d80e2e`

Dedicated workflow:

`P3 Runtime GitHub E2E`

Run:

`33193773687` — `SUCCESS`

Job:

`98925604992` — `SUCCESS`.

Observed real GitHub connector evidence:

- create trace: `TR-c9ca3ebca1e3`;
- update trace: `TR-1e7fe1a17e26`;
- persisted SHA after update: `d3287757b644047d6de70a548cf202e34dab1e49`;
- probe path: `Quality/E2E/P3_RUNTIME_SRV009_LIVE_PROBE.md`;
- create/update/read-back succeeded;
- cleanup succeeded;
- final missing/read-back verification succeeded.

Evidence boundary:

This E2E proves the real ENG-006/SRV-009 adapter + GitHubRepositoryConnector path remains healthy after the authorization-id dependency closure. It does NOT independently prove that the new integration-only RUN-010 observation helper itself executed against the real GitHub connector. That RUN-010 observation seam is proven by the governed pull-request integration suite using the controlled fake connector. These two evidence classes remain separate.

## 9. P374 / REL-009 Gate Reassessment

P374 required:

1. RUN-010 originating execution context;
2. explicit SRV-009 target;
3. observed callable boundary;
4. attributable dispatch event;
5. preserved authorization/provenance;
6. controlled observation side effect;
7. exact-head governed CI.

The clean integration seam now supplies direct test/CI evidence for these requirements within its declared isolated integration scope.

The provider-backed E2E independently confirms the reused governed adapter/connector implementation against GitHub.

Therefore:

`B07/B08 = TECHNICALLY SATISFIED WITHIN THE CLEAN ISOLATED EVIDENCE SCOPE / PROMOTION REVIEW ELIGIBLE`.

This does NOT itself mutate `REP-014` or promote REL-009. The canonical matrix explicitly says B06+B07+B08 satisfaction permits the relationship state to be reconsidered; it does not mandate automatic promotion.

## 10. Concurrent HORUS Safety

The user explicitly stated that HORUS is concurrently updating accumulated experience/repository knowledge.

Observed HORUS branch family includes:

- `horus/identity-and-knowledge-foundation`;
- `horus/meta-learning-foundation` through `v6`.

Latest specifically inspected `horus/meta-learning-foundation-v6` head during this session:

`f250edd2c4ba86039941e2a2efdee6055689ecd8`.

Final session synchronization re-read `main` and still observed:

`09b216e403fe99a6f1a4a35e3c3038831398f6a3`.

No current-main collision with the P3 branch was observed during this session.

Mandatory continuation rule while HORUS or another agent may be active:

`RE-READ MAIN HEAD IMMEDIATELY BEFORE PROMOTION/MERGE -> COMPARE NEW MAIN AGAINST CANDIDATE -> INSPECT OVERLAPPING PATHS -> REVALIDATE REQUIRED CI -> ONLY THEN DECIDE`.

No blind rebase/cherry-pick/merge is permitted from a stale snapshot.

This is a concurrency safety application, not a new governance rule.

## 11. Tool/Execution Incidents

Several accidental pull-request creation calls were issued with deliberately/nonexistent placeholder heads while navigating connector surfaces. GitHub rejected each with `422 Validation Failed`.

Classification:

`TOOL INVOCATION ERROR / REJECTED BEFORE STATE CHANGE`.

Result:

- no unintended PR created;
- no ref changed;
- no repository mutation caused by those rejected actions.

The incident does not affect repository evidence but is retained for session traceability.

## 12. Accumulated Knowledge Reassessment

Validated/reapplied in this session:

1. Repository reality outranks session memory.
2. Exact-head/checkout attribution is mandatory.
3. `NO RUN`, `NO STATUS`, `PASS`, `FAIL` and `NOT OBSERVED` are distinct states.
4. Successful branch CI does not make a branch a good promotion unit.
5. Historical evidence must be extracted by dependency closure, not copied wholesale.
6. A candidate gap does not authorize mutation.
7. Test success proves only the exercised boundary.
8. A trace producer is not a downstream invocation.
9. Runtime/provider proof and integration-harness proof must remain distinguishable.
10. A deliberate negative architecture guard should not be weakened merely because a new proof harness was placed on the wrong side of it.
11. Consolidation can be a higher-value engineering action than adding another test or document.
12. Concurrent-agent work requires immediate pre-promotion state reconciliation.
13. Documentation, memoirs and learning records do not self-upgrade authority.

## 13. Debt / Roadmap After This Session

### Priority 1 — P3 promotion review

Technical construction/evidence is complete enough to enter a bounded promotion review.

Review must determine whether the isolated evidence justifies changing canonical REL-009 state, and if so what exact state wording is supported. Do not infer universal runtime routing: RUN-010 still states that the sequence is a relationship description and not every runtime operation must use the path.

No builder self-approval or automatic registry mutation is recorded here.

### Priority 2 — P4 critical graph validation

After P3 disposition, continue bidirectional critical graph validation from current REP-014/REP-022 evidence.

### Priority 3 — Control-plane truth synchronization

Reconcile remaining discoverability/state-reference debt, including the GOV-013 reference to `CONTROL_PLANE_STATUS.md` against the actual REP-015/root control-plane bootstrap surfaces. Do not invent a replacement file merely to satisfy a historical name.

### Priority 4 — Branch/workstream hygiene

After explicit promotion/disposition decisions:

- retain PR #63/#64/self-audit as evidence/provenance as appropriate;
- stop functional growth on them;
- close/retire only through explicit lifecycle decisions;
- keep future promotion units current-main-based and dependency-closed.

### Priority 5 — broader Connected Baseline

Resume repository-wide relationship/domain validation before feature expansion.

## 14. Explicit Non-Claims

- ARGO is not globally clean.
- Connected Baseline is not complete.
- REL-009 is not canonically promoted by this record.
- The normal connected spine is not converted to production dispatch.
- The provider E2E does not prove the integration helper itself ran against GitHub.
- PR #65 CI success is not merge authorization.
- HORUS outputs are not auto-promoted into HERMUZ authority.
- P2 bounded reconciliation is not repository-wide semantic closure.

## 15. Session Closure

Execution: COMPLETE for the bounded P3 clean construction/evidence objective.

Verification: COMPLETE for source/read-back, exact-head PR CI, integrity regression, integration regression, Full-Stack, and provider-backed adapter/connector E2E within their declared scopes.

Documentation: COMPLETE in this transfer record and the clean mutation matrix.

Learning assessment: COMPLETE; no new lesson promoted to governance.

Concurrent-agent reconciliation: COMPLETE at final observed main snapshot; must be repeated before any future promotion/merge.

Session state:

`CLOSED / RESUME-SAFE / P3 CLEAN BUILD VERIFIED / REL-009 PROMOTION REVIEW NEXT / MAIN UNCHANGED AT FINAL OBSERVATION`.

## 16. Next Safe Entry

`RE-READ main + HORUS-relevant changes -> confirm PR #65 head/base/diff -> perform bounded REL-009 promotion review against P374/P4 matrix/RUN-010/REP-014 -> promote only if authority and evidence support the exact state -> otherwise retain open with reason -> then proceed to P4 critical graph validation`.
