# P331 — Multi-Instance Repository-First Execution

Status: `CLOSED / AMENDMENT RECORDED / CANONICAL PROMOTION PENDING`

## Finding
The operational test demonstrated that session-local continuity is insufficient when multiple AI instances/windows/platforms work concurrently. Project continuity must be reconstructed from current repository evidence.

## Design Decision
`Repository = shared operational memory`
`Session = execution context`

Every HERMUZ invocation must perform repository-first re-entry and reconciliation before continuing.

## Parallelism
Distinct tasks may execute concurrently when scope, mutation boundary, affected seams and revalidation requirements are explicit. A different window/platform does not create a separate project state.

## Evidence Graph
Material work must be reconstructable as:
`Instance/Session → Mutation → Artifact → Contract → Relationship → Consumer → Test → CI → Outcome → Checkpoint`

## Safety
Current repository evidence outranks stale session memory. Concurrent changes require re-read and impact reconciliation before mutation. No force-overwrite or speculative merge is authorized by this amendment.

## Implementation
Added `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md` as a governed additive amendment on the isolated build branch. The existing canonical GOV-013 was not overwritten because its current blob identity was not available for a safe replacement operation.

## Promotion Gate
`GOV-013A = CANDIDATE / GOVERNED / PENDING CANONICAL PROMOTION`

Canonical promotion requires authority/conflict review and CI/revalidation. This checkpoint does not claim that GOV-013 itself has already been upgraded.

`MAIN = UNCHANGED`
`SESSION = CLOSED`
