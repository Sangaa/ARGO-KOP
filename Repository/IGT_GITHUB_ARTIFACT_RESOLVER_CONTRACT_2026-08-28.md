# IGT GitHub Immutable Artifact Resolver Contract — 2026-08-28

Status: `CONTROLLED CANDIDATE / READ-ONLY PROVIDER ADAPTER / NOT MODEL AUTHORITY`
Transaction: `MUT-2026-08-28-IGT-GITHUB-ARTIFACT-RESOLVER-001`
Authority: `NONE`

## Purpose

Define a provider-specific read-only adapter that acquires external IGT evidence artifacts from GitHub by exact repository path and immutable commit SHA.

The adapter is a provenance mechanism for **repository artifacts**. It is not a model-provider execution verifier.

## Core Separation

`GITHUB ARTIFACT PROVENANCE != ARTIFACT TRUTH != MODEL EXECUTION AUTHENTICITY`.

GitHub can establish which bytes are stored at an exact commit/path. It cannot establish that claims written inside those bytes are true.

## Immutable Reference

Accepted form:

`github+artifact://OWNER/REPO@FULL_40_HEX_COMMIT_SHA/PATH`

Rejected before network access:
- branch names;
- tags;
- `main` or default branch;
- abbreviated SHAs;
- missing owner/repository/path;
- empty path segments;
- `.` / `..` traversal;
- backslash ambiguity.

## Read-Only Boundary

The adapter exposes only:
- participant evidence acquisition;
- attestation evidence acquisition.

It exposes no create/update/delete/write operation.

The GitHub API request is a GET to the Contents API with explicit:

`?ref=<full commit SHA>`.

## Provider Response Requirements

A successful target must:
- be `type=file`;
- expose a GitHub blob SHA;
- contain base64-encoded UTF-8 content;
- decode to a JSON object.

Directory-like/non-file targets fail closed.

## Resolver Identity Boundary

Artifact JSON may not contain:
- `resolver_id`;
- `resolution_id`;
- `requested_ref`.

These remain controlled by the governed adapter-execution gate.

The GitHub adapter may append repository provenance metadata:
- owner;
- repository;
- commit SHA;
- path;
- GitHub blob SHA.

Those fields identify the artifact acquisition source only.

## Missing Evidence

Confirmed GitHub HTTP 404 is represented as an identified acquisition with:

`status = UNAVAILABLE`.

This means the artifact was not retrievable at the exact immutable reference.

It is not automatically an evidence mismatch.

Other HTTP, network, decoding, or JSON failures are explicit adapter failures.

## Credentials

GitHub credentials are loaded from runtime environment for production configuration.

Required law inherited from ARGO connector architecture:

`TECHNICAL ACCESS != AUTHORITY`.

Possession of a GitHub token does not make the adapter authoritative over model claims.

## Integration with Trusted Adapter Gate

A registered GitHub artifact resolver can flow through the existing governed adapter gate.

A matching deterministic transport fixture may reach:

`APPROVED_ADAPTER_PATH_CORRELATED`.

But even then:

`external_authenticity = INCONCLUSIVE`

and:

`provider_backed_authenticity = NOT_ESTABLISHED`.

This is intentional because deterministic transport fixtures do not prove a live GitHub acquisition, and GitHub acquisition does not prove model execution.

## Live E2E Requirement

Before claiming live provider-backed artifact acquisition, a separate E2E must:
1. use a real GitHub credential/runtime boundary;
2. fetch a controlled artifact from an exact immutable commit/path;
3. preserve request/ref identity;
4. preserve returned blob SHA and content digest/evidence;
5. avoid repository mutation;
6. prove cleanup is unnecessary because the path is read-only;
7. preserve exact workflow/commit identity.

Only then may the bounded claim become:

`LIVE GITHUB ARTIFACT ACQUISITION = VERIFIED`.

Even that does not become:

`MODEL EXECUTION AUTHENTICITY = VERIFIED`.

## Current Boundary

`GITHUB ARTIFACT RESOLVER MECHANICS = CANDIDATE`.

`LIVE GITHUB PROVIDER ACQUISITION = UNVERIFIED`.

`MODEL EXECUTION AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`AUTHORITY = NONE`.
