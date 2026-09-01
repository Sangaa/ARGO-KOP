# R Unauthorized Temp-File Incident — 2026-09-01

State: RECOVERY RECORD / MATERIAL FIX PENDING CI
Incident commit: `c38783c38962063a7fc38f6c99adad3547e4e6fd`
Pre-incident R candidate: `c5c695597a6df18876ff83542c65bed2797fe98f`
Recovery Matrix commit: `671123cc83655bc35e8d07b60e0c416eb5b396e9`

## What failed

While preparing the Transaction-R closure, the intended operation was to construct Git objects for updates already authorized by the R transaction. The wrong repository write action was invoked and directly created the empty file:

`Repository/INVALID_SHOULD_NOT_CREATE.tmp`

The path was outside the authorized R material change set.

## Evidence

- The incident commit is a direct child of the clean R candidate.
- The created file is empty and has blob SHA `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`.
- Git history preserves the incident; no reset, force push, or history rewrite is used.
- The incident's Full-Stack Repository Audit, Runtime Prototype/Integration, and M2 workflows all completed successfully. Therefore green CI did not establish transaction-scope correctness for this accidental path.

## Classification

Primary: `IMPLEMENTATION_FAILURE` — wrong write action/tool selection during closure preparation.

Governance: original write `NON-COMPLIANT`; existing GOV-014A already governs the failure mechanism, so this incident does not by itself prove a new governance gap.

CI/evidence boundary: `GREEN CI != AUTHORIZED CHANGE-SET PROOF`. The current workflow set did not reject this exact accidental `.tmp` path. Whether this is a repeatable CI coverage gap requires separate bounded validation before any rule or test promotion.

## What did not fail

- The previously validated R semantic finding was not altered.
- RUN-002 and CORE-003 source content were not changed.
- REP-014 was not changed.
- Core folder status was not changed.
- No relationship, authority, certification, Phase-1, Connected-Baseline, or Global-PASS state was promoted.
- The R candidate's prior 4/4 exact-head evidence remains historical evidence for `c5c695597...`; it is not silently rebound to the incident commit.

## Prior learning

P217 / GOV-014A is `DIRECTLY APPLICABLE`: protected mutation must have an applicable Matrix before the write. The incident is a failure to apply an existing control, not evidence that the control was absent.

The first attempt to create the recovery Matrix was blocked by the connector before repository mutation. This was a tooling limitation, not a second repository write. A bounded retry created the pre-write recovery Matrix successfully.

## Root cause

Available evidence supports a high-confidence operator/execution root cause: the wrong repository write action was called while intending to prepare non-published Git objects. The operation bypassed the planned pre-publish compare step and immediately mutated `main`.

## Corrective pattern

For protected work, distinguish explicitly between:

`OBJECT PREPARATION` and `REPOSITORY MUTATION`.

Before invoking any write-capable action, bind:

`intended action -> exact target path(s) -> current Matrix authorization -> whether main will move`.

This pattern remains `SESSION-LEARNING` until repeat evidence demonstrates that promotion is warranted.

## Recovery

The governed recovery is:

1. preserve this incident in Git history;
2. create the recovery Matrix before corrective mutation;
3. remove only the unauthorized temp artifact;
4. preserve all R and control-plane semantics;
5. run exact-head CI/integration verification;
6. only after recovery closure, return to Transaction R.

No rollback by history rewrite is authorized.
