# P312 — INTERNAL-ID DUPLICATE AUDIT EVIDENCE BOUNDARY

Date: 2026-08-17
Status: Recorded / Priority 1 Evidence Expansion / Integrity Hold
Checkpoint: P312

## Scope
Exhaustive internal Document-ID/content duplicate reconciliation as a direct blocker to final Priority-1 closure.

## Evidence Method A — Repository Tree

A recursive Git tree was retrieved from current `main` after P311. The tree establishes the current physical filename/path universe, including active and historical areas such as `Architecture/` and `Archive/`.

This method is sufficient to reason about physical filename identity and path provenance, but it does not by itself prove that every file's internal `Document ID` matches its filename or that no duplicated internal IDs exist across differently named files.

## Evidence Method B — Repository Search

Independent repository search for `Document ID:` namespace content returned no reliable result for `ARC-*`. Similar search misses have occurred previously in the current repository tooling.

Therefore a negative search result is classified under the Search Defect Rule as:

`SEARCH FAILURE / NO ABSENCE CLAIM`

## Current Finding

The duplicate-ID audit remains **PARTIAL / NOT CLOSED**.

The following are established:

- physical namespace enumeration is available from the Git tree;
- known historical `Archive/ARC-*` artifacts remain distinguishable from active Architecture ownership by path context;
- internal-ID/content equivalence cannot be certified from filename/tree evidence alone;
- repository search cannot currently be trusted as an exhaustive content enumerator for this audit.

## Decision

Do not rename, merge, delete, or reassign artifacts based on filename-only evidence.
Do not claim exhaustive duplicate-ID PASS.
Do not fabricate internal-ID matches from path names.

## Next Safe Entry

Use targeted direct reads of high-risk namespaces and known collision families, beginning with:

1. active vs Archive `ARC-*` identities;
2. `GOV-*` active namespace and historical collisions;
3. `ENG-*` internal-ID reconciliation;
4. `REP-*` artifact identity vs reference occurrences;
5. any namespace where filename and internal Document ID previously diverged.

---

End of P312
