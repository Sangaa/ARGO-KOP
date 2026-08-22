# EJR-309 — HERMUZ Controlled Adapter CI Binding Boundary

Date: 2026-08-22
Status: Closed — Mutation + Read-back Verified
Scope: Controlled test execution binding

## Trigger

EJR-308 created a controlled runtime-lineage-to-P6 adapter regression but classified it as `CONTROLLED_SYNTHETIC` because no live runner evidence had been observed.

## Mutation

The Full-Stack Repository Audit workflow was updated to execute:

`python Quality/Integration/test_p6_runtime_lineage_adapter.py`

The workflow is configured for `push` to `main`, pull requests, and manual dispatch, and its existing checkout identity gate binds execution to `github.sha`.

## Observation

The update commit was:

`4b2e10448ff94e83cd0b54b8622d63349a31b73b`

The workflow file was read back after mutation with blob SHA:

`9dfe15f807b269b9939494d6bea170afb79e7da0`

A commit-scoped workflow-run query returned an empty set. The available connector surface documents that this query is pull-request-triggered-run scoped, so the empty result cannot establish that the push-triggered workflow did not execute.

## Interpretation

This step proves workflow binding by configuration, not runtime execution. The controlled adapter therefore remains `CONTROLLED_SYNTHETIC` until an independent execution surface exposes a matching run identity.

## Learning

A test can be correctly bound into CI and still lack observable runtime evidence. Therefore `configured`, `invoked`, `executed`, and `observed` remain separate evidence states.

## Closure

Mutation: COMPLETE
Read-back: VERIFIED
Workflow binding: VERIFIED BY CONFIGURATION
Runtime execution observation: NOT VERIFIED
Controlled adapter execution: NOT CLAIMED
Canonical CI PASS: NOT VERIFIED
P6 root cause: NOT CLAIMED
Relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — READ-BACK VERIFIED`.
