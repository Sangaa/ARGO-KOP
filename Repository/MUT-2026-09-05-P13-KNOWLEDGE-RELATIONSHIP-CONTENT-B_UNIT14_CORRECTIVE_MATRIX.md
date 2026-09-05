# CORRECTIVE MATRIX — P13 KNOWLEDGE B / UNIT 14 GUARD REPRESENTATION REPAIR

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Failed material head: `56531b9861fa5603cea6fdc443bf593ac00f5014`
Failed workflow: `ARGO Runtime Prototype and Integration Tests` run `33984873042`
Failure scope: `integrity-tests only / 1 assertion / 297 passed`
Corrective guard commit: `09ac4710a2694d9f560939a3770ad047d66f6ff3`
State: `CORRECTIVE GUARD TYPE-NORMALIZATION / MATERIAL UNIT-14 DATA UNCHANGED`

## Root cause

The Unit-14 path-level allocation manifest is correct. The guard parsed TSV rows with `str.split`, producing lists, but constructed the expected exact transform as tuples. Python sequence equality therefore failed despite identical field values.

`VALUE EQUALITY INTENT != PYTHON LIST/TUPLE TYPE EQUALITY`.

## Tool-bound execution note

The preferred atomic Git-data tree creation for the corrective pair was blocked by the execution tool before GitHub mutation. The correction therefore used the permitted Contents API in two bounded commits: first the one-line guard representation repair, then this Matrix record. No force update or policy bypass was used.

## Corrective scope

Only two logical paths belong to this corrective:

1. `Quality/Integrity/test_knowledge_p13_rep012_exact_allocation_binding.py`
2. this corrective Matrix

No manifest, REP-012 binding, Knowledge source, or canonical control-plane file changed.

## Corrective invariant

The expected transform uses the same row representation returned by the parser while preserving all substantive assertions:

- 50 inventory rows;
- 50 manifest rows;
- unique paths;
- exact path + physical-role equality;
- `ALLOCATED` allocation state;
- `NONE_BY_ALLOCATION` authority effect;
- `P13_TRANSACTION_A_EXACT_INVENTORY` source evidence;
- exact sorted-path digest;
- canonical REP-012 fold remains OPEN.

## Required gate

`MATRIX COMMIT → COMPARE LOGICAL 2-PATH CORRECTIVE CHAIN → ALL FOUR WORKFLOW FAMILIES EXPLICITLY COMPLETED/SUCCESS`

No Unit-15 work may begin before this gate passes.

---

End of Unit-14 Corrective Matrix
