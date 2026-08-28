# IGT GitHub Immutable Artifact Resolver — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-RESOLVER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`
Working branch: `hermuz/igt-github-artifact-resolver-20260828`
Status: `PRE-WRITE / PROVIDER-BACKED ARTIFACT ACQUISITION`
Authority: `NONE`

## Entry State

Trusted Resolver Adapter Execution Boundary is merged and post-merge verified:
- main `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`;
- Runtime/Integration `33208386402` — SUCCESS;
- Full-Stack `33208386395` — SUCCESS;
- M2 `33208386433` — SUCCESS.

## Goal

Implement the first real provider-specific **read-only evidence acquisition adapter** using GitHub immutable repository artifacts.

The claim is deliberately narrow:

`GITHUB-BACKED ARTIFACT ACQUISITION != MODEL EXECUTION AUTHENTICITY`.

The adapter may establish that an exact JSON evidence artifact was fetched from an exact GitHub repository path at an exact immutable commit SHA. It may not establish that the model/provider described inside that JSON actually executed.

## Reference Contract

Only immutable references are accepted:

`github+artifact://OWNER/REPO@40_HEX_COMMIT_SHA/PATH`

Branch names, tags, default-branch reads, floating `main`, abbreviated SHAs, and path traversal are rejected.

Participant and attestation package refs may point to separate artifacts at the same or different immutable commits.

## Target Invariants

1. Adapter is read-only; no GitHub write method exists in its surface.
2. Reference must include owner, repo, full 40-hex commit SHA, and non-empty normalized path.
3. Mutable refs (`main`, branches, tags, short SHA) are rejected before network access.
4. Path traversal / empty segments / backslash ambiguity are rejected.
5. HTTP request must address GitHub Contents API with explicit immutable `ref=<commit_sha>`.
6. GitHub response must be a file, not directory/submodule/symlink-like target.
7. Returned GitHub blob SHA and content are captured in acquisition observation metadata.
8. Content must decode as UTF-8 JSON object.
9. The JSON artifact must be an observation payload only; resolver identity fields remain forbidden and are injected by the governed gate.
10. HTTP 404 maps to an explicit `UNAVAILABLE` observation from an identified acquisition event rather than a fabricated mismatch.
11. Other HTTP/network/decode failures fail closed as adapter errors.
12. Credentials/repository access do not imply authority.
13. GitHub artifact provenance proves only repository artifact acquisition.
14. Model execution authenticity remains `UNVERIFIED / INCONCLUSIVE`.
15. Deterministic transport tests verify adapter mechanics; a later live GitHub E2E is required before provider-backed acquisition is called live-verified.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | ADD | read-only immutable GitHub artifact resolver implementing existing evidence adapter interface | N | N |
| C02 | `Quality/Integration/test_github_evidence_resolver_adapter.py` | ADD | parsing, immutability, transport, JSON, 404/unavailable, reserved identity, and nonclaim regressions | N | N |
| C03 | `Repository/IGT_GITHUB_ARTIFACT_RESOLVER_CONTRACT_2026-08-28.md` | ADD | immutable reference/provider boundary contract | N | N |
| C04 | current integration suite | VERIFY | exact-head test discovery/execution | N | N |
| C05 | dedicated live GitHub read-only E2E | FUTURE | fetch a controlled immutable artifact by exact commit/path and preserve provider response evidence | N | N |

## Explicit Non-Claims

- GitHub account/repository access is not model-provider authentication.
- A JSON artifact saying `source_model=X` does not prove model X produced it.
- Commit immutability stabilizes artifact identity; it does not validate artifact truth.
- Successful deterministic tests do not count as live GitHub provider evidence.
- No model execution or cognitive-benefit claim is promoted by this transaction.

## Closure Boundary

Potential deterministic result:

`GITHUB ARTIFACT RESOLVER MECHANICS = EXECUTION-VERIFIED`.

while:

`LIVE GITHUB ARTIFACT ACQUISITION = UNVERIFIED UNTIL E2E`.

and:

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.
