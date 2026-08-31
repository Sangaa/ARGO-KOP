# MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264

Status: DISPOSITION-RECORDED / VERIFICATION-PENDING
Scope: Priority-2 EJR-233 disposition only; no identity mutation.
Opening main: `d21a08a3b88cdf271a051fe4a46d3d5bc1bbc9b2`.
Pre-write Matrix264: `93454a3d66af1df88debb51b59ccab93c69e8719`.

## Current deterministic evidence

Lease263 final census artifact `9750922890`, digest `sha256:1948d5e7ea91d7dc416a88d99180e4f04ad0ef4426c66178da7f645d577a29be`, reports EJR-233 as an expected two-member `MEMORY_EJR → ROOT_EJR` ambiguity group with:
- external exact-ID references: 0
- exact references to either member path: 0
- distinct content bodies: true

Current members were directly re-read before this disposition:
- `Memory/Engineering_Journal/EJR-233_2026-08-14_P51_SESSION_CLOSURE.md`, current blob `31ea54a8101a3cafdd17beb54f78f515a1f4033b`.
- `EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md`, current blob `f78a69c14793fb8331fe0096e656bfd1957a94a7`.

## Chronology proof

Path history independently establishes:
- Memory EJR-233 first appears at commit `a57e245489dd8519884615d53b7873610e48d67e`, 2026-08-14T21:00:09Z, message `docs: close P51 Knowledge namespace audit checkpoint`.
- Root EJR-233 first appears at commit `768c49a18f67749ac8730527f245ff6d97342f86`, 2026-08-17T16:20:24Z, message `EJR-233: record first governed application of GOV-015`.

The Memory allocation is therefore the earlier established EJR-233 identity. The root allocation is later and semantically distinct.

## Disposition

- RETAIN `Memory/Engineering_Journal/EJR-233_2026-08-14_P51_SESSION_CLOSURE.md` under EJR-233.
- CLASSIFY `EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md` as a later displaced EJR allocation requiring a new unique identity before the ambiguity can be repaired.
- Do not alter either record in this lease.

## Boundaries

This disposition does NOT authorize:
- rename/delete/rewrite of either member;
- allocation of any replacement EJR number;
- a vacancy claim based on current-tree absence;
- consumer rewrites;
- cohort baseline change;
- Global Integrity promotion.

A successor identity may be selected only after a separate complete-history vacancy proof reaches `VACANT / history_complete=true`, then a separate repair lease may execute the bounded path/H1 mutation.

## Validation requirement

This disposition is effective only after its own commit passes Full-Stack, Runtime, Real Mutation Matrix where applicable, and M2. After that, close Matrix264 and this record as RESUME-SAFE.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.