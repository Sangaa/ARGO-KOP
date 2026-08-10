# REP-012

---

# ARGO KOP — REPOSITORY ALLOCATION, STATE & RECOVERY REGISTRY

Platform: ARGO KOP
Document ID: REP-012
Version: 1.0.0
Status: Proposed / Active Control / Integrity Hold
Category: Repository Control
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1
Last Audit Date: 2026-08-10

---

## 1. Purpose

Provide a technical registry analogous to a file-allocation table, partition map and recovery registry for the ARGO KOP repository.

The registry shall answer, before work begins:

- what exists;
- where it belongs;
- who/what owns its semantic authority;
- what review state it is in;
- which repository state was last reviewed;
- what dependencies and consumers are known;
- what remains open;
- how the previous known-good state can be recovered or reconstructed.

This registry complements `REP-011`. It does not replace Git history, domain authority, or the canonical content of the registered files.

---

## 2. Design Analogy

ARGO KOP shall use the following conceptual mapping:

| Technical concept | ARGO KOP equivalent |
|---|---|
| Disk / volume | Repository |
| Partition | Domain / top-level repository area |
| Allocation table | Artifact allocation registry |
| File record | Document/artifact registration record |
| File system metadata | Identity, path, version, state, hash, commit |
| Inode-like identity | Stable Document ID + canonical path history |
| Directory index | Master Index / Repository Map |
| Journal | Engineering Journal / mutation evidence |
| Checkpoint | Known-good repository state / commit SHA |
| Recovery point | Explicit recovery commit/tag/reference |
| Bad sector / corruption marker | Contradicted, stale, damaged or untrusted artifact state |
| fsck-style validation | Repository integrity / allocation / relationship audit |

These are architectural analogies, not implementation requirements.

---

## 3. Core Rule

**No build session should have to rediscover repository state from scratch.**

Before modifying an artifact, the worker should be able to resolve its registry record and determine whether work is:

`NEW → REVIEW → REVALIDATE → MODIFY → RE-READ → LINK → CHECKPOINT`

or whether an existing checkpoint can safely be resumed.

---

## 4. Artifact Identity

Each registered artifact should have, where applicable:

- Document ID;
- canonical path;
- artifact type;
- owning domain;
- semantic authority source;
- current version;
- development baseline;
- current Git commit SHA;
- current content/blob SHA when available;
- last reviewed commit SHA;
- last reviewed content/blob SHA;
- review state from `REP-011`;
- dependency set;
- consumer set;
- unresolved scope;
- recovery checkpoint.

A path alone is not a sufficient identity.

A Document ID alone is not sufficient if its path or ownership has changed without recorded history.

---

## 5. Allocation States

Controlled allocation states:

`UNALLOCATED`

Artifact exists or is expected but has no valid registry assignment.

`ALLOCATED`

Artifact has a valid owner/domain/path assignment.

`MAPPED`

Artifact is represented in the repository map/index.

`REVIEWED`

Current content is bound to repository evidence and a recorded review scope.

`DIRTY`

Artifact changed since its last registered review/checkpoint.

`REVALIDATION_REQUIRED`

Existing review cannot safely be reused because of changed dependencies, authority, contradictory evidence, methodological failure, or other trigger.

`CHECKPOINTED`

A known-good or provisionally accepted repository state is explicitly recorded for recovery purposes.

`CLOSED_FOR_PHASE_1`

The artifact/domain has explicit Phase 1 closure evidence. This state must never be inferred.

`QUARANTINED`

Artifact is retained for evidence but excluded from normal promotion/use until resolved.

---

## 6. Partition / Domain Control

Top-level domains should be treated as logical partitions, including:

- Core
- Governance
- Architecture
- Models
- Knowledge
- Engine
- Services
- Runtime
- AI
- Memory
- Repository
- Specifications
- Templates
- Release
- Projects
- Archive

A partition is not considered complete because its directory exists or selected files have been reviewed.

Each partition requires an explicit inventory and completion state.

---

## 7. Dirty-State Detection

Before touching a file, compare:

`Current Commit/Blob → Registered Last-Reviewed Commit/Blob`

Possible outcomes:

### MATCH

Current content equals the registered reviewed content. Re-review may be skipped if no other trigger exists.

### CONTENT_CHANGED

The file changed. Review/re-read is required.

### DEPENDENCY_CHANGED

The file itself may be unchanged, but a material authority, dependency or consumer changed. Relationship revalidation is required.

### EVIDENCE_CHANGED

New contradictory or stronger evidence appeared. The prior conclusion requires review.

### HISTORY_UNCERTAIN

The registry cannot establish a trustworthy previous checkpoint. Do not assume completion.

---

## 8. Allocation Record

Minimum logical record:

```text
Document ID:
Canonical Path:
Domain/Partition:
Artifact Type:
Semantic Authority:
Current Version:
Development Baseline:
Current Commit SHA:
Current Blob SHA:
Last Reviewed Commit SHA:
Last Reviewed Blob SHA:
Review State:
Allocation State:
Dependencies:
Consumers:
Last Review Scope:
Unresolved Scope:
Last Mutation:
Recovery Checkpoint:
Next Review Trigger:
```

The registry may later be implemented as Markdown, JSON, YAML, SQLite, database tables or another controlled machine-readable format. The semantic contract remains independent of storage technology.

---

## 9. Recovery Model

Recovery shall operate at multiple levels:

### Level 1 — File Recovery

Restore or inspect the last known checkpoint for one artifact.

### Level 2 — Domain Recovery

Restore/reconstruct a coherent partition state using registered artifacts and their relationship evidence.

### Level 3 — Session Recovery

Resume an interrupted build/review session from its last checkpoint, open scope and mutation journal.

### Level 4 — Repository Recovery

Reconstruct the last known coherent repository state using commit history, allocation registry, indexes, journals and explicit recovery checkpoints.

Recovery must preserve uncertainty. It must not silently promote recovered artifacts to canonical status.

---

## 10. Checkpoint Rules

A checkpoint should record:

- repository commit SHA;
- timestamp;
- reason;
- scope covered;
- files/domains included;
- review state;
- known unresolved items;
- known quarantined/pre-failure artifacts;
- recovery instructions or reconstruction entry point.

A commit is evidence of repository state, not proof of semantic correctness.

Therefore a checkpoint may be classified as:

`TECHNICAL_CHECKPOINT`

`REVIEWED_CHECKPOINT`

`PROVISIONAL_CHECKPOINT`

`KNOWN_GOOD_CHECKPOINT`

`RECOVERY_ONLY_CHECKPOINT`

---

## 11. Build Session Resume Protocol

A new model/session should begin with:

1. Load the current repository checkpoint.
2. Load `REP-012` allocation/state information.
3. Load `REP-011` review evidence.
4. Compare current content identities with registered identities.
5. Identify dirty/revalidation-required artifacts.
6. Load open/unresolved scope.
7. Load relevant engineering journal entries.
8. Resume from the highest-confidence unfinished work item.

The session must not assume that an older handoff is current without checking repository state.

---

## 12. Mutation Protocol

For a material mutation:

`ALLOCATE → READ → VERIFY IDENTITY → VERIFY AUTHORITY → CHECK DEPENDENCIES → CHECK CONSUMERS → MUTATE → COMMIT → RE-READ → UPDATE REGISTRY → UPDATE REVIEW LEDGER → CHECKPOINT IF WARRANTED`

If post-mutation re-read fails, the artifact remains `DIRTY` or `REVALIDATION_REQUIRED` and must not be marked complete.

---

## 13. Recovery vs Revert

Recovery is not equivalent to automatic revert.

When a mutation is suspicious:

1. preserve the current evidence;
2. identify the pre-mutation checkpoint;
3. compare the states;
4. determine whether the mutation is wrong, incomplete or merely unverified;
5. choose retain, repair, revert or quarantine;
6. record the decision and evidence.

No destructive recovery action should occur solely because a file is marked uncertain.

---

## 14. Phase 1 Completion Control

For each partition/domain, the registry shall preserve:

- allocated artifacts;
- unallocated artifacts;
- reviewed artifacts;
- dirty artifacts;
- revalidation-required artifacts;
- quarantined artifacts;
- unresolved dependencies;
- unresolved consumers;
- recovery checkpoints.

A partition can only become `CLOSED_FOR_PHASE_1` after an explicit decision supported by `REP-011`, relevant indexes/maps, and domain evidence.

---

## 15. Machine-Readable Future

The current canonical specification is Markdown for human inspection and cross-model portability.

A future implementation may generate a machine-readable registry automatically from Git metadata and repository documents.

The future registry should support at minimum:

- deterministic artifact lookup;
- content identity comparison;
- dependency/consumer impact detection;
- stale-review detection;
- checkpoint lookup;
- session resume;
- recovery planning;
- Phase 1 completion reporting.

Automation must report evidence; it must not silently decide semantic authority.

---

## 16. Relationship to REP-011

`REP-012` answers:

**Where is the artifact, what state is it in, and what checkpoint can recover it?**

`REP-011` answers:

**What review evidence exists for that artifact and what review scope was actually completed?**

The two systems are complementary:

`REP-012 = Allocation / State / Recovery`

`REP-011 = Review / Mutation / Evidence`

Neither replaces the other.

---

## 17. Initial Deployment Rule

Because the repository does not yet have a fully populated allocation registry, the initial deployment status is:

`PARTIAL REGISTRY / RECONSTRUCTION REQUIRED`

Existing repository files must not be marked `ALLOCATED + REVIEWED + CHECKPOINTED` merely because they appear in indexes.

The registry shall be populated incrementally during Phase 1 review.

---

## 18. Related Documents

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Repository/REP-010_RELEASE_BASELINE.md`
- `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md`
- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `Memory/Engineering_Journal/EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md`
- `Memory/Engineering_Journal/EJR-016_2026-08-10_REVIEW_TRACEABILITY_AND_PHASE1_COMPLETION_CONTROL.md`

---

## 19. Guiding Rule

**Know where every artifact belongs, know which repository state was last trusted, know what changed, and know how to recover without pretending uncertainty is completion.**

---

End of Document
