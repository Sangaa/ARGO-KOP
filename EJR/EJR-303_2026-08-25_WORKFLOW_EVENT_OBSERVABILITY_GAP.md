# EJR-303 — Workflow Event Observability Gap

**Date:** 2026-08-25
**Status:** OPEN — investigation required
**Trigger:** P221 / de89759d91ec959bb4d55bff8b409ca001df025c

## Finding

Runtime and M2 workflows executed successfully for the same main push SHA, while the Full-Stack Repository Audit workflow was not surfaced by the commit-scoped workflow-run query. The repository workflow definition on the same SHA contains `push: branches: [main]`, so the absence cannot be interpreted as proof that GitHub did not execute the workflow.

## Evidence

- Runtime and M2 successful runs exist for `de89759…`.
- `fetch_commit_workflow_runs` returned no Full-Stack run for that SHA.
- Repository-wide Actions inspection exposed runs that the commit-scoped surface did not expose.
- `full-stack-audit.yml` at `de89759…` explicitly declares `push` on `main`.
- Earlier commit `2aab31c…` demonstrably triggered Full-Stack and failed at Mutation Matrix preflight, proving the workflow is executable in this repository.

## Classification

**Unknown — Workflow Event/Run Observability Gap.**

Do not classify as workflow trigger failure, GitHub suppression, or tool defect until event/run correlation is independently established.

## Required investigation

1. Correlate push event SHA/ref/time with each workflow's run.
2. Inspect workflow identity, event name, ref, SHA, and run conclusion.
3. Compare Full-Stack workflow configuration at `de89759…` against the last known triggered revision.
4. Check whether workflow path/name, permissions, concurrency, or event eligibility changed.
5. Use repository-wide Actions surface as corroboration when commit-scoped lookup returns zero.
6. Do not modify workflow configuration until the causal gap is proven.

## Governance Learning

`No run returned by tool X` means **NOT OBSERVED BY TOOL X**, not `NO RUN EXISTS`.
A trigger declaration in YAML proves eligibility configuration, not event delivery.
A successful sibling workflow proves the push reached Actions, but does not prove every workflow was scheduled.

## Closure Gate

EJR remains OPEN until the causal path is proven with GitHub evidence and the result is documented in a follow-up EJR/GOV update.
