# MUTATION MATRIX — P13 KNOWLEDGE EXACT INVENTORY ALLOCATION A

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A`
Priority: `13 — Knowledge`
Entry HEAD: `f4638a9842f17b55d9734223228c54f72e5e3e57`
State: `OPEN / MATERIAL UNIT 1 PREPARED / EXACT-HEAD VALIDATION PENDING`

## Objective

Establish the exact tracked physical allocation of the current `Knowledge/` partition before identity, authority, content, dependency, consumer or relationship promotion.

This transaction does not close Priority 13 and does not treat physical location as semantic authority.

## Material truth established at entry

- exact tracked leaf count: `50`
- sorted-path SHA-256: `8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`
- top-level semantic artifacts: `KNW-001..KNW-010`
- supporting physical surfaces include `Knowledge/Learning`, `Knowledge/Mathematics`, and `Knowledge/Programming`
- the current README declares only `KNW-001..KNW-010` as canonical Knowledge artifacts
- prior P51 evidence knew about executable Learning files but did not perform Priority-13 exact allocation

Invariant:

`PHYSICAL ALLOCATION != CANONICAL PROMOTION != RELATIONSHIP VALIDATION != PARTITION CLOSURE`

## Authorized material unit 1

Exactly four paths are authorized:

1. `Knowledge/_FOLDER_STATUS.md` — synchronize current exact inventory scope without closing or promoting the domain.
2. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv` — immutable path/physical-role evidence for this material unit.
3. `Quality/Integrity/test_knowledge_p13_exact_inventory.py` — executable exact-set/digest and non-promotion guard.
4. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_MUTATION_MATRIX.md` — transaction evidence/control surface.

No KNW semantic artifact, Learning implementation, REP-014 relationship registry, REP-016 queue, REP-020 manifest, Architecture, Memory, Engine or Models artifact is authorized for mutation in Unit 1.

## Evidence classification

- `KNW-001..010`: physically present and declared canonical by current Knowledge README; individual identity/authority/content revalidation remains pending under P13.
- `Learning/*`: physically present supporting evidence/executable/test surface; allocation confers no canonical status.
- `Mathematics/*`: physically present subdomain documentation; allocation confers no canonical status.
- `Programming/*`: physically present subdomain/support surface; allocation confers no canonical status.
- README/status: domain control documentation, not proof of downstream relationship validity.

## Validation gate

After applying Unit 1:

1. compare entry HEAD → material HEAD and prove one commit / exactly four authorized files;
2. re-read all four paths from exact material HEAD;
3. run exact-head four-family CI;
4. classify any failure before further mutation;
5. only after 4/4 SUCCESS may Transaction A closure be considered;
6. closure, if justified, must be Matrix-only followed by closure-head 4/4.

## Explicit non-claims

This transaction does not claim:

- Priority 13 closure;
- canonical promotion of all 50 leaves;
- relationship validity from path co-location;
- Knowledge ↔ Memory validity;
- Knowledge ↔ Engine/Learning validity;
- Knowledge ↔ MOD-011 validity;
- Phase 1 closure;
- Global Integrity PASS.

---

End of Transaction-A Matrix
