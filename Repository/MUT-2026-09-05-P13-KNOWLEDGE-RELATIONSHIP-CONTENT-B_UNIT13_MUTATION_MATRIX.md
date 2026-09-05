# MUTATION MATRIX ADDENDUM — P13 KNOWLEDGE B / UNIT 13 / REP-002 EXACT PHYSICAL MAP

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Parent verified head: `5d6bf626df40b47e30a51d291ebebd2b9db418e2`
State: `UNIT 13 PREPARED / REP-002 EXACT MAP ADDENDUM / CANONICAL FOLD PENDING`

## Preconditions

- Unit 12 exact REP-013 content-tree addendum passed exact-head 4/4.
- Priority-13 Transaction-A exact path source contains 50 unique Knowledge leaves with sorted-path digest `8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`.
- Current REP-002 v1.7.8 lacks an exact Priority-13 Knowledge physical-map binding.
- Active REP-001 admission remains a separate authority-aware decision and must not be inferred from physical mapping.

## Authorized paths

Exactly three paths:

1. `Repository/REP-002_PRIORITY13_KNOWLEDGE_EXACT_MAP_ADDENDUM_2026-09-05_G.md` — CREATE.
2. `Quality/Integrity/test_knowledge_p13_rep002_exact_map_addendum.py` — CREATE.
3. this Matrix addendum — CREATE.

No existing canonical file is changed in Unit 13.

## Expected result

- physical Knowledge mapping is bound exactly to Transaction-A's 50-path TSV, digest and blob identity;
- mapping grants no authority and does not admit KNW-001..010 to REP-001;
- Learning/Programming/Mathematics/support leaves remain noncanonical by mapping alone;
- canonical REP-002 fold remains explicitly OPEN;
- Priority 13 remains OPEN.

## Verification

`CREATE → COMMIT → COMPARE EXACT 3 PATHS → READ BACK → EXACT-HEAD 4/4`

## Next legal step after 4/4

Create the REP-012 path-level allocation binding in a separate unit. Allocation evidence must preserve `NONE_BY_ALLOCATION` for every path and must not close or promote the domain.

---

End of Unit-13 Matrix Addendum
