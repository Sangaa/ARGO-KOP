# MUT-2026-08-30 — P2 EJR CONTROLLED IDENTITY-REPAIR PLAN — LEASE 204

Status: `PREWRITE / PLANNING ONLY / NO IDENTITY MUTATION AUTHORIZED`
Lease: `R71-20260830-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204`
Baseline: `main@329a7700f9d880674ed7ae317c1464be785ce2f8`

## Trigger
Lease 203 proved that EJR-211, EJR-214, EJR-219, EJR-301 and EJR-302 are distinct legitimate identity-reuse collisions with recoverable contextual referents. The next legal action is to produce a governed repair plan before any EJR renumbering or path mutation.

## Objective
Define a deterministic retention/displacement rule, identify the exact records that would retain the reused identifiers, identify records requiring future replacement identities, enumerate consumer/provenance rewrite obligations, and require Lease-193 complete-history vacancy proof before any replacement allocation.

## Governing retention rule under review
Default rule:

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE PROVES THAT FIRST ALLOCATION WAS ITSELF INVALID, UNAUTHORIZED, OR NEVER CONSTITUTED AN IDENTITY ALLOCATION.`

A later governed consumer may prove which record it means, but it does not retroactively transfer ownership of an already-used identifier.

## Evidence already established
- EJR-211 Memory P29 record predates the later Root P2 record; Memory creation commit `eb9fd770e0b4c52f86e813341a92da2fc6063b67` is 2026-08-14 and Root creation commit `e54fb22f9f582b4e3bf164aa05e4a3a97a0f8950` is 2026-08-17.
- EJR-214 Memory P31 record is dated 2026-08-14; later Root P2 closure creation commit `7207214ace7a44dc80bbbc0b0a34d771858988c5` is 2026-08-17.
- EJR-219 Memory P36 record is dated 2026-08-14; competing Root record is dated 2026-08-17.
- EJR-301 Memory P6 record creation commit `079d7042583e01e8c831bf0f9592bbf6cf3fd648` is 2026-08-22; Root GT-040 creation commit `cc90f7822460ccbfb60e3e083c3189b04a3ed4eb` is 2026-08-24.
- EJR-302 Memory current-head record creation commit `9e8a73a8bd52b30f632569348b513e7ec2f2f77e` is 2026-08-22; Root GT-041 creation commit `3b6ecfb236bc1baa2592fd083b0eb6fcb6156add` is 2026-08-24; Root CI-decision-boundary record creation commit `eb1c200740c6c5fac4380c5d42ced6c0584f67d9` is 2026-08-25.

## Planning boundaries
This lease may create planning/evidence documents only. It MUST NOT:
- rename, move, delete or modify any EJR record;
- allocate any replacement EJR number;
- rewrite any consumer;
- modify REP-012, REP-016 or REP-020;
- suppress ambiguity groups;
- claim Priority 2, Phase 1, Connected Baseline, or global integrity closure.

## Required functional deliverable
A repair plan that, for every record in the five collision groups:
1. records retention/displacement disposition under the rule above;
2. lists exact current consumers/provenance edges already proven by Lease 203;
3. states future rewrite obligations for displaced records;
4. marks replacement ID as `UNALLOCATED / VACANCY PROOF REQUIRED` until Lease-193 gate returns `VACANT`;
5. preserves chronology and semantic content;
6. separates identity repair from canonical promotion.

## Verification
Functional verification requires exact-head repository workflows. Planning-only closure must remain resume-safe even if no identity mutation is authorized.
