# EJR-321 — GitHub Connector Self-Training: GT-013 Branch Lifecycle + Sequential Update Safety

Date: 2026-08-24
Protocol: GOV-017 / HERMUZ session protocol
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first

## Objective

Extend GT-012 from disposable read/write/delete safety into branch-scoped sequential mutation: create a disposable branch, create a file on that branch, read its exact blob identity, update using that identity, read back the new identity, delete using the new identity, and verify final absence.

## Probe

Branch: `probe/hermuz-gt013-20260824-v1`

### Branch creation

Branch was created from `main` and subsequently addressed explicitly by all mutations.

### Create

File: `Quality/Integration/.hermuz_gt013_probe`

Create commit: `da202ac2aacdde32e7a870e2c2741bebb951b64c`

Initial blob SHA: `1a8c05051a777a2a4c96a31a879e2626647426e8`

### Sequential update

Update used the exact current blob SHA and produced:

Commit: `0335626d89ba5a459614d5d7a93a7a744ec83db0`

New blob SHA: `2dcb5d107d303ac1e56158c00c84c29c192eecc7`

Read-back confirmed the updated marker and new blob identity.

### Cleanup

Delete used the new exact blob SHA.

Delete commit: `2165605a3833e77930625cec75f200aa85c0fed6`

Final exact fetch returned `404 Not Found`.

## Learning

1. Branch creation can isolate an entire mutation lifecycle from `main`.
2. File update is a separate capability from create/delete and requires the current blob identity.
3. A successful update should be followed by exact read-back before the next mutation.
4. The blob SHA changes after update and the new SHA becomes the safety token for subsequent deletion.
5. Explicit branch targeting prevents accidental default-branch mutation.
6. Cleanup must be verified independently through final absence.

## Boundary

This probe does not test PR creation, merge, workflow dispatch, branch deletion, force-ref updates, or production promotion. Those remain separate capability classes.

## Closure

`Create branch → create → read-back → update by SHA → read-back → delete by SHA → verify absence → close`

GT-013 is closed for the exercised branch-scoped sequential mutation path.
