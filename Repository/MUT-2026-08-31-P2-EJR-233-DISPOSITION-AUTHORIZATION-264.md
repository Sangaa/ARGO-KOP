# MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Priority-2 EJR-233 disposition only; no identity mutation.

## Chain

- Opening main: `d21a08a3b88cdf271a051fe4a46d3d5bc1bbc9b2`.
- Pre-write Matrix264: `93454a3d66af1df88debb51b59ccab93c69e8719`.
- Disposition record: `35d0a533c022aec90ed52893bfc762e51c485741`.
- Matrix264 closure: `531dbe3606bea1650ef82cd9e3255bf8083f9d88`.

## Current deterministic evidence

Lease263 final census artifact `9750922890`, digest `sha256:1948d5e7ea91d7dc416a88d99180e4f04ad0ef4426c66178da7f645d577a29be`, reports EJR-233 as an expected two-member `MEMORY_EJR → ROOT_EJR` ambiguity group with zero external exact-ID references, zero exact references to either member path, and distinct content bodies.

Direct reads established:
- Memory member blob `31ea54a8101a3cafdd17beb54f78f515a1f4033b`.
- Root member blob `f78a69c14793fb8331fe0096e656bfd1957a94a7`.

## Chronology proof

- Memory EJR-233 first appears at `a57e245489dd8519884615d53b7873610e48d67e`, 2026-08-14T21:00:09Z.
- Root EJR-233 first appears at `768c49a18f67749ac8730527f245ff6d97342f86`, 2026-08-17T16:20:24Z.

The Memory allocation is therefore the earlier established EJR-233 identity; the root allocation is later and semantically distinct.

## Final disposition

- RETAIN `Memory/Engineering_Journal/EJR-233_2026-08-14_P51_SESSION_CLOSURE.md` under EJR-233.
- CLASSIFY `EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md` as a later displaced EJR allocation requiring a new unique identity before ambiguity repair.
- No EJR file was altered by Lease264.

## Validation

Pre-write Matrix264 passed:
- Full-Stack #2361: SUCCESS
- Runtime #2136: SUCCESS
- Real Mutation Matrix #201: SUCCESS
- M2 #1018: SUCCESS

Disposition record commit passed:
- Full-Stack #2362 / run `33373679277`: SUCCESS
- Runtime #2137 / run `33373679263`: SUCCESS
- M2 #1019 / run `33373679259`: SUCCESS

## Learning / transfer disposition

No new permanent rule is needed. Lease264 is another execution-confirmed application of the established evidence hierarchy: current census for target selection, direct reads for member identity, and path history for chronology; negative/current-tree absence is insufficient for replacement vacancy.

## Boundary and resume

This lease authorizes no rename, delete, replacement number, vacancy claim, consumer rewrite, cohort update, or Global Integrity promotion.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next safe entry: re-discover live main and open a separate complete-history replacement-vacancy proof for the displaced root EJR-233. Only a `VACANT / history_complete=true` result may authorize a later bounded repair lease.