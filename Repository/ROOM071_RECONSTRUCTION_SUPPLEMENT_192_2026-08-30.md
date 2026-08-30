# ROOM 071 RECONSTRUCTION SUPPLEMENT 192 — 2026-08-30

Session state: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-PROVENANCE-CENSUS-192`
Entry head: `ed4036c86a0e5c2e3900776106eedfbaf7a47793`
Prewrite head: `595ebd23e393bc7eb57de6930d60ce7211a66e9a`
Analytical evidence commit: `d1c071cb386814e97de67e4d462d267e86fa99d0`
Matrix reconciliation commit: `87ba026e9246973dc2c6ffb7a73465915bcd76b6`

## Completed

- Re-entered from Lease 191 and independently rediscovered live `main`.
- Downloaded and parsed exact Internal-ID artifact `9731526902` from functional head `044c5c41c31f98d944c663b33cc73d88784a71d6`.
- Established exact census: 144 ambiguous groups, 121 EJR groups, exactly six EJR groups with an explicit `DOCUMENT_ID_FIELD` member.
- Bounded groups: EJR-003, EJR-026, EJR-180, EJR-181, EJR-182, EJR-183.
- Read representative/current member content and Git chronology.
- Confirmed historical allocation/discovery defects for EJR-026, EJR-181 and EJR-183.
- Classified EJR-003 as early explicit claim followed by distinct later reuse.
- Preserved EJR-180 and EJR-182 as unresolved multi-claim groups rather than manufacturing an owner from metadata strength.
- Re-read REP-012 and bound the discovered gap to its allocation/identity precondition.
- Performed no EJR rename, delete, ID rewrite, detector suppression or ambiguity-membership reduction.

## Tool-policy incident

A standalone census artifact plus updated Matrix were prepared as Git blobs. `create_tree` was blocked twice by the tool-policy layer before a functional tree was created or `main` was moved.

No partial functional mutation occurred. The analytical evidence was persisted safely in the Lease record and the Matrix explicitly records that the standalone functional artifact was not applied.

## New learning

`AN ALLOCATION REPAIR IS NOT SAFE UNTIL VACANCY IS PROVEN ACROSS ALL IDENTITY-BEARING SURFACES AND HISTORY.`

Required candidate-ID gate:

`METADATA → H1 → FILENAME → GIT HISTORY → ALLOCATE`

## Resume point

Next bounded work:

`P2 EJR COLLISION-SAFE ALLOCATION GATE`

Before any historical EJR migration, build or verify a deterministic vacancy check that treats metadata IDs, identity-bearing H1 claims, filename prefixes and Git-history existence as occupancy evidence.

Do not reopen Release Priority 20. Do not suppress the 121 EJR ambiguity groups. Do not assign replacement IDs by “next-looking number” alone.

## Preserved holds

- Priority 2 historical/provenance identity scope: OPEN.
- Phase 1 overall: OPEN.
- Global Connected Baseline: OPEN.
- Provider Authentication: HARD HOLD where real trust anchor is absent.
- Global `BOOTED / INTEGRITY PASS`: NOT CLAIMED.

Session is CLOSED / RESUME-SAFE.
