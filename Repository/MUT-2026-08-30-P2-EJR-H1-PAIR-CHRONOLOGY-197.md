# MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197

Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-H1-PAIR-CHRONOLOGY-197`
Base: `ac9bd78e6ccd99498131477b06eac241d5c156ca`
Functional head: `7aea5f0c507523027be39ceac353e92aaee84a49`

## Purpose

Build an evidence-only historical chronology classifier for the dominant Priority-2 subset identified by Lease 196: current EJR ambiguity groups that are `FIRST_H1_FALLBACK_ONLY` and have exactly two members.

## Implemented scope

Functional paths changed exactly as authorized:
- `Quality/Integration/ejr_h1_pair_chronology.py`
- `Quality/Integration/test_ejr_h1_pair_chronology.py`
- `.github/workflows/internal-id-audit.yml`
- `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197_MUTATION_MATRIX.md`

The classifier consumes current ambiguity evidence and complete locally reachable Git history. It reports exact-path first-seen commit/time and ancestry ordering where provable. It does not decide canonical ownership.

## Exact-head verification

At `7aea5f0c507523027be39ceac353e92aaee84a49`:
- Internal Document-ID Audit `33316564556` — `SUCCESS`.
- Full-Stack Repository Audit `33316564465` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33316564503` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33316564500` — `SUCCESS`.
- Real Mutation Matrix Regression `33316564478` — `SUCCESS`.

Chronology artifact:
- ID `9733622947`
- digest `sha256:f3e88a958288321de1ea928acd8fff72246d2e78e8d40111af704c303125aab5`

## Observed chronology result

The executable intersection was recomputed rather than inferred from Lease 196 marginal counts:
- qualifying H1-only, cardinality-2 EJR groups: `101`;
- `LEFT_FIRST_SEEN_ANCESTOR`: `57`;
- `RIGHT_FIRST_SEEN_ANCESTOR`: `44`;
- missing path history: `0`;
- divergent/unordered: `0`;
- same first-seen commit: `0`;
- classification complete: `true`;
- history complete: `true`;
- history scope: all locally reachable refs.

Lease 196 reported `103` EJR groups of cardinality 2 across the whole EJR ambiguity surface. That was a marginal cardinality count, not the H1-only/cardinality-2 intersection. Lease 197 correctly recomputed the intersection as `101` instead of hard-coding `103`.

## Learned rules

1. `MARGINAL COUNTS MUST NOT BE TREATED AS INTERSECTION COUNTS; RECOMPUTE THE FILTERED POPULATION AT EXECUTION TIME.`
2. Chronological precedence is evidence, not canonical ownership authority.
3. Exact-path history is narrower than rename-lineage history; it must be labeled accordingly.
4. Incomplete history or missing path evidence must fail closed rather than manufacture precedence.

## Preserved boundaries

- no EJR content mutation, rename, delete, migration, reassignment, normalization, suppression, or allocation;
- internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, and REP-020 unchanged;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target

Recompute and classify the remaining H1-only EJR ambiguity groups outside the two-member subset. Prefer a generalized multi-member chronology evidence pass. Keep the task evidence-only unless a later governed lease explicitly authorizes identity mutation.
