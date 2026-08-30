# GOV-015 — EXECUTION DOCUMENTATION & KNOWLEDGE TRANSFER STANDARD

Status: ACTIVE / GOVERNED
Date: 2026-08-17
Scope: All governed build, mutation, validation, testing, and reconciliation sessions, plus bounded transfer-learning assessment of practical non-repository tasks when this standard is active

## 1. Purpose

This standard makes documentation and knowledge transfer mandatory parts of execution. A technically successful action is not complete until its evidence, decision boundary, reusable learning, and transfer status are recorded.

For ordinary practical tasks outside direct ARGO-KOP repository construction, permanent documentation is not mandatory merely because the interaction occurred. Section 3A defines the bounded external-transfer rule.

## 2. Mandatory Execution Record

Every governed execution must record, at minimum:

1. Intent and bounded scope.
2. Starting repository state and current HEAD/SHA.
3. Governing controls and evidence used to authorize the action.
4. Mutation Matrix / test matrix used, where applicable.
5. Target files and preservation boundary.
6. Candidate/pre-execution validation result.
7. Actual execution result, commit and workflow evidence when available.
8. Post-write repository read-back.
9. Failures, rejected attempts, stale-state events, and recovery actions.
10. Explicit statement of what was not proven.
11. Session closure state and next safe entry.

The reusable execution record template is `Templates/GOV-015_EXECUTION_RECORD_TEMPLATE.md` and should be used as the default session record structure.

## 3. Knowledge Transfer Protocol

A new lesson must pass this chain before becoming reusable knowledge:

`Observation → Root Cause → Lesson → General Rule → Test → Validation → Promotion → Transfer`

The lesson must identify the evidence that supports it and the boundary where it does not apply.

### Promotion levels

- `SESSION-LEARNING`: useful only for the current transaction/session.
- `REUSABLE-LEARNING`: demonstrated useful in more than one applicable context.
- `GOVERNANCE-RULE`: promoted into a governing control after evidence and validation.
- `DEFAULT-PRACTICE`: approved routine method used by default.

No model/operator assertion alone may promote a lesson to `GOVERNANCE-RULE` or `DEFAULT-PRACTICE`.

## 3A. External Transfer Task Learning

A practical task whose primary objective is outside direct ARGO-KOP repository construction may be classified as:

`EXTERNAL_TRANSFER_TASK`

Examples include programming/debugging outside ARGO-KOP, Lua/Roblox work, operational or logistics problems, communication drafting, document/spreadsheet/data analysis, research, troubleshooting, and other practical user tasks.

### Classification boundary

Task context determines this classification. User identity does not.

ARGO/HERMUZ must not infer who is using an account merely to decide whether a task is a learning opportunity. Identity should be used only when explicitly supplied and genuinely necessary for the task under applicable controls.

### Primary operating rule

For every `EXTERNAL_TRANSFER_TASK`:

`UNDERSTAND USER GOAL → SOLVE USER NEED FIRST → VERIFY WHERE PRACTICAL → SILENTLY ASSESS LEARNING VALUE → CAPTURE ONLY IF JUSTIFIED`

The quality, clarity, speed, or usefulness of the user-facing answer must not be degraded merely to make the interaction resemble a training session.

Transfer-learning reflection may remain silent/background from the user's perspective when no explanation is needed. The user does not need repeated notices that an ordinary task is being examined for reusable learning.

### Learning separation

External-task learning must distinguish at least:

1. **DOMAIN-SPECIFIC LEARNING** — useful primarily inside the task domain, such as Lua behavior, Roblox conventions, shipping workflow details, spreadsheet behavior, or API-specific constraints.
2. **TRANSFERABLE REASONING LEARNING** — potentially reusable across domains, such as assumption testing, evidence qualification, ambiguity handling, scope control, dependency tracing, failure isolation, incremental verification, or separating symptom from root cause.

Domain-specific evidence must not be promoted as a general reasoning law merely because it solved one external task.

### Evidence and promotion boundary

`EXTERNAL EXPERIENCE ≠ CANONICAL KNOWLEDGE`

One successful answer, one failure, one user correction, or one domain observation does not create authority automatically.

Material external learning may enter the existing promotion chain only when evidence justifies it, for example when:

- a meaningful failure exposes a reusable assumption or control weakness;
- a lesson recurs across more than one applicable case;
- a verification method materially reduces error or ambiguity;
- a reasoning principle transfers successfully across different domains;
- later HERMUZ/HORUS review or equivalent governed verification establishes retention value.

Unproven or one-off observations should remain session-bounded or local.

### No forced documentation

Ordinary external interactions do not require:

`EVERY CHAT → NEW FILE`

Prefer:

`SIGNIFICANT REUSABLE LEARNING → BOUNDED CAPTURE`

A permanent repository artifact is justified only when the learning value, reusability, evidence, and governance cost warrant retention. Otherwise no repository mutation is required.

### Privacy and minimization boundary

Learning capture must preserve the reusable mechanism rather than unnecessary personal detail.

Do not preserve credentials, passwords, private secrets, sensitive personal information, or unnecessary identifying details as learning artifacts. When a reusable lesson can be expressed without personal/user-specific data, use the minimized form.

### Post-task reflection

When explicitly requested, or when learning value is materially significant, reflection may assess:

- what was attempted;
- what worked or failed;
- which assumptions changed;
- what evidence changed the conclusion;
- what was domain-specific;
- what reasoning transferred successfully;
- what reusable lesson may exist;
- what remains unproven;
- whether bounded repository capture is justified.

Reflection must not rewrite history to make the task appear more successful than it was.

### Transfer objective

The higher-value transfer question is:

> Can ARGO preserve evidence discipline, scope control, uncertainty handling, and verification behavior when the problem no longer resembles ARGO-KOP?

A positive answer must be earned through repeated evidence, not assumed from one successful task.

This section creates no new permanent role and does not interrupt the current legal repository build priority. After a bounded external task or learning assessment, current repository work resumes from its existing checkpoint when construction is invoked again.

## 4. Test and Channel Learning

Any new test, fixture strategy, CI channel, audit, or verification method that materially improves safety, accuracy, speed, repeatability, or model-independence must be recorded as reusable knowledge after successful validation.

The record must state:

- previous method;
- new method;
- measured/observed benefit;
- failure modes and limits;
- required regression coverage;
- whether it becomes default or remains integration/periodic regression.

## 5. Required Separation of Evidence

The following must never be conflated:

- audit completeness ≠ runtime connectivity;
- candidate validation ≠ current-state write validation;
- test success ≠ canonical promotion;
- fixture success ≠ repository integration proof;
- documentation ≠ evidence;
- historical learning ≠ current repository state.

## 6. Closure Gate

A session may be closed only after:

`Execution Evidence + Verification + Documentation + Learning Assessment + Transfer Decision + Next Safe Entry`

are recorded.

If learning is identified but not yet validated, it must remain explicitly marked `UNVALIDATED` and must not silently become a rule.

The mandatory execution-record requirement in this section applies to governed repository execution. An ordinary `EXTERNAL_TRANSFER_TASK` that produces no governed repository mutation may end without creating a repository record unless Section 3A's bounded-capture threshold is met.

## 7. Interaction With Existing Controls

GOV-015 supplements, and does not replace, existing governance, session, mutation, traceability, identity, CI, preservation, SHA/current-state, read-back, privacy, safety, or system controls. Where controls conflict, the higher-authority governing control remains binding.

External-task learning remains subject to the `GOV-013` Learning Promotion Gate and does not override domain-specific authority.

## 8. Model Independence Principle

The purpose of this standard is to move execution safety and accumulated experience from individual model memory into repository-governed artifacts, tests, and repeatable controls when durable transfer is justified. Future models must be able to discover and apply retained rules without relying on conversational memory.

This principle does not require permanent capture of every interaction; disciplined non-capture is valid when an external task yields no sufficiently reusable learning.

---

End of GOV-015
