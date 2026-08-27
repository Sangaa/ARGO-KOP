# GOV-013A — Repository-First Multi-Instance Execution Amendment

Status: `CANDIDATE / GOVERNED / PENDING CANONICAL PROMOTION`
Parent: `GOV-013`

## Core Rule

**The repository is the shared operational memory; a session is only an execution context.**

Session/conversation memory may accelerate work but MUST NOT establish authoritative project state. Every HERMUZ invocation must reconstruct the current state from repository evidence.

## Re-entry Contract

`RE-ENTER → OBSERVE CURRENT REPOSITORY → RECONCILE → SCOPE → EXECUTE → VERIFY → RECORD → CLOSE`

At re-entry the engineer MUST:

1. identify current branch/ref and latest relevant commit;
2. read current control-plane state and applicable canonical protocols;
3. inspect relevant checkpoints, journals, matrices and registries;
4. search for recent/concurrent changes affecting the intended seam or dependency;
5. reconcile session memory with current repository evidence;
6. treat current repository evidence as authoritative over stale conversation memory;
7. continue only from the reconciled state.

## Parallel Work

Multiple AI instances, windows, platforms, agents or human engineers MAY work concurrently when their scopes are materially distinct.

Each parallel work item MUST declare:

`SCOPE + MUTATION BOUNDARY + AFFECTED SEAMS + RELATIONSHIP IMPACT + REVALIDATION REQUIREMENTS`

A different window or platform does not create a separate project state.

## Concurrent Change Rule

Before mutation, inspect current ref and relevant changes since the last checkpoint. If concurrent changes are detected:

`RE-READ → IMPACT ANALYSIS → RECONCILE → THEN MUTATE`

An older context MUST NOT overwrite newer repository state.

## Shared Evidence Graph

Material work MUST leave reconstructable evidence:

`Instance/Session → Mutation → Artifact → Contract → Relationship → Consumer → Test → CI → Outcome → Checkpoint`

A future instance must be able to understand what changed, why, impact, proof and remaining work without the originating conversation.

## Evidence Precedence

`Canonical Authority > Current Repository Evidence > Current CI/Runtime Evidence > Session Memory > Conversational Summary`

If a prior session reports completion but current repository evidence does not confirm it, state is `UNRECONCILED`, not complete.

If current repository evidence confirms completion, do not rebuild merely because historical conversation is unavailable.

## Safe Concurrent Mutation

`PRE-CHECK → CURRENT-STATE COMPARISON → MINIMAL CHANGE → RE-READ → RELATIONSHIP/INDEX VALIDATION → AFFECTED TESTS → CI WHEN APPLICABLE → CHECKPOINT`

A successful local result never overrides a newer repository state.

## Handoff Minimum

Every material checkpoint MUST record:

- current state;
- completed work;
- evidence;
- unresolved gap/blocker;
- affected relationships;
- next safe action;
- explicit non-claims;
- closure state.

## Learning Promotion

A repeatable synchronization/retrieval/concurrency weakness MUST be classified through the existing learning mechanism and, when justified, promoted into the canonical protocol rather than remaining only in conversation.

## Canonical Promotion Gate

This amendment is intentionally additive and does not silently replace GOV-013. It becomes canonical only after:

`Review → Authority Check → Conflict Check → Repository Re-read → Integration/CI Validation → Canonical Promotion Decision`
