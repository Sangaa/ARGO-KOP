# EJR-320 — GitHub Connector Self-Training: GT-012B/GT-012C Git Object Lifecycle

Date: 2026-08-23
Protocol: GOV-017
Status: GT-012B PARTIAL / GT-012C COMPLETED — CONTRACT-CHAIN BOUNDARY DOCUMENTED
Training mode: capability-first, not P6-first

## Objective

Train the Git object lifecycle independently of P6:

`blob → tree → commit → ref → read-back → cleanup`

The probe was intentionally isolated and created a disposable training branch. No production file or P6 logic was targeted.

## GT-012B Executed

1. `get_repo` verified repository identity and confirmed default branch `main`.
2. `create_branch` successfully created:
   `training/gt012b-git-object-lifecycle-20260823`
   from `main`.
3. `create_blob` successfully created an isolated training blob and returned:
   `c2c18662892200126aa8ddba1f4cc7d69e447001`
4. `create_tree` accepted the blob and base tree and returned a tree identifier.
5. `create_commit` was then attempted using the returned tree identifier.
6. `fetch_blob` independently read the returned blob successfully, confirming that at least the blob identifier crossed the write/read boundary correctly.
7. The disposable branch ref was reset to `main` after the failed commit attempt; no training commit was attached to the branch.

## GT-012B Failure observed

`create_commit` returned HTTP-style `422` validation failure:

`The tree parameter must be exactly 40 characters and contain only [0-9a-f].`

The returned `create_tree` identifier was:

`8a1481ee09515feb3067c40b40bbc1b07aa38d1`

The connector returned this value as successful tree creation, but the value is 39 hexadecimal characters. Repeating `create_tree` produced the same malformed-length identifier and the same downstream validation failure.

## GT-012C Contract-chain validation

The chain was analyzed as independent contracts rather than treating each successful call as proof that the next call can consume its output.

Observed chain:

`create_blob → fetch_blob`

This chain was valid in the probe: the blob SHA returned by creation was accepted by the independent read operation and the expected training content was recovered.

Observed chain:

`create_tree → create_commit`

This chain was invalid at the connector output boundary: `create_tree` returned a value that its downstream consumer explicitly rejected. No padding, truncation, or synthetic correction was attempted.

This establishes a reusable rule:

> A successful mutation envelope is not sufficient evidence that its returned identifier satisfies the contract of the next operation.

## Classification

The tree failure is not classified as:

- GitHub repository failure;
- permission failure;
- missing capability;
- P6 failure;
- generic commit creation failure in the provider API.

It is classified as:

`Connector output-contract / normalization defect OR tool-wrapper defect at create_tree output boundary.`

The evidence is strong because:

- `create_tree` reported success;
- its returned identifier violates the input contract explicitly enforced by `create_commit`;
- repeating `create_tree` reproduced the same malformed identifier;
- `create_commit` rejected the identifier deterministically.

## GT-012C Cleanup-surface inventory

The training also exposed a cleanup asymmetry:

- `update_ref` is exposed and was sufficient to reset the disposable branch to `main`.
- A dedicated branch-delete operation was not exposed in the current session surface.
- Therefore branch deletion could not be performed through the available contract in this session.
- The limitation is recorded rather than hidden.

This produces a second reusable rule:

> Every experimental mutation surface must be assessed for both creation capability and cleanup capability before it is used repeatedly.

A mutation surface without a known cleanup path is higher-risk and should require explicit isolation and a bounded rollback strategy.

## Important learning

1. **A successful upstream operation cannot be trusted solely from its success envelope. Validate identifiers before passing them downstream.**
2. **Cross-operation contracts must be tested as chains, not as isolated calls.**
3. **Connector normalization can introduce defects even when the underlying provider operation may have succeeded.**
4. **A downstream 422 can reveal an upstream output-contract defect.**
5. **When an identifier violates a documented downstream contract, stop rather than guessing, padding, truncating, or synthesizing the identifier.**
6. **Capability training must include contract-consistency tests between adjacent operations.**
7. **Read-back must be independent where possible; `create_blob → fetch_blob` is a positive example.**
8. **Mutation capability and cleanup capability are separate capabilities.**
9. **Resetting a ref is not equivalent to deleting the ref; the evidence must state which cleanup actually occurred.**
10. **A missing cleanup operation is itself connector knowledge and must be retained for future planning.**

## Boundary / cleanup

The disposable branch was created but no commit was attached to it. No production ref was changed and no production file was modified by this probe.

The blob/tree objects were not promoted into a branch commit. They therefore do not represent repository-visible production state.

The branch was reset to `main` using the exposed `update_ref` capability. A dedicated branch-delete capability was not available in the current session surface, so the branch remains as an isolated training branch rather than being falsely reported as deleted.

## P6 independence

This probe was selected solely to train Git object lifecycle and connector contract semantics. It does not change P6 status and must not be used as P6 execution evidence.

## Result

`GT-012B = PARTIAL / BLOCKED BY CONNECTOR OUTPUT CONTRACT`

`GT-012C = COMPLETED / CONTRACT-CHAIN AND CLEANUP BOUNDARY DOCUMENTED`

## Next task

`GT-013 — Broader Connector Surface Inventory and Capability-to-Evidence Mapping.`

Focus:
- continue capability-first training without selecting tools from P6;
- inventory remaining GitHub operations and their evidence classes;
- identify operation chains and cleanup requirements;
- distinguish implementation capability, session exposure, and evidence capability;
- only after the general map is sufficiently mature, revisit repository-specific problem mapping.

Session rule: Execute → document → read-back → verify → close.
