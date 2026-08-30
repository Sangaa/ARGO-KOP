# P2 EJR NON-MONOTONIC PROVENANCE CENSUS — LEASE 200

Date: 2026-08-30
Execution role: HERMUZ / Room71
Transaction: `MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Baseline: `main@9762b1dbc0240dc9a8cfc4c409ed39982018d1d9`
State: `OPEN / PREWRITE / EVIDENCE-ONLY`

## Trigger
Lease 199 proved four non-monotonic H1-only ambiguity groups: `EJR-195`, `EJR-196`, `EJR-197`, `EJR-198`, each with exact-path namespace chronology `ROOT_EJR → MEMORY_EJR → ROOT_EJR`.

Chronology and namespace direction do not establish ownership. Before any identity migration, these exceptional groups require independent content/reference/consumer provenance evidence.

## Bounded objective
Create a deterministic companion census for only `EJR-195..198` that records, without assigning ownership:
- exact current member paths from the live ambiguity report;
- first-H1 titles and content SHA-256 digests;
- exact-ID references from other tracked text files;
- exact sibling-path references from other tracked text files;
- whether group member content is byte-distinct;
- complete-history requirement inherited from the chronology evidence boundary.

## Authorized functional scope
- `Quality/Integration/ejr_nonmonotonic_provenance_census.py` — ADD
- `Quality/Integration/test_ejr_nonmonotonic_provenance_census.py` — ADD
- `.github/workflows/internal-id-audit.yml` — MODIFY only to execute and upload the new evidence report
- `Repository/MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200_MUTATION_MATRIX.md` — same-change synchronization

## Forbidden scope
No EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, canonical promotion, or ownership assignment. No scanner semantic change. No REP-012/016/020 mutation. No P2, Phase-1, Connected-Baseline, or Global PASS closure.

## Pre-read content finding
Manual exact-head read-back shows that the 2026-08-14 records are control-plane/session-closure evidence while the later 2026-08-17 root records carry materially different P4/P1/P2 scopes. This is a triage observation only; the functional census must expose deterministic evidence before any stronger disposition.

## Acceptance
Lease may close only if:
1. synthetic tests pass;
2. all four target groups are found with exactly the current ambiguity membership;
3. current census completes under complete Git history;
4. exact-head workflow evidence is observed;
5. no ownership or migration disposition is emitted by the tool.
