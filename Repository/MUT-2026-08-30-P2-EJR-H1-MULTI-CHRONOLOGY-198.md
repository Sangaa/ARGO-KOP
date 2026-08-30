# MUT-2026-08-30-P2-EJR-H1-MULTI-CHRONOLOGY-198

Status: `OPEN / PREWRITE`
Lease: `R71-20260830-P2-EJR-H1-MULTI-CHRONOLOGY-198`
Base: `main@96ac69f8ca9a4b402841764d995911cf23d5c99f`

## Goal
Deterministically classify historical exact-path chronology for current H1-only EJR ambiguity groups with cardinality greater than two.

## Evidence contract
- recompute current ambiguity membership at execution time from `internal_document_id_audit.scan`;
- include only EJR groups whose members are all `FIRST_H1_FALLBACK` and whose current cardinality is greater than two;
- require complete non-shallow locally reachable Git history;
- record each current path's first-seen commit/time;
- compare every pair of first-seen commits by Git ancestry;
- classify each group as a total ancestry chain, same-first-seen collision, divergent/partial order, or missing history;
- chronology is evidence only and does not establish canonical ownership or rename lineage.

## Authorized functional scope
1. `Quality/Integration/ejr_h1_multi_chronology.py`
2. `Quality/Integration/test_ejr_h1_multi_chronology.py`
3. `.github/workflows/internal-id-audit.yml`
4. `Repository/MUT-2026-08-30-P2-EJR-H1-MULTI-CHRONOLOGY-198_MUTATION_MATRIX.md`

## Forbidden
No EJR mutation, migration, rename, delete, reassignment, normalization, suppression, allocation, authority promotion, REP-012/016/020 change, Priority-2 closure, Phase-1 closure, or global integrity claim.

## Verification
Functional exact-head Internal-ID plus general repository/runtime gates. If any evidence path is missing or history is shallow, classification must fail closed rather than infer chronology.
