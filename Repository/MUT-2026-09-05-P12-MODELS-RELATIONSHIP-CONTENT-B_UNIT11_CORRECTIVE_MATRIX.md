# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 11 Corrective Matrix

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-11 CORRECTIVE GUARD REPAIR APPLIED / EXACT-HEAD FOUR-FAMILY CI PENDING`

Material Unit-11 Matrix head: `f7e74beda97e548cb48f1aaa562a4bee76e034d1`
Guard-repair head: `a85043d5377aa915088721b4c04e400827dc2575`

## Failure classification

Unit-11 material head produced:

- Real Mutation Matrix — SUCCESS (`33975709022`)
- M2 — SUCCESS (`33975709058`)
- Full-Stack — SUCCESS (`33975709015`)
- Runtime/Integration — FAILURE (`33975708939`)

Runtime prototype and integration jobs were successful; only the repository integrity job failed.

Direct post-failure review found a representation defect in the newly introduced Unit-11 guard: it searched for the source sentence `MEM-001 MUST NOT be treated as a duplicate` while the actual stable source representation correctly contained the identifier in Markdown code ticks: `` `MEM-001` MUST NOT be treated as a duplicate ``.

Classification:

`NEW GUARD REPRESENTATION DEFECT / SOURCE SEMANTICS VALID / NO UNIT-11 SOURCE ROLLBACK`.

The guard was corrected to test the exact current source representation. No semantic contract, evidence row, status claim or Memory-domain artifact was changed by the corrective commit.

## Trigger-family requirement

The guard-only corrective commit triggered only three workflow families. This Corrective Matrix exists to restore exact-head validation across all four required families on one SHA rather than treating a three-family head as closure evidence.

## Invariant

`VALID SEMANTIC BOUNDARY != BUGGY TEST LITERAL`.

When a new guard misstates the representation it intends to protect, repair the guard; do not roll back a verified source boundary merely to satisfy the mistaken literal.

## Next gate

Exact-head SUCCESS for M2, Real Mutation Matrix, Full-Stack and Runtime/Integration on the head containing this Corrective Matrix is required before Unit 12 begins.
