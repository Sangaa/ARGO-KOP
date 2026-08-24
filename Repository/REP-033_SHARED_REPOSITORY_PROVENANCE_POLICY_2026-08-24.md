# REP-033 Shared Repository Provenance Policy

Date: 2026-08-24
Checkpoint: GT-033
State: EXECUTED / DOCUMENTED / VERIFIED

## Purpose

ARGO-KOP is treated as a shared concurrent repository. Multiple AI agents or human/operator processes may mutate the same repository. Presence of an artifact in the repository is therefore not sufficient to attribute that artifact to HERMUZ.

## Attribution Rule

Evidence must be separated into existence, provenance, and attribution.

- Evidence exists: the resource is observable.
- Provenance identified: the resource can be linked to a commit, PR, run, issue, or other exact identity.
- HERMUZ-attributed: a causal chain links the resource to a mutation executed by HERMUZ in the current governed session.
- External-attributed: reliable evidence links the resource to another actor/process.
- Unattributed: the resource exists but its originating actor cannot be established.
- Concurrent/shared: multiple actors may have interacted with the same surface and attribution cannot safely be isolated.

## Minimum HERMUZ Attribution Chain

HERMUZ action → exact resource identity → mutation/read-back evidence → temporal/session correlation → causal linkage.

Missing any material link prevents HERMUZ attribution.

## Interpretation Rule

Unattributed evidence may be used as evidence about repository state, but must not be used as evidence of HERMUZ success, failure, learning, or causation.

## Actions Evidence

Workflow runs, jobs, logs, artifacts, PR merge refs, and commits are shared repository evidence. A workflow failure is not attributed to HERMUZ merely because it was observed during a HERMUZ session.

## Operational Rule

Before interpreting a shared artifact as a HERMUZ result, perform provenance and attribution checks. If attribution is uncertain, classify the evidence as UNATTRIBUTED or SHARED/CONCURRENT and do not promote it to a HERMUZ result.

## Closure

This policy records the shared-repository attribution boundary learned during GT-033. No production logic was changed.
