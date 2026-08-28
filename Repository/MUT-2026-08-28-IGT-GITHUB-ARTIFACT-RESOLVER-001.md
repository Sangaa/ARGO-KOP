# IGT GitHub Immutable Artifact Resolver — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-RESOLVER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`
Working branch: `hermuz/igt-github-artifact-resolver-20260828`
Status: `SOURCE + READ-BACK + PRE-DOC-HEAD CI VERIFIED / FINAL DOC-HEAD CI REQUIRED`
Authority: `NONE`

## Entry State

Trusted Resolver Adapter Execution Boundary is merged and post-merge verified:
- main `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`;
- Runtime/Integration `33208386402` — SUCCESS;
- Full-Stack `33208386395` — SUCCESS;
- M2 `33208386433` — SUCCESS.

## Goal and Claim Boundary

Implement a provider-specific read-only evidence acquisition adapter for exact GitHub repository artifacts.

`GITHUB ARTIFACT PROVENANCE != ARTIFACT TRUTH != MODEL EXECUTION AUTHENTICITY`.

Only immutable references are accepted:

`github+artifact://OWNER/REPO@FULL_40_HEX_COMMIT_SHA/PATH`.

Branches, tags, floating `main`, abbreviated SHAs, path traversal, empty path segments and backslash ambiguity are rejected before network access.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | read-only immutable-ref GitHub Contents API resolver | Y | Y |
| C02 | `Quality/Integration/test_github_evidence_resolver_adapter.py` | immutable-ref/request/read-only/JSON/404/non-file/reserved-identity/governed-gate regressions | Y | Y on pre-doc head |
| C03 | `Repository/IGT_GITHUB_ARTIFACT_RESOLVER_CONTRACT_2026-08-28.md` | artifact/provider/model-execution separation contract | Y | Y |
| C04 | current integration suite | deterministic discovery/execution | Y | Y on pre-doc head; final doc-head required |
| C05 | dedicated live GitHub read-only E2E | exact immutable provider fetch | N | FUTURE after deterministic closure |

## Hardened Boundaries

- No create/update/delete/write method exists on the adapter surface.
- Full 40-hex commit SHA is mandatory.
- GitHub Contents API GET always carries explicit immutable `ref=<commit_sha>`.
- Target must be `type=file` and expose GitHub blob SHA.
- Content must decode base64 -> UTF-8 -> JSON object.
- Artifact cannot self-inject `resolver_id`, `resolution_id`, or `requested_ref`.
- GitHub owner/repo/commit/path/blob SHA are captured as artifact provenance metadata.
- Confirmed 404 becomes an identified `UNAVAILABLE` acquisition, not mismatch.
- HTTP/network/decode/JSON failures fail closed.
- Credentials imply technical access only, not authority.

## Read-Back / Diff Reconciliation

Before PR creation, compare from exact base `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa` showed:
- behind = 0;
- exactly 4 changed paths;
- all paths declared by this transaction;
- no Runtime, cognition, memory, workflow, or repository write-path mutation.

## Pre-Documentation-Head CI Evidence

PR #81 was opened Draft from exact base with head:

`8eb264a2f89087ce9c6cd1a2a4e3f460df6d2fe9`.

Required CI succeeded:
- Runtime/Prototype/Integration workflow `33208672937` — SUCCESS;
- Full-Stack Repository Audit `33208672931` — SUCCESS.

Integration job:
- job `98976180502` — SUCCESS;
- PR merge-ref checkout `e6e4037bdc3449c47941c2c2467ae46f2f157ced`;
- checkout identity: `Merge 8eb264a2f89087ce9c6cd1a2a4e3f460df6d2fe9 into 90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`;
- command: `python -m pytest -q Quality/Integration`;
- result: `383 passed, 1 warning, 11 subtests passed`.

Main integration baseline before this transaction was 365. Therefore exactly 18 new resolver regressions were discovered/executed:

`383 - 365 = 18`.

The existing P2 identity-scope warning is unchanged and is not classified as a GitHub-resolver defect.

## Evidence Interpretation

`CI SUCCESS = DETERMINISTIC GITHUB RESOLVER MECHANICS VERIFIED ON THIS HEAD`.

It does not establish:
- a live GitHub API acquisition occurred through this adapter;
- GitHub authenticated any model-provider execution;
- JSON claims are true merely because GitHub stores them;
- model execution authenticity or cognitive benefit.

## Exact-Head Closure Rule

This documentation update changes the branch head. Therefore the CI above remains valid pre-documentation execution evidence but is not the final merge gate.

Required next sequence:
1. exact new-head Runtime/Integration + Full-Stack CI;
2. freeze after success;
3. reconcile current main, PR #81, open-PR surface and exact four-path diff;
4. expected-head-SHA squash merge only;
5. post-merge exact-main verification;
6. then design dedicated live read-only GitHub E2E.

## Explicit Non-Claims

- GitHub repository access is not model-provider authentication.
- Commit immutability stabilizes artifact identity; it does not validate artifact truth.
- Deterministic fixtures do not count as live provider evidence.
- Even later live GitHub acquisition proves artifact source, not model execution authenticity.

## Closure Boundary

Current bounded result:

`GITHUB ARTIFACT RESOLVER MECHANICS = SOURCE + READ-BACK + PRE-DOC-HEAD EXECUTION-VERIFIED`.

while:

`LIVE GITHUB ARTIFACT ACQUISITION = UNVERIFIED UNTIL DEDICATED E2E`.

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.
