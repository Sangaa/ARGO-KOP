# MUT-2026-08-31-P2 — EJR-247 → EJR-426 Identity Repair — Lease 306

Status: OPEN / AUTHORIZED BY CLOSED VACANCY GATE 305
Date: 2026-08-31
Scope: Priority 2 deterministic MEMORY_TO_ROOT_EJR ambiguity cohort.

## Authorization Basis

Lease305 established:

- Memory `EJR-247` is the earlier first-valid constituted allocation;
- root `EJR-247` is the later displaced allocation;
- complete-history gate proved `EJR-426 = VACANT`;
- Full-Stack passed on the proof head.

## Authorized Mutation

Atomically:

1. remove `EJR/EJR-247_2026-08-17_MULTI_CHANNEL_TRAINING_COMPLETION.md`;
2. create `EJR/EJR-426_2026-08-17_MULTI_CHANNEL_TRAINING_COMPLETION.md` with identical body except first H1 identity changes from `EJR-247` to `EJR-426`;
3. preserve `Memory/Engineering_Journal/EJR-247_2026-08-15_P66_SESSION_CLOSURE.md` unchanged.

Historical narrative references to EJR-247 are not cosmetically rewritten.

## Validation

- exact post-state read-back of old root/new root/Memory;
- Internal Document-ID Audit;
- MEMORY_TO_ROOT provenance census artifact inspection;
- Full-Stack Repository Audit.

Expected deterministic consequence: cohort 11 → 10, requiring a separate baseline-only normalization lease if and only if the only failure is `__COHORT_COUNT_DRIFT__`.

## Non-Claims

No Global Integrity promotion. No content-authority promotion. No automatic resolution of other cohort members.
