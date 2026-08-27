# GOV-013

---

# HERMUZ — SESSION BUILD, VERIFICATION & REPOSITORY INTEGRITY PROTOCOL

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: GOV-013
Version: 1.1.3
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

## 4A. Mandatory Prior-Learning Retrieval Gate

Before proposing or implementing any new solution to a material problem, the engineer MUST first attempt to recover relevant prior ARGO learning and experience.

The retrieval gate is:

**Problem Definition → Prior-Learning Retrieval → Prior-Evidence Review → Solution Simulation → New-Learning Search only if required**

At minimum, the engineer MUST search for relevant:

1. Engineering Journal / lessons learned / mistakes and prior session evidence.
2. Existing protocols, rules, matrices, registries and canonical contracts.
3. Prior implementations, tests, checkpoints, issues or incidents addressing the same or materially similar failure mode.

The search MUST use materially different retrieval methods where available. A direct exact-name search alone is insufficient for a material problem.

### 4A.1 Prior-Learning Classification

Recovered prior knowledge MUST be classified before reuse:

- **DIRECTLY APPLICABLE** — same problem/failure mode and same boundary; may guide the current solution after verification.
- **TRANSFERABLE** — materially similar mechanism but different context; requires explicit adaptation and revalidation.
- **HISTORICAL / SUPERSEDED** — useful context but not authoritative for the current state.
- **CONTRADICTORY / UNRESOLVED** — must not be silently reused; reconcile against current authority/evidence.
- **NOT FOUND** — retrieval completed but no adequate prior learning was found.

Finding an old artifact is not enough; the engineer MUST verify whether its assumptions, authority, environment and repository state still apply.

### 4A.2 Simulation Before New Learning

When relevant prior learning exists, the engineer MUST perform a bounded mental/design simulation against the current problem before searching for or creating a new solution.

The simulation should answer:

- Does an existing known pattern already explain the failure?
- What would happen if the prior remedy were applied to the current boundary?
- What assumptions differ?
- What evidence is missing to safely reuse it?

If the prior learning resolves the problem, do not invent a new solution.

If it does not resolve the problem, explicitly identify the **remaining gap** before initiating new research or experimentation.

### 4A.3 New-Learning Escalation

Only after the Prior-Learning Retrieval Gate and bounded simulation fail to resolve the problem may the engineer escalate to:

**new evidence search → controlled experiment → new implementation → candidate learning**.

New learning MUST NOT overwrite, duplicate or contradict existing learning merely because the current search path failed to retrieve it.

### 4A.4 Search-Failure Learning

If prior learning is later discovered after a new solution was proposed or tested, classify the event as a **Prior-Learning Retrieval Defect** and determine why retrieval failed:

- indexing/search limitation;
- query/path/identifier mismatch;
- semantic mismatch;
- pagination/truncation;
- branch/ref mismatch;
- repository placement problem;
- connector/tool coverage limitation;
- failure to search the correct canonical learning surface.

If repeatable and materially useful, promote the retrieval lesson through the Learning Promotion Gate rather than treating it as a one-off observation.

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

### 9B. Mandatory CI Failure Root-Cause Gate

A failing CI/Action/Workflow is a **HARD HOLD**, not a reason to continue to the next checkpoint.

The engineer MUST NOT:

- treat a failing Action as informational;
- skip, ignore, or summarize away a failed Job/Step;
- infer the cause from the Action title or summary alone;
- declare the current checkpoint complete while an applicable required check is failing;
- move to the next build point merely because other Jobs passed;
- treat a commit succeeding as evidence that the build is correct.

For every failed required Action, the engineer MUST execute this sequence:

**Workflow → Run → Job → Step → Test/Command → First Meaningful Failure → Root Cause → Prior-Learning Retrieval → Minimal Safe Fix → Re-run → Full Result Review → Post-change Validation → Documentation → Checkpoint Closure**

The engineer MUST inspect the failed Job's steps and logs, not merely the workflow conclusion. Where logs are available, the first meaningful failure boundary must be identified and distinguished from downstream/cascading failures.

The engineer MUST classify the failure before choosing a fix, at minimum as one or more of:

- implementation/code defect;
- test defect;
- fixture/data defect;
- configuration/workflow defect;
- manifest/index/version drift;
- evidence/matrix inconsistency;
- repository synchronization defect;
- environment/tooling/connector limitation;
- governance/authority defect;
- unknown/unresolved.

A suspected cause is **not** a root cause until the available evidence supports it and, where practical, the correction removes the observed failure on a re-run.

### 9B.1 Failure Boundary Before Fix

Before modifying anything, record:

1. exact failing workflow/run;
2. commit/ref under test;
3. failed Job and Step;
4. exact failing test/command or assertion;
5. relevant error output;
6. first meaningful failure boundary;
7. known upstream/downstream failures;
8. applicable prior ARGO learning and whether it is directly applicable, transferable, historical, contradictory, or not found.

Do not modify a file merely because it appears near the failure.

### 9B.2 Fix Verification Gate

After a fix:

1. re-read the changed artifact(s);
2. verify IDs, versions, relationships, indexes and affected consumers;
3. rerun the smallest sufficient targeted test;
4. rerun the affected workflow/required integration checks;
5. inspect **all required Jobs/Steps** in the resulting run;
6. investigate any new or remaining failure independently;
7. only then classify the fix as verified.

If the re-run fails, the checkpoint remains **OPEN/HOLD** and the cycle repeats from failure-boundary analysis. A new failure must not be silently appended to the previous cause.

### 9B.3 No-Transition Rule

**No failed required check → next checkpoint transition is permitted.**

A checkpoint may advance only when:

- all required applicable checks pass; or
- the repository's governing authority explicitly classifies a known non-blocking condition as such, with provenance and evidence recorded.

A user request to continue does not override this gate.

### 9B.4 Complete-Run Review

A green headline is insufficient when any required Job, Step, matrix row, artifact, runtime evidence surface or post-change validation remains unexamined or failed.

For material checkpoints, the engineer must reconcile:

**Workflow Result + Job Results + Step/Log Evidence + Test Result + Runtime Evidence (when applicable) + Matrix/Registry State + Commit/File State.**

Only the reconciled state may be used to choose the next build point.

### 9B.5 Failure Learning Promotion

If a failure exposes a repeatable control weakness, the engineer MUST search existing ARGO learning before creating new guidance. If no adequate rule exists, record candidate learning and determine whether it should be promoted into this protocol, a test gate, a matrix rule, or another canonical learning surface.

A prior occurrence of the same failure that was not retrieved is a **Prior-Learning Retrieval Defect** and must be documented when materially relevant.

---

## 10. Model Creation Gate

A new Model may be proposed only after:

`Existing Models → Current Relationships → Consumer Proof → Repository Reconciliation → Verified Gap Assessment`

If an existing model covers the requirement, extend/reconcile it rather than creating a duplicate model.

If no evidence proves a real gap, create no new Model.

---

## 11. Learning Promotion Gate

Learning MUST NOT become canonical merely because it was observed, repeated, or documented.

Candidate learning requires:

`Observation → Evidence → Boundary → Reproducibility/Transfer Test → Review → Explicit Promotion Decision`

Where applicable, classify learning as:

- `OBSERVED`
- `CANDIDATE`
- `REUSABLE`
- `VERIFIED`
- `CANONICAL`

The classification must preserve provenance and uncertainty.

---

## 11A. Provenance and Authority State

Every material analytical claim received from another execution identity, analysis surface, external evaluation, or prior session MUST preserve two separate dimensions:

**Evidence State** and **Authority State**.

Minimum evidence states:

- `REPORTED` — stated by a source but not independently checked by the current executor.
- `PROVEN` — supported by direct repository/tool/test evidence available to the current executor.
- `CANDIDATE` — plausible analytical inference requiring validation.
- `UNPROVEN` — not independently established.
- `INVALIDATED` — previously recorded evidence subsequently shown to be contaminated, contradicted, stale, or baseline-invalid.

Minimum authority states:

- `NON-AUTHORITATIVE`
- `CANDIDATE-AUTHORITY`
- `GOVERNANCE-AUTHORITY`
- `CANONICAL`

**Documentation does not upgrade authority.**

Preserving a claim in `main`, an Engineering Journal, a Knowledge Package, or another shared memory surface does not by itself promote its authority or validity.

For claims crossing execution identities, preserve at minimum:

`SOURCE_IDENTITY → CLAIM → SOURCE_EVIDENCE → EVIDENCE_STATE → VERIFIED_BY → VERIFICATION_METHOD → AUTHORITY_STATE → VERIFICATION_DATE → CHECKPOINT`

`PROVEN` must mean proven by the current evidence record, not merely asserted by the source.

---

## 11B. Session Closure Gate

A session is not closed by writing the word `CLOSED` in a report.

Before closure, the engineer MUST complete, as applicable:

`EXECUTE → VERIFY → DOCUMENT → RE-READ → COMMIT/SHA VERIFY → CHECKPOINT RECORD → CLOSE`

For any material mutation, the final repository state must be re-read after the mutation and its commit/blob identity must be verified before the session may be reported as closed.

If verification is unavailable or incomplete, the session state MUST remain explicitly `OPEN / HOLD / VERIFICATION-PENDING`, as applicable; the report must not claim completed closure.

---

## 12. Session Closure

A session may close only when:

1. all planned safe actions for the checkpoint are complete, or a genuine blocker has been recorded;
2. required post-change verification is complete;
3. open contradictions or unresolved authority conflicts are explicitly recorded;
4. checkpoint evidence is written to the repository;
5. no required failing CI/integration check is being silently carried forward;
6. the next continuation point is explicit;
7. for material mutations, re-read and commit/blob verification are complete.

The final report should state:

- what was completed;
- what was discovered;
- what remains unproven/open;
- verification state;
- checkpoint;
- closure state.

The report should remain concise. Detailed evidence belongs in the repository.
