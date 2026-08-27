# GOV-013A — Repository-First Multi-Instance Execution Amendment

Status: `PROPOSED / GOVERNANCE-CONTROLLED / NOT YET CANONICAL`
Parent: `GOV-013`
Date: `2026-08-27`

## Purpose
Prevent session-local memory from being mistaken for current project state when ARGO is operated through multiple AI instances, browser windows, platforms, agents, or human engineers.

## Core Rule
`REPOSITORY = SHARED OPERATIONAL MEMORY`
`SESSION = EXECUTION CONTEXT`

Every continuation invocation must reconstruct current project state from repository evidence before selecting work.

## Mandatory Re-entry
`RE-ENTER → OBSERVE CURRENT REPOSITORY → RECONCILE → SCOPE → EXECUTE → VERIFY → RECORD → CLOSE`

At minimum:
1. identify current branch/ref and current relevant commit;
2. read canonical control-plane and applicable protocol;
3. inspect recent checkpoints, deltas, journals, matrices and registries;
4. detect concurrent/recent changes affecting the intended seam or dependency;
5. reconcile session knowledge against current repository evidence;
6. treat current repository evidence as authoritative over stale session memory;
7. continue only from the reconciled state.

## Parallel Work
Different instances MAY work concurrently when scopes are materially distinct. Each scope must declare:
`TASK SCOPE + MUTATION BOUNDARY + AFFECTED SEAMS + RELATIONSHIP IMPACT + REVALIDATION REQUIREMENTS`.

A different window or platform never creates an independent project state.

## Concurrent Change Rule
If a newer repository change affects the intended surface:
`RE-READ → IMPACT ANALYSIS → RECONCILE → THEN MUTATE`.

An older session must not overwrite newer repository state merely because its local context is older.

## Shared Evidence Graph
Material work must be reconstructable as:
`INSTANCE/SESSION → MUTATION → ARTIFACT → CONTRACT → RELATIONSHIP → CONSUMER → TEST → CI/RUNTIME → OUTCOME → CHECKPOINT`.

The originating conversation must not be required to understand why a material repository change exists.

## Evidence Precedence
`CANONICAL AUTHORITY > CURRENT REPOSITORY EVIDENCE > CURRENT CI/RUNTIME EVIDENCE > SESSION MEMORY > CONVERSATIONAL SUMMARY`

Session memory accelerates work but cannot establish project truth alone.

## No Rebuild From Memory
A prior claim of completion without current repository evidence is `UNRECONCILED`, not complete.

Conversely, current evidence proving completion must prevent unnecessary reconstruction of already-complete work.

## Safe Mutation
`PRE-CHECK → CURRENT-STATE COMPARISON → MINIMAL CHANGE → RE-READ → RELATIONSHIP VALIDATION → AFFECTED TESTS → CI WHEN APPLICABLE → CHECKPOINT`.

## Handoff
Each material checkpoint must expose current state, completed work, evidence, unresolved gap, affected relationships, next safe action, non-claims, and closure state.

## Promotion Gate
This document is intentionally `PROPOSED` until validated against existing governance and promoted through the applicable governance/learning mechanism. No status claim in this file grants authority or runtime permission.
