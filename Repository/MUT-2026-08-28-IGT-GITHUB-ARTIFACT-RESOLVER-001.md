# IGT GitHub Immutable Artifact Resolver — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-RESOLVER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`
Working branch: `hermuz/igt-github-artifact-resolver-20260828`
Status: `SOURCE IMPLEMENTED / READ-BACK RECONCILED / DETERMINISTIC CI PENDING`
Authority: `NONE`

## Entry State

Trusted Resolver Adapter Execution Boundary is merged and post-merge verified:
- main `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`;
- Runtime/Integration `33208386402` — SUCCESS;
- Full-Stack `33208386395` — SUCCESS;
- M2 `33208386433` — SUCCESS.

## Goal

Implement the first provider-specific read-only evidence acquisition adapter using GitHub immutable repository artifacts.

Narrow claim:

`GITHUB-BACKED ARTIFACT ACQUISITION != MODEL EXECUTION AUTHENTICITY`.

## Reference Contract

Only:

`github+artifact://OWNER/REPO@40_HEX_COMMIT_SHA/PATH`

is accepted.

Branches, tags, floating `main`, abbreviated SHAs, traversal, empty segments and backslash ambiguity are rejected before network access.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | read-only immutable-ref GitHub Contents API adapter implementing existing evidence resolver interface | Y | Y source/read-back |
| C02 | `Quality/Integration/test_github_evidence_resolver_adapter.py` | immutable-ref, request, read-only, JSON, 404, non-file, reserved identity, governed-gate and nonclaim regressions | Y | Y source/read-back; CI pending |
| C03 | `Repository/IGT_GITHUB_ARTIFACT_RESOLVER_CONTRACT_2026-08-28.md` | provider/artifact/model-execution separation contract | Y | Y source/read-back |
| C04 | current integration suite | exact-head deterministic test discovery/execution | Y | CI pending |
| C05 | dedicated live GitHub read-only E2E | real immutable artifact fetch | N | FUTURE after deterministic gate |

## Hardened Boundaries

- Adapter surface contains no create/update/delete/write method.
- Full 40-hex commit SHA required.
- GET Contents API request always includes explicit immutable `ref=<commit_sha>`.
- Target must be `type=file` with GitHub blob SHA.
- Content must be valid base64 -> UTF-8 -> JSON object.
- Artifact cannot self-inject `resolver_id`, `resolution_id`, or `requested_ref`.
- GitHub owner/repo/commit/path/blob SHA are appended as artifact provenance metadata.
- Confirmed 404 becomes identified `UNAVAILABLE`, not mismatch.
- Other HTTP/network/decode failures fail closed.
- Credentials imply technical access only, not authority.

## Read-Back / Diff Reconciliation

Compare from exact base `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa` showed:
- ahead = 4 before this documentation update;
- behind = 0;
- exactly 4 changed paths;
- all paths declared by this transaction;
- no Runtime, cognition, memory, workflow, or write-path mutation.

## Explicit Non-Claims

- GitHub repository access is not model-provider authentication.
- JSON claims do not authenticate themselves.
- Commit immutability stabilizes artifact identity but does not validate artifact truth.
- Deterministic transport fixtures do not count as live GitHub provider evidence.
- Even future live GitHub acquisition will prove artifact source, not model execution authenticity.

## Verification Plan

1. Implement adapter/tests/contract — PASS.
2. Read-back and exact diff reconciliation — PASS.
3. Open Draft PR from exact main — NEXT.
4. Require exact-head Runtime/Integration + Full-Stack CI; inspect actual test count and merge-ref.
5. Document failure/repair if any.
6. Final documentation-head CI → freeze → expected-SHA squash merge → post-merge exact-main verification.
7. Only after deterministic closure, design a dedicated read-only live GitHub E2E.

## Closure Boundary

Potential deterministic result:

`GITHUB ARTIFACT RESOLVER MECHANICS = EXECUTION-VERIFIED`.

while:

`LIVE GITHUB ARTIFACT ACQUISITION = UNVERIFIED UNTIL E2E`.

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.
