# MUT-2026-08-31-P2-EJR-297-TO-424-IDENTITY-REPAIR-300

Status: OPEN / IDENTITY REPAIR PENDING
Scope: execute the already-governed displacement of root EJR-297 to reserved successor EJR-424.
Opening main: `bf8bdc9a24310c84d2320985d97ba8add9e23554`
Pre-write Matrix300: `1d3980e21294fe43875f77e31ac018c8d2b9a2f1`
Predecessor Lease299: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE

## Authorized state transition

- RETAIN: `Memory/Engineering_Journal/EJR-297_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP02_FETCH_GATE.md` under EJR-297.
- DISPLACE: `EJR/EJR-297_2026-08-22_HERMUZ_BLIND_LAW_PREDICTION_TEST.md`.
- RECREATE displaced content at `EJR/EJR-424_2026-08-22_HERMUZ_BLIND_LAW_PREDICTION_TEST.md`.
- Change only the first H1 identity from `EJR-297` to `EJR-424`; preserve the remainder of the document as historical content.

EJR-424 complete-history vacancy was proven under Lease299 by workflow run `33410673926` and artifact `9764977768`.

## Required validation

The functional repair is not closed until:
- the move is atomic with no intermediate duplicate identity state;
- root EJR-297 is absent and root EJR-424 exists;
- Memory EJR-297 remains unchanged;
- Full-Stack is SUCCESS;
- Internal-ID evidence is inspected;
- any deterministic cohort-count drift is handled only by a separate baseline lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
