# HERMUZ Current-State Build Roadmap — 2026-08-28

Status: `SESSION CLOSED / P3 CLEAN BUILD VERIFIED / P4 RECONNAISSANCE COMPLETE / PROMOTION REVIEW NEXT`
Protocol: `GOV-013 + GOV-013A + GOV-014 + GOV-015`
Base branch observed: `main`
Base HEAD observed through final synchronization cycle: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Roadmap branch: `hermuz/current-state-roadmap-20260828`
Authority class: `Analysis / Recovery / Execution / Transfer Evidence — NON-CANONICAL`

## 1. Session Purpose

Reconstruct ARGO-KOP from current repository evidence before further construction; reconcile accumulated HERMUZ experience with current authority; remove stale branch/promotion assumptions; identify the actual priority chain; construct and verify the smallest dependency-closed P3/REL-009 evidence candidate; preserve concurrent HORUS safety; investigate the next P4 architectural decision without inventing symmetry; and leave one compact resume-safe transfer surface rather than another long sequence of checkpoint files.

This record does not itself promote a relationship, governance rule, branch or runtime capability.

## 2. Evidence Precedence

`Current main + Canonical Authority + Exact-HEAD CI/Runtime Evidence > Current Reconciliation Records > Historical Branch Evidence > Memoirs/Learning > Conversation Narrative`

Key authority/evidence used:

- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Repository/REP-021_P2_INDEX_SCOPE_RECONCILIATION_2026-08-17.md`
- `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md`
- `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md`
- `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md`
- `Repository/REP-042_SESSION_DELTA_2026-08-28_P374.md`
- current GitHub branch/PR/workflow evidence.

Historical/self-audit/HORUS material was treated according to its actual evidence and authority state; documentation never auto-promoted it.

## 3. Reconstructed Priority State

Current reconciliation evidence establishes:

- `P1 = CLOSED` within inspected Ring-0 control-plane scope.
- `P2 = RECONCILED` within verified active inventory scope.
- `P3 = OPEN / EXECUTABLE RELATIONSHIP PROOF` at session entry.
- `P4 = OPEN / BIDIRECTIONAL CRITICAL GRAPH VALIDATION`.
- `P5 = EXECUTION-VERIFIED / BUILD CLOSED` within its harness scope.
- `P6 = EXECUTION-VERIFIED / POLICY-UNRESOLVED / NO-AUTO-PROMOTION`.

The old P2-open wording retained in REP-016 does not override newer REP-021/REP-022 reconciliation.

The recurring `identity_scope_reconciled=false` CI warning does not authorize blind index mutation. REP-021 already classifies the twelve Core/Knowledge canonical-unindexed records as deferred authority/cross-layer scope rather than direct active-index defects.

## 4. Historical Workstream Cleanup

### PR #63

Disposition:

`HISTORICAL DESIGN + EXECUTION EVIDENCE SOURCE / NOT A WHOLESALE PROMOTION UNIT`.

Its branch is materially diverged from current main. P374 permits design reuse only after current-main reconciliation. PR metadata was corrected to prevent future sessions from treating it as the active promotion path.

### PR #64

Disposition:

`EVIDENCE-RICH EXPERIMENTAL WORKSTREAM / NOT A CLEAN PROMOTION UNIT`.

Its current exact head had successful Runtime/Integration and Full-Stack CI, superseding the stale historical `NO RUN` narrative. The 85-commit / 79-file accumulated branch was deliberately not promoted wholesale. PR metadata was corrected accordingly.

### Self-audit branch

Disposition:

`HISTORICAL ANALYSIS + EVIDENCE SOURCE`.

The branch itself demonstrates that an audit branch can become accumulation debt. No new functional construction was added to it.

## 5. Clean P3 Extraction

Fresh branch created directly from current main:

`hermuz/p3-rel009-clean-observation-20260828`

PR:

`#65 — P3: clean isolated REL-009 observation seam`

Current candidate head:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

Current final diff against main:

- 4 commits;
- exactly 8 changed files;
- ahead by 4 / behind by 0 at final comparison;
- no unexpected path;
- `Runtime/Execution/connected_spine_runner.py` unchanged;
- canonical `REP-014` REL-009 state unchanged.

Mutation control:

`Repository/MUT-2026-08-28-P3-REL009-CLEAN-001_MUTATION_MATRIX.md`

All C01-C08 rows reached:

`Applied = Y / Verified = Y`.

### Included clean design

1. `Runtime/Execution/run010_handoff_contract.py`
   - pure handoff builder;
   - no repository I/O;
   - no `SRV-009` literal/dispatch;
   - validates execution trace, authorization state and authorization identity.

2. `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py`
   - preserves the existing governed dispatcher path;
   - now requires explicit `authorization_id` before connector access;
   - fails closed when authorization identity is absent.

3. `Quality/Integration/rel009_run010_srv009_observation.py`
   - integration-only evidence harness;
   - composes the pure handoff contract with the existing governed production adapter;
   - records RUN-010 origin, explicit SRV-009 target, callable boundary, execution/task/session/source-trace identity, authorization identity, downstream trace, dispatch status and post-read verification.

4. Focused positive/fail-closed integration regressions.

5. Existing P3 provider E2E workflow updated only for authorization-id dependency closure.

### Rejected historical path

Historical PR #64's `Runtime/Execution/run010_eng006_srv009_consumer.py` performs lower-level connector read/create/update/read-back directly.

It was deliberately not extracted because it would create a parallel dispatch implementation beside the already governed ENG-006/SRV-009 production adapter. The clean candidate composes the existing governed adapter instead.

## 6. CI Failure → Root Cause → Clean Correction

Initial clean-candidate head:

`c83683e3262412dc7015a62bae94389dfef6b020`

Observed:

- Full-Stack: PASS.
- Prototype: PASS.
- Integration: PASS.
- Integrity: FAIL.

First meaningful failure:

`Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py`

The existing guard intentionally prohibits the literal `SRV-009` inside `Runtime/Execution/*.py`. The first observation helper had been placed at `Runtime/Execution/run010_srv009_observation.py`.

Root classification:

`NEW EVIDENCE SEAM PLACED IN PROTECTED RUNTIME SCOPE / EXISTING INTEGRITY RULE CORRECT / DESIGN LOCATION DEFECT`.

The guard was not weakened, bypassed or rewritten.

Correction:

- relocate evidence helper to `Quality/Integration/rel009_run010_srv009_observation.py`;
- delete initial Runtime/Execution helper;
- preserve Runtime/Execution negative boundary;
- preserve connected-spine simulation semantics.

Correction commit:

`180b4c89ee51ff93f0f2ba1043bdcbccd511865b`.

Post-correction read-back confirmed the old Runtime path absent, new Quality path present, focused test bound to the relocated helper, and final diff still exactly eight files.

Learning classification:

`SESSION-LEARNING / TRANSFERABLE CANDIDATE`.

Lesson: when a proof harness conflicts with a deliberate architecture guard, reassess the proof placement before weakening the guard merely to make CI green.

No governance promotion is implied.

## 7. Exact-HEAD Governed CI

Final clean candidate:

`499c3cfda8e1fff52e3f808cff9ab80ed36e39db`

Runtime/Prototype/Integration run:

`33193670294` — SUCCESS

Jobs:

- prototype-tests `98925253840` — SUCCESS;
- integrity-tests `98925254152` — SUCCESS, `111 passed`;
- integration-tests `98925254218` — SUCCESS, `295 passed / 1 expected P2 identity warning / 11 subtests`.

Full-Stack Repository Audit:

`33193670090` — SUCCESS on the same candidate head.

Classification:

`SOURCE-VERIFIED + READ-BACK-VERIFIED + EXACT-HEAD PULL-REQUEST CI VERIFIED`.

## 8. Provider-Backed E2E

Isolated branch created from exact candidate `499c3cfd...`:

`e2e/runtime-srv009-p3-clean-20260828`

Trigger-only descendant:

`a5352d4b90f14387d12ad20a3f7d4676c0d80e2e`

Dedicated workflow:

`P3 Runtime GitHub E2E`

Run:

`33193773687` — SUCCESS

Job:

`98925604992` — SUCCESS

Observed provider evidence:

- create trace `TR-c9ca3ebca1e3`;
- update trace `TR-1e7fe1a17e26`;
- persisted SHA `d3287757b644047d6de70a548cf202e34dab1e49`;
- probe `Quality/E2E/P3_RUNTIME_SRV009_LIVE_PROBE.md`;
- create/update/read-back succeeded;
- cleanup succeeded;
- final missing/read-back verification succeeded.

Boundary:

The E2E proves the real ENG-006/SRV-009 adapter + GitHubRepositoryConnector remains healthy after authorization-id dependency closure. It does not independently prove the new integration-only RUN-010 observation helper executed against GitHub. The RUN-010 observation seam is proven by governed pull-request integration CI with a controlled fake connector. These evidence classes remain separate.

## 9. P3 / REL-009 Evidence Reassessment

P374 requires:

1. RUN-010 originating execution context;
2. explicit SRV-009 target;
3. observed callable boundary;
4. attributable dispatch event;
5. preserved authorization/provenance;
6. controlled side effect;
7. exact-head governed CI.

The clean integration seam now provides those within its declared isolated integration scope. The provider E2E independently confirms the reused adapter/provider path.

Therefore:

`B07/B08 = TECHNICALLY SATISFIED WITHIN CLEAN ISOLATED EVIDENCE SCOPE / PROMOTION-REVIEW ELIGIBLE`.

This does not automatically promote REL-009. The canonical matrix says B06+B07+B08 satisfaction permits reconsideration; GOV-015 explicitly separates test success from canonical promotion.

PR #65 was moved from Draft to `Ready for Review` after technical verification. It remains open/unmerged and had no submitted review or review thread at the final promotion-readiness inspection.

## 10. P4 Reverse-Evidence Reassessment

P4 has a separate concern from P3 executable proof: critical-edge directional/reverse evidence.

Three materially different current checks were performed:

1. direct canonical read of `Services/SRV-009_UPDATE_SERVICE.md`;
2. repository searches for RUN-010/SRV-009 caller/consumer/reverse relationship evidence;
3. independent Services-domain/reference and Architecture dependency/integration review, including `SRV-010`, `ARC-006` and `ARC-007`.

Current evidence:

- `SRV-009` explicitly identifies itself as the controlled mutation service consumed by `ENG-006`;
- it does not independently identify `RUN-010` as caller/consumer endpoint;
- `SRV-010` acknowledges RUN-010 only at the broader runtime/service boundary and explicitly warns that this does not prove every service executes on every runtime path;
- `ARC-006` requires dependencies to be necessary, directionally justified and free of circularity;
- `ARC-007` says Runtime may consume approved service interfaces and each component owns its implementation/interface boundary.

No new direct reverse endpoint evidence was found.

### Architectural finding

The absence of a reverse `SRV-009 -> RUN-010` dependency/reference must not automatically be treated as a defect to repair by adding documentation.

`REL-009` is semantically directional: `RUN-010 CONSUMES SRV-009`.

Forcing SRV-009 to depend on or name every runtime consumer merely to create graph symmetry risks artificial coupling and may violate the repository's own dependency principles.

The P4 matrix already permits critical relationships to be explicitly dispositioned as intentionally one-way rather than forcing a reverse edge.

Candidate P4 disposition:

`REL-009 = INTENTIONAL ONE-WAY CONSUMER RELATIONSHIP / EXECUTABLE EVIDENCE AVAILABLE IN ISOLATED INTEGRATION SCOPE / NON-UNIVERSAL RUNTIME PATH / REVERSE DEPENDENCY NOT REQUIRED`

This is an analytical candidate, not canonical state. An applicable architecture/relationship promotion review must determine whether this wording is justified before mutating P4/REP-014.

### Important correction to the old path

The next P4 action should NOT be “add RUN-010 to SRV-009 so reverse evidence exists”.

The next action should be:

`DECIDE WHETHER THE EDGE IS INTENTIONALLY ONE-WAY BASED ON ARCHITECTURAL SEMANTICS -> only if rejected, search for a genuinely required reverse contract`.

This changes the problem from document completion to semantic relationship disposition.

## 11. Concurrent HORUS Safety

The user explicitly stated HORUS is concurrently working on accumulated experience and may update repository state.

Observed HORUS branch family includes `horus/identity-and-knowledge-foundation` and `horus/meta-learning-foundation` through `v6`.

Latest specifically inspected `horus/meta-learning-foundation-v6` head during the session:

`f250edd2c4ba86039941e2a2efdee6055689ecd8`.

Repeated current-main synchronization still observed:

`09b216e403fe99a6f1a4a35e3c3038831398f6a3`.

No current-main collision with PR #65 was observed during this session.

Mandatory continuation rule while another agent may be active:

`RE-READ MAIN IMMEDIATELY BEFORE PROMOTION/MERGE -> COMPARE NEW MAIN AGAINST CANDIDATE -> INSPECT OVERLAPPING PATHS -> REVALIDATE REQUIRED CI -> ONLY THEN DECIDE`.

No blind rebase/cherry-pick/merge from a stale snapshot.

## 12. Tool Incidents

Several accidental PR creation calls were issued with nonexistent placeholder heads while navigating connector surfaces. GitHub rejected each with `422 Validation Failed`.

Classification:

`TOOL INVOCATION ERROR / REJECTED BEFORE STATE CHANGE`.

No unintended PR, ref change or repository mutation resulted.

## 13. Validated / Reapplied Knowledge

1. Repository reality outranks session memory.
2. Exact-head/checkout attribution is mandatory.
3. `NO RUN`, `NO STATUS`, `PASS`, `FAIL`, and `NOT OBSERVED` are distinct states.
4. Successful CI does not make an accumulated branch a good promotion unit.
5. Historical evidence should be dependency-closed and extracted, not copied wholesale.
6. A candidate gap does not authorize mutation.
7. Test success proves only the exercised boundary.
8. Trace production is not downstream invocation.
9. Provider proof and integration-harness proof are distinct evidence classes.
10. Deliberate architecture guards should not be weakened merely because evidence code was placed on the wrong side of them.
11. Consolidation can be higher-value engineering than adding another test/report.
12. Concurrent-agent work requires immediate pre-promotion reconciliation.
13. Documentation/memoirs do not self-upgrade authority.
14. Bidirectional validation must not become a mechanical demand for symmetric dependencies when the semantic relationship is directional.
15. A missing reverse reference can be an intentional architecture property; decide semantics before mutating documentation.

Items 14-15 remain `SESSION-LEARNING / CANDIDATE-REUSABLE` until independently validated; they are not governance rules.

## 14. Roadmap After This Session

### Priority 1 — bounded P3/P4 relationship disposition review

Review PR #65 technical evidence and the P4 intentional-one-way candidate together, without conflating them.

Possible justified endpoint if authority accepts the semantics:

`RUN-010 -> SRV-009 = CONSUMES / EXECUTABLE-VERIFIED WITHIN ISOLATED INTEGRATION SCOPE / INTENTIONAL ONE-WAY / NON-UNIVERSAL RUNTIME PATH`.

Do not claim normal connected-spine dispatch or universal runtime reachability.

### Priority 2 — canonical mutation only after disposition authority

If the relationship disposition is approved:

- re-read current main/HORUS changes;
- build a small GOV-014 mutation for the exact P4/REP-014 state update;
- run required CI;
- re-read and reconcile;
- only then consider merging the implementation PR and/or relationship-state mutation in the authorized order.

If the disposition is not approved, leave REL-009 open with the exact unresolved semantic question rather than manufacturing reverse evidence.

### Priority 3 — remaining P4 critical graph

REL-005 is already bidirectional/executable-verified; REL-061 is already intentionally one-way/governance-revalidated. Once REL-009 is dispositioned, perform an explicit P4 closure review rather than reopening already settled edges.

### Priority 4 — control-plane truth synchronization

Reconcile the GOV-013 reference to `CONTROL_PLANE_STATUS.md` against the actual REP-015/root bootstrap surfaces. Do not invent a replacement merely to satisfy a historical filename.

### Priority 5 — branch hygiene

After explicit disposition decisions, stop functional growth on PR #63/#64/self-audit, retain useful provenance, and close/retire only through explicit lifecycle decisions.

### Priority 6 — broader Connected Baseline

Resume repository-wide relationship/domain validation before feature expansion.

## 15. Explicit Non-Claims

- ARGO is not globally clean.
- Connected Baseline is not complete.
- REL-009 is not canonically promoted by this record.
- The normal connected spine is not converted to production dispatch.
- Provider E2E does not prove the integration helper itself ran against GitHub.
- PR #65 success/readiness is not merge authorization.
- HORUS outputs are not auto-promoted into HERMUZ authority.
- The intentional-one-way P4 disposition is a candidate pending authorized review.

## 16. Closure

Execution: COMPLETE for the bounded P3 clean construction/evidence objective.

Verification: COMPLETE for source/read-back, exact-head PR CI, integrity regression, integration regression, Full-Stack and provider-backed adapter/connector E2E within declared scopes.

Historical branch cleanup: COMPLETE at metadata/disposition level; no destructive branch lifecycle action taken.

P4 reconnaissance: COMPLETE / no mutation; old reverse-reference chase replaced with a semantic disposition question.

Documentation/knowledge transfer: COMPLETE in this consolidated record and the clean mutation matrix.

Concurrent-agent reconciliation: COMPLETE at final observed snapshot; mandatory to repeat before any future promotion/merge.

Session state:

`CLOSED / RESUME-SAFE / P3 CLEAN BUILD VERIFIED / PR65 READY FOR REVIEW / P4 INTENTIONAL-ONE-WAY DISPOSITION CANDIDATE / MAIN UNCHANGED AT FINAL OBSERVATION`.

## 17. Next Safe Entry

`RE-READ main + HORUS-relevant changes -> confirm PR #65 head/base/diff/CI -> perform authorized semantic disposition review for REL-009 -> if accepted, create smallest canonical registry/P4 mutation with GOV-014 and verify -> perform explicit P4 closure review -> continue Connected Baseline`.
