# EJR-324 — GT-053 Main Workflow Run Discovery Capability Gap

**Date:** 2026-08-24
**Training Domain:** GitHub Actions / P6 execution evidence
**Status:** CAPABILITY GAP IDENTIFIED / NO PRODUCT MUTATION

## Objective

Determine whether the currently exposed GitHub connector surfaces can discover canonical GitHub Actions workflow runs for the current `main` HEAD, so that the existing execution-evidence chain can be extended from training PRs to the canonical repository state.

## Known Current Main HEAD

`bc0ab35b5051a436d44f42b5fff9413659ede083`

Commit message:

`docs: record GT-033 shared repository provenance policy`

## Evidence Already Established

A training PR HEAD (`c1df6b127aefd70643aad519c8bf16e1200f86cd`) was successfully resolved through:

`HEAD -> workflow run -> job -> steps -> artifacts`

The successful run exposed P6 regressions, runtime evidence, CI execution identity, and artifacts bound to that exact SHA.

## New Observation

The available commit-to-workflow-run surface is PR-trigger scoped. For the current `main` HEAD it returned no visible workflow runs. A direct public GitHub Actions endpoint for branch-wide run discovery was not accepted by the connector surface.

Therefore the correct classification is **NOT OBSERVED / CAPABILITY SURFACE GAP**, not `CI FAILED` and not `CI NEVER RAN`.

## Boundary Rule

Do not infer absence of execution from an empty result on a PR-scoped surface. Do not add an ARGO workaround or modify P6 solely to compensate for an unproven discovery surface.

## Next Training Step

Re-evaluate GitHub capability surfaces for canonical workflow-run discovery. If a supported surface is found, resolve:

`main HEAD -> run_id -> job -> steps -> logs/artifacts -> P6 evidence`

If no supported surface exists, record the connector capability limitation separately before considering any implementation change.

## Decision

**No P6 mutation authorized by this checkpoint.**

This checkpoint intentionally preserves the distinction between:

- capability existence,
- connector surface exposure,
- observation availability,
- and actual CI execution state.
