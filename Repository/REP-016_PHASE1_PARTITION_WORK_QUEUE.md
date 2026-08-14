# REP-016 — PHASE 1 PARTITION WORK QUEUE

Platform: ARGO KOP  
Document ID: REP-016  
Version: 1.0.4  
Status: Active / Phase 1 Open / Integrity Hold  
Development Baseline: 3.2.1  
Last Audit: 2026-08-14

## Purpose

Convert the repository control plane into an ordered, recoverable Phase-1 execution queue.

This file does not replace REP-011 through REP-015. It coordinates them and records the executable scope. Future control-plane candidates recorded in `ROADMAP.md` are not automatically queue items.

## Work-State Vocabulary

```text
NOT_STARTED
INVENTORYING
ALLOCATING
REVIEWING
RELATIONSHIP_VALIDATION
RECONCILIATION
READY_FOR_CLOSURE_REVIEW
CLOSED_FOR_PHASE_1
BLOCKED
QUARANTINED
```

## Queue State Semantics

A queue state is an execution claim, not a semantic correctness claim.

Every state change must be supported by current repository evidence and, where material, synchronized with the applicable control-plane registries.

## Ring Alignment

Phase-1 queue execution follows the ring-based progression defined by REP-015. Rings are bounded execution scopes, not new authority layers.

```text
RING 0 — CONTROL PLANE
        ↓
RING 1 — AUTHORITY CORE
        ↓
RING 2 — EXECUTION FOUNDATION
        ↓
RING 3 — KNOWLEDGE & DOMAIN
        ↓
RING 4 — OPERATIONAL SURFACES
        ↓
RING 5 — RELEASE & EVOLUTION
```

The queue must record the active ring for any material work item. A partition may not be promoted solely because its predecessor has many completed records.

### Ring Entry Gate

Before entering a new ring, verify:

- predecessor exit evidence;
- current repository HEAD;
- affected authority artifacts;
- cross-ring dependencies and consumers;
- unresolved scope;
- recovery checkpoint.

If evidence is insufficient, retain the item in its current state or mark `REVALIDATION_REQUIRED` rather than promoting it.

### Cross-Ring Impact Rule

If a mutation crosses ring boundaries:

`DETECT IMPACT → IDENTIFY AFFECTED ARTIFACTS → VERIFY AUTHORITY → REVIEW RELATIONSHIPS/CONSUMERS → MUTATE → RECONCILE BOTH RINGS`

A queue item is not closed while a material cross-ring impact remains unresolved.

## Control-Plane Reconciliation Gate

The first executable unit remains **Repository Control Plane reconciliation**.

Current control-plane evidence has advanced but is not fully closed. The synchronized working set is:

```text
REP-011 Review/Evidence
        ↕
REP-012 Allocation/State/Recovery
        ↕
REP-013 Content Inventory
        ↕
REP-014 Relationships
        ↕
REP-015 Bootstrap Rules
        ↕
REP-016 Execution State
        ↕
REP-020 Impact Matrix / Lookup Evidence
```

Required reconciliation states are:

`NOT_CHECKED → PARTIALLY_RECONCILED → RECONCILED`

or, when evidence conflicts:

`CONFLICT / REVALIDATION_REQUIRED`

No reconciliation state may be promoted by assumption.

### Visual Artifact Synchronization Gate

`DIAG-001` is a registered orientation/provenance artifact and is not a canonical completion source.

When the source state represented by `DIAG-001` materially changes:

`DIAG-001 → REVALIDATION_REQUIRED`

until the diagram and metadata are regenerated or explicitly superseded.

The queue may use the diagram for orientation only. Canonical decisions must resolve to `REP-011` through `REP-016`, `REP-020`, and applicable domain authority.

## Partition Queue

| Priority | Partition / Workstream | Current State | Required Entry Point | Closure Authority |
|---:|---|---|---|---|
| 1 | Repository Control Plane | RECONCILIATION | REP-011..016 + REP-020 | REP-011 + explicit closure decision |
| 2 | Executable relationship proof | RELATIONSHIP_VALIDATION | RUN-010 → ENG-006 → SRV-009 | REP-011/014 + Runtime/Engine/Service evidence |
| 3 | Exhaustive duplicate-ID audit | RELATIONSHIP_VALIDATION | REP-001 + full current tree | REP-011/014 + explicit identity decisions |
| 4 | Bidirectional critical graph validation | RELATIONSHIP_VALIDATION | REP-014 + critical edges | REP-014 + endpoint evidence |
| 5 | Core | INVENTORYING | Core/_FOLDER_STATUS.md + REP-013 | Domain authority + REP-011 |
| 6 | Governance | INVENTORYING | Governance/_FOLDER_STATUS.md + REP-013 | Governance authority + REP-011 |
| 7 | Architecture | RELATIONSHIP_VALIDATION | ARC_MAP + ARC-001..011 | Architecture authority + REP-011/014 |
| 8 | Runtime | RELATIONSHIP_VALIDATION | Runtime/_FOLDER_STATUS.md + REP-013 | Runtime authority + REP-011/014 |
| 9 | Interfaces | RELATIONSHIP_VALIDATION | INTF-001/004/006/010 | Interface authority + REP-011/014 |
| 10 | Models | RELATIONSHIP_VALIDATION | MOD-001/002/003/004/011 | Model authority + REP-011/014 |
| 11 | Knowledge | INVENTORYING | KNW-002/003/004/008/009 | Knowledge authority + REP-011/014 |
| 12 | Engine | RELATIONSHIP_VALIDATION | ENG-002/004/006/007 | Engine authority + REP-011/014 |
| 13 | Services | INVENTORYING | SRV catalog + exact file enumeration | Service authority + REP-011/014 |
| 14 | Plugins | RELATIONSHIP_VALIDATION | PLG-001 + plugin inventory | Plugin authority + REP-011/014 |
| 15 | Memory | INVENTORYING | Engineering Journal + content tree | Memory authority + REP-011 |
| 16 | Specifications | INVENTORYING | SPEC-001 + exact enumeration | Specification authority + REP-011/014 |
| 17 | Templates | NOT_STARTED | Exact physical enumeration | Template authority + REP-011 |
| 18 | Release | NOT_STARTED | Exact physical enumeration | Release authority + REP-011/014 |
| 19 | Projects | NOT_STARTED | Exact physical enumeration | Project authority + REP-011/014 |
| 20 | Docs | NOT_STARTED | Exact physical enumeration | Documentation authority + REP-011 |
| 21 | Examples | NOT_STARTED | Exact physical enumeration | Example scope decision + REP-011 |
| 22 | Assets | INVENTORYING | `Assets/Diagrams/` + exact physical enumeration | Asset scope decision + REP-011 |
| 23 | Archive | NOT_STARTED | Exact physical enumeration + provenance | Archive policy + REP-011 |

## DIAG-001 Queue Record

| Artifact | Source | Inventory | Allocation | Relationship | Review | Queue Role |
|---|---|---|---|---|---|---|
| DIAG-001 SVG | REP-012-derived | REP-013 | REP-012 | REP-014 | REP-011 | Orientation |
| DIAG-001 Metadata | REP-012-derived | REP-013 | REP-012 | REP-014 | REP-011 | Provenance / interpretation |

The pair is not a Phase-1 closure artifact. Its purpose is to help a new session understand repository state quickly while preserving the canonical-source boundary.

## Execution Contract

For every partition:

```text
ENUMERATE
  ↓
ALLOCATE
  ↓
VERIFY IDENTITY
  ↓
VERIFY AUTHORITY
  ↓
REVIEW CURRENT CONTENT
  ↓
COMPARE LAST-REVIEWED IDENTITY
  ↓
VALIDATE DEPENDENCIES
  ↓
VALIDATE CONSUMERS
  ↓
REGISTER RELATIONSHIPS
  ↓
RECONCILE INDEX / MAP / STATUS
  ↓
CHECKPOINT
  ↓
RE-READ
  ↓
CLOSURE REVIEW OR KEEP OPEN
```

## Material Mutation Contract

A material mutation is one persistence unit:

`ONE MATERIAL CHANGE → COMMIT → RE-READ → RECORD EVIDENCE → NEXT CHANGE`

The conversation is not the persistence boundary.

If a session ends after a commit but before all applicable registry synchronization is complete, the item remains open and the next session must detect and reconcile the partial state.

## Evidence Freshness Gate

Before resuming an existing queue item, compare:

- current repository HEAD;
- current content identity;
- last reviewed identity;
- latest mutation evidence;
- relevant dependency/consumer changes;
- new methodological or contradictory evidence.

A historical queue state may be preserved as history while requiring current revalidation.

## Recovery Rule

Every queue item must be resumable from repository evidence alone.

A session interruption must not require reconstructing progress from conversation history.

At minimum the next session needs:

- current HEAD;
- queue state;
- active ring;
- affected partition;
- completed work item;
- remaining work item;
- relevant registry entries;
- latest checkpoint;
- unresolved scope.

## Anti-Loop Rule

If a partition is repeatedly reviewed without changing its evidence state, stop repeating the same pass.

Record:

- what was already verified;
- why it remains open;
- the missing evidence required;
- the next concrete action.

## Anti-Premature-Closure Rule

No queue item may be moved to `CLOSED_FOR_PHASE_1` because:

- all visible files were read once;
- a previous model declared it complete;
- a folder status says complete without supporting evidence;
- an index contains the files;
- or the latest commit is technically valid.

Closure requires evidence across the relevant control-plane registries.

## Active Control-Plane Artifacts

The following are now active control-plane work artifacts and are not future proposals:

- `REP-011` Review / Mutation / Evidence Ledger
- `REP-012` Allocation / State / Recovery Registry
- `REP-013` Content Inventory
- `REP-014` Relationship Registry
- `REP-015` Bootstrap / Execution Gates
- `REP-016` Phase-1 Work Queue
- `REP-020` Dependency & Consumer Impact Matrix

`REP-020` remains provisional and non-authoritative, but it is an active evidence/lookup surface for the current Phase-1 work.

## Future Control-Plane Candidates

The following remain **future candidates only** and are governed by `ROADMAP.md`:

- `REP-017` Mutation Registry
- `REP-018` Repository Reconciliation Register
- `REP-019` Repository Checkpoint Registry
- `REP-021` Artifact Lifecycle State Machine
- `REP-022` Evidence Confidence / Trust Classification
- `REP-023` Unified Control-Plane Schema

They must not be treated as implemented merely because they are named here.

Promotion remains:

`Proposal → Evidence → Design Review → Compatibility Check → Explicit Decision → Implementation → Re-read → Registry Synchronization`

## Current Queue Decision — 2026-08-14

The control plane has passed a significant evidence milestone but remains open.

Completed/reconciled within current scope:

- obsolete PR #1 and PR #3 verification paths closed;
- PR #9 candidate evidence passed Prototype + canonical acceptance + 80/80 Integration;
- REP-012 baseline authority reconciled to 3.2.1;
- REP-013 canonical Specification path reconciled;
- REP-011 updated with current review evidence;
- REP-014 updated with current relationship-cycle evidence;
- REP-020 updated to v0.1.8.

Next highest-strength work items:

1. **Executable consumer proof** for `RUN-010 → ENG-006 → SRV-009`;
2. **Exhaustive internal-ID/duplicate audit** with explicit owner/authority decisions;
3. **Bidirectional critical-edge validation**;
4. **Controlled mutation/reconciliation harness**;
5. **Final Boot Verification** only after the first four are closed or explicitly bounded.

The current active execution ring remains **RING 0 — CONTROL PLANE** until the control-plane reconciliation gate is explicitly satisfied.

No broad repository completion claim is permitted from this queue alone.

---

End of Document