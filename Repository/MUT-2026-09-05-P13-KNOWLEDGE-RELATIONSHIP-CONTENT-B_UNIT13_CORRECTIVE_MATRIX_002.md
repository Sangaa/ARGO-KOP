# CORRECTIVE MATRIX ADDENDUM — P13 KNOWLEDGE B / UNIT 13 SECOND GUARD REPAIR

Parent corrective head: `23b473b23b5920277067f336212886144fea8622`
Failed Runtime run: `33984087512`
State: `ONE REPRESENTATION ASSERTION REMAINS / 294 PASS / 1 FAIL`

The first corrective reduced the integrity failures from 9 to 1 without changing semantic source/control-plane authority.

Remaining failure:

`test_knw010_rep010_reference_uses_current_physical_identity`

The guard expected the phrase `stale reference`, while the current source truth says `stale physical reference`. The semantic invariant is unchanged:

- active Related Documents contains only `Repository/REP-010_RELEASE_BASELINE.md`;
- historical repair provenance may preserve the former `Repository/REP-010_REPOSITORY_MAINTENANCE.md` string;
- the REP-010 title/path coherence gap remains separate.

Authorized exactly two paths:

1. `Quality/Integrity/test_knowledge_p13_identity_migration_residue.py` — change the provenance representation assertion only.
2. this corrective Matrix addendum.

No Knowledge source, registry, map, allocation, queue, manifest or status artifact changes.

Required acceptance remains strict:

`ALL FOUR WORKFLOW FAMILIES = status completed + conclusion success`.

---

End of Second Corrective Matrix
