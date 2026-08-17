# ARGO KOP — REPOSITORY ALLOCATION, STATE & RECOVERY REGISTRY

Platform: ARGO KOP
Document ID: REP-012
Version: 1.0.9
Status: Active Control / Integrity Hold / Phase 1 Population In Progress
Category: Repository Control
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1
Last Audit Date: 2026-08-16

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

## 2. Design Analogy

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

## 3. Core Rule

**No build session should have to rediscover repository state from scratch.**

Before modifying an artifact, the worker should resolve its registry record and determine whether work is:

`NEW → REVIEW → REVALIDATE → MODIFY → RE-READ → LINK → CHECKPOINT`

or whether an existing checkpoint can safely be resumed.

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
- allocation state;
- dependency set;
- consumer set;
- unresolved scope;
- recovery checkpoint.

A path alone is not a sufficient identity.

A Document ID alone is not sufficient if its path or ownership has changed without recorded history.

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

A repository state is explicitly recorded for recovery purposes. Checkpoint classification determines whether it is trusted for technical, reviewed, provisional, known-good or recovery-only use.

`CLOSED_FOR_PHASE_1`

The artifact/domain has explicit Phase 1 closure evidence. This state must never be inferred.

`QUARANTINED`

Artifact is retained for evidence but excluded from normal promotion/use until resolved.

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
- Interfaces
- Plugins
- Templates
- Release
- Projects
- Docs
- Examples
- Assets
- Archive

A partition is not considered complete because its directory exists or selected files have been reviewed.

Each partition requires an explicit inventory and completion state.

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
Reconciliation State:
Next Review Trigger:
```

## 9. Initial Population Record

The registry is now beginning population through explicit work items. The following records establish the first control-plane allocation set; they do **not** claim repository-wide allocation completeness.

| Artifact | Domain | Allocation | Review | Relationship | Reconciliation | Checkpoint |
|---|---|---|---|---|---|---|
| REP-011 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| REP-012 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| REP-013 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| REP-014 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| REP-015 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| REP-016 | Repository | ALLOCATED | REVIEWED / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED / Integrity Hold | 2026-08-10 control-plane checkpoint |
| DIAG-001 | Assets/Diagrams | ALLOCATED | REVIEWED / Orientation Artifact | ACTIVE | PARTIAL / PROVENANCE LINKED | 2026-08-10 diagram artifact |

DIAG-001 consists of the paired artifacts:

- `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.svg`
- `Assets/Diagrams/DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.md`

The pair is an orientation/provenance artifact. It is not a source of canonical completion truth.

## 10. Control-Plane Reconciliation State

The allocation registry must not report an artifact as fully trusted merely because its path is allocated.

For the active control-plane set, reconcile:

1. `REP-011` — review and mutation evidence;
2. `REP-012` — allocation/state/recovery evidence;
3. `REP-013` — physical content inventory;
4. `REP-014` — relationship evidence;
5. `REP-015` — bootstrap and execution gates;
6. `REP-016` — current Phase 1 work state.

Controlled reconciliation states are:

`NOT_CHECKED`

`PARTIALLY_RECONCILED`

`RECONCILED`

`CONFLICT`

`REVALIDATION_REQUIRED`

`CLOSED`

The current control-plane state is **PARTIALLY RECONCILED / INTEGRITY HOLD**.

### Reconciliation Evidence Recorded 2026-08-10

The current control-plane review established the following evidence boundaries:

| Check | Result | Meaning |
|---|---|---|
| REP-011 ↔ REP-012 | PARTIAL | Review/evidence and allocation/recovery concepts are linked, but full per-artifact state synchronization is not yet populated. |
| REP-012 ↔ REP-013 | PARTIAL | Initial control-plane allocation exists, but repository-wide allocation/content reconciliation is incomplete. |
| REP-013 ↔ REP-014 | PARTIAL | Control-plane artifacts are represented in the relationship graph, but full repository relationship validation remains open. |
| REP-014 ↔ REP-015 | PARTIAL | Bootstrap/control-plane relationships are explicit; closure evidence remains open. |
| REP-015 ↔ REP-016 | RECONCILED WITHIN CURRENT SCOPE | Bootstrap order and Phase-1 queue are explicitly linked; this does not close Phase 1. |
| REP-016 ↔ REP-011..014 | PARTIAL | Queue state references the control-plane registries, while complete state-by-state reconciliation remains open. |
| DIAG-001 ↔ REP-012 | PROVENANCE LINKED | The diagram pair is allocated and identified; its values remain directional and must not be promoted to canonical completion metrics. |

**Important:** These results are scoped to the control-plane artifacts actually inspected. They are not a claim that the entire repository has been reconciled.

### Baseline Authority Reconciliation — 2026-08-14

Earlier versions of this registry carried Development Baseline `3.3.0`. That declaration conflicted with the current repository authority chain.

Current authoritative evidence establishes Development Baseline `3.2.1`:

- `Release/VERSION.md` declares `3.2.1` as the Development Baseline;
- `PROJECT_STATUS.md` records `3.2.1` and points to the release/version declaration as the baseline authority;
- `REP-001_MASTER_INDEX.md` records `3.2.1`;
- `REP-002_REPOSITORY_MAP.md` records `3.2.1`;
- `RUN-001_BOOT_SEQUENCE.md` records `3.2.1` as the Runtime development baseline.

Therefore this registry is reconciled to **3.2.1**. The prior `3.3.0` value is treated as a conflicting historical declaration, not as current authority.

This reconciliation does **not** imply Phase 1 completion or repository-wide semantic closure. Any artifact still declaring `3.3.0` remains an explicit follow-up target for authority/state reconciliation.

`RECONCILED` continues to mean that the required views agree within the recorded scope; it does not mean the entire repository or Phase 1 is complete.

## 11. Recovery Model

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

## 12. Checkpoint Rules

A checkpoint should record:

- repository commit SHA;
- timestamp;
- reason;
- scope covered;
- files/domains included;
- review state;
- reconciliation state;
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

## 13. Build Session Resume Protocol

A new model/session should begin with:

1. Load the current repository checkpoint.
2. Load `REP-012` allocation/state information.
3. Load `REP-011` review evidence.
4. Load `REP-013` content inventory for the working scope.
5. Load `REP-014` relationship state for the working scope.
6. Load `REP-015` bootstrap gates.
7. Load `REP-016` current work queue.
8. Compare current content identities with registered identities.
9. Identify dirty/revalidation-required/reconciliation-open artifacts.
10. Load open/unresolved scope.
11. Load relevant engineering journal entries.
12. Resume from the highest-confidence unfinished work item.

The session must not assume that an older handoff is current without checking repository state.

## 14. Mutation Protocol

For a material mutation:

`ALLOCATE → READ → VERIFY IDENTITY → VERIFY AUTHORITY → CHECK DEPENDENCIES → CHECK CONSUMERS → MUTATE → COMMIT → RE-READ → UPDATE REP-013 → UPDATE REP-014 → UPDATE REP-011 → UPDATE REP-012 → RECONCILE → CHECKPOINT IF WARRANTED`

If post-mutation re-read fails, the artifact remains `DIRTY` or `REVALIDATION_REQUIRED` and must not be marked complete.

## 15. Session-Safe Mutation Rule

When session termination is possible, every material mutation must be treated as a final persisted unit.

The worker must not accumulate several uncommitted logical changes and rely on conversation continuity.

Required sequence:

`ONE MATERIAL CHANGE → COMMIT → RE-READ → RECORD CHECKPOINT → ONLY THEN START NEXT CHANGE`

If the session ends immediately after a commit, the repository remains the source of truth and the next session can resume from the committed state.

A final response may summarize work, but the repository commit is the persistence boundary.

## 16. Recovery vs Revert

Recovery is not equivalent to automatic revert.

When a mutation is suspicious:

1. preserve the current evidence;
2. identify the pre-mutation checkpoint;
3. compare the states;
4. determine whether the mutation is wrong, incomplete or merely unverified;
5. choose retain, repair, revert or quarantine;
6. record the decision and evidence.

No destructive recovery action should occur solely because a file is marked uncertain.

## 17. Phase 1 Completion Control

For each partition/domain, the registry shall preserve:

- allocated artifacts;
- unallocated artifacts;
- reviewed artifacts;
- dirty artifacts;
- revalidation-required artifacts;
- reconciliation-open artifacts;
- quarantined artifacts;
- unresolved dependencies;
- unresolved consumers;
- recovery checkpoints.

A partition can only become `CLOSED_FOR_PHASE_1` after an explicit decision supported by `REP-011`, `REP-013`, `REP-014`, `REP-015`, `REP-016`, relevant indexes/maps, and domain evidence.

## 18. Machine-Readable Future

The current canonical specification is Markdown for human inspection and cross-model portability.

A future implementation may generate a machine-readable registry automatically from Git metadata and repository documents.

The future registry should support at minimum:

- deterministic artifact lookup;
- content identity comparison;
- dependency/consumer impact detection;
- stale-review detection;
- reconciliation-state detection;
- checkpoint lookup;
- session resume;
- recovery planning;
- Phase 1 completion reporting.

Automation must report evidence; it must not silently decide semantic authority.

## 19. Relationship to Control Plane

`REP-012` answers:

**Where is the artifact, what state is it in, and what checkpoint can recover it?**

`REP-011` answers:

**What review evidence exists for that artifact and what review scope was actually completed?**

`REP-013` answers:

**What files are physically inventoried under each folder?**

`REP-014` answers:

**What relationships connect the registered artifacts?**

`REP-015` answers:

**What evidence and execution gates must be passed before work resumes or mutates the repository?**

`REP-016` answers:

**What Phase 1 work remains explicitly open and in what execution state?**

The six systems are complementary:

`REP-012 = Allocation / State / Recovery`

`REP-011 = Review / Mutation / Evidence`

`REP-013 = Content Inventory`

`REP-014 = Relationship Graph`

`REP-015 = Bootstrap / Execution Gates`

`REP-016 = Phase 1 Work State`

## 20. Registry Integrity Rule

The control-plane records themselves are repository artifacts and must be registered, reviewed and checkpointed like any other critical artifact.

A registry entry cannot establish its own correctness merely by existing.

Material changes to any active control-plane artifact (`REP-011` through `REP-016`) require cross-registry reconciliation before affected claims are treated as closed.

## 21. Initial Deployment Rule

Because the repository does not yet have a fully populated allocation registry, the initial deployment status is:

`PARTIAL REGISTRY / RECONSTRUCTION REQUIRED`

Existing repository files must not be marked `ALLOCATED + REVIEWED + CHECKPOINTED` merely because they appear in indexes.

The registry shall be populated incrementally during Phase 1 review.

## 22. Control-Plane Checkpoint Synchronization — 2026-08-14

The active control plane has continued to mutate after the earlier 2026-08-10 allocation checkpoint. The registry therefore records the current reconciliation state explicitly rather than silently treating the older checkpoint as current.

| Artifact | Current Observed State | Synchronization Meaning |
|---|---|---|
| REP-011 | Current repository control-plane artifact | Review/mutation evidence remains subject to cross-registry reconciliation |
| REP-012 | Updated to v1.0.7 / baseline 3.2.1 | This commit becomes the next allocation-registry reconciliation checkpoint |
| REP-013 | Current repository content tree | Content inventory is synchronized for the currently inspected Runtime and control-plane scope |
| REP-014 | Current relationship registry | Relationship closure remains scoped and incomplete |
| REP-015 | Current bootstrap/control-plane artifact | Boot gates remain authoritative within current scope |
| REP-016 | Current Phase-1 queue | Open work remains governed by explicit queue state |

### Synchronization Rule

Because `REP-012` itself has now been changed, its resulting commit and content identity become the next checkpoint for control-plane reconciliation. Any subsequent material mutation to a listed control-plane artifact invalidates a claim of full synchronization until the affected record is re-read and reconciled again.

### Diagram Freshness

`DIAG-001` remains valid only as an orientation/provenance artifact relative to the source state from which it was generated. The baseline reconciliation above does not make its historical displayed values current; if values are consumed as status metrics, the diagram must be regenerated or explicitly superseded.

## 23. Relationship and Current Review Trace

The current review cycle records these tested paths:

- `RUN-001 → PROJECT_BOOTSTRAP → REP-001 → REP-002` — boot/authority documentation verified;
- `RUN-010 → ENG-006 → SRV-009` — documentation relationship verified, executable consumer proof still open;
- `REP-001 ↔ REP-002` — active inventory/path agreement verified within inspected scope;
- `REP-013 ↔ Specifications/01-Knowledge-Organization.md` — canonical physical path verified;
- `PR #1 / PR #3` — stale verification branches closed without merge;
- `PR #9` — prototype and integration evidence passed, candidate closed without merge.

Tests recorded in the associated REP-020 evidence deltas remain cumulative; this section is a navigation bridge, not a replacement for their detailed evidence.

## 24. Runtime Allocation Reconciliation — 2026-08-15

The current Runtime inventory and relationship graph are now synchronized for the inspected Cognitive Loop scope. The allocation registry records the physical Runtime artifacts as mapped/reviewed within scope while keeping the broader repository allocation state open.

| Artifact | Domain | Allocation | Review | Relationship | Reconciliation | Checkpoint |
|---|---|---|---|---|---|---|
| RUN-011 | Runtime | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |
| RUN-012 | Runtime | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |
| RUN-013 | Runtime | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |
| RUN-014 | Runtime | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |
| RUN-015 | Runtime | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |
| Runtime/Prototype/PROTOTYPE_INTEGRATION_CONTRACT.md | Runtime/Prototype | MAPPED | RE_READ / Integrity Hold | ACTIVE | PARTIALLY_RECONCILED | P75 / current main |

Evidence boundary:

- `REP-001` and `REP-002` enumerate the same Runtime inventory.
- `REP-013` now enumerates the physical Runtime inventory.
- `REP-014` now records the corresponding relationship set `REL-055..060`.
- `REP-011` records the review/re-read evidence for the affected mutations.

These records do not establish executable Runtime authority, Phase 1 closure, or repository-wide allocation completeness.

The affected control-plane path is now:

`REP-001/REP-002 → REP-013 → REP-014 → REP-011 → REP-012`

with the overall reconciliation state remaining:

`PARTIALLY RECONCILED / INTEGRITY HOLD`

## 25. P267 Services Identity Allocation Reconciliation — 2026-08-16

A current-main identity correction was made in `REP-013` for `SRV-010`:

`SRV-010_SERVICE_REFERENCE.md` is the canonical physical identity within the inspected scope.

The prior inventory token `SRV-010_SERVICE_CATALOG.md` was an identity mismatch, not a second service artifact. Direct current-main read-back of the canonical reference and Services folder status confirm the corrected identity.

Allocation disposition:

- `SRV-010` remains `ALLOCATED` in the Services partition;
- its review/reconciliation state remains bounded and under Integrity Hold;
- physical identity correction does not establish implementation or runtime execution;
- the broader Services partition remains open.

Evidence:

`REP-013 v1.1.0`, commit `ec36514b503db3857f57cefb9414512bfb866a48`, content SHA `638d47a34f87acff744ba09b9f0b6730c8863e48`.

Checkpoint:

`Repository/REP-020_SESSION_DELTA_2026-08-16_P267.md`

This update does not close the control plane.

## 26. P269 Services Inventory Allocation Reconciliation — 2026-08-16

`REP-013` now contains exact current-main physical identities for the ten declared Services artifacts rather than wildcard placeholders.

The current physical allocation evidence is:

- `SRV-001_SERVICE_ARCHITECTURE.md`
- `SRV-002_REPOSITORY_SERVICE.md`
- `SRV-003_MEMORY_SERVICE.md`
- `SRV-004_KNOWLEDGE_SERVICE.md`
- `SRV-005_VALIDATION_SERVICE.md`
- `SRV-006_SEARCH_SERVICE.md`
- `SRV-007_LOGGING_SERVICE.md`
- `SRV-008_INDEX_SERVICE.md`
- `SRV-009_UPDATE_SERVICE.md`
- `SRV-010_SERVICE_REFERENCE.md`

Allocation disposition remains `ALLOCATED` for the Services partition within the inspected scope. Exact physical identity does not promote review, implementation, runtime execution, or partition closure.

Evidence:

`REP-013 v1.1.1`, commit `f5e0e3f709442ba66861a75b07405bbd554be774`, content SHA `e4cbcaba859554485f6c659d103118506629f824`.

The Services folder status remains `INTEGRITY HOLD`, and the four previously identified metadata-baseline gaps for `SRV-003`, `SRV-006`, `SRV-007`, and `SRV-008` remain unresolved rather than being inferred from the repository baseline.

This update does not close the control plane.

## 27. P308 Control-Plane Binding Reconciliation — 2026-08-17

P307 bound `REP-011` to the current reconciliation evidence while preserving its complete prior content. P308 performs the corresponding minimum binding for `REP-012`.

Current binding evidence:

- `REP-012` pre-mutation blob: `5b51e0b468e479842d7d83468e8e7c20a06ec1b1`;
- current session evidence: `P306` and `P307`;
- P305 remains the evidence delta that first distinguished physical currentness from internal binding lag.

`REP-012` is **PRESENT / CURRENT with INTERNAL BINDING LAG** within the inspected control-plane scope. The historical 2026-08-16 audit date remains historical provenance and is not retroactively converted into a new audit date merely by this binding section.

This section records allocation/checkpoint synchronization evidence only. It does not mark `REP-012` `CLOSED_FOR_PHASE_1`, `RECONCILED`, or globally current across all dependencies and consumers.

Next required state transition:

`REP-011 + REP-012 BOUND → REP-013/014/015/016/020 RECONCILIATION → EXPLICIT PRIORITY 1 CLOSURE REVIEW`

## P353 Current Control-Plane Closure Synchronization — 2026-08-17

The explicit Priority-1 closure decision is persisted in:

`Repository/REP-020_SESSION_DELTA_2026-08-17_P350.md`

The current authoritative queue in `REP-016` now records:

`Priority 1 = CLOSED / RING-0 CONTROL-PLANE RECONCILED WITHIN CURRENT INSPECTED SCOPE`

Current allocation/control-plane disposition:

`REP-012 = RECONCILED WITHIN RING-0 CONTROL-PLANE CLOSURE SCOPE`

This is not `CLOSED_FOR_PHASE_1` for the whole repository. It records that the allocation/state/recovery view is reconciled for the Ring-0 closure decision.

The historical `PARTIALLY_RECONCILED / INTEGRITY HOLD` statements above remain preserved as historical evidence; P353 is the current closure-synchronization disposition.

No executable SRV-009 proof, global graph closure, exhaustive repository-wide identity cleanliness, controlled mutation harness closure, or final Boot PASS is claimed.

---

End of Document
