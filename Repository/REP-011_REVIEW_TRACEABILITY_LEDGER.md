# REP-011

---

# ARGO KOP — REVIEW & MUTATION TRACEABILITY LEDGER

Platform: ARGO KOP
Document ID: REP-011
Version: 1.0.1
Status: Active / Integrity Hold
Category: Repository Control
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1
Last Audit Date: 2026-08-10

---

## 1. Purpose

Provide a technical repository-level basis for determining whether a file, folder, relationship or domain has actually been reviewed, modified, re-read and connected to the current repository state.

The ledger exists to prevent duplicated review effort, loss of completed work, accidental re-review of unchanged material, and false completion claims.

It also preserves unfinished scope until Phase 1 repository completion is explicitly declared.

---

## 2. Core Rule

**A file is not considered reviewed because it was mentioned, documented, committed, or claimed as reviewed.**

A review state must be tied to repository evidence.

Minimum evidence for a completed review record:

- canonical path;
- document identity where applicable;
- repository commit containing the reviewed state;
- content/blob identity when available;
- review timestamp;
- reviewer/model/session identifier when useful;
- scope actually inspected;
- relationships actually checked;
- mutation performed, if any;
- post-mutation re-read result;
- remaining unresolved scope.

---

## 3. Review States

Use the following controlled states:

`NOT_REVIEWED`

No current review evidence exists.

`REVIEWED`

The file was read and inspected at a specific repository state, but no claim of semantic or relationship closure is made.

`MODIFIED`

A repository mutation was performed, but post-mutation validation is not yet complete.

`RE_READ`

The modified/current file was read again after mutation.

`RELATIONSHIPS_REVALIDATED`

The declared relationships within the recorded scope were checked against source, target and relevant consumer evidence.

`PROVISIONALLY_ACCEPTED`

The current content may be retained, but an identified historical or semantic uncertainty remains.

`CLOSED_FOR_PHASE_1`

The file/domain has been explicitly reviewed to the agreed Phase 1 boundary, with remaining exclusions recorded. This state must not be inferred from silence.

`REVALIDATION_REQUIRED`

Existing evidence is insufficient, stale, contradicted, or derived from a pre-failure mutation and requires another review.

---

## 4. Evidence Freshness

Review evidence must be interpreted temporally.

A later documentation date does not automatically validate an earlier mutation.

Before accepting a review claim, determine:

1. when the reviewed mutation occurred;
2. when the review/audit was recorded;
3. whether a failure or methodological discovery occurred between them;
4. whether newer repository evidence exists;
5. whether the reviewer had access to that newer evidence;
6. whether the current file content is actually the content that was reviewed.

A review performed before discovery of a material methodological failure is **not automatically invalid**, but its affected semantic conclusions require independent revalidation.

---

## 5. Repository Binding

For every mutation or material review, the preferred binding is:

`Path → Document ID → Commit SHA → Content/Blob SHA → Review Scope → Result`

When a content/blob SHA is unavailable, the commit SHA plus exact path and post-read timestamp shall be retained.

The commit proves that a repository state existed. It does not by itself prove that the reasoning or semantic interpretation behind the mutation was correct.

`Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` provides the complementary allocation/state/checkpoint layer. REP-011 records review evidence; REP-012 records where the artifact is allocated, what repository state is registered, and what recovery checkpoint is available.

---

## 6. Folder Completion Control

A folder shall not be marked complete merely because selected files inside it were reviewed.

For every active folder/domain, the ledger must distinguish:

- files reviewed;
- files modified;
- files re-read;
- relationships revalidated;
- files intentionally excluded;
- files not yet reviewed;
- unresolved dependencies;
- historical/pre-failure mutations awaiting revalidation.

Until an explicit `CLOSED_FOR_PHASE_1` decision exists, remaining folder content must remain visibly open and must not be silently treated as complete.

---

## 7. Phase 1 Closure Rule

Phase 1 repository completion requires an explicit closure decision supported by:

- folder/domain inventory coverage;
- file review coverage;
- mutation/re-read evidence;
- relationship coverage;
- unresolved-item register;
- historical/pre-failure mutation disposition;
- index/map synchronization;
- allocation/state registry synchronization;
- final repository-wide integrity review.

No individual folder may imply Phase 1 completion for the whole repository.

---

## 8. Re-review Avoidance Rule

Before starting a review of a file, the reviewer should consult both the review ledger (`REP-011`) and allocation/state registry (`REP-012`) and compare the current repository state with the last recorded review/checkpoint state.

If the current content identity is unchanged and the recorded scope is sufficient, the file should not be re-reviewed without a reason.

A re-review is justified when:

- the file changed;
- a dependency changed;
- a referenced authority changed;
- a relevant consumer changed;
- a new contradictory artifact appeared;
- a methodological failure affects the prior review;
- the prior review scope was incomplete;
- the recovery checkpoint changed materially;
- Phase 1 closure requires broader coverage.

---

## 9. Learning From Review Failures

A review failure or mistaken interpretation shall be preserved as reusable engineering knowledge when it changes future review behavior.

Examples include:

- trusting a conversation claim without repository evidence;
- using documentation date without temporal/causal analysis;
- treating commit existence as semantic correctness;
- assuming a folder is complete because selected files were reviewed;
- accepting a relationship because a reference exists without checking authority and consumers;
- performing a mutation without post-mutation re-read;
- losing track of the last trusted repository state because no allocation/checkpoint record existed.

The purpose is not to preserve blame. The purpose is to make future reconstruction and cross-model handoff safer.

---

## 10. Current Known Audit Boundary — 2026-08-10

The current repository contains material reviewed and modified during the 2026-08-09 pre-failure window. `EJR-015` identifies those mutations as requiring independent audit.

Current Phase 1 work therefore uses:

`Historical Mutation Audit → Current Repository Review → Relationship Revalidation → Post-Mutation Re-read → Allocation/Checkpoint Update → Explicit Closure`

The existence of `EJR-015` does not itself close any affected domain.

---

## 11. Minimum Review Record Template

For each material review, record at minimum:

```text
Path:
Document ID:
Review Date/Time:
Repository Commit:
Content/Blob SHA:
Review State:
Previous Review Evidence:
Reason for Review/Re-review:
Authority Checked:
Relationships Checked:
Consumers Checked:
Mutation:
Post-Mutation Re-read:
Allocation State:
Recovery Checkpoint:
Unresolved Scope:
Next Review Trigger:
```

---

## 12. Authority Boundary

This ledger controls review traceability and completion evidence only.

It does not grant semantic authority over Core, Governance, Architecture, Models, Runtime, Knowledge or other domain content.

Domain-specific canonical authorities remain controlling.

---

## 13. Related Documents

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-003_REPOSITORY_STANDARDS.md`
- `Repository/REP-008_REPOSITORY_BASELINE.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Repository/REP-010_RELEASE_BASELINE.md`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
- `Memory/Engineering_Journal/EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md`
- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`

---

## 14. Guiding Rule

**Never spend review effort twice because the repository forgot what was already proven; never declare unfinished work complete because the repository forgot what remains open.**

---

End of Document
