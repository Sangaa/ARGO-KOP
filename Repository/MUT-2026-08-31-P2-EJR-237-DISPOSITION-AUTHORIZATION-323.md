# Lease 323 — EJR-237 Disposition Authorization

Status: CLOSED / DISPOSITION-VERIFIED / NO IDENTITY MUTATION
Date: 2026-08-31
Protocol: GOV-013 / GOV-014A

## Current queue boundary
Priority 2 remains the active legal queue. Lease322 established the current deterministic MEMORY_TO_ROOT cohort at 6 groups: EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296.

## Target evidence — EJR-237
Current members:
- `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md`
- `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md`

Current census evidence shows two members, distinct semantic bodies, MEMORY→ROOT lineage, and zero exact-member-path consumers.

Git path history proves:
- Memory allocation: `51057be94fe4981258c0a02cbc1461a1e43e72d8`, 2026-08-15T05:15:05Z;
- root allocation: `93248a0f5feb2abb5b84db3dfd9c19ba1e8e5b6d`, 2026-08-17T16:46:35Z.

The later root record has live semantic-evidence references in EJR-418 and REP-020 P322. Those references are consumer-preservation obligations if the root identity moves; they do not invalidate the earlier Memory allocation or transfer ownership of EJR-237.

## Disposition
Under the bounded first-valid historical-allocation rule:

`RETAIN = Memory EJR-237`

`DISPLACEMENT CANDIDATE = root EJR-237`

This disposition lease performs no rename, delete, allocation, reassignment, consumer rewrite, relationship promotion, runtime work, or baseline change.

## Next legal action
Discover one successor candidate for the displaced root record and prove vacancy with complete locally reachable history in a separate lease before any identity mutation.

Priority 2: OPEN.
Phase 1: OPEN.
Global Integrity: HOLD.
