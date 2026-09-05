# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 11 Corrective Matrix

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-11 SECOND CORRECTIVE REPAIR APPLIED / EXACT-HEAD FOUR-FAMILY CI PENDING`

Material Unit-11 Matrix head: `f7e74beda97e548cb48f1aaa562a4bee76e034d1`
First guard-repair head: `a85043d5377aa915088721b4c04e400827dc2575`
First Corrective-Matrix head: `a87996e4fa250d7f9c5dba3c24dfe0d033559668`
Historical-disposition status-marker repair head: `25db8f6c9a5fdc0117949df51dc73c08c2ee1c3b`

## Failure classification — first corrective issue

Unit-11 material head produced:

- Real Mutation Matrix — SUCCESS (`33975709022`)
- M2 — SUCCESS (`33975709058`)
- Full-Stack — SUCCESS (`33975709015`)
- Runtime/Integration — FAILURE (`33975708939`)

Runtime prototype and integration jobs were successful; only repository integrity failed.

The newly introduced Unit-11 guard searched for `MEM-001 MUST NOT be treated as a duplicate` while the valid current source representation contained the identifier in Markdown code ticks: `` `MEM-001` MUST NOT be treated as a duplicate ``.

Classification:

`NEW GUARD REPRESENTATION DEFECT / SOURCE SEMANTICS VALID / NO UNIT-11 SOURCE ROLLBACK`.

The guard was corrected without changing source semantics.

## Failure classification — second exact-head issue

The first Corrective-Matrix head `a87996e4fa250d7f9c5dba3c24dfe0d033559668` restored four-family triggering, but Runtime/Integration run `33975808383` still failed only in repository integrity.

Decoded exact job logs established:

- `239 passed`;
- `1 failed`;
- sole failure: `test_models_p12_historical_disposition.py::test_status_marks_numeric_restoration_resolved_without_partition_promotion`;
- required stable marker: `numeric restoration disposition resolved / no blind recreation`.

The marker had been dropped when `_FOLDER_STATUS.md` was synchronized for Unit 11, even though the underlying Unit-4 historical disposition remained valid and the stronger permanent sentence `No missing artifact is to be recreated merely to complete a numeric sequence.` was preserved.

Classification:

`VALID UNIT-4 STATUS INVARIANT LOST DURING UNIT-11 STATUS REWRITE / CURRENT AUTHORITY SPLIT VALID / RESTORE MARKER, DO NOT WEAKEN GUARD`.

The status repair at `25db8f6c9a5fdc0117949df51dc73c08c2ee1c3b` restored exactly:

`Numeric restoration disposition resolved / no blind recreation.`

No Unit-11 semantic source, evidence row, Memory-domain artifact, historical disposition or partition maturity was rolled back.

## Trigger-family requirement

This updated Corrective Matrix is the exact-head trigger surface for the final Unit-11 corrective state. SUCCESS is required from all four families on the same resulting SHA.

## Invariants reinforced

`VALID SEMANTIC BOUNDARY != BUGGY TEST LITERAL`.

`STATUS REWRITE != PERMISSION TO DROP A STILL-VALID STABLE INVARIANT`.

A historical guard may be stale in one transaction and valid in another; disposition depends on whether the protected representation remains part of the stable contract.

## Next gate

1. exact-head SUCCESS for M2, Real Mutation Matrix, Full-Stack and Runtime/Integration on the head containing this updated Corrective Matrix;
2. only then begin Unit 12 active-model authority overlap reconciliation;
3. no Priority-12 or Models closure is implied by Unit-11 success.
