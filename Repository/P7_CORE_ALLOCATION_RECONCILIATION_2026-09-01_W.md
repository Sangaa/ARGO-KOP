# Priority 7 — Core Allocation Reconciliation — Transaction W

Date: 2026-09-01
State: `MATERIAL CANDIDATE PREPARED / CORE ALLOCATION 18-OF-18 RECORDED / CI PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-CORE-ALLOCATION-20260901`
Entry HEAD: `911f51d3a0881728125b36bfc09d266214730154`
Refined pre-write Matrix HEAD: `2a82218d8faf47ceea81d9e72a3edb00f0897007`

## Trigger

Explicit Core Certification Review V correctly refused certification because REP-013 requires an allocation record for every known file while canonical REP-012 had no per-Core allocation population.

## Current evidence

- direct current `Core/` enumeration = 18 top-level files;
- `Core/Core.md` independently lists 17 members and self-excludes;
- legacy `CORE-000_PLATFORM_IDENTITY.md` remains physical but noncanonical / superseded;
- Core readiness remains PASS;
- Core certification remains blocked/open pending allocation reconciliation and fresh review.

## Content-preservation decision

During W pre-write inspection, canonical REP-012 was found to contain a long historical/control-plane evidence body. Rewriting that entire artifact merely to append one bounded partition population would create unnecessary content-preservation risk.

W therefore uses `REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md` as a governed, non-replacing bounded allocation evidence surface subordinate to REP-012. Canonical REP-012 itself is not mutated in W.

This is not a shortcut around REP-012 authority: the addendum explicitly adopts REP-012 allocation semantics and leaves its repository-wide `Phase 1 Population In Progress` state unchanged. A fresh certification review must decide sufficiency.

## Material result prepared

The addendum records all 18 current top-level Core paths as `ALLOCATED` within the Core partition and preserves identity/authority boundaries for sensitive artifacts.

Especially:

- `CORE-000_PLATFORM_ARCHITECTURE.md` remains active canonical CORE-000 architecture owner;
- `CORE-000_PLATFORM_IDENTITY.md` remains `Canonical: No / Legacy / Superseded` provenance only;
- `CORE-002_ARGO_IDENTITY.md` remains active platform identity owner;
- `CORE-003_CONSTITUTION.md` retains constitutional authority;
- `Core.md` remains inventory only;
- `_FOLDER_STATUS.md` remains status/evidence only.

No relationship, dependency, consumer or certification state is created by allocation.

## Candidate boundary

Authorized candidate paths only:

1. `Repository/REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md`
2. this W record
3. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
4. W Mutation Matrix

Expected: one commit / four paths / zero expansion.

## Non-authority

W does not certify Core, close `CROSS-LAYER VALIDATION OPEN`, close Priority 7, modify Core semantics, mutate REP-014, weaken REP-013, or claim Phase-1 / Connected Baseline / repository-wide graph / Global PASS.

## Learning

`ALLOCATION IS A LOCATION/OWNERSHIP FACT, NOT A SEMANTIC CERTIFICATE.`

`PRESERVE A LARGE CONTROL-PLANE BODY WHEN BOUNDED ADDITIVE EVIDENCE CAN BE RECORDED WITHOUT REPLACEMENT; LET THE NEXT AUTHORITY REVIEW DECIDE SUFFICIENCY.`
