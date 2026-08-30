# MUT-2026-08-30 — P2 EJR H1 NAMESPACE LINEAGE SIGNAL CENSUS — LEASE 199

Status: `PREWRITE / OPEN`
Lease: `R71-20260830-P2-EJR-H1-NAMESPACE-LINEAGE-199`
Baseline: `main@6b011215286aae70d78d0ad86d6d8acc75ee7fa2`

## Purpose
Build an evidence-only companion classifier for the `115` current H1-only EJR ambiguity groups now covered by Leases 197-198 chronology. The classifier will combine exact-path first-seen ancestry with journal namespace surface (`EJR/` vs `Memory/Engineering_Journal/`) to expose provenance-direction signals without assigning ownership.

## Authorized functional scope
1. `Quality/Integration/ejr_h1_namespace_lineage.py` — ADD.
2. `Quality/Integration/test_ejr_h1_namespace_lineage.py` — ADD.
3. `.github/workflows/internal-id-audit.yml` — MODIFY only to execute/test/emit/upload this evidence report.
4. `Repository/MUT-2026-08-30-P2-EJR-H1-NAMESPACE-LINEAGE-199_MUTATION_MATRIX.md` — synchronize same-change evidence.

## Required semantics
- recompute current H1-only ambiguity membership from the live internal-ID report;
- require complete locally reachable Git history and fail closed if shallow;
- classify each exact current path as `ROOT_EJR`, `MEMORY_EJR`, or `OTHER`;
- construct an ancestry-ordered namespace sequence only when exact-path first-seen commits form a total order;
- expose same-surface reuse, directional cross-surface transition, multi-transition, and unresolved/non-total states;
- chronology + namespace are provenance signals only, never canonical ownership authority;
- exact current paths do not prove rename lineage or semantic origin.

## Forbidden
No EJR mutation, migration, rename, delete, reassignment, normalization, suppression, allocation, ownership promotion, scanner-semantic change, REP-012/016/020 mutation, Priority-2 closure, Phase-1 closure, or global integrity claim.

## Verification target
Synthetic tests + deterministic exact-head report + Internal-ID/Full-Stack/Runtime/M2/Real-Matrix exact-head observation. A CI PASS without the report population/classification result is not sufficient closure evidence.
