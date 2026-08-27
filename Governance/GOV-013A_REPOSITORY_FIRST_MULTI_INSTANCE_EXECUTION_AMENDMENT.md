# GOV-013A — Repository-First Multi-Instance Execution Amendment

**Parent:** GOV-013  
**Status:** Canonical Amendment  
**Version:** 1.0.0  
**Priority:** Critical

## 1. Core Rule

**The repository is the shared operational memory; a session is only an execution context.**

Conversational memory, window-local state, or an AI instance's prior context MUST NOT establish authoritative project state.

Every continuation invocation MUST reconstruct the current project state from current repository evidence before execution.

## 2. Mandatory Re-entry

Every invocation follows:

`RE-ENTER → OBSERVE CURRENT REPOSITORY → RECONCILE → DEFINE SCOPE → EXECUTE → VERIFY → RECORD → CLOSE`

At re-entry, the executing instance MUST:

1. identify current branch/ref and latest relevant repository state;
2. read current control-plane and applicable canonical protocols;
3. inspect relevant checkpoints, session deltas, journals, matrices and registries;
4. detect recent/concurrent changes affecting the intended seam, artifact or dependency;
5. reconcile session knowledge against current repository evidence;
6. treat current repository evidence as authoritative over stale session memory;
7. continue only from the reconciled state.

## 3. Parallel Windows / Platforms / Instances

Multiple execution contexts MAY work concurrently when their scopes are materially distinct.

Each concurrent task MUST have:

`SCOPE + MUTATION BOUNDARY + AFFECTED SEAMS + RELATIONSHIP IMPACT + REVALIDATION REQUIREMENTS`

A different window, platform or AI instance does not create a separate project state.

## 4. Concurrent Change Rule

Before mutation, compare current repository state with the last known checkpoint.

If another context has changed the affected surface:

`RE-READ → IMPACT ANALYSIS → RECONCILE → THEN MUTATE`

An older context MUST NOT overwrite newer repository state merely because its local context is older or its proposed change appears simpler.

## 5. Shared Evidence Graph

Material work MUST be recorded as reconstructable relationships where applicable:

`Instance/Session → Mutation → Artifact → Contract → Relationship → Consumer → Test → CI/Runtime → Outcome → Checkpoint`

The record MUST allow an independent instance to determine what changed, why it changed, what it affects, what evidence proved it, and what remains unresolved without access to the originating conversation.

## 6. Evidence Precedence

Use the following precedence:

`Canonical Authority > Current Repository Evidence > Current CI/Runtime Evidence > Session Memory > Conversational Summary`

Session memory accelerates work; it cannot establish a project fact by itself.

## 7. No Rebuild From Memory

If a prior session reports completion but current repository evidence does not confirm it, classify the state as `UNRECONCILED`, not complete.

If current repository evidence confirms completion, do not rebuild merely because the current session lacks historical context.

## 8. Safe Concurrent Mutation

Every material mutation follows:

`PRE-CHECK → CURRENT-STATE COMPARISON → MINIMAL CHANGE → RE-READ → RELATIONSHIP/INDEX VALIDATION → AFFECTED TESTS → CI WHEN APPLICABLE → CHECKPOINT`

A successful local result does not override a newer repository change.

## 9. Handoff Contract

Every material checkpoint MUST contain:

- current state;
- completed work;
- evidence;
- unresolved gap/blocker;
- affected relationships;
- next safe action;
- explicit non-claims;
- closure state.

## 10. Learning Promotion

A repeatable synchronization, retrieval, or concurrency weakness MUST enter the existing Learning Promotion Gate. It must not remain only in a conversation summary.

## 11. Scope

This amendment applies to all HERMUZ continuation sessions and all ARGO KOP work performed through multiple windows, platforms, agents or human collaborators.

It strengthens GOV-013 and does not weaken higher-authority Constitution, Bootstrap, Governance, Architecture, Release, or domain-specific authority.
