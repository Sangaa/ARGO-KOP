# P430 — ARGO KOP Repository Archaeology Tour & Debt Map

Date: 2026-08-28
Protocol: GOV-013
Status: `CLOSED / ANALYSIS-VERIFIED / NO FUNCTIONAL MUTATION / DEBT-MAPPED / NO PROMOTION`

## 1. Purpose

This checkpoint is a deliberate architectural pause: reconstruct the repository's recent history, compare the historical intent with the present state, identify accumulated technical/process debt, and avoid continuing the current path merely because it is already in motion.

No functional code was changed in P430.

## 2. Historical Layers Observed

### Layer A — Connected-Baseline / Integrity Era

The repository's control plane established a strong doctrine: current repository evidence outranks memory; local PASS is bounded; references require relationship validation; status files summarize evidence but do not create authority.

The root README still describes the platform as a Connected-Baseline Integrity Validation system and explicitly requires repository-first boot, relationship-graph review, and bounded evidence claims.

### Layer B — Capability / Seam Discovery Era

The repository then evolved toward evidence-backed seam discovery: contracts, tests, traces, registries, canonical-spine validation and full-stack audit tooling. The stated direction was to discover candidate seams first and promote only complete evidence-backed relationships.

### Layer C — KRS / GitHub Capability-Training Era

The branch history contains a substantial training/experimentation phase around repository capabilities, issue lifecycle, reactions, assignments, Actions semantics, KRS provenance and relationship-evidence schemas. This was not wasted work: it built the operational knowledge required to interrogate GitHub as an execution/evidence system rather than treating it as a passive file store.

### Layer D — REL-009 / B07-B08 Diagnostic Era

P375 deliberately created a fresh branch from current `main` specifically to avoid importing divergent PR #63 wholesale. The original design was minimal, isolated and evidence-first.

P382 then created PR #64 as an isolated execution-observation surface after `NO RUN` observations. The PR was explicitly intended as a probe, not as a promotion package.

### Layer E — Progressive Runtime Proof Era

P391 and the subsequent checkpoints added focused tests, authorization identity boundaries, RUN-010 handoff composition, ENG-006/SRV-009 consumer paths, and finally real provider-backed E2E execution. P420 established real GitHubRepositoryConnector Create → Update → Read-back → Cleanup evidence on an isolated E2E path.

### Layer F — Promotion-Gate Era

After runtime evidence became sufficient, the work stopped being primarily a coding problem. P421–P429 repeatedly established that the remaining blocker is governance authorization for the complete PR, not another functional test.

## 3. Present-Day Snapshot

The current PR #64 is:

- `OPEN`
- `UNMERGED`
- `MERGEABLE`
- base: `main`
- current head: `20b166802fea90d5f1e4df34821f5be0ed2afa24`
- 83 commits ahead of `main`
- 77 changed files
- 3,352 additions / 7 deletions

The PR title remains `P382: isolated B07 execution observation`, while the head now contains checkpoints through P426. The original PR body also describes the earlier P381/P382 observation purpose rather than the present complete workstream.

This is historical provenance, but it is also presentational debt: the promotion surface no longer describes its current scope accurately.

## 4. What the Change Set Became

The PR began as a narrow execution-observation probe but accumulated:

- runtime/consumer/adapter implementation;
- integration and regression tests;
- two GitHub Actions workflows/trigger adjustments;
- mutation matrices;
- approximately 52 checkpoint/session/evidence documents in the PR file list;
- repeated session-delta records from P375 through P426;
- multiple provenance corrections and process-repair records.

The central architectural shift is therefore not merely `B07/B08 implementation`. The branch became a combined **experimental implementation + evidence archive + process history + promotion candidate**.

That combination is the principal debt discovered by the archaeology tour.

## 5. Debt Map

### D-001 — Diagnostic Branch Drift

**Origin:** P375 intentionally created a fresh branch to prevent historical divergence from PR #63 from contaminating the experiment.

**Present condition:** The same branch is now 83 commits ahead of `main` and is itself a large historical workstream.

**Risk:** The original isolation boundary has transformed into a long-lived promotion surface. This weakens the distinction between experiment, evidence collection and candidate canonical change.

**Disposition:** HIGH. Requires consolidation/reconciliation design before merge; do not blindly merge the branch wholesale.

### D-002 — PR Narrative Drift

**Origin:** PR #64 was created at P382 as an execution-observation probe.

**Present condition:** Its title/body still describe the original P382/P381 observation purpose while its head contains P426-era work and production-provider E2E evidence.

**Risk:** A reviewer cannot infer the current scope accurately from the PR metadata.

**Disposition:** HIGH. Documentation/governance repair is justified, but should occur only after the complete change-set classification is finished.

### D-003 — Control-Plane Staleness

**Evidence:** README and PROJECT_STATUS describe older audit dates/baseline snapshots while the active branch contains later P420–P426 work.

**Risk:** A new engineer can boot from repository documents and receive a materially older picture than the current branch state.

**Disposition:** HIGH. Reconcile status/index claims after the promotion/consolidation boundary is decided; do not hide the divergence by casually editing timestamps.

### D-004 — Session-Delta Proliferation

**Evidence:** The PR contains a long sequence of per-checkpoint REP records plus separate mutation matrices and process-correction records.

**Risk:** Provenance is strong but the signal-to-noise ratio is falling. Future agents may follow checkpoint chronology instead of architectural intent and current authority.

**Disposition:** MEDIUM/HIGH. Preserve raw provenance, but add a higher-level synthesis/index rather than deleting history.

### D-005 — Evidence/Implementation Co-location

**Evidence:** Functional code, tests, workflow changes, matrices and dozens of historical session records coexist in the same promotion branch.

**Risk:** Reviewers may confuse evidence volume with implementation scope; future consolidation may accidentally promote process artifacts as if they were runtime capability.

**Disposition:** HIGH. Requires explicit functional-vs-evidence classification before promotion.

### D-006 — Architecture Reassessment Gap

**Finding:** The repository's stated objective is connected-baseline stabilization, yet the current workstream has become strongly centered on one narrow runtime seam (`RUN-010 → ENG-006 → SRV-009 → GitHubRepositoryConnector`).

**Risk:** Local excellence may hide whether this seam is actually the highest-value remaining repository problem.

**Disposition:** HIGH. Before further functional construction, perform a repository-wide priority reassessment against the current GAP MAP / control-plane state.

### D-007 — Promotion Authorization Gap

**Evidence:** P426 and later live checks show no authorized PR review/approval.

**Risk:** The technical evidence is stronger than the governance evidence, but the latter remains the controlling boundary.

**Disposition:** BLOCKING. Must not be bypassed by more tests or by self-approval.

## 6. Architectural Reading of the Journey

The strongest creation in this historical path is not a single adapter. It is the repository's evolving evidence discipline:

`documented → source-reconciled → contract-bound → test-bound → exact-head-bound → CI-observed → runtime-verified → promotion-governed`

The main weakness is the opposite side of that success: the evidence machinery became so successful that the experiment accumulated a large amount of process history around a single branch.

Therefore the next architectural task should not be "add another proof." It should be **compress the proven knowledge into a clean, reviewable promotion unit without destroying provenance**.

## 7. Future View — Recommended Route

1. Freeze functional mutation on PR #64 until consolidation analysis is complete.
2. Classify all 77 changed files into `functional`, `test`, `workflow`, `evidence`, `process-correction`, `historical/provenance`.
3. Identify the minimal functional delta actually justified by the proven B07/B08 outcome.
4. Separate reusable evidence from promotion payload without deleting provenance.
5. Reconcile PR title/body and root control-plane status only after scope is known.
6. Re-run the affected audit/E2E suite against the resulting candidate promotion unit.
7. Obtain authorized human review for the resulting promotion surface.
8. Only then decide whether merge is justified.

## 8. Learning Disposition

No new canonical learning is promoted in P430.

Candidate observations for later validation:

- A branch created as an isolated diagnostic surface can become a promotion-debt container if its lifecycle is not explicitly bounded.
- Strong provenance can itself create review complexity when raw checkpoint evidence and functional payload are never periodically synthesized.
- Once runtime proof is established, continued local testing without a renewed repository-wide priority check can become evidence accumulation rather than engineering progress.

These remain candidate observations until reused/validated by a later governed checkpoint.

## 9. Close

`P430 = CLOSED / ARCHITECTURAL PAUSE COMPLETE / DEBT MAP ESTABLISHED / NO FUNCTIONAL MUTATION / NO PROMOTION`

Next safe checkpoint:
`P431 → classify the complete PR change set → derive minimal promotion unit → reconcile control-plane/documentation scope → only then resume targeted construction if a real Gap remains.`
