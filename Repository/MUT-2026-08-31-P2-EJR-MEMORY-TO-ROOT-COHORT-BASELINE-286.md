# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-286

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair285.
Opening repair head: `6db3cc4f571cfbb4a6405f0f59d4be7a1e2e155b`
Pre-write Matrix286: `957ac01dc64e3e9df99b91a76719904cbb6733cf`

## Trigger

Repair285 reduced observed MEMORY_TO_ROOT membership from 18 to 17. Artifact `9757343910`, digest `sha256:84f59b30aa4e3ddc90db470cfa042bd4cb5e411c8dd8e71a2dc3a5fa95a91cf8`, proves history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Authorized normalization: change only `EXPECTED_GROUP_COUNT = 18` to `EXPECTED_GROUP_COUNT = 17`.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
