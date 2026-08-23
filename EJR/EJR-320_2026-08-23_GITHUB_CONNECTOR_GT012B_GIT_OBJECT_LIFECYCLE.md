# EJR-320 — GitHub Connector Self-Training: GT-012B Git Object Lifecycle

Date: 2026-08-23
Protocol: GOV-017
Status: PARTIALLY COMPLETED — TOOL CONTRACT FAILURE OBSERVED
Training mode: capability-first, not P6-first

## Objective

Train the Git object lifecycle independently of P6:

`blob → tree → commit → ref → read-back → cleanup`

The probe was intentionally isolated and created a disposable training branch. No production file or P6 logic was targeted.

## Executed

1. `get_repo` verified repository identity and confirmed default branch `main`.
2. `create_branch` successfully created:
   `training/gt012b-git-object-lifecycle-20260823`
   from `main`.
3. `create_blob` successfully created an isolated training blob and returned:
   `c2c18662892200126aa8ddba1f4cc7d69e447001`
4. `create_tree` accepted the blob and base tree and returned a tree identifier.
5. `create_commit` was then attempted using the returned tree identifier.

## Failure observed

`create_commit` returned HTTP-style `422` validation failure:

`The tree parameter must be exactly 40 characters and contain only [0-9a-f].`

The returned `create_tree` identifier was:

`8a1481ee09515feb3067c40b40bbc1b07aa38d1d`

The connector returned this value as successful tree creation, but the value is 39 hexadecimal characters. Repeating `create_tree` produced the same malformed-length identifier and the same downstream validation failure.

## Classification

This is not classified as:

- GitHub repository failure;
- permission failure;
- missing capability;
- P6 failure;
- commit creation failure in the provider API generally.

It is classified as:

`Connector output-contract / normalization defect OR tool-wrapper defect at create_tree output boundary.`

The evidence is especially strong because:

- `create_tree` reported success;
- its returned identifier violates the input contract explicitly enforced by `create_commit`;
- repeating the same operation reproduced the same malformed identifier;
- `create_commit` rejected the identifier deterministically.

## Important learning

1. **A successful upstream operation cannot be trusted solely from its success envelope. Validate identifiers before passing them downstream.**
2. **Cross-operation contracts must be tested as chains, not as isolated calls.**
3. **Connector normalization can introduce defects even when the underlying provider operation may have succeeded.**
4. **A downstream 422 can reveal an upstream output-contract defect.**
5. **When an identifier violates a documented downstream contract, stop rather than guessing, padding, truncating, or synthesizing the identifier.**
6. **Capability training must include contract-consistency tests between adjacent operations.**

## Cleanup / boundary

The disposable branch was created but no commit was attached to it. No production ref was changed and no production file was modified by this probe.

The blob/tree objects were not promoted into a branch commit. They therefore do not represent repository-visible production state.

Because the currently exposed connector surface does not provide a dedicated branch-delete operation, the branch cannot be deleted through the available tool contract in this session. This is recorded as a cleanup-surface limitation rather than hidden.

## P6 independence

This probe was selected solely to train Git object lifecycle semantics. It does not change P6 status and must not be used as P6 execution evidence.

## Result

GT-012B = PARTIAL / BLOCKED BY CONNECTOR OUTPUT CONTRACT

Next task:
`GT-012C — Connector contract-chain validation and cleanup-surface inventory.`

Focus:
- identify operations whose outputs feed other operations;
- validate returned identifiers before chaining;
- inventory cleanup operations for each mutation surface;
- distinguish provider success from connector-contract validity.

Session rule: Execute → document → read-back → verify → close.
