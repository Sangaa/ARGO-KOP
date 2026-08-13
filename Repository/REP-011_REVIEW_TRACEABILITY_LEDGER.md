# REP-011

---

# ARGO KOP — REVIEW & MUTATION TRACEABILITY LEDGER

Platform: ARGO KOP
Document ID: REP-011
Version: 1.0.7
Status: Active / Integrity Hold
Category: Repository Control
Canonical: Yes
Priority: Critical
Development Baseline: 3.3.0
Last Audit Date: 2026-08-13

---

## 1. Purpose

Provide a technical repository-level basis for determining whether a file, folder, relationship or domain has actually been reviewed, modified, re-read and connected to the current repository state.

The ledger exists to prevent duplicated review effort, loss of completed work, accidental re-review of unchanged material, false completion claims, and stale-content acceptance.

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
- consumers/dependencies actually checked where material;
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
6. whether the current file content is actually the content that was reviewed;
7. whether current content still satisfies the latest applicable content contract and governing instructions.

A review performed before discovery of a material methodological failure is not automatically invalid, but affected semantic conclusions require independent revalidation.

## 6. Content Freshness & Fitness Rule

**Physical presence is not evidence of current fitness.**

Every material or canonical file that predates a relevant repository update, instruction change, model change, relationship change, or methodological discovery must be evaluated for current fitness even when its path and content identity are unchanged.

Current fitness requires, within the applicable scope:

- current repository baseline compatibility;
- compliance with the latest applicable content instructions;
- compatibility with current canonical authorities;
- compatibility with current dependencies and consumers;
- consistency with current relationship definitions;
- no superseding artifact or instruction that materially changes its meaning;
- no known historical/pre-failure condition that affects its conclusions;
- evidence that its behavior or operational role remains consistent with current artifacts where executable/operational behavior is claimed.

A file may therefore be:

`PRESENT / STALE`, `PRESENT / CURRENT`, `PRESENT / REVALIDATION_REQUIRED`, or `PRESENT / CONFLICT`.

A file must not be promoted to a current validated state solely because it is old, canonical, referenced by another document, or successfully committed.

## 7. Cross-Document Learning Rule

**Review across files is a knowledge-producing operation, not only a consistency check.**

When comparing two or more artifacts produces a new reusable rule, interpretation, failure mode, mapping correction, authority boundary, relationship rule, or review method, preserve that discovery as engineering knowledge.

A material cross-document learning event must record:

- source artifacts inspected;
- current repository checkpoint/commit;
- observed discrepancy or pattern;
- reasoning that establishes the new learning;
- affected domains/relationships;
- resulting rule or operational implication;
- whether existing artifacts require revalidation or mutation;
- follow-up work item/checkpoint.

The learning must be persisted in the repository before it is treated as durable cross-session project knowledge.

A conversation-only discovery is **unpersisted knowledge** and must not be treated as a completed project-memory update.

## 8. Repository Binding

For every mutation or material review, the preferred binding is:

`Path → Document ID → Commit SHA → Content/Blob SHA → Review Scope → Result`

The commit proves that a repository state existed. It does not by itself prove that the reasoning or semantic interpretation behind the mutation was correct.

`REP-012` provides the complementary allocation/state/checkpoint layer.

## 9. Cross-Registry Consistency Rule

Before a review is marked `RELATIONSHIPS_REVALIDATED` or `CLOSED_FOR_PHASE_1`, reconcile within the applicable scope:

1. physical path and document identity;
2. `REP-013` content inventory entry;
3. `REP-012` allocation/state/checkpoint entry;
4. `REP-014` relationship entries, where applicable;
5. current repository content/commit evidence;
6. latest applicable content instructions and authority boundaries.

If any required registry view is missing or materially inconsistent, the review remains open or becomes `REVALIDATION_REQUIRED`.

## 10. Control-Plane Reconciliation Matrix

The Phase-1 control-plane artifacts must be evaluated as one synchronized system, not as isolated documents.

| Artifact | REP-011 Review | REP-012 Allocation | REP-013 Inventory | REP-014 Relationships | REP-016 Queue | Current Reconciliation |
|---|---|---|---|---|---|---|
| REP-011 | Self | Required | Required | Required | Required | OPEN / Integrity Hold |
| REP-012 | Required | Self | Required | Required | Required | OPEN / Integrity Hold |
| REP-013 | Required | Required | Self | Required | Required | OPEN / Integrity Hold |
| REP-014 | Required | Required | Required | Self | Required | OPEN / Integrity Hold |
| REP-015 | Required | Required | Required | Required | Required | OPEN / Integrity Hold |
| REP-016 | Required | Required | Required | Required | Self | OPEN / Integrity Hold |
| DIAG-001 | Required | Provenance | Inventoried | Relationship-linked | Orientation only | PROVENANCE LINKED / OPEN |

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

## 11. Relationship Verification Boundary

A relationship may not be considered verified merely because a reference exists.

Where material, verify:

`Source Identity → Target Identity → Relationship Type → Evidence → Authority → Impact → Consumer Scope → Current State`

An unresolved endpoint, identity conflict, quarantine state, or material unreviewed mutation prevents a closed relationship claim.

## 12. Folder Completion Control

A folder shall not be marked complete merely because selected files inside it were reviewed.

For every active folder/domain, distinguish:

- files reviewed;
- files modified;
- files re-read;
- relationships revalidated;
- intentionally excluded files;
- not-yet-reviewed files;
- unresolved dependencies;
- historical/pre-failure mutations awaiting revalidation;
- files present but stale or current-fitness-unverified.

Until an explicit `CLOSED_FOR_PHASE_1` decision exists, remaining content stays open.

## 13. Phase 1 Closure Rule

Phase 1 repository completion requires an explicit closure decision supported by:

- folder/domain inventory coverage;
- file review coverage;
- current-fitness/content-contract checks;
- mutation/re-read evidence;
- relationship coverage;
- unresolved-item register;
- historical/pre-failure mutation disposition;
- cross-document learning disposition;
- index/map synchronization;
- allocation/state registry synchronization;
- relationship registry synchronization where applicable;
- final repository-wide integrity review.

## 14. Re-review Avoidance Rule

Before starting a review, consult `REP-011`, `REP-012`, `REP-013`, and `REP-014` within the applicable scope and compare current repository state with the last recorded review/checkpoint state.

If content identity is unchanged, material registry bindings remain consistent, recorded scope is sufficient, **and current-fitness/content-contract conditions remain satisfied**, do not re-review without a reason.

Re-review is justified when the file, dependency, authority, consumer, evidence, methodology, checkpoint, content instructions, current-fitness assessment, or required Phase 1 scope materially changes.

## 15. Learning From Review Failures

Review failures or mistaken interpretations shall be preserved as reusable engineering knowledge when they change future review behavior.

Examples include trusting conversation claims without repository evidence, using documentation date without temporal analysis, treating commit existence as semantic correctness, assuming selected-file review closes a folder, accepting references as relationships without authority/consumer checks, mutating without post-read, losing the last trusted state because no checkpoint existed, treating logical domain names as physical paths without evidence, or accepting an old file as current merely because it still exists.

## 16. Persistence Boundary

A material mutation is not considered safely persisted for cross-session continuation until the repository contains the mutation and it has been re-read successfully.

Required persistence sequence:

`MUTATE → COMMIT → RE-READ → RECORD EVIDENCE → CONTINUE`

The conversation may describe the operation, but it is not the persistence boundary.

If a session ends after the commit but before registry synchronization, the next session must detect that incomplete synchronization from repository state and leave the affected review open until reconciliation is performed.

## 17. Visual Artifact Review Boundary

Visual or derived artifacts are reviewable repository artifacts, but they do not become canonical merely because they are stored or referenced.

For `DIAG-001`, the review ledger recognizes:

- SVG: `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.svg`
- Metadata: `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.md`
- Source/provenance: `REP-012`
- Relationship registration: `REP-014`

The pair is an **orientation/provenance artifact**. Its numerical/status claims must be checked against current canonical registries before use as evidence.

If its source registry changes materially, the diagram enters `REVALIDATION_REQUIRED` until regenerated or explicitly superseded.

## 18. Current Known Audit Boundary — 2026-08-13

The current repository contains material reviewed and modified during the 2026-08-09 pre-failure window. `EJR-015` identifies those mutations as requiring independent audit.

The current audit also established a material methodological learning: historical checkpoints can remain valid historical evidence while their physical paths, content, relationships, and conclusions require independent validation against the current HEAD. A logical memory domain must not be assumed to equal a physical directory name without current repository evidence.

Current Phase 1 work therefore uses:

`Historical Mutation Audit → Current Repository Review → Content-Fitness Check → Relationship Revalidation → Cross-Document Learning Capture → Post-Mutation Re-read → Registry Reconciliation → Allocation/Checkpoint Update → Explicit Closure`

The existence of `EJR-015` does not close any affected domain.

## 19. Minimum Review Record Template

```text
Path:
Document ID:
Review Date/Time:
Repository Commit:
Content/Blob SHA:
Review State:
Previous Review Evidence:
Reason for Review/Re-review:
Current Baseline Checked:
Content Contract Checked:
Current-Fitness State:
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
Cross-Document Learning:
Reconciliation State:
Unresolved Scope:
Next Review Trigger:
```

## 20. Authority Boundary

This ledger controls review traceability, content-fitness evidence, learning persistence and completion evidence only. Domain-specific canonical authorities remain controlling.

## 21. Related Documents

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
- `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.svg`
- `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.md`
- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`

## 22. Guiding Rule

**Never spend review effort twice because the repository forgot what was already proven; never declare unfinished work complete because the repository forgot what remains open; never treat an old file as current until its content, instructions, dependencies, relationships and operational fitness survive revalidation.**

---

End of Document
