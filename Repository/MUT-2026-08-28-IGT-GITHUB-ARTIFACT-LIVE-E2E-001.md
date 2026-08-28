# IGT GitHub Immutable Artifact — Live Read-Only E2E

Transaction ID: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-LIVE-E2E-001`
Base: `main@45ed9275e99ea59680507e25b52f9ba4183dba47`
Branch: `hermuz/igt-github-artifact-live-e2e-20260828`
Status: `PRE-EXECUTION / ISOLATED READ-ONLY PROVIDER E2E`
Authority: `NONE`

## Entry State

Deterministic GitHub artifact resolver is merged and post-merge verified:
- Runtime `33208878627` — SUCCESS;
- Full-Stack `33208878616` — SUCCESS;
- M2 `33208878641` — SUCCESS.

## E2E Claim

The live E2E may prove only:

`LIVE GITHUB IMMUTABLE ARTIFACT ACQUISITION = VERIFIED`.

It may not prove:

`MODEL EXECUTION AUTHENTICITY = VERIFIED`.

## Design

1. Isolated branch from exact main.
2. Controlled JSON fixture contains no model/provider claim and no resolver identity.
3. Workflow permission: `contents: read` only.
4. Runtime passes GitHub's workflow token to `ARGO_GITHUB_TOKEN`.
5. Adapter constructs immutable ref using the workflow's exact `GITHUB_SHA`.
6. Fetch fixture through real GitHub Contents API.
7. Assert owner/repo/commit/path/blob SHA provenance.
8. Fetch a deliberately absent path at the same immutable SHA and assert `UNAVAILABLE`.
9. No repository write occurs in workflow; cleanup is not applicable.
10. Preserve run/job/log evidence and exact branch SHA.

## Non-Claims

- GitHub proves repository artifact retrieval, not the truth of arbitrary JSON claims.
- Workflow token access is technical access, not governance authority.
- This probe does not populate IGT B0/L1/L2 participant evidence.
- This probe does not establish cognitive effect.
