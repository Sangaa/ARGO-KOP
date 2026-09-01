# REP-012 CORE ALLOCATION ADDENDUM — TRANSACTION W

Date: 2026-09-01
Applies to: `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
Parent authority: `REP-012 v1.0.10 / Active Control / Integrity Hold / Phase 1 Population In Progress`
Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
State: `BOUNDED CORE ALLOCATION POPULATION / NON-REPLACING / PRIORITY 7 OPEN`

## Authority boundary

This addendum records bounded Core allocation evidence under REP-012's allocation/state model. It does not replace REP-012, does not change REP-012's repository-wide population state, and does not claim that allocation equals review, relationship validation, canonical authority, certification, or Phase-1 closure.

REP-012 defines `ALLOCATED` as a valid owner/domain/path assignment. REP-013 requires every known file to have an allocation record before a folder may become `CLOSED_FOR_PHASE_1`.

## Exact current Core allocation set

Direct current repository enumeration establishes 18 top-level files in `Core/`. `Core/Core.md` independently lists the other 17 members and explicitly excludes itself by design.

| Path | Domain | Allocation | Identity / authority boundary |
|---|---|---|---|
| `Core/ARGO_KERNEL.md` | Core | ALLOCATED | current Core artifact; no new authority promotion |
| `Core/CORE-000_PLATFORM_ARCHITECTURE.md` | Core | ALLOCATED | active canonical CORE-000 architecture owner |
| `Core/CORE-000_PLATFORM_IDENTITY.md` | Core | ALLOCATED | physical provenance only; `Canonical: No / Legacy / Superseded`; not second active CORE-000 authority |
| `Core/CORE-000A_PLATFORM_GLOSSARY.md` | Core | ALLOCATED | current glossary artifact; allocation only |
| `Core/CORE-001_ARGO_MANIFEST.md` | Core | ALLOCATED | current manifest artifact; allocation only |
| `Core/CORE-002_ARGO_IDENTITY.md` | Core | ALLOCATED | active platform-identity owner |
| `Core/CORE-003_CONSTITUTION.md` | Core | ALLOCATED | constitutional authority unchanged |
| `Core/CORE-004_CORE_PRINCIPLES.md` | Core | ALLOCATED | current principles artifact; allocation only |
| `Core/CORE-005_COGNITIVE_MODEL.md` | Core | ALLOCATED | current cognitive-model artifact; allocation only |
| `Core/CORE-006_SYSTEM_PHILOSOPHY.md` | Core | ALLOCATED | current philosophy artifact; allocation only |
| `Core/CORE-007_DESIGN_PRINCIPLES.md` | Core | ALLOCATED | current design-principles artifact; allocation only |
| `Core/CORE-008_ARCHITECTURAL_LAWS.md` | Core | ALLOCATED | current architectural-laws artifact; allocation only |
| `Core/CORE-009_PLATFORM_LIFECYCLE.md` | Core | ALLOCATED | Core lifecycle artifact; separate LIF-001 authority preserved |
| `Core/CORE-010_PLATFORM_ROADMAP.md` | Core | ALLOCATED | planning artifact; ordering does not prove dependency |
| `Core/CORE-011_PLATFORM_CHARTER.md` | Core | ALLOCATED | current charter artifact; allocation only |
| `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` | Core | ALLOCATED | unique current CORE-012 identity |
| `Core/Core.md` | Core | ALLOCATED | canonical local inventory surface; self-excluding by design |
| `Core/_FOLDER_STATUS.md` | Core | ALLOCATED | status/evidence surface; Core remains Integrity Hold / not certified |

## Exact-set result

`CORE PHYSICAL ALLOCATION RECORD SET = 18 / 18 CURRENT TOP-LEVEL FILES`

No guessed path, numeric sequence filler, reverse relationship, dependency, consumer, or canonical promotion is created by this allocation population.

## Non-promotion boundary

`18/18 ALLOCATED ≠ 18/18 SEMANTICALLY CERTIFIED`

`ALLOCATION COMPLETE WITHIN CURRENT CORE PHYSICAL SET ≠ RELATIONSHIP GRAPH COMPLETE`

`ALLOCATION COMPLETE WITHIN CURRENT CORE PHYSICAL SET ≠ CORE CERTIFIED`

`ALLOCATION COMPLETE WITHIN CURRENT CORE PHYSICAL SET ≠ PRIORITY 7 CLOSED`

`ALLOCATION COMPLETE WITHIN CURRENT CORE PHYSICAL SET ≠ PHASE 1 CLOSED`

The repository-wide REP-012 state remains `Phase 1 Population In Progress`.

## Required next review

After this addendum is exact-head CI verified and W is closed Resume-Safe, a fresh Explicit Core Certification Review must re-read REP-012, REP-013, this addendum, current Core inventory/status, relationship evidence and queue authority. That review must independently decide whether this bounded allocation record set satisfies the allocation prerequisite and whether any other blocker remains.
