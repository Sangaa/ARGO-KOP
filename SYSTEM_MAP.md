# ARGO KOP — SYSTEM MAP

---

## Current Relationship Model

```text
                              ARGO KOP
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
           Core              Governance          Repository
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                           Architecture
                                  │
          ┌───────────────┬───────┼────────┬───────────────┐
          │               │       │        │               │
      Lifecycle        Models  Interfaces Knowledge       Memory
          │               │       │        │               │
          └───────────────┴───────┼────────┴───────────────┘
                                  │
                              Runtime
                                  │
                               Engine
                                  │
                       ┌──────────┼──────────┐
                       │          │          │
                    Context    Reasoning  Coordination
                    / ENG-009  / ENG-001  / ENG-010
                       │          │          │
                       └──────────┼──────────┘
                                  │
                             Decision
                                  │
                                AI
                                  │
                              Services
                                  │
                           Intelligence
                                  │
                               Quality
                                  │
                              Release
                                  │
                                Logs
                                  │
                               Future
```

## Relationship Interpretation

This map is a **high-level relationship model**, not proof that every displayed relationship is currently verified.

Physical folder placement does not establish authority by itself.

Canonical authority remains distributed according to the applicable domain documents and repository governance.

## Current Audit Boundaries

The following relationships have been materially revalidated during the current connected-baseline audit:

- `Repository/REP-001_MASTER_INDEX.md` ↔ `Repository/REP-002_REPOSITORY_MAP.md`
- Lifecycle identity migration to `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`
- Architecture map identity separation: `Architecture/ARC_MAP.md` vs `ARC-001`
- Engine coordination boundary: `Engine/ENG-010_ENGINE_COORDINATION.md`
- GEM dependency/authority boundary: `Engine/ENG-011_MARITIME_GAME_ENGINE.md`

These are bounded results. Cross-layer and repository-wide relationship certification remains open.

## Evidence Rule

A relationship should be treated as verified only after the applicable evidence chain is completed:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read → Revalidate**

## Integrity State

**CONNECTED-BASELINE INTEGRITY VALIDATION / INTEGRITY WARNING**

The map intentionally does not claim global PASS. A relationship can remain unresolved even when both endpoint files exist.

---

End of System Map
