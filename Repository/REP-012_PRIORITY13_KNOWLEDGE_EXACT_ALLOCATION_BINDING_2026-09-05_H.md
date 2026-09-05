# REP-012 Priority-13 Knowledge Exact Allocation Binding — Unit 14

Date: 2026-09-05
Priority: `13 — Knowledge`
Parent allocation authority: `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` v1.0.13
Exact inventory source: `Repository/MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv`
Path-level allocation manifest: `Repository/REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_MANIFEST_2026-09-05_H.tsv`
State: `EXACT ALLOCATION EVIDENCE / CANONICAL REP-012 FOLD PENDING`

## Exact allocation boundary

Tracked Knowledge leaves: `50`

Sorted-path SHA-256:
`8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`

Every exact Transaction-A path is represented once in the path-level allocation manifest with:

- `allocation_state = ALLOCATED`;
- its observed physical role preserved from Transaction A;
- `authority_effect = NONE_BY_ALLOCATION`;
- `source_evidence = P13_TRANSACTION_A_EXACT_INVENTORY`.

`ALLOCATED != MAPPED ACTIVE AUTHORITY != REVIEWED != CANONICAL PROMOTION != CLOSED_FOR_PHASE_1`.

## Authority boundary

Allocation answers where the tracked path belongs. It does not decide whether the artifact is semantically authoritative, reviewed, relationship-valid, admitted to REP-001, or eligible for partition closure.

In particular:

- KNW-001..010 retain only their existing file/domain authority state;
- Learning executable/test/evidence surfaces receive no authority by allocation;
- Programming/Mathematics support surfaces receive no authority by allocation;
- REP-001 active admission remains a separate current P13 decision;
- REP-002 and REP-013 canonical folds remain separate control-plane debts;
- cross-layer REL-168..206 canonical REP-014 fold remains separate.

## Canonical synchronization requirement

Before Priority-13 control-plane closure, full REP-012 must safely bind this exact path-level allocation set while preserving its historical recovery/control content. Until that full fold is performed and exact-head validated:

`P13 EXACT KNOWLEDGE ALLOCATION = VERIFIED BY MANIFEST + ADDENDUM`

`CANONICAL REP-012 SYNCHRONIZATION = OPEN`

`PRIORITY 13 = OPEN`

---

End of Unit-14 REP-012 Allocation Binding
