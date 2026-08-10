# REP-016 — PHASE 1 PARTITION WORK QUEUE

Platform: ARGO KOP  
Document ID: REP-016  
Version: 1.0.0  
Status: Active / Phase 1 Open  
Development Baseline: 3.2.1  
Last Audit: 2026-08-10

## Purpose

Convert the repository control plane into an ordered, recoverable Phase-1 execution queue.

This file does not replace REP-011 through REP-015. It coordinates them.

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

## Partition Queue

| Priority | Partition | Current State | Required Entry Point | Closure Authority |
|---:|---|---|---|---|
| 1 | Repository Control Plane | RECONCILIATION | REP-011..015 | REP-011 + explicit closure decision |
| 2 | Core | INVENTORYING | Core/_FOLDER_STATUS.md + REP-013 | Domain authority + REP-011 |
| 3 | Governance | INVENTORYING | Governance/_FOLDER_STATUS.md + REP-013 | Governance authority + REP-011 |
| 4 | Architecture | RELATIONSHIP_VALIDATION | ARC_MAP + ARC-001..011 | Architecture authority + REP-011/014 |
| 5 | Runtime | INVENTORYING | Runtime/_FOLDER_STATUS.md + REP-013 | Runtime authority + REP-011 |
| 6 | Interfaces | RELATIONSHIP_VALIDATION | INTF-001/004/006/010 | Interface authority + REP-011/014 |
| 7 | Models | RELATIONSHIP_VALIDATION | MOD-001/002/003/004/011 | Model authority + REP-011/014 |
| 8 | Knowledge | INVENTORYING | KNW-002/003/004/008/009 | Knowledge authority + REP-011/014 |
| 9 | Engine | RELATIONSHIP_VALIDATION | ENG-002/004/006/007 | Engine authority + REP-011/014 |
| 10 | Services | INVENTORYING | SRV catalog + exact file enumeration | Service authority + REP-011/014 |
| 11 | Plugins | RELATIONSHIP_VALIDATION | PLG-001 + plugin inventory | Plugin authority + REP-011/014 |
| 12 | Memory | INVENTORYING | Engineering Journal + content tree | Memory authority + REP-011 |
| 13 | Specifications | INVENTORYING | SPEC-001 + exact enumeration | Specification authority + REP-011/014 |
| 14 | Templates | NOT_STARTED | Exact physical enumeration | Template authority + REP-011 |
| 15 | Release | NOT_STARTED | Exact physical enumeration | Release authority + REP-011/014 |
| 16 | Projects | NOT_STARTED | Exact physical enumeration | Project authority + REP-011/014 |
| 17 | Docs | NOT_STARTED | Exact physical enumeration | Documentation authority + REP-011 |
| 18 | Examples | NOT_STARTED | Exact physical enumeration | Example scope decision + REP-011 |
| 19 | Assets | NOT_STARTED | Exact physical enumeration | Asset scope decision + REP-011 |
| 20 | Archive | NOT_STARTED | Exact physical enumeration + provenance | Archive policy + REP-011 |

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

## Recovery Rule

Every queue item must be resumable from repository evidence alone.

A session interruption must not require reconstructing progress from conversation history.

At minimum the next session needs:

- current HEAD;
- queue state;
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

## Current Queue Decision

The next executable unit is **Repository Control Plane reconciliation**, followed by the highest-impact canonical domain whose inventory and relationships can be resolved without inventing missing evidence.

No broad repository completion claim is permitted from this queue alone.

---

End of Document
