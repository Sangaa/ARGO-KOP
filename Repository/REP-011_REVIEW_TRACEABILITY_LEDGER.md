# REP-011

---

# ARGO KOP — REVIEW & MUTATION TRACEABILITY LEDGER

Platform: ARGO KOP
Document ID: REP-011
Version: 1.0.4
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
- `REP-011` = review/evidence/mutation traceability;
- `REP-016` = Phase 1 execution queue.

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

## 8. Control-Plane Reconciliation Matrix

The Phase-1 control-plane artifacts must be evaluated as one synchronized system, not as isolated documents.

| Artifact | REP-011 Review | REP-012 Allocation | REP-013 Inventory | REP-014 Relationships | REP-016 Queue | Current Reconciliation |
|---|---|---|---|---|---|---|
| REP-011 | Self | Required | Required | Required | Required | OPEN / Integrity Hold |
| REP-012 | Required | Self | Required | Required | Required | OPEN / Integrity Hold |
| REP-013 | Required | Required | Self | Required | Required | OPEN / Integrity Hold |
| REP-014 | Required | Required | Required | Self | Required | OPEN / Integrity Hold |
| REP-015 | Required | Required | Required | Required | Required | OPEN / Integrity Hold |
| REP-016 | Required | Required | Required | Required | Self | OPEN / Integrity Hold |

`Required` means the relationship/evidence must be reconciled before the corresponding claim can be promoted to closed. It does not mean the reconciliation has already succeeded.

### Reconciliation Decision States

```text
NOT_CHECKED
PARTIALLY_RECONCILED
RECONCILED
CONFLICT
REVALIDATION_REQUIRED
CLOSED
```

The current control-plane state remains **PARTIALLY_RECONCILED / INTEGRITY HOLD** until all required cross-registry checks are supported by current repository evidence.

This explicit state prevents a successful edit of one control-plane file from being mistaken for repository-wide consistency.

## 9. Relationship Verification Boundary

A relationship may not be considered verified merely because a reference exists.

Where material, verify:

`Source Identity → Target Identity → Relationship Type → Evidence → Authority → Impact → Consumer Scope → Current State`

An unresolved endpoint, identity conflict, quarantine state, or material unreviewed mutation prevents a closed relationship claim.

## 10. Folder Completion Control

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

## 11. Phase 1 Closure Rule

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

## 12. Re-review Avoidance Rule

Before starting a review, consult `REP-011`, `REP-012`, `REP-013`, and `REP-014` within the applicable scope and compare current repository state with the last recorded review/checkpoint state.

If content identity is unchanged, material registry bindings remain consistent, and recorded scope is sufficient, do not re-review without a reason.

Re-review is justified when the file, dependency, authority, consumer, evidence, methodology, checkpoint, or required Phase 1 scope materially changes.

## 13. Learning From Review Failures

Review failures or mistaken interpretations shall be preserved as reusable engineering knowledge when they change future review behavior.

Examples include trusting conversation claims without repository evidence, using documentation date without temporal analysis, treating commit existence as semantic correctness, assuming selected-file review closes a folder, accepting references as relationships without authority/consumer checks, mutating without post-read, or losing the last trusted state because no checkpoint existed.

## 14. Persistence Boundary

A material mutation is not considered safely persisted for cross-session continuation until the repository contains the mutation and it has been re-read successfully.

Required persistence sequence:

`MUTATE → COMMIT → RE-READ → RECORD EVIDENCE → CONTINUE`

The conversation may describe the operation, but it is not the persistence boundary.

If a session ends after the commit but before registry synchronization, the next session must detect that incomplete synchronization from repository state and leave the affected review open until reconciliation is performed.

## 15. Current Known Audit Boundary — 2026-08-10

The current repository contains material reviewed and modified during the 2026-08-09 pre-failure window. `EJR-015` identifies those mutations as requiring independent audit.

Current Phase 1 work therefore uses:

`Historical Mutation Audit → Current Repository Review → Relationship Revalidation → Post-Mutation Re-read → Registry Reconciliation → Allocation/Checkpoint Update → Explicit Closure`

The existence of `EJR-015` does not close any affected domain.

## 16. Minimum Review Record Template

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
REP-016 Work Item:
Mutation:
Post-Mutation Re-read:
Recovery Checkpoint:
Reconciliation State:
Unresolved Scope:
Next Review Trigger:
```

## 17. Authority Boundary

This ledger controls review traceability and completion evidence only. Domain-specific canonical authorities remain controlling.

## 18. Related Documents

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-003_REPOSITORY_STANDARDS.md`
- `Repository/REP-008_REPOSITORY_BASELINE.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Repository/REP-010_RELEASE_BASELINE.md`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
- `Repository/REP-013_REPOSITORY_CONTENT_TREE.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md`
- `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md`
- `Memory/Engineering_Journal/EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md`
- `Memory/Engineering_Journal/EJR-022_2026-08-10_HERMUZ_BUILD_METHOD_LESSONS.md`
- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`

## 19. Guiding Rule

**Never spend review effort twice because the repository forgot what was already proven; never declare unfinished work complete because the repository forgot what remains open.**

---

End of Document
