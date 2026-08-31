# Repair 315 — Root EJR-234 to EJR-429 Identity Repair

Status: OPEN / AUTHORIZED BY LEASE 314
Date: 2026-08-31

## Authorization
Lease314 complete-history proof established EJR-429 as VACANT. First-valid historical allocation retains EJR-234 for the earlier Memory journal. The later root journal is authorized for displacement only.

## Mutation scope
Atomically:
1. create `EJR/EJR-429_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md` from the current root EJR-234 content;
2. change only the first H1 identity from `EJR-234` to `EJR-429`;
3. remove `EJR/EJR-234_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md` in the same Git tree;
4. keep `Memory/Engineering_Journal/EJR-234_2026-08-14_P52_SESSION_CLOSURE.md` byte-for-byte unchanged.

## Preservation boundary
Historical narrative and embedded execution references inside the displaced root record are not cosmetically rewritten. No authority promotion, governance-policy change, or consumer claim is implied.

## Validation gate
After the atomic repair:
- old root path must be absent;
- successor root path must exist with identical body except H1;
- Memory EJR-234 blob must remain unchanged;
- Full-Stack must succeed;
- Internal Document-ID census may fail only for deterministic cohort-count drift; any other failure stops the chain.

Global Integrity remains HOLD.
