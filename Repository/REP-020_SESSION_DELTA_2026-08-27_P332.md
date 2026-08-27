# P332 — Canonical Multi-Instance Execution Amendment

Status: `CLOSED / CANONICAL / NO-RUNTIME-MUTATION`

## Problem Proven
A session can retain correct local knowledge while the repository has changed through another window/platform/instance. Session-local continuity is therefore insufficient for project continuity.

## Decision
Adopt repository-first re-entry as a canonical HERMUZ amendment:

`RE-ENTER → OBSERVE CURRENT REPOSITORY → RECONCILE → DEFINE SCOPE → EXECUTE → VERIFY → RECORD → CLOSE`

The repository is the shared operational memory; each session is only an execution context.

## Parallel Work
Distinct instances may work concurrently when scopes and mutation boundaries are explicit. Before mutation, current state and concurrent changes must be reconciled. Material work records its evidence graph so an independent instance can resume without the originating conversation.

## Evidence Precedence
`Canonical Authority > Current Repository Evidence > Current CI/Runtime Evidence > Session Memory > Conversational Summary`

## Canonical Artifact
`Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md`

## Boundary
This changes execution/re-entry governance only. It does not authorize concurrent conflicting mutations, bypass existing gates, or grant additional repository/runtime authority.

`MAIN = UPDATED`
`RUNTIME = UNCHANGED`
`AUTHORITY = UNCHANGED`
`SESSION = CLOSED`
