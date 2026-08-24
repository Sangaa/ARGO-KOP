# EJR-320 — GitHub Connector Self-Training: GT-012 Read/Write Mutation Safety

Date: 2026-08-24
Protocol: GOV-017 / HERMUZ session protocol
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first, not P6-first

## Objective

Exercise the distinction between read capability and mutation capability using a disposable branch and disposable file, with mandatory read-back and deletion verification. No production logic is modified.

## Probe

Branch:
`probe/hermuz-gt012-20260824-v10`

Starting checkpoint:
`4f947676b8f1cc9185bdc9288ccf365e7b0d4805`

### Write

Created:
`Quality/Integration/.hermuz_gt012_probe`

Write commit:
`10a34d9efee605c5c32f07b6d69ac6fd9010dd28`

### Read-back

Exact file retrieval on the probe branch returned the expected marker and blob SHA:
`2d24c9b39a6cd5e7860626a4ddf520576fc61652`

### Delete

The exact blob SHA was supplied to the delete operation.

Delete commit:
`cac38a8aa62d9de3e51408a912fe1573f54cc65a`

### Final verification

A subsequent exact fetch returned provider `404 Not Found`, confirming the disposable file was removed from the probe branch.

## Learning

1. Repository read capability and mutation capability are distinct capabilities.
2. A successful write is not complete evidence until exact read-back confirms content and identity.
3. Delete requires the current blob identity; the read-back SHA is therefore part of mutation safety.
4. Final absence must be verified explicitly rather than inferred from the delete response.
5. A disposable branch isolates mutation training from `main` production state.
6. Provider `404` after a verified delete is interpreted as expected absence because repository, branch, and exact path identity were already validated.
7. Branch creation is itself a mutation capability and should be treated as part of the disposable-surface lifecycle.
8. Repeating an already-existing branch name produced a provider `422 Reference already exists`; this is a mutation precondition error, not evidence of repository failure.

## Boundary

This probe does not test PR creation, workflow execution, merge, or production-logic mutation. Those are separate capability classes.

No P6 selection or promotion is made from this training.

## Closure

`Execute → document → read-back → verify → cleanup → close`

GT-012 is complete for the exercised read/write/delete path.

Next capability-first training remains the authoritative sequence; P6 remains an application of connector knowledge, not the training selector.
