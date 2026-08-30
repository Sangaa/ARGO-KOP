# MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197

Status: `PREWRITE / OPEN`
Lease: `R71-20260830-P2-EJR-H1-PAIR-CHRONOLOGY-197`
Base: `ac9bd78e6ccd99498131477b06eac241d5c156ca`

## Purpose

Build an evidence-only historical chronology classifier for the dominant Priority-2 subset identified by Lease 196: EJR ambiguity groups that are `FIRST_H1_FALLBACK_ONLY` and have exactly two current members.

## Scope

Authorized functional paths:
- `Quality/Integration/ejr_h1_pair_chronology.py`
- `Quality/Integration/test_ejr_h1_pair_chronology.py`
- `.github/workflows/internal-id-audit.yml`
- `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197_MUTATION_MATRIX.md`

The classifier may consume current ambiguity evidence and complete locally reachable Git history. It may report chronology facts such as first-seen commit/time for each current path and pair ordering where provable.

## Hard boundaries

- evidence classification only;
- no EJR content mutation, rename, delete, migration, reassignment, normalization, suppression, or allocation;
- no ownership/canonicality decision derived solely from chronology;
- no REP-012, REP-016, REP-020 change;
- no change to internal Document-ID audit semantics;
- no Priority-2, Phase-1, Connected-Baseline, or global PASS closure;
- incomplete/shallow history must fail closed rather than fabricate chronology certainty.

## Evidence model

The first bounded population is exactly the current EJR groups satisfying:
1. ambiguity group;
2. source signature = `FIRST_H1_FALLBACK_ONLY`;
3. cardinality = 2.

Lease 196 observed 103 such groups at its functional head. Lease 197 must recompute the current set at execution time rather than hard-code that count.

For each member path, chronology must be derived from Git history for that path. A missing or non-provable timestamp/commit is evidence of incomplete classification, not permission to infer precedence.

## Prewrite rule

No functional write is authorized until this lease and its Mutation Matrix are committed to `main` by a non-force fast-forward after live-parent recheck.
