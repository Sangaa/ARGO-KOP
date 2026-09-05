# P12 Models Relationship/Content Transaction B — Unit 15 Registry Allocation Matrix

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Unit: `15 — canonical REP-014 allocation planning`
State: `ALLOCATION PLAN COMPLETE / CANONICAL REGISTRY UNCHANGED / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Entry gate

Unit-14 exact-head `7b205935d5ab440c8fe2e305eb989608c77b796d` passed all four required workflow families.

## Allocation result

Current REP-014 contains exactly stable IDs `REL-001..REL-080`; repository search found no `REL-081` allocation.

The latest Priority-12 evidence surfaces B..L were reconciled by latest semantic disposition, not by first-observed candidate state. Explicit `DO_NOT_REGISTER`, `NO_EDGE`, generic consumer classes and ripple-only targets remain excluded.

The resulting canonical-write plan contains:

- `43` new direct-source relationships allocated contiguously as `REL-081..REL-123`;
- stable-ID correction `REL-002: SRV-004 → MOD-001 = DEPENDS_ON`;
- stable-ID type correction `REL-012: MOD-011 → KNW-004 = REFERENCES`;
- `REL-001`, `REL-010`, `REL-011`, `REL-013`, `REL-014` retained;
- no `MOD-004 → RUN-004/RUN-008/RUN-009/ENG-007` relationship reintroduced;
- endpoint/target holds preserved as relationship-state qualifiers rather than silently promoted.

Allocation surface:

`Repository/REP-014_PRIORITY12_REGISTRY_ALLOCATION_PLAN_2026-09-05_M.tsv`.

Executable allocation guard:

`Quality/Integrity/test_models_p12_registry_allocation_plan.py`.

## Control-plane coupling

Current `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` binds `REP-014` at version `1.2.19`. Therefore any canonical REP-014 version bump MUST update the current manifest in the same protected atomic change set.

The canonical registry write is not authorized until this Unit-15 exact-head passes all four required workflow families.

## Next legal action after exact-head success

Atomic protected change set:

`REP-014 full-content-preserving v1.2.20 write + REP-020 current manifest rebind + canonical registry guard + same-change-set Unit-16 Matrix`.

No Priority-12 or Transaction-B closure is implied by allocation planning.
