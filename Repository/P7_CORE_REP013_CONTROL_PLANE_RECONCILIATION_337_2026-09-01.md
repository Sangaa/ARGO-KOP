# P7 CORE REP-013 CONTROL-PLANE RECONCILIATION — P337

Date: 2026-09-01
Priority: 7 — Core
State: IN_PROGRESS / REP-013 SUBGATE CANDIDATE

## Finding
P336 reconciled the exact local Core inventory to 18 top-level files, but current `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` still recorded a stale Core subset beginning at CORE-003. Direct current-path reads confirmed the divergence.

## Repair scope
P337 reconciles only the REP-013 `### Core/` physical content inventory to the exact current Core directory, while preserving artifact authority boundaries:
- `CORE-000_PLATFORM_IDENTITY.md` remains physical legacy / noncanonical / superseded;
- `CORE-000A_PLATFORM_GLOSSARY.md` is represented as current physical Core inventory;
- `CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` is represented as current physical Core inventory;
- no physical listing promotes canonical authority.

A direct integration regression compares the REP-013 Core block to the exact top-level `Core/` files.

## Scope boundary
This does not reconcile REP-001 or REP-002, does not settle GOV-006 naming/path disposition, does not validate all Core consumers/dependencies, and does not certify Core or close Priority 7.

## Execution note
The P337 session incurred an entry-order defect: its first Matrix write preceded live-main rediscovery. The defect and subsequent redundant Matrix-only commit are retained in the P337 Mutation Matrix. Compare evidence proved no protected functional target changed before the corrected pre-functional gate was established.
