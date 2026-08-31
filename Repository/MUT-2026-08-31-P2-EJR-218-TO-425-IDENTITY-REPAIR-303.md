# Lease 303 — EJR-218 to EJR-425 Identity Repair

Status: OPEN / EXECUTION GATE
Date: 2026-08-31

## Authority Boundary
Lease302 proved `EJR-425` vacant against complete history and established the disposition candidate: Memory EJR-218 retains the first-valid allocation; the later root EJR-218 is displaced.

## Allowed Mutation
Atomically move only `EJR/EJR-218_CURRENT_BUILD_RECONCILIATION_2026-08-17.md` to `EJR/EJR-425_CURRENT_BUILD_RECONCILIATION_2026-08-17.md`, changing only the first H1 identity from EJR-218 to EJR-425. Preserve body content and all historical narrative references.

## Required Post-State
- Memory EJR-218 unchanged;
- old root EJR-218 path absent;
- new root EJR-425 present;
- Full-Stack Repository Audit SUCCESS;
- Internal Document-ID Audit inspected;
- any sole cohort-count drift handled only in a separate baseline lease.

No Global Integrity promotion.
