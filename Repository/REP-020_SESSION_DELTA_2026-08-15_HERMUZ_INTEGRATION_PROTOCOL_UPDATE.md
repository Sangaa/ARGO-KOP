# REP-020 — HERMUZ INTEGRATION PROTOCOL UPDATE — 2026-08-15

## Change

`GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md` was updated from v1.0.0 to v1.1.0.

## New Mandatory Rule

Integration verification is now a mandatory parallel workstream for every material module, file relationship, folder/layer boundary, service, engine, runtime component, interface, and memory component that is built, modified, reconciled, or materially revalidated.

The rule explicitly requires:

- existing integration tests to be recovered and reused before creating new tests;
- module/file/folder cross-boundary verification where applicable;
- full-stack audit usage at appropriate checkpoints when present;
- runtime reachability claims to require runtime evidence;
- integration results to reconcile into the applicable Matrix/Registry;
- regression testing after material mutations;
- interrupted integration work to be recovered rather than silently dropped.

## Invocation Effect

The canonical invocation remains:

> «أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»

A new session receiving that phrase must load GOV-013 v1.1.0 and recover the latest repository and integration-test state before continuing.

## Verification

GOV-013 was committed successfully and re-read from `main` after the mutation.

## Status

`ACTIVE / CANONICAL / INTEGRATION-TESTING-MANDATORY`
