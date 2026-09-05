# P12 Models Relationship/Content Transaction B — Unit 14 Specifications ↔ Models Matrix

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Unit: `14 — Specifications ↔ Models concrete relationship reconciliation`
State: `MATERIAL COMPLETE / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Entry gate

Unit-13 exact-head `6308f9307703b5ae7d68b2df7260f31aa922b054` passed all four required workflow families.

## Current-source findings

1. `REL-001` remains a bounded `SPEC-001-KNOWLEDGE-ORGANIZATION → MOD-001 = DEPENDS_ON` relationship. The September Priority-8 bounded revalidation supersedes the earlier pre-promotion hold while retaining non-global scope.
2. `MOD-001` independently names `Specifications/01-Knowledge-Organization.md` as active operational guidance that does not override model authority. That supports a distinct reverse documentary relationship: `MOD-001 → SPEC-001-KNOWLEDGE-ORGANIZATION = REFERENCES`.
3. The Specification refers generically to applicable canonical Models but does not identify `MOD-002`, `MOD-003`, `MOD-004` or `MOD-011`; no concrete edge is manufactured from that generic class statement.
4. The current Specifications physical domain contains only `01-Knowledge-Organization.md` and `README.md`; no additional Specification artifact supplies a concrete Models target in the inspected scope.

## Material sequence

| Step | Surface | Action | Result |
|---|---|---|---|
| U14-1 | SPEC-001 + MOD-001 + REP-014/P8 evidence | direct semantic re-read | REL-001 preserved boundedly |
| U14-2 | Specifications exact physical domain | enumerate/read | no second specification relationship source found |
| U14-3 | `REP-014_PRIORITY12_SPEC_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_L.tsv` | create | one preserved edge, one reverse candidate, four no-edge dispositions |
| U14-4 | `test_models_p12_spec_relationships.py` | create | guard generic-class vs concrete-target distinction and independent reverse evidence |
| U14-5 | this Matrix | bind unit | exact-head CI pending |

## Registry impact

No canonical registry mutation is performed in this unit. On a later full-content-preserving REP-014 write:

- preserve `REL-001` as bounded `DEPENDS_ON`;
- add `MOD-001 → SPEC-001-KNOWLEDGE-ORGANIZATION = REFERENCES` if no duplicate appears and the next free stable ID remains available;
- do not add SPEC→MOD-002/003/004/011 from generic authority wording.

`GENERIC AUTHORITY CLASS != CONCRETE RELATIONSHIP TARGET`.

`REVERSE DIRECTION REQUIRES ITS OWN SOURCE EVIDENCE`.

Priority 12 and Transaction B remain OPEN pending safe canonical registry synchronization and closure review.
