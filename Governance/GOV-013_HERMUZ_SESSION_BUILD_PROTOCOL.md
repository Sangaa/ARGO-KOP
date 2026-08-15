# GOV-013

---

# HERMUZ — SESSION BUILD, VERIFICATION & REPOSITORY INTEGRITY PROTOCOL

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: GOV-013
Version: 1.1.0
Status: Approved / Canonical / Session Operating Contract
Category: Governance / Engineering Operating Protocol
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1

---

## 1. Purpose

HERMUZ is the fixed operating contract for an AI engineer or human engineer continuing ARGO KOP repository construction, verification, reconciliation and safe mutation.

It defines how a session is resumed, how evidence is searched and rechecked, how relationships are proven, how changes are validated, how integration between modules/files/folders is tested, how learning is evaluated, and when a session may close.

HERMUZ is an operating protocol. It does not replace or override `Core/CORE-003_CONSTITUTION.md`, `PROJECT_BOOTSTRAP.md`, applicable Governance authority, canonical Architecture, Release authority, or domain-specific authority.

Where HERMUZ conflicts with a higher-authority ARGO rule, the higher authority prevails and the conflict must be recorded rather than silently resolved.

---

## 2. Invocation Contract

The following user instruction is the canonical invocation phrase for this protocol:

> **«أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»**

Equivalent English invocation:

> **Continue the build according to the HERMUZ build protocol.**

When either invocation is received, the engineer MUST:

1. Identify the repository and current branch/ref from current repository evidence.
2. Load `PROJECT_BOOTSTRAP.md` and the current repository control-plane evidence.
3. Load this document (`GOV-013`) as the HERMUZ session operating contract.
4. Inspect the current checkpoint, open work and highest-priority safe continuation point.
5. Continue from the current repository state; do not restart completed work merely because a new chat/session was opened.
6. Apply the evidence, search, relationship, mutation, integration-testing, validation, learning and closure rules in this document and the higher-authority ARGO rules.
7. Do not require the user to resend this protocol unless current repository evidence proves the protocol artifact is unavailable.

The invocation phrase is a **continuation command**, not permission to ignore repository evidence or to bypass safety/integrity gates.

---

## 3. Session Operating Mode

During normal construction, responses to the user should remain operationally concise and focus on:

1. What was completed.
2. What was discovered.
3. The next decision/action.
4. A real blocker or material risk only.

The engineer should perform detailed verification, matrix tracing, relationship analysis, integration testing, post-change validation and learning assessment as part of the work itself, not as repetitive user-facing protocol recitations.

The protocol must not be reprinted in every operational response.

---

## 4. Continuation Before Reconstruction

Before starting a task:

- inspect current `main` state and latest relevant commit;
- inspect existing session deltas, Engineering Journal entries, matrices and checkpoint evidence;
- determine what is already complete;
- identify the highest-priority safe continuation point;
- recover the latest known integration-test state where one exists;
- never repeat completed work without evidence that revalidation is required.

Repository reality outranks conversation memory, prior summaries and previous status claims.

---

## 5. Mandatory Three-Search Rule

For every material negative search result, one search is never sufficient.

The engineer MUST perform at least **three materially different retrieval attempts** before treating the result as a verified negative finding, where the tools and repository scope permit.

Preferred sequence:

1. **Identifier / exact-name search**
2. **Semantic / path / filename / content search using materially different terms**
3. **Reverse / inferential search** through references, consumers, indexes, relationships, commits or neighboring artifacts

Then perform **direct current-path or ID verification** whenever a plausible path or identity is known.

A negative result remains provisional when any retrieval method is unavailable, truncated, paginated incompletely, stale, or otherwise unreliable.

---

## 6. Search Failure Learning

If an artifact is found after one or more negative searches, the engineer MUST NOT merely accept the artifact and move on.

The engineer must determine, where evidence permits, why the earlier search failed. Possible causes include:

- search-index staleness;
- insufficient query terms;
- path/name mismatch;
- identifier mismatch;
- semantic mismatch;
- pagination/truncation;
- branch/ref mismatch;
- search scope limitation;
- historical result overshadowing current result;
- connector/tool coverage limitation.

The event must be classified as an **Evidence Search Defect** when the search method, rather than the repository, caused the false negative.

If the cause is repeatable and materially improves ARGO's engineering control, it may become candidate reusable learning. It is not permanent knowledge merely because it occurred once.

---

## 7. Evidence and Relationship Discipline

Never promote a relationship from `REFERENCE` to `CONSUMES`, `DEPENDS_ON`, `IMPLEMENTS` or executable dependency without evidence supporting that relationship type.

For a material relationship, seek the chain:

**Forward Evidence → Reverse Evidence → Consumer/Dependency Evidence → Implementation/Executable Evidence → Integration Test Evidence → Matrix Classification**

Use the strongest justified state only. `DOCUMENTED ≠ EXECUTED ≠ TESTED ≠ VERIFIED`.

`REP-014` is the relationship registry and must preserve provenance, authority, evidence, review state and checkpoint.

Where practical, validate critical relationships in both directions.

---

## 8. Safe Mutation Rules

Never perform:

- destructive changes without explicit evidence and authority;
- document-ID renumbering as a convenience fix;
- mass baseline rewrites to hide conflicts;
- speculative relationship creation;
- creation of a new Model before the current model/relationship gap is proven;
- normalization solely to make inventories look complete.

Use the smallest sufficient mutation that resolves the verified issue.

Every mutation requires:

**Pre-check → Change → Re-read → Relationship/Index Validation → Integration/Regression Validation when applicable → Checkpoint Evidence**

If a write succeeds but post-change validation fails, the work is not complete.

---

## 9. Construction Priority

Maintain the repository as a connected graph and prioritize work by integrity value:

1. Connectivity / critical integrity risks
2. Core architecture and authority seams
3. Repository control plane and matrices
4. Runtime / Engine / Interface verified seams
5. **Integration / regression / CI evidence for module and cross-folder relationships**
6. Validation and CI evidence
7. Canonical documentation and inventory synchronization
8. Improvements and future capability
9. Model-gap assessment only after the current chain is stable

A smaller set of strongly connected, tested and documented artifacts is preferable to a larger set of superficially modified files.

---

## 9A. Mandatory Module Integration Verification

Integration testing is a **mandatory parallel workstream**, not a deferred phase after completion of the matrices.

For every module, service, engine, runtime component, interface, memory component, or other material artifact being built, modified, reconciled or materially revalidated, the engineer MUST determine and execute the applicable integration verification before treating the work group as complete.

The minimum required scope is:

1. **Module ↔ Module** — verify declared consumers, dependencies and interfaces where executable evidence is available.
2. **File ↔ File** — verify imports, references, IDs, contracts, schemas, producers/consumers and expected data/trace flow where applicable.
3. **Folder/Layer ↔ Folder/Layer** — verify the actual cross-layer path for material boundaries such as Engine ↔ Runtime, Runtime ↔ Services, Services ↔ Repository Control Plane, and Engine/Memory ↔ Knowledge/Memory governance.
4. **Test ↔ Implementation** — verify that an integration test exercises the intended implementation path and is not merely a structural or isolated unit test.
5. **Runtime Reachability** — do not claim executable reachability without runtime evidence.
6. **CI/Workflow Integration** — inspect applicable workflows and test results when the repository provides them.

For each material relationship, classify the strongest supported state:

`STRUCTURAL → CONTRACT → IMPLEMENTED → INTEGRATION-TESTED → RUNTIME-VERIFIED`

No state may be promoted merely because a neighboring document declares the relationship.

### 9A.1 Existing Tests First

Before creating a new integration test, the engineer MUST search for and inspect existing tests, fixtures, runners, workflows and evidence capture mechanisms that may already cover the relationship.

Do not duplicate an existing test without a demonstrated coverage gap.

### 9A.2 Test Recovery Rule

If integration testing was previously started and later interrupted, the engineer MUST recover the latest known test/checkpoint state and resume it as part of the current build. It must not be silently dropped because matrix construction or documentation work took priority temporarily.

### 9A.3 Matrix/Test Synchronization

Integration results MUST feed the applicable Matrix/Registry state:

- PASS with adequate evidence → strengthen the supported relationship state.
- FAIL → record the first meaningful failure boundary and keep the relationship below the unsupported state.
- NOT TESTABLE → record the environmental or architectural reason.
- STRUCTURAL ONLY → do not label it executable proof.
- RUNTIME evidence absent → do not claim runtime verification.

The Matrix does not replace integration testing, and integration testing does not replace relationship/evidence reconciliation.

### 9A.4 Full-Stack Audit

When `full-stack-audit.yml` and its associated audit tooling are present, the engineer MUST use them as part of the repository-wide integration/evidence sweep at appropriate checkpoints.

Audit findings are evidence candidates, not automatic architectural proof. Negative findings require independent verification, and runtime reachability requires runtime evidence.

### 9A.5 Regression After Mutation

After any material mutation affecting a module or cross-layer seam, rerun the smallest sufficient affected integration/regression set before promoting the change as complete.

A successful commit alone does not satisfy integration verification.

---

## 10. Model Creation Gate

A new Model may be proposed only after:

`Existing Models → Current Relationships → Consumer Proof → Repository Reconciliation → Verified Gap Assessment`

If an existing model covers the requirement, extend/reconcile it rather than creating a duplicate model.

If no evidence proves a real gap, create no new Model.

---

## 11. Learning Promotion Gate

Any newly observed engineering experience must first be checked against existing ARGO knowledge.

Permanent promotion requires evidence that the learning is:

- genuinely new or materially improves an existing rule;
- repeatable or sufficiently important;
- supported by repository evidence;
- non-contradictory with higher authority;
- assigned to the correct canonical learning location;
- reviewed and documented with provenance.

Otherwise record it as session evidence/candidate learning only.

---

## 12. Matrix and Traceability Rule

Important paths and relationships must be reflected in the applicable repository matrices/registries, especially:

- `REP-001` — Master Index
- `REP-002` — Repository Map
- `REP-011` — Review Traceability Ledger
- `REP-012` — Allocation / State / Recovery Registry
- `REP-013` — Content Tree
- `REP-014` — Relationship Registry
- `REP-015` — Control-Plane Bootstrap Checklist
- `REP-020` — Session Delta / Engineering Checkpoint evidence

Matrix entries are evidence-bearing control records; they do not create domain authority by themselves.

Integration evidence must be traceable back to the affected relationship/module and its test or runtime source.

---

## 13. Post-Change Verification

After every material mutation:

1. verify the resulting commit;
2. re-read every changed file;
3. verify affected IDs, versions and status;
4. verify affected indexes/maps;
5. verify affected relationship entries;
6. verify applicable integration/regression tests and CI;
7. check for propagation to consumers and dependencies;
8. record the checkpoint and provenance.

A commit alone is not proof that the change is correct.

---

## 14. Session Continuation Rule

Do NOT close a session merely because one task or one checkpoint is complete.

After completing a coherent work group, automatically continue to the highest-priority safe task available under the current build order.

Continue while:

- useful safe work remains;
- required evidence is available or the work can be bounded honestly;
- no material blocker prevents the next step.

Do not wait for the user to repeat the protocol between tasks.

Integration testing remains active while construction and matrix reconciliation continue; it is not a separate session stage unless the current evidence explicitly makes testing impossible.

---

## 15. Session Closure Rule

Session Closure occurs only when:

- all safe high-priority work reasonably available in the session is complete;
- a real blocker prevents safe continuation; or
- the user explicitly requests closure.

Before closure perform a concise closing audit:

- current state;
- work completed;
- changes made;
- evidence verified;
- integration/regression status;
- matrices/indexes synchronized;
- remaining work and blockers;
- next continuation point;
- learning assessment;
- final commit/checkpoint.

Do not mark a session `CLOSED` when final documentation, integration verification or other required validation failed.

---

## 16. Cross-Session Determinism

A new AI chat must be able to interpret the invocation phrase without relying on the previous conversation.

The deterministic resolution path is:

`Invocation Phrase`

→ `PROJECT_BOOTSTRAP.md`

→ `GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`

→ `Current Repository State`

→ `REP-020 / Engineering Journal / Matrices / Integration-Test State`

→ `Highest-Priority Safe Continuation`

This path makes the phrase a stable operational command while preserving current-repository authority.

---

## 17. Authority Boundary

HERMUZ does not grant permission to bypass ARGO governance.

Authority remains ordered by the current ARGO constitutional/governance structure. HERMUZ controls **how the engineer works**, not **what the engineer is authorized to override**.

The engineer must preserve `INTEGRITY HOLD` whenever unresolved evidence or relationships justify it. No false PASS may be created for convenience.

---

## 18. Canonical Invocation Summary

When a new chat receives:

> **«أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»**

it must interpret this as:

> **Resume ARGO KOP construction from the current repository state, load the canonical HERMUZ operating contract, inspect the latest verified checkpoint and open work, recover and continue any previously interrupted integration-testing work, apply three-method negative-search verification, preserve evidence/authority/relationship boundaries, perform integration verification in parallel with Matrix construction for every material module and cross-layer seam, make only safe evidence-backed mutations, update the required matrices, validate every change, promote learning only when justified, and continue automatically to the highest-priority safe task until a real blocker, explicit closure request, or exhaustion of safe high-priority work.**

---

End of GOV-013
