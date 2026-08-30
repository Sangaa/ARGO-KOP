# MUTATION MATRIX — P2 EJR PROVENANCE CENSUS 192

Transaction ID: `MUT-2026-08-30-P2-EJR-PROVENANCE-CENSUS-192`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-PROVENANCE-CENSUS-192`
State: `PREWRITE / NOT YET APPLIED`
Entry head: `ed4036c86a0e5c2e3900776106eedfbaf7a47793`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 192-001 | bounded census artifact | CREATE | exact six-group EJR provenance/chronology classification; no identity mutation | N | N |
| 192-002 | this Matrix | UPDATE | bind functional evidence and exact changed set | N | N |

## KEEP / prohibition

All existing EJR files are KEEP in Lease 192.

Forbidden in this transaction:

- rename/delete of any EJR artifact;
- changing `Document ID`, H1, filename, Canonical or Status fields;
- detector suppression or ambiguity-membership reduction;
- claiming a unique owner where chronology/authority evidence is insufficient.

## Required verification

- final live-parent recheck;
- force=false fast-forward;
- exact changed-set compare;
- read-back census + Matrix;
- no existing EJR path changed;
- CI workflows observed on exact functional head where triggered;
- Priority 2 remains OPEN after bounded census closure.
