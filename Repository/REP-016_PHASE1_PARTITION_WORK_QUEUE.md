# REP-016 — PHASE 1 PARTITION WORK QUEUE

Platform: ARGO KOP  
Document ID: REP-016  
Version: 1.1.6  
Status: Active / Phase 1 Open / Integrity Hold  
Development Baseline: 3.2.1  
Last Audit: 2026-08-14

## Purpose

Convert the repository control plane into an ordered, recoverable Phase-1 execution queue. This file coordinates REP-011 through REP-015 and the provisional REP-020 evidence surface; it does not replace their authority.

## Active Ring

**RING 0 — CONTROL PLANE**

No promotion to a later ring is allowed until predecessor exit evidence, affected authority artifacts, dependencies/consumers, unresolved scope, and a recovery checkpoint are verified.

## Partition Queue

| Priority | Partition / Workstream | Current State | Required Entry Point | Closure Authority |
|---:|---|---|---|---|
| 1 | Repository Control Plane reconciliation | RECONCILIATION | REP-011..016 + REP-020 | REP-011 + explicit closure decision |
| 2 | Exhaustive duplicate-ID audit | RELATIONSHIP_VALIDATION | REP-001 + full current tree/content | REP-011/014 + explicit identity decisions |
| 3 | Executable relationship proof | RELATIONSHIP_VALIDATION | RUN-010 → ENG-006 → SRV-009 | REP-011/014 + Runtime/Engine/Service evidence |
| 4 | Bidirectional critical graph validation | RELATIONSHIP_VALIDATION | REP-014 + critical edges | REP-014 + endpoint evidence |
| 5 | Controlled mutation/reconciliation harness | NOT_STARTED | Current control-plane contract | REP-011/014 + mutation evidence |
| 6 | CI ↔ impact-matrix observability | NOT_STARTED | REP-020 + workflow evidence | REP-011/020 evidence review |
| 7 | Core | INVENTORYING | Core/_FOLDER_STATUS.md + REP-013 | Domain authority + REP-011 |
| 8 | Governance | INVENTORYING | Governance/_FOLDER_STATUS.md + REP-013 | Governance authority + REP-011 |
| 9 | Architecture | RELATIONSHIP_VALIDATION | ARC_MAP + ARC-001..011 | Architecture authority + REP-011/014 |
| 10 | Runtime | RELATIONSHIP_VALIDATION | Runtime/_FOLDER_STATUS.md + REP-013 | Runtime authority + REP-011/014 |
| 11 | Interfaces | RELATIONSHIP_VALIDATION | INTF-001/004/006/010 | Interface authority + REP-011/014 |
| 12 | Models | RELATIONSHIP_VALIDATION | MOD-001/002/003/004/011 | Model authority + REP-011/014 |
| 13 | Knowledge | INVENTORYING | KNW-002/003/004/008/009 | Knowledge authority + REP-011/014 |
| 14 | Engine | RELATIONSHIP_VALIDATION | ENG-002/004/006/007 | Engine authority + REP-011/014 |
| 15 | Services | INVENTORYING | SRV catalog + exact file enumeration | Service authority + REP-011/014 |
| 16 | Plugins | RELATIONSHIP_VALIDATION | PLG-001 + plugin inventory | Plugin authority + REP-011/014 |
| 17 | Memory | INVENTORYING | Engineering Journal + content tree | Memory authority + REP-011 |
| 18 | Specifications | INVENTORYING | SPEC-001 + exact enumeration | Specification authority + REP-011/014 |
| 19 | Templates | NOT_STARTED | Exact physical enumeration | Template authority + REP-011 |
| 20 | Release | NOT_STARTED | Exact physical enumeration | Release authority + REP-011/014 |
| 21 | Projects | NOT_STARTED | Exact physical enumeration | Project authority + REP-011/014 |
| 22 | Docs | NOT_STARTED | Exact physical enumeration | Documentation authority + REP-011 |
| 23 | Examples | NOT_STARTED | Exact physical enumeration | Example scope decision + REP-011 |
| 24 | Assets | INVENTORYING | Assets/Diagrams + exact physical enumeration | Asset scope decision + REP-011 |
| 25 | Archive | NOT_STARTED | Exact physical enumeration + provenance | Archive policy + REP-011 |

## Execution Contract

For every partition:

```text
ENUMERATE → ALLOCATE → VERIFY IDENTITY → VERIFY AUTHORITY → REVIEW CONTENT
→ COMPARE LAST-REVIEWED IDENTITY → VALIDATE DEPENDENCIES → VALIDATE CONSUMERS
→ REGISTER RELATIONSHIPS → RECONCILE INDEX/MAP/STATUS → CHECKPOINT → RE-READ
→ CLOSURE REVIEW OR KEEP OPEN
```

Material mutation remains:

`ONE MATERIAL CHANGE → COMMIT → RE-READ → RECORD EVIDENCE → NEXT CHANGE`

## Search Evidence Contract

For every material search result, positive or negative, use two materially different retrieval methods before making an absence or current-state claim.

For material negative results:

`SEARCH-A → INDEPENDENT SEARCH-B → CONFIRM ABSENCE OR RECOVER → ANALYZE FAILURE → READ CURRENT AUTHORITY → RECORD`

For material positive results:

`SEARCH RESULT → CAPTURE REF/SHA → COMPARE CURRENT REF → RE-READ CURRENT AUTHORITY → FRESH/STALE CLASSIFICATION → USE/DISCARD`

A negative result is never an absence claim from one search. A positive result is never current-main evidence until its ref/SHA is reconciled with the current authoritative ref.

## P37 Evidence

P37 applied the dual-search discipline to `MOD-003_DOCUMENT_MODEL.md`. A broad search returned the artifact at an older commit, while a materially different targeted filename search did not return it. Direct current-main retrieval recovered the file. The stale search result was compared with current main; the exact internal index-refresh mechanism remained unproven and was not asserted.

## P38 — Search Freshness + Current Service Namespace Revalidation

P38 re-applied the rule to the Service namespace using two materially different searches:

1. `Document ID: SRV-` search: broad semantic/identity-oriented retrieval.
2. `Services/SRV-` search: path-oriented retrieval.

Both search result sets were pinned to commit `601b07e829af2f29aebefe92591fc352f1118954`, not current `main`. Therefore neither search result set was accepted as current-main evidence without reconciliation.

A direct current-main directory enumeration of `Services/` was then performed. It recovered exactly ten active Service artifacts `SRV-001` through `SRV-010`, plus non-SRV support files. This establishes the current filename namespace within the Services directory. It does not, by itself, close internal Document-ID uniqueness across the repository.

A commit comparison from the search-result ref to current main (`ac476465dfde3c9e52526eb20b0c3eb7f11dacea`) showed current main is **5 commits ahead / 0 behind**. The changed files in that interval are control/evidence records only; no Service artifact change was identified in that comparison. The internal search/index refresh mechanism remains unproven.

P38 therefore classifies the two search results as **STALE SEARCH EVIDENCE**, the current directory enumeration as **CURRENT AUTHORITATIVE INVENTORY EVIDENCE**, and the Service filename namespace as **10 active artifacts / no active filename duplicate observed**.

## P38 Search-Failure Learning Decision

P38 does not promote a new permanent platform lesson. `MEM-009` already contains the validated rules for independent negative-search confirmation and current-ref freshness reconciliation. P38 adds provenance and confirms those rules on a second namespace, but introduces no materially new principle.

## Current Queue Decision — P38

1. **Exhaustive duplicate-ID audit** remains first and open. Filename uniqueness is not internal-ID uniqueness.
2. Current Service inventory is revalidated as a bounded current-tree fact and should be used as the Service-side input to REP-020/REP-011 reconciliation.
3. **Executable consumer proof** for `RUN-010 → ENG-006 → SRV-009` remains next after identity evidence is sufficiently bounded.
4. Bidirectional critical-edge validation remains after executable proof.
5. Controlled mutation/reconciliation harness follows graph closure.
6. CI-to-impact-matrix observability follows mutation evidence.
7. Final Boot Verification remains last and blocked by unresolved identity/relationship scope.

## Recovery / Anti-Loop / Anti-Premature-Closure

Every item must be resumable from repository evidence alone. Repeated review without new evidence must stop and record the missing evidence. No item may be closed merely because files were read, an index lists them, a previous model declared completion, or CI passed.

## Current Checkpoint

P38 evidence is recorded in:

`Repository/REP-020_SESSION_DELTA_2026-08-14_P38.md`

The session closure record is created only after the P38 mutation and its audit evidence are verified.

Next session resumes at **Priority 2 — Exhaustive duplicate-ID audit**, with P31/P36/P37/P38 search/reconciliation evidence preserved.

---

End of Document