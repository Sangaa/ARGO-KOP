# MUTATION MATRIX ADDENDUM — P13 KNOWLEDGE B / UNIT 12 / REP-013 EXACT CONTENT TREE

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Parent verified head: `f6b05b9f831bcea4297bc4045697169d7dad9509`
State: `UNIT 12 PREPARED / REP-013 EXACT CONTENT-TREE ADDENDUM / CANONICAL FOLD PENDING`

## Preconditions

- Transaction A exact Knowledge inventory: `50` leaves / digest `8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`.
- Unit 11 control-plane reconciliation plan: exact-head `4/4 SUCCESS`.
- Current canonical REP-013 v1.1.6 retains an old five-file Knowledge subset.
- Full blob retrieval is readable, but the available mutation surface lacks safe patch-in-place; manual whole-file reconstruction is prohibited by the existing P293 content-preservation lesson.

## Authorized paths

Exactly three paths:

1. `Repository/REP-013_PRIORITY13_KNOWLEDGE_EXACT_CONTENT_TREE_ADDENDUM_2026-09-05_F.md` — CREATE.
2. `Quality/Integrity/test_knowledge_p13_rep013_exact_content_tree_addendum.py` — CREATE.
3. this Matrix addendum — CREATE.

No existing canonical file is changed in Unit 12.

## Expected result

- the exact 50-leaf Knowledge content tree is preserved as explicit REP-013-subordinate evidence;
- every Transaction-A path is represented exactly in the addendum;
- support/evidence/test/executable leaves are explicitly non-promoting;
- canonical REP-013 synchronization remains `OPEN` and its stale five-file Knowledge section is not silently treated as current;
- Priority 13 remains OPEN;
- no REP-001 admission, REP-002 mapping, REP-012 allocation binding, relationship registration, queue closure or Global Integrity claim occurs.

## Verification

`CREATE → COMMIT → COMPARE EXACT 3 PATHS → READ BACK → EXACT-HEAD 4/4`

## Next legal step after 4/4

Reconcile REP-002 physical mapping in a separate material unit. Do not combine REP-002 and REP-012 solely for convenience.

---

End of Unit-12 Matrix Addendum
