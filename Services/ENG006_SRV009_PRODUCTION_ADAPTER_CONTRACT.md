# ENG-006 → SRV-009 PRODUCTION ADAPTER CONTRACT

---

Document ID: `SRV-009-ADAPTER-001`
Status: `Contract / Integrity Hold`
Category: `Execution Integration`
Scope: `Production Adapter Boundary`

## Purpose

Define the minimum contract required before `ENG-006` may obtain a production callable path to `SRV-009`.

This document does **not** implement the adapter and does not grant runtime or repository authority.

## Required Capabilities

A production adapter SHALL provide all of the following through a governed connector:

1. `read_current(path)` — return the current repository artifact and its current content/blob identity, or a confirmed not-found result.
2. `create_file(path, content, commit_message)` — create a previously confirmed absent artifact and return the resulting commit identity.
3. `update_file(path, content, commit_message, current_sha)` — replace an existing artifact only against the currently observed content/blob identity.
4. `read_back(path)` — read the artifact after mutation and return its persisted content and identity.

## Mandatory Properties

- No mutation may be selected from filename intent alone.
- Update requires current identity evidence.
- Create requires confirmed absence.
- Post-write read-back is mandatory.
- Read-back content MUST equal the governed candidate content before successful completion is reported.
- Connector failures, race conditions, ambiguous identity, or read-back mismatch MUST produce an explicit failure/hold.
- The adapter MUST preserve the separation between technical write success and governed update acceptance.
- The adapter MUST NOT create canonical authority merely because technical repository access exists.

## ENG-006 Boundary

`ENG-006` may supply an authorized execution candidate to this adapter.

The adapter SHALL NOT infer authorization, invent validation, or bypass `SRV-005`/applicable governance controls.

## SRV-009 Boundary

`SRV-009` remains the governed update service and authoritative service contract.

This adapter is only the executable connector boundary required to make the existing `ENG-006 → SRV-009` relationship callable.

## Current Status

`OPEN — PRODUCTION CONNECTOR NOT IMPLEMENTED`

The current repository contains the governed write dispatcher and a validated prototype seam, but no production repository connector satisfying all four required capabilities under the Runtime path.

## Closure Evidence Required

P3 may only be promoted to `EXECUTABLE-VERIFIED` when a real connector implementation:

- is callable from the governed Runtime path;
- uses an authorized execution candidate;
- invokes the `SRV-009` governed service boundary;
- performs real repository mutation only through the approved connector;
- performs post-write read-back;
- records execution and update traceability;
- passes integration, integrity, and full-stack tests on the same HEAD.

---

End of Document
