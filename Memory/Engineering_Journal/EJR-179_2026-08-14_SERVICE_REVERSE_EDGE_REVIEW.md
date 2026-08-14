# EJR-179 — Service Reverse-Edge Review

**Date:** 2026-08-14
**Baseline:** 3.2.1
**Integrity:** HOLD

## Review

The current service documents were re-read against REP-020. SRV-003, SRV-006, SRV-007, SRV-008 remain metadata-complete in identity/version/status but do not declare an explicit Development Baseline. No baseline was inferred.

Reverse-edge checks were performed at the documentation level for the highest-value service boundary:

- SRV-003 ↔ SRV-002/SRV-004: declared relationship symmetry is incomplete; retain `OBSERVED` pending independent reverse evidence.
- SRV-006 ↔ SRV-007: SRV-006 explicitly names SRV-007, and SRV-007 explicitly names SRV-006 in Related Documents; promote to `PARTIALLY_VERIFIED` for the documentation boundary only.
- SRV-007 ↔ SRV-008: both explicitly name each other; promote to `PARTIALLY_VERIFIED` for the documentation boundary only.
- SRV-008 ↔ SRV-009: both explicitly name each other; promote to `PARTIALLY_VERIFIED` for the documentation boundary only.
- SRV-009 → SRV-005/SRV-007/SRV-008: SRV-009 explicitly declares these dependencies; reverse operational validation remains open.

## Matrix action

REP-020 remains the working matrix. New reverse-edge states are recorded in this journal as evidence pending a controlled matrix mutation. The matrix must remain the authoritative lookup layer only, never the authority itself.

## Engineering learning

A reciprocal filename mention is stronger than a one-sided declaration but is still not proof of runtime/operational coupling. Therefore documentation reciprocity should be represented as `PARTIALLY_VERIFIED`, not `VERIFIED`, until implementation/runtime evidence is available.

## Next

Continue from the service boundary into Runtime Consumers and Repository/Index consumers. Update REP-020 with the new reverse-edge evidence in the same review pass.
