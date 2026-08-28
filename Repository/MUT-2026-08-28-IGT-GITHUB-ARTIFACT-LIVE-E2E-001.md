# IGT GitHub Immutable Artifact — Live Read-Only E2E

Transaction ID: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-LIVE-E2E-001`
Base: `main@45ed9275e99ea59680507e25b52f9ba4183dba47`
Branch: `hermuz/igt-github-artifact-live-e2e-20260828`
Status: `CLOSED / HISTORICAL LIVE E2E EVIDENCE / NOT CANONICAL FEATURE PATH`
Authority: `NONE`

## Entry State

Deterministic GitHub artifact resolver was already merged and post-merge verified on canonical main:
- main `45ed9275e99ea59680507e25b52f9ba4183dba47`;
- Runtime `33208878627` — SUCCESS;
- Full-Stack `33208878616` — SUCCESS;
- M2 `33208878641` — SUCCESS.

## Bounded E2E Claim

Verified:

`LIVE GITHUB IMMUTABLE ARTIFACT ACQUISITION = VERIFIED`.

Not verified:

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED`.

This distinction is mandatory. GitHub verified the retrieval surface for one exact repository artifact; it did not attest that any model/provider described by arbitrary artifact content actually executed.

## Tested Head

The live execution ran against exact isolated branch head:

`113f8cc09f0b41e174b69b844de72dedb2be1caa`.

The historical branch contains:
- this mutation/evidence record;
- controlled fixture `Quality/E2E/IGT_GITHUB_ARTIFACT_LIVE_FIXTURE.json`;
- read-only workflow `.github/workflows/igt-github-artifact-live-e2e.yml`.

The fixture deliberately declares:
- `claim_boundary = ARTIFACT_PROVENANCE_ONLY`;
- `model_execution_claim = NONE`.

## Live Workflow Evidence

Workflow:

`IGT GitHub Immutable Artifact Live E2E`.

Run:

`33209003534` — SUCCESS.

Job:

`98977287929` — SUCCESS.

All workflow steps succeeded, including:
- checkout exact branch commit;
- setup Python;
- execute live immutable artifact acquisition.

### Runtime permissions

GitHub reported:
- `Contents: read`;
- `Metadata: read`.

No contents-write permission was present.

`repository_mutation = NONE`.

Cleanup was not required because the live provider operation was read-only.

## Exact Checkout Evidence

The workflow fetched and checked out:

`113f8cc09f0b41e174b69b844de72dedb2be1caa`.

`git log -1 --format=%H` returned the same exact SHA.

The adapter then constructed its immutable provider reference from `GITHUB_SHA` rather than a floating branch name.

## Live Provider Result

The workflow emitted:

- `result = PASS`;
- repository = `Sangaa/ARGO-KOP`;
- commit SHA = `113f8cc09f0b41e174b69b844de72dedb2be1caa`;
- fixture path = `Quality/E2E/IGT_GITHUB_ARTIFACT_LIVE_FIXTURE.json`;
- GitHub blob SHA = `cc56558060c68913e1f0416c7ae032ea358c99f5`;
- acquisition ID = `GH-EVID-PARTICIPANT-000001`;
- claim = `LIVE_GITHUB_IMMUTABLE_ARTIFACT_ACQUISITION_VERIFIED`;
- model execution authenticity = `UNVERIFIED`;
- repository mutation = `NONE`.

The returned artifact passed exact owner/repository/commit/path checks and preserved the GitHub blob identity.

## Live Negative Retrieval

The same adapter/session requested a deliberately absent path at the exact same immutable SHA:

`Quality/E2E/THIS_PATH_MUST_NOT_EXIST.json`.

Observed state:

`UNAVAILABLE`.

This confirms the live provider path preserves the intended distinction:

`NOT RETRIEVABLE AT EXACT IMMUTABLE REF != CONTENT MISMATCH`.

## Evidence Classification

### Proven by this run

- production GitHub Contents API can be reached by the implemented adapter;
- exact full-SHA immutable reference is usable live;
- real repository artifact content and GitHub blob SHA are acquired;
- exact missing path maps to `UNAVAILABLE`;
- workflow/provider path is read-only under observed permissions;
- no repository mutation was required or performed.

### Not proven by this run

- truth of arbitrary JSON claims stored in GitHub;
- model/provider execution identity;
- participant B0/L1/L2 authenticity;
- model learning/cognitive benefit;
- governance authority.

## Transferable Learning

`PROVIDER-BACKED EVIDENCE MUST BE DECOMPOSED BY WHAT THE PROVIDER ACTUALLY ATTESTS`.

GitHub can attest repository artifact retrieval from an immutable repository state. It cannot attest model execution merely because an artifact stored in the repository claims that execution occurred.

Therefore:

`GITHUB ARTIFACT PROVENANCE != MODEL EXECUTION PROVENANCE`.

This boundary should be preserved for every future evidence provider.

## Branch Lifecycle

This branch is classified as:

`HISTORICAL LIVE E2E EVIDENCE / PRESERVE / DO NOT TREAT AS CANONICAL FEATURE PATH`.

The live fixture/workflow are not automatically promoted to main merely because the probe succeeded. Any decision to retain a reusable live E2E workflow canonically requires a separate controlled mutation with its own utility/maintenance rationale.

No PR/merge from this historical evidence branch is required for this E2E result.

## Closure

`LIVE GITHUB IMMUTABLE ARTIFACT ACQUISITION = VERIFIED WITHIN EXACT ISOLATED E2E SCOPE`.

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

`SESSION E2E TRANSACTION = CLOSED / RESUME-SAFE`.
