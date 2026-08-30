# ROOM 071 — RECONSTRUCTION SUPPLEMENT 197 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-H1-PAIR-CHRONOLOGY-197`
Functional head: `7aea5f0c507523027be39ceac353e92aaee84a49`

## What was resolved

The dominant current H1-only two-member EJR ambiguity subset now has deterministic historical chronology evidence without changing any identity owner, EJR artifact, or internal-ID gate semantics.

A companion analyzer was added rather than embedding chronology policy into the identity scanner. It recomputes the qualifying intersection at execution time and fails closed on shallow or incomplete history.

## Exact-head evidence

At `7aea5f0c507523027be39ceac353e92aaee84a49`:
- Internal Document-ID Audit `33316564556` — `SUCCESS`.
- Full-Stack Repository Audit `33316564465` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33316564503` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33316564500` — `SUCCESS`.
- Real Mutation Matrix Regression `33316564478` — `SUCCESS`.

Chronology artifact:
- ID `9733622947`
- digest `sha256:f3e88a958288321de1ea928acd8fff72246d2e78e8d40111af704c303125aab5`

## Chronology result

Current qualifying intersection: `101` H1-only, cardinality-2 EJR ambiguity groups.

- `57` = left path's first-seen commit is ancestor of the right path's first-seen commit.
- `44` = right path's first-seen commit is ancestor of the left path's first-seen commit.
- `0` missing path histories.
- `0` divergent/unordered pairs.
- `0` same-first-seen-commit pairs.
- classification complete = `true`.
- history complete = `true`.
- history scope = all locally reachable refs.

Lease 196's `103` count was the marginal count of all EJR cardinality-2 ambiguity groups, not the intersection with the H1-only signature. Lease 197 recomputed the intersection and established the correct bounded population as `101`.

## Learned rules

1. `MARGINAL COUNTS MUST NOT BE TREATED AS INTERSECTION COUNTS; RECOMPUTE THE FILTERED POPULATION AT EXECUTION TIME.`
2. Chronological precedence is evidence, not canonical ownership authority.
3. Exact-path chronology must not be silently upgraded into rename-lineage chronology.
4. Missing or shallow history is a classification hold, never permission to infer precedence.

## Preserved boundaries

- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, or allocation;
- internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target

Recompute and classify the remaining H1-only EJR ambiguity groups outside the two-member subset using a generalized multi-member chronology evidence pass. Do not infer ownership from chronology and do not mutate identity unless a later governed lease explicitly authorizes it.
