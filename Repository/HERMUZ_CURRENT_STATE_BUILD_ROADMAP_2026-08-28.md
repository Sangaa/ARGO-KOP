# HERMUZ Current-State Build Roadmap — 2026-08-28

Status: `ACTIVE / ANALYSIS COMPLETE / EXECUTION IN PROGRESS`
Protocol: `GOV-013 + GOV-013A`
Base branch: `main`
Base HEAD: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Working branch: `hermuz/current-state-roadmap-20260828`
Authority class: `Analysis / Recovery / Planning Evidence — NON-CANONICAL`

## 1. Purpose

Reconstruct the current ARGO-KOP state from repository evidence before further construction; reconcile accumulated HERMUZ lessons with current canonical authority; identify branch/control-plane debt; establish the current build order; perform only evidence-justified mutations; and leave one compact resume-safe session surface rather than another sequence of checkpoint documents.

This document does not promote architecture, relationships, governance, runtime capability, or branch content.

## 2. Evidence Precedence Used

Current-state interpretation followed:

`Current main + Canonical Authority + Current CI/Runtime Evidence > Current Reconciliation Records > Historical Branch Evidence > Memoirs/Learning > Conversation Narrative`

The following were treated as controlling or current evidence where applicable:

- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`
- `Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md`
- `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md`
- `Repository/REP-021_P2_INDEX_SCOPE_RECONCILIATION_2026-08-17.md`
- `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `PROJECT_STATUS.md`
- current `main` branch identity and current workflow evidence.

Historical/self-audit material was reviewed for reusable evidence but not granted canonical authority.

## 3. Current Repository State — FACTS

### 3.1 Main

Current canonical main HEAD is:

`09b216e403fe99a6f1a4a35e3c3038831398f6a3`

Commit message:

`docs: record P374 minimum B07 B08 observation design`

The current main Runtime/Integration workflow executed successfully on this HEAD. The integration suite reported:

`291 passed / 1 warning / 11 subtests passed`

The warning is the emitted P2 identity report, not a test failure.

### 3.2 Platform phase

`PROJECT_STATUS.md` still places the platform in:

`CONNECTED-BASELINE STABILIZATION / INTEGRITY WARNING`

The immediate objective remains repository connectivity, evidence integrity, relationship validation and consolidation — not feature expansion.

### 3.3 Current priority authority

`REP-022` is the current reconciliation record for operational priority interpretation:

- `P1 = CLOSED` within inspected Ring-0 control-plane scope.
- `P2 = RECONCILED` within verified active inventory scope.
- `P3 = OPEN / EXECUTABLE RELATIONSHIP PROOF`.
- `P4 = OPEN / BIDIRECTIONAL CRITICAL GRAPH VALIDATION`.
- `P5 = EXECUTION-VERIFIED / BUILD CLOSED` within its harness scope.
- `P6 = EXECUTION-VERIFIED / POLICY-UNRESOLVED / NO-AUTO-PROMOTION`.

`REP-016` retains an older `P2 = OPEN` statement. This is preserved history/state layering; it must not override newer REP-021/REP-022 reconciliation.

### 3.4 P2 interpretation

Current main CI emits:

- `active_duplicate_pass = true`
- `duplicate_active_ids = {}`
- `ambiguous_duplicate_ids = {}`
- `filename_alignment_pass = true`
- `unreadable = []`
- `identity_scope_reconciled = false`
- `canonical_unindexed_records = 12`

The 12 records are two Core artifacts and ten Knowledge artifacts.

`REP-021` already explains why they are not direct index defects: Core and Knowledge remain authority/cross-layer validation scopes under Integrity Hold. It explicitly forbids mutating those domains merely to reduce the unindexed count.

Therefore:

`identity_scope_reconciled=false` is a scanner-level/global-scope signal, not evidence that the twelve files must be inserted into REP-001.

P2 active identity/index reconciliation is complete within the verified scope; broader semantic/cross-layer identity closure remains outside that bounded claim.

## 4. P3 / REL-009 Current State

Canonical main currently records:

- `REL-005: ENG-006 -> SRV-009 = BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E`.
- `REL-008: RUN-010 -> ENG-006 = Revalidated within inspected scope`.
- `REL-009: RUN-010 -> SRV-009 = REVALIDATION REQUIRED`.

P374 defines the current-main minimum evidence contract for REL-009 and explicitly rejects importing historical PR #63 wholesale.

Required proof remains conceptually:

`RUN-010 execution identity -> observable callable boundary -> explicit SRV-009 target -> attributable dispatch event -> preserved authorization/provenance -> side-effect-controlled observation -> exact-head governed CI`.

No canonical promotion follows merely from branch-level test success.

## 5. Branch / PR Reality

### 5.1 PR #63

Current state:

- open;
- head `a18bf9bae5fbdc29cde0fd237830f0c63b71556c`;
- 48 commits / 39 files;
- diverged from current main;
- 48 commits ahead and 67 commits behind current main from merge-base `2ce52292...`.

It contains useful historical RUN-010/ENG-006 design and tests and had successful PR CI. The workflow executed a GitHub-generated PR merge ref, proving compatibility with the then-base at that run, not making the branch current-main authority.

Current disposition:

`HISTORICAL DESIGN + EXECUTION EVIDENCE SOURCE / NOT A WHOLESALE PROMOTION UNIT`.

This supersedes any reading of the earlier P448 note that might imply PR #63 should become the active B08 promotion container. P374 on current main explicitly bounds PR #63 to historical design reuse.

### 5.2 PR #64

Current state:

- open / unmerged / mergeable;
- base = current main `09b216e...`;
- head `f21ede4a9b9941e51813b4fdb3db858d23255426`;
- 85 commits / 79 files;
- +3586 / -7;
- Runtime/Integration and Full-Stack workflows on current PR HEAD are successful.

The PR began as a narrow B07 execution-observation probe but accumulated implementation, tests, workflow changes, mutation matrices, evidence and a large session-history surface.

Its title/body remain materially stale: the body still preserves the earlier `P381 NO RUN` narrative although exact-head workflow execution is now observed.

Current disposition:

`EVIDENCE-RICH EXPERIMENTAL WORKSTREAM / NOT YET A CLEAN PROMOTION UNIT`.

### 5.3 Self-audit branch

`hermuz/self-audit-20260828` is currently 105 commits ahead of main.

Its archaeology, memoir, process-correction and reconciliation work is valuable, but the branch itself demonstrates the same accumulation risk it diagnosed: a review branch can become a history container if it is used indefinitely.

Current disposition:

`HISTORICAL ANALYSIS + EVIDENCE SOURCE / FREEZE FURTHER ACCUMULATION EXCEPT CORRECTION IF REQUIRED`.

## 6. Accumulated Experience Reassessment

### VALIDATED KNOWLEDGE

1. Repository evidence outranks session memory.
2. `NO RUN`, `PASS`, `FAIL`, `NO STATUS`, and `NOT OBSERVED` are different evidence states.
3. Exact-head/checkout attribution is mandatory before assigning CI evidence.
4. A branch can execute successfully while still being unsuitable as a promotion unit.
5. A candidate Gap does not authorize mutation.
6. A local/test PASS proves the tested invariant only.
7. Independent callable/dispatch evidence must not be inferred from surrounding trace production.
8. Raw provenance and session records are evidence, not executable payload.
9. A long-lived isolated branch can become promotion debt.
10. Current priority must be reconstructed from current reconciliation records, not from chronological momentum.
11. An audit metric may remain globally false while the bounded operational sub-scope is correctly reconciled; scope semantics must be read before mutation.
12. Successful technical proof and promotion/governance authority are independent states.

### USEFUL BUT NON-NORMATIVE

- HERMUZ memoirs.
- post-archaeology future operating mandate.
- historical branch recommendations.
- session-level synthesis and proposed future procedures.

These may guide review but do not become governance by existence.

### SUPERSEDED / BOUNDED

- old `NO RUN` claims when later exact-head workflow evidence exists;
- treating PR #63 as the active B08 container;
- treating all twelve canonical-unindexed records as index defects;
- assuming more REL-009 tests are automatically the next highest-value work.

## 7. Current Debt Map

### D1 — Promotion surface accumulation — HIGH

PR #63, PR #64 and self-audit each contain useful evidence mixed with historical work. No branch should be promoted wholesale solely because CI succeeded.

### D2 — PR narrative drift — HIGH

PR #64 metadata materially understates/incorrectly describes its current state and preserves a stale `NO RUN` claim.

### D3 — Control-plane reference drift — MEDIUM/HIGH

GOV-013 normal-entry prose references `CONTROL_PLANE_STATUS.md`, but current main has no such file. The operational bootstrap is actually provided by `REP-015` plus current root/control-plane records. This is a recoverability/document-reference inconsistency, not evidence that a new status file should be invented.

### D4 — Queue/reconciliation layering — MEDIUM

REP-016 retains older P2-open language while REP-021/REP-022 provide newer bounded reconciliation. This is preserved historical state but requires readers to know the precedence rule.

### D5 — Session-delta proliferation — HIGH

The P375+ work demonstrates that frequent checkpointing can preserve provenance while reducing signal. Future sessions should prefer one compact current-state/closure surface where possible.

### D6 — P3 clean-extraction gap — BLOCKING FOR PROMOTION

Technical evidence exists across branches, but a dependency-closed current-main promotion unit has not been proven.

### D7 — P4 remains open — HIGH AFTER P3 RECONCILIATION

Bidirectional critical graph validation remains the next canonical priority after P3 disposition.

## 8. Build Order

### Priority A — Consolidate P3 evidence before more P3 code

1. inspect PR #64 implementation/test/workflow dependencies;
2. classify required executable payload vs tests vs evidence/history;
3. identify the smallest dependency-closed current-main candidate;
4. reject superseded or duplicate test generations;
5. do not modify normal connected-spine simulation semantics unless current authority requires it;
6. run candidate against exact-head governed CI;
7. inspect the specific callable/dispatch evidence;
8. only then perform REL-009 promotion review.

### Priority B — P4 critical graph validation

After P3 disposition, resume current critical graph validation against REP-014 with endpoint authority, reverse evidence and consumer impact.

### Priority C — Control-plane truth synchronization

After the promotion/consolidation boundary is known:

- reconcile stale PR metadata;
- reconcile the GOV-013 `CONTROL_PLANE_STATUS.md` reference against the actual REP-015 bootstrap model through an authorized governance review;
- synchronize root/status/index claims only from proven state;
- preserve history rather than rewriting old evidence.

### Priority D — Branch/workstream hygiene

- freeze further functional growth on evidence-history branches;
- preserve them as provenance;
- use fresh current-main branches for clean promotion candidates;
- close/retire old PRs only through explicit decision, never as a side effect of cleanup.

### Priority E — Resume broader Connected Baseline

Once P3/P4 are reconciled, continue repository-wide relationship/domain validation according to PROJECT_STATUS and current priority evidence before feature expansion.

## 9. Immediate Execution Decisions

### AUTHORIZED / JUSTIFIED

- create this fresh analysis branch directly from current main;
- create one current-state roadmap/closure artifact;
- correct stale PR metadata that contradicts observed exact-head evidence;
- perform read-only P3 dependency/extraction analysis;
- update this same artifact with execution outcomes and session closure.

### NOT YET JUSTIFIED

- merging PR #63 or PR #64;
- copying either branch wholesale;
- adding the twelve deferred Core/Knowledge artifacts to REP-001;
- changing REL-009 state on main;
- wiring production side effects into the normal connected spine;
- promoting memoir/future-mandate content into governance;
- closing old PRs without explicit lifecycle decision.

## 10. Known Tool Incident This Session

A pull-request creation action was accidentally invoked with a non-existent placeholder head and returned GitHub `422 Validation Failed`.

Result:

`NO PR CREATED / NO REPOSITORY MUTATION / NO STATE CHANGE`.

The failed action was not retried. The correct explicit branch-creation surface was then used.

## 11. Session Execution Log

- Repository/bootstrap/current-priority reconstruction: COMPLETE.
- Current-main exact identity and CI observation: COMPLETE.
- P2 scanner warning reconciliation against REP-021: COMPLETE.
- PR #63 current-head / branch divergence / CI review: COMPLETE.
- PR #64 current-head / file-surface / CI review: COMPLETE.
- self-audit divergence review: COMPLETE.
- P3 clean-extraction review: IN PROGRESS.
- PR metadata correction: PENDING.
- learning/session closure: PENDING.

## 12. Explicit Non-Claims

- ARGO is not globally clean.
- Connected Baseline is not complete.
- REL-009 is not promoted.
- PR #63 is not canonical.
- PR #64 is not approved for merge.
- successful CI is not promotion authority.
- P2 bounded reconciliation is not repository-wide semantic closure.
- this roadmap is not canonical governance.

## 13. Next Safe Action

`P3 clean extraction review -> remove stale promotion assumptions -> exact dependency map -> metadata reconciliation -> decide whether a fresh minimal P3 candidate is justified -> verify -> close this session artifact`.
