# MUT-2026-08-31-P2-EJR-173-DISPOSITION-AUTHORIZATION-230

Status: PREWRITE / AUTHORIZATION EVIDENCE ONLY
Scope: one candidate group `EJR-173`

## Re-entry evidence
- live main: `36765d62599232b495f6ccaa64d14002041cca08`
- Checkpoint229: Priority 2 OPEN, baseline 31.
- Lease184 classifies Memory+root EJR reuse as traceability conflict candidates requiring provenance-aware review.
- Plan204 is bounded to its five proven groups and does not itself authorize EJR-173 repair.

## Current EJR-173 evidence
Retain candidate:
- `Memory/Engineering_Journal/EJR-173_2026-08-13_REP020_MATRIX_EXPANSION.md`
- path history first commit: `f3c93ad327d79b7fd18061f313ea536e13796ad5` at 2026-08-13T18:07:13Z.

Displace candidate:
- `EJR/EJR-173_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md`
- path history first commit: `448822fdda4e630309811d4354fc2192c3e8ff14` at 2026-08-14T05:56:32Z.

The records are semantically different events. The current deterministic MEMORY_TO_ROOT census at functional head `1972ebe9fd5b32e3eaf5703866e671d697e27975` reports EJR-173 as exactly one Memory member plus one root member, with zero external exact-ID references and zero exact-member-path references.

## Disposition
Apply the already proven bounded rule from Plan204 to this newly inspected group only:

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE INVALIDATES IT.`

No reviewed evidence invalidates the 2026-08-13 Memory allocation. Therefore:
- retain Memory EJR-173;
- classify the 2026-08-14 root EJR-173 as the displaced record candidate;
- do not mutate it until a replacement candidate independently passes complete-history vacancy proof.

## Authorization boundary
This lease authorizes only the next vacancy-proof step for a replacement ID and, if that proof closes VACANT, a separate one-record repair lease for the root record. It performs no rename, allocation, consumer rewrite, baseline change, detector weakening, or global promotion.

Priority 2 remains OPEN. Global integrity remains HOLD.
