# EJR-018 — REPOSITORY CONTENT AND RELATIONSHIP REGISTRIES

Date: 2026-08-10  
Status: Recorded / Phase 1 Open  

## Trigger

The repository needs more than a folder map. A recoverable operating system requires three complementary views:

1. allocation/state/recovery;
2. exact folder → file content inventory;
3. file → file relationship registry.

## Implemented

Created:

- `Repository/REP-013_REPOSITORY_CONTENT_TREE.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`

These complement:

- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`

## Operating Model

```text
REP-002  = WHERE / DOMAIN STRUCTURE
REP-013  = WHAT FILES ARE THERE
REP-014  = HOW FILES RELATE
REP-011  = WHAT WAS REVIEWED + EVIDENCE
REP-012  = STATE + ALLOCATION + CHECKPOINT + RECOVERY
```

Together they form a repository control plane rather than five competing inventories.

## Important Boundary

REP-013 is not a declaration that all folders or files are complete.
REP-014 is not a declaration that every relationship is verified.
REP-011 is not authority over domain semantics.
REP-012 is not authority over file content.

Each registry has a distinct function.

## Learning

The system should not require a future model to reconstruct repository topology from narrative conversation. The repository must contain enough machine-readable structure for a new session to discover:

- where artifacts are;
- which artifacts exist;
- what they connect to;
- what has been reviewed;
- what changed;
- what remains open;
- and where recovery can begin.

## Phase 1 Rule

No folder is considered complete until its content inventory, allocation state, review state, and material relationship coverage are reconciled and explicitly closed.

Phase 1 remains OPEN.

---

End of Entry
