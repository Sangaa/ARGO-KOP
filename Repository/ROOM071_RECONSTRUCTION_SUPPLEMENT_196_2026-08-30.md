# ROOM 071 — RECONSTRUCTION SUPPLEMENT 196 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Functional head: `32021e605f5410de2a4833c73cbeca5350c1cbd6`

## What was resolved

Priority-2 EJR ambiguity is no longer an undifferentiated set for analysis. A companion evidence analyzer now classifies current ambiguity groups by identity-source signature and cardinality without altering the internal Document-ID gate or any EJR artifact.

The implementation deliberately consumes Lease-191 member-level observability instead of adding analytical policy to the identity scanner.

## Exact-head evidence

At `32021e605f5410de2a4833c73cbeca5350c1cbd6`:

- Internal Document-ID Audit `33315075640` — `SUCCESS`.
- Full-Stack Repository Audit `33315075636` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33315075614` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33315075651` — `SUCCESS`.
- Real Mutation Matrix Regression `33315075663` — `SUCCESS`.

Census artifact:
- ID `9733176940`
- digest `sha256:1bd941ff549e22bc91a41adb836fc9ff770abdbdb0c9f30913a0ad61e2af047c`

## Census result

Whole ambiguity surface: `144` groups = `128 FIRST_H1_FALLBACK_ONLY` + `16 MIXED`.

EJR ambiguity surface: `121` groups = `115 FIRST_H1_FALLBACK_ONLY` + `6 MIXED`.

EJR cardinality:
- 2 members: `103` groups
- 3 members: `12` groups
- 4 members: `3` groups
- 5 members: `2` groups
- 6 members: `1` group

The mixed EJR set is exactly:
`EJR-003`, `EJR-026`, `EJR-180`, `EJR-181`, `EJR-182`, `EJR-183`.

This independently reproduces the six-group explicit-metadata surface recorded by Lease 192. The remaining `115` EJR groups are H1-only under current executable evidence.

## Learned rules

1. When a source gate already exposes sufficient member facts, analytical aggregation belongs in a companion evidence analyzer rather than in the source gate.
2. Large ambiguity populations should be partitioned by observable source signature and cardinality before chronology or ownership analysis.
3. Agreement between an independently generated census and an earlier bounded manual census strengthens confidence without converting the evidence into migration authority.

## Preserved boundaries

- no EJR mutation, migration, rename, delete, reassignment, normalization, or suppression;
- internal-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target

Open the next bounded Priority-2 lease for historical/provenance chronology classification of the `115` H1-only EJR ambiguity groups. Prefer the dominant cardinality-2 subset (`103` groups) for the first pass. The task is evidence classification only unless a later governed lease explicitly authorizes identity mutation.
