# REP-011

---

# ARGO KOP — REVIEW & MUTATION TRACEABILITY LEDGER

Platform: ARGO KOP
Document ID: REP-011
Version: 1.0.2
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

## 2. Control-Plane Relationship

REP-011 is one component of the repository control plane:

- `REP-002` = structural/domain map;
- `REP-013` = folder → file content inventory;
- `REP-014` = artifact relationship registry;
- `REP-012` = allocation/state/checkpoint/recovery;
- `REP-011` = review/evidence/mutation traceability.

These records are complementary and must remain synchronized.

## 3. Core Rule

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

## 4. Review States

`NOT_REVIEWED`, `REVIEWED`, `MODIFIED`, `RE_READ`, `RELATIONSHIPS_REVALIDATED`, `PROVISIONALLY_ACCEPTED`, `CLOSED_FOR_PHASE_1`, `REVALIDATION_REQUIRED` are the controlled states.

`CLOSED_FOR_PHASE_1` must never be inferred from silence or registry presence.

## 5. Evidence Freshness

Review evidence must be interpreted temporally.

A later documentation date does not automatically validate an earlier mutation.

Before accepting a review claim, determine:

1. when the reviewed mutation occurred;
2. when the review/audit was recorded;
3. whether a failure or methodological discovery occurred between them;
4. whether newer repository evidence exists;
5. whether the reviewer had access to that newer evidence;
6. whether the current file content is actually the content that was reviewed.

A review performed before discovery of a material methodological failure is not automatically invalid, but affected semantic conclusions require independent revalidation.

## 6. Repository Binding

For every mutation or material review, the preferred binding is:

`Path → Document ID → Commit SHA → Content/Blob SHA → Review Scope → Result`

The commit proves that a repository state existed. It does not by itself prove that the reasoning or semantic interpretation behind the mutation was correct.

`REP-012` provides the complementary allocation/state/checkpoint layer.

## 7. Cross-Registry Consistency Rule

Before a review is marked `RELATIONSHIPS_REVALIDATED` or `CLOSED_FOR_PHASE_1`, reconcile within the applicable scope:

1. physical path and document identity;
2. `REP-013` content inventory entry;
3. `REP-012` allocation/state/checkpoint entry;
4. `REP-014` relationship entries, where applicable;
5. current repository content/commit evidence.

If any required registry view is missing or materially inconsistent, the review remains open or becomes `REVALIDATION_REQUIRED`.

## 8. Relationship Verification Boundary

A relationship may not be considered verified merely because a reference exists.

Where material, verify:

`Source Identity → Target Identity → Relationship Type → Evidence → Authority → Impact → Consumer Scope → Current State`

An unresolved endpoint, identity conflict, quarantine state, or material unreviewed mutation prevents a closed relationship claim.

## 9. Folder Completion Control

A folder shall not be marked complete merely because selected files inside it were reviewed.

For every active folder/domain, distinguish:

- files reviewed;
- files modified;
- files re-read;
- relationships revalidated;
- intentionally excluded files;
- not-yet-reviewed files;
- unresolved dependencies;
- historical/pre-failure mutations awaiting revalidation.

Until an explicit `CLOSED_FOR_PHASE_1` decision exists, remaining content stays open.

## 10. Phase 1 Closure Rule

Phase 1 repository completion requires an explicit closure decision supported by:

- folder/domain inventory coverage;
- file review coverage;
- mutation/re-read evidence;
- relationship coverage;
- unresolved-item register;
- historical/pre-failure mutation disposition;
- index/map synchronization;
- allocation/state registry synchronization;
- relationship registry synchronization where applicable;
- final repository-wide integrity review.

## 11. Re-review Avoidance Rule

Before starting a review, consult `REP-011`, `REP-012`, `REP-013`, and `REP-014` within the applicable scope and compare current repository state with the last recorded review/checkpoint state.

If content identity is unchanged, material registry bindings remain consistent, and recorded scope is sufficient, do not re-review without a reason.

Re-review is justified when the file, dependency, authority, consumer, evidence, methodology, checkpoint, or required Phase 1 scope materially changes.

## 12. Learning From Review Failures

Review failures or mistaken interpretations shall be preserved as reusable engineering knowledge when they change future review behavior.

Examples include trusting conversation claims without repository evidence, using documentation date without temporal analysis, treating commit existence as semantic correctness, assuming selected-file review closes a folder, accepting references as relationships without authority/consumer checks, mutating without post-read, or losing the last trusted state because no checkpoint existed.

## 13. Current Known Audit Boundary — 2026-08-10

The current repository contains material reviewed and modified during the 2026-08-09 pre-failure window. `EJR-015` identifies those mutations as requiring independent audit.

Current Phase 1 work therefore uses:

`Historical Mutation Audit → Current Repository Review → Relationship Revalidation → Post-Mutation Re-read → Registry Reconciliation → Allocation/Checkpoint Update → Explicit Closure`

The existence of `EJR-015` does not close any affected domain.

## 14. Minimum Review Record Template

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
REP-013 Inventory State:
REP-012 Allocation State:
REP-014 Relationship State:
Mutation:
Post-Mutation Re-read:
Recovery Checkpoint:
Unresolved Scope:
Next Review Trigger:
```

## 15. Authority Boundary

This ledger controls review traceability and completion evidence only. Domain-specific canonical authorities remain controlling.

## 16. Related Documents

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-003_REPOSITORY_STANDARDS.md`
- `Repository/REP-008_REPOSITORY_BASELINE.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Repository/REP-010_RELEASE_BASELINE.md`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
- `Repository/REP-013_REPOSITORY_CONTENT_TREE.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Memory/Engineering_Journal/EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md`
- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`

## 17. Guiding Rule

**Never spend review effort twice because the repository forgot what was already proven; never declare unfinished work complete because the repository forgot what remains open.**

---

End of Document
