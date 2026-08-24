# EJR-323 — GitHub Connector GT-016 Issue Lifecycle

Date: 2026-08-24
Protocol: GOV-017 / Hermuz session build protocol
Status: CLOSED / DOCUMENTED / VERIFIED
Training mode: capability-first

## Objective

Exercise the GitHub Issue lifecycle as a distinct connector capability: create, fetch, comment, label, fetch comments, close, and verify final state. No production logic is modified and no P6 selection is made.

## Evidence

Issue created: `#28`
Title: `GT-016 capability probe — issue lifecycle`
Initial state: `open`

A top-level issue comment was created with id `5390542145`, then retrieved through the issue-comments surface. The exact marker was returned in the comment body.

The issue was labeled `documentation`; the subsequent issue snapshot showed the label and `comments = 1`.

The issue was then closed with `state_reason = completed`. Final snapshot showed `state = closed`, `comments = 1`, label retained, and a populated `closed_at` timestamp.

## Learning

1. Issue creation, issue retrieval, comment mutation/readback, label mutation, and state transition are separate observable capabilities.
2. Comment creation is verified independently through the comments endpoint rather than inferred from the issue comment count.
3. Label mutation is reflected in the normalized issue snapshot.
4. Closing an issue can carry an explicit completion reason; the final snapshot is the authoritative state evidence.
5. Issue lifecycle can be exercised without touching repository files or production logic.
6. This capability is operationally distinct from pull-request lifecycle and GitHub Actions execution.

## Boundary

This probe does not test issue assignment, milestone mutation, locking, reactions, or issue-to-PR conversion. Those remain separate capabilities until explicitly trained.

## Closure

`Execute → document → read-back → verify → close`

GT-016 is complete for the exercised issue lifecycle path.
