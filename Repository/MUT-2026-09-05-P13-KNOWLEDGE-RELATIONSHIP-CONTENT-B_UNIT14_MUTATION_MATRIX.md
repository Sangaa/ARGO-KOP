# MUTATION MATRIX ADDENDUM — P13 KNOWLEDGE B / UNIT 14 / REP-012 EXACT ALLOCATION

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Parent verified head: `99486944dddec6f967ac9edd85bdaf24ed626154`
State: `UNIT 14 PREPARED / REP-012 EXACT ALLOCATION MANIFEST + BINDING / CANONICAL FOLD PENDING`

## Preconditions

- Unit-13 corrective chain is exact-head 4/4 SUCCESS with all four workflow families explicitly completed/success.
- Transaction-A exact Knowledge inventory remains 50 unique leaves with sorted-path digest `8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`.
- Current canonical REP-012 v1.0.13 does not yet bind that exact P13 inventory.
- Physical allocation must not admit or promote artifacts.

## Authorized paths

Exactly four created paths:

1. `Repository/REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_MANIFEST_2026-09-05_H.tsv`
2. `Repository/REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_BINDING_2026-09-05_H.md`
3. `Quality/Integrity/test_knowledge_p13_rep012_exact_allocation_binding.py`
4. this Matrix addendum

No existing canonical control-plane or Knowledge source file changes in Unit 14.

## Expected result

- exactly 50 path-level allocation records;
- exact path+physical-role equality with Transaction-A inventory;
- every row `ALLOCATED / NONE_BY_ALLOCATION / P13_TRANSACTION_A_EXACT_INVENTORY`;
- exact path digest recomputes to the Transaction-A digest;
- REP-012 addendum explicitly preserves nonpromotion semantics;
- canonical REP-012 fold remains OPEN;
- REP-001 active admission remains untouched;
- Priority 13 remains OPEN.

## Verification

`CREATE → COMMIT → COMPARE EXACT 4 PATHS → READ-BACK → ALL FOUR WORKFLOW FAMILIES EXPLICITLY COMPLETED/SUCCESS`

## Next connected work after 4/4

Re-read Knowledge status and executable `Knowledge/Learning` surfaces. Status synchronization may remove obsolete “not started” language only after exact remaining blockers are classified. Dependency/consumer validation for executable Learning surfaces remains a real material requirement and must not be skipped merely because physical control-plane evidence exists.

---

End of Unit-14 Matrix Addendum
