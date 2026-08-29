# GOV-015 — EXECUTION DOCUMENTATION & KNOWLEDGE TRANSFER PROTOCOL

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: `GOV-015`  
Version: `1.0.0`  
Status: `Approved / Canonical / Operating Contract`  
Category: `Governance / Execution Documentation / Knowledge Transfer`  
Canonical: `Yes`  
Priority: `Critical`  
Date: `2026-08-29`

---

## 1. Purpose

Define the minimum sufficient execution record that makes every ARGO work session resumable, auditable, collision-safe, and transferable between HERMUZ, HORUS, MAAT, Control Room #71, future task-specific agents, and a human owner.

This protocol fills the execution-documentation and knowledge-transfer dependency already named by `GOV-016`. It does not grant implementation, merge, promotion, semantic, or architectural authority.

The governing objective is:

**Repository evidence → bounded work contract → execution → verification → handoff → reusable learning → deterministic resume.**

---

## 2. Authority and precedence

This protocol is subordinate to:

1. `Core/CORE-003_CONSTITUTION.md`;
2. `PROJECT_BOOTSTRAP.md`;
3. applicable canonical Governance and Architecture authority;
4. `GOV-013` and `GOV-013A` for HERMUZ session execution/bootstrap;
5. `GOV-014` for controlled high-risk document mutation;
6. `GOV-016` for failure-to-learning handling.

If this protocol conflicts with higher authority, the higher authority prevails and the conflict is recorded.

---

## 3. Mandatory session entry record

Before material mutation, every worker records or can reconstruct:

```text
Repository:
Canonical branch:
Exact base SHA:
Executor role:
Session/task identity:
Current control-room/task issue:
Owned semantic scope:
Allowed write paths:
Forbidden write paths:
Read scope:
Known branch/PR dependencies:
Required evidence for closure:
Handoff target:
Independence state:
```

A missing or stale base SHA blocks mutation until re-entry is performed.

Conversation history may provide context but cannot fill a missing repository field as fact.

---

## 4. Deterministic activation pipeline

Every material session follows this order unless a higher authority requires more:

```text
CURRENT HEAD
  ↓
PROJECT_BOOTSTRAP
  ↓
CORE / GOVERNANCE AUTHORITY
  ↓
REP-001 / REP-002
  ↓
REP-013 / REP-012 / REP-011 / REP-014
  ↓
REP-015 / REP-016
  ↓
RELEVANT PRIOR LEARNING / JOURNAL / MUTATION RECORDS
  ↓
CURRENT CONTROL ROOM / TASK CONTRACT
  ↓
EXACT GAP RECHECK
  ↓
WORK LEASE
  ↓
MUTATION / ANALYSIS
  ↓
READ-BACK / TEST / EVIDENCE
  ↓
HANDOFF
  ↓
LEARNING CAPTURE
  ↓
SESSION CLOSURE
```

An earlier session's `NEXT` line is a candidate continuation, not current authority. The gap must still exist on current HEAD.

---

## 5. Work Lease — mandatory for parallel mutation

A Work Lease is the operational boundary for a writer. It is not semantic authority.

Minimum fields:

```text
Lease ID
Role
Task issue
Base SHA
Branch
Semantic scope
Allowed path globs
Forbidden path globs
Shared-read surfaces
Required checks
Handoff destination
Lease state
```

Rules:

1. One semantic owner per active mutation boundary.
2. A worker may read outside its lease when needed for evidence.
3. A worker may write only inside the allowed paths explicitly required by its task.
4. Same-file collision or same-semantic-contract collision causes `HOLD_SCOPE_COLLISION`.
5. If `main` moves and the intervening delta touches the lease scope, state becomes `HOLD_BASELINE_MOVED` until re-entry.
6. Cross-zone mutation requires a lease amendment before writing.
7. A branch is not authority; branch existence is provenance only.
8. A green check does not widen the lease.
9. No worker may infer ownership from a folder name alone.

---

## 6. Role operating boundaries

### 6.1 HERMUZ — Builder / Integrator / Reconciler

Primary function: bounded repository construction, implementation, reconciliation, testing, and evidence-backed promotion candidates.

HERMUZ MAY:

- mutate only paths leased by the active task;
- create or repair implementation/tests/controlled records required by the proven gap;
- consume HORUS findings as candidate analysis;
- report evidence-ready results.

HERMUZ MUST NOT:

- treat its own successful implementation as independent validation;
- promote a claim beyond the evidence layer proved;
- mutate HORUS analytical conclusions as if they were implementation files;
- use stale historical branches as automatic continuation authority;
- widen a task because a nearby improvement is attractive.

### 6.2 HORUS — Semantic / Experience / Historical Auditor

Primary function: inspect meaning, assumptions, accumulated learning, obsolete rules, duplication, provenance, applicability, and falsifiable validation questions.

Default write mode: analysis/documentation surfaces explicitly leased to HORUS.

HORUS MUST NOT:

- mutate production Runtime/Services/Engine or canonical registries by default;
- turn repeated analysis into authority;
- merge or promote its own conclusion;
- become a second implementation lane for the same semantic boundary.

HORUS output states must distinguish at least:

`FACT / INFERENCE / CANDIDATE / UNRESOLVED / HISTORICAL / SUPERSEDED`.

### 6.3 MAAT — Coordinator / Collision Controller

Primary function: maintain the current work map, resolve stale bases, compare write leases, detect file/semantic/authority/evidence collisions, and route handoffs.

Default write mode: issue/status/orchestration surfaces only.

MAAT MUST NOT:

- implement repository production changes;
- create semantic or canonical authority;
- merge merely because checks are green;
- strengthen another role's evidence state;
- call a same-session review independent.

MAAT may place work on HOLD when ownership or evidence is ambiguous.

### 6.4 Control Room #71 — operational command surface

Control Room #71 is the single issue-native orchestration surface for human direction, current task map, leases, holds, handoffs, and final priority decisions.

It is NOT a replacement for repository Governance and cannot override canonical authority.

A command in #71 may activate work only after repository re-entry and lease creation. It must not cause a worker to skip bootstrap because the room itself contains a summary.

---

## 7. Independence and review labels

Independence is an evidence property, not a role name.

Required labels:

- `SELF_REVIEWED_NOT_INDEPENDENT` — implementation and review were performed by the same model/session or inseparable execution context.
- `CROSS_ROLE_REVIEW_NOT_PROVEN_INDEPENDENT` — different role labels exist but execution-source independence is not established.
- `INDEPENDENTLY_VALIDATED` — independence is supported by a distinct evidence/execution source appropriate to the claim.
- `EXTERNAL_VALIDATION_UNVERIFIED` — external material exists but provider/source authenticity or independence is not established.

No role may self-upgrade an evidence record to `INDEPENDENTLY_VALIDATED` by changing its label.

---

## 8. Material action record

For each material action, record the smallest sufficient trace:

`BASE → CLAIM/GAP → PRIOR LEARNING → SCOPE → ACTION → CHANGED PATHS → READ-BACK → TEST/EVIDENCE → RESULT → LIMITS → NEXT SAFE ACTION`.

When a controlled document mutation is involved, the `GOV-014` Mutation Matrix remains the transaction specification and this protocol references it rather than duplicating it.

---

## 9. Evidence-class separation

A handoff must not collapse distinct evidence classes.

Keep separate where applicable:

- repository persistence;
- source/content read-back;
- structural validation;
- unit/integration/regression test result;
- CI/workflow observability;
- runtime execution;
- external delivery;
- provider authenticity;
- provenance/correlation;
- semantic qualification;
- authority/promotion;
- cognitive effect;
- external/user/market validation.

`COMMIT ≠ CI PASS ≠ RUNTIME PROOF ≠ EXTERNAL AUTHENTICITY ≠ COGNITIVE BENEFIT ≠ AUTHORITY`.

---

## 10. Mandatory handoff capsule

Every material worker handoff must be consumable without replaying the whole conversation or branch history.

Minimum capsule:

```text
HANDOFF ID
ROLE / TASK
BASE SHA
HEAD SHA
BRANCH / PR (if any)
SEMANTIC SCOPE
CHANGED PATHS
EVIDENCE OBSERVED
EVIDENCE NOT OBSERVED
CLAIMS PROVED
CLAIMS FORBIDDEN
TEST / CI / RUNTIME STATE
OPEN HOLDS
COLLISIONS
LEARNING CAPTURE
NEXT LEGAL ACTION
TARGET ROLE / CONTROL ROOM
```

A handoff that omits a material uncertainty must not be treated as stronger evidence by the receiving role.

---

## 11. Parallel-session collision protocol

MAAT or the active coordinator compares leases before concurrent mutation.

Collision classes:

- `C1_FILE` — same path may be written;
- `C2_SEMANTIC` — different paths alter the same contract/meaning;
- `C3_BASELINE` — one task is stale against current main;
- `C4_AUTHORITY` — a role attempts authority outside its contract;
- `C5_EVIDENCE` — incompatible claims use different scope/time/evidence identity;
- `C6_HANDOFF` — downstream work begins before upstream evidence state is suitable.

Default response: **HOLD the narrower affected mutation, preserve evidence, reallocate deliberately.**

Do not solve a collision by allowing both writers to proceed and reconciling afterward unless explicit authority accepts that risk.

---

## 12. Issue and task lifecycle

Operational task states:

`BACKLOG → READY → CLAIMED → ACTIVE → EVIDENCE_READY → REVIEW → DONE`.

Exceptional states:

- `HOLD_BASELINE_MOVED`
- `HOLD_SCOPE_COLLISION`
- `HOLD_AUTHORITY`
- `HOLD_EVIDENCE`
- `HOLD_EXTERNAL`
- `SUPERSEDED`

Closing an issue preserves its historical evidence. A superseded issue should be closed with a pointer to the current evidence/transaction that made its original work item obsolete.

An external-evidence dependency must remain HOLD/OPEN if it cannot be proved locally.

---

## 13. Failure and learning transfer

Material failure invokes `GOV-016`.

Reusable learning transfer follows:

`OBSERVATION → ROOT CAUSE → BOUNDED LESSON → REGRESSION/RECHECK → REUSE CONDITIONS → TARGET SURFACE`.

Possible target surfaces:

- test;
- Mutation Matrix pattern;
- Engineering Journal;
- issue task template;
- canonical protocol only when repeat evidence and authority justify it.

Do not create a new governance rule for a one-off anomaly when a test or bounded lesson is sufficient.

---

## 14. Session closure gate

A session with mutation closes only after:

1. changed artifacts were re-read from the actual branch/HEAD;
2. required relationship/index/status effects were reconciled or explicitly held;
3. applicable targeted tests/checks were inspected;
4. failures were classified under `GOV-016`;
5. open points were classified `DONE / SUPERSEDED / HOLD / OPEN` with evidence;
6. a handoff capsule exists for unfinished work;
7. reusable learning was recorded or explicitly judged unnecessary;
8. the next legal action is deterministic.

For a single-executor session, closure review is labeled `SELF_REVIEWED_NOT_INDEPENDENT` unless independent evidence was actually obtained.

---

## 15. Minimal-control principle

The goal is not to create more ceremony.

Use the minimum control that makes ownership, evidence, collision handling, handoff, and resume deterministic. If an existing mechanism already satisfies the requirement, reference and reuse it rather than create a duplicate layer.

---

## 16. Governing statement

**Read broadly enough to understand; write only inside the proven lease; prove only the evidence layer observed; hand off enough state that the next worker can continue from the repository rather than from memory.**

---

End of GOV-015
