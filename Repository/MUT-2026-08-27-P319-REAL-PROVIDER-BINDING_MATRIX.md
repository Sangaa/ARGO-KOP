# P320 — Real ENG-006 → SRV-009 Provider Binding Matrix

Status: `GOVERNED / ISOLATED / NO-PROMOTION`

## Evidence Gap
P319 verified the connected spine reaches an injected ENG-006 consumer. The remaining gap is binding that consumer to the concrete governed GitHub repository connector through the existing ENG-006 → SRV-009 adapter.

## Existing Evidence
`Services/GITHUB_REPOSITORY_CONNECTOR.py` implements the provider-neutral connector using explicit environment configuration, current SHA checks, create/update separation, and post-write read-back.

## Minimal Mutation
Introduce only a provider factory/adapter binding that constructs `GitHubRepositoryConnector` from environment configuration and passes it to `execute_update`. No credentials are stored in the repository; no authorization source is changed.

## Acceptance
- Missing configuration fails closed.
- Authorized candidate only.
- Target current SHA is revalidated before update.
- Post-write read-back is mandatory.
- Connector errors remain explicit.
- No authority is inferred from GitHub access.
- Existing simulation fallback remains available when real provider binding is absent.
- Full CI gates pass.

## Non-Claims
This matrix does not authorize live mutation against `main`, automatic deployment, registry changes, or REL-009 promotion.

## Safety Boundary
End-to-end production evidence must use a controlled non-canonical test target/branch. Canonical `main` is not a valid mutation target for this proof.
