# MUTATION MATRIX — EJR-297 TO EJR-424 IDENTITY REPAIR 300

Status: OPEN / PRE-WRITE GATE
Transaction ID: MUT-2026-08-31-P2-EJR-297-TO-424-IDENTITY-REPAIR-300
Opening main: `bf8bdc9a24310c84d2320985d97ba8add9e23554`
Execution role: HERMUZ
Predecessor disposition/vacancy lease: 299 CLOSED / EXECUTION-VERIFIED / RESUME-SAFE

## Authorized repair

Retain `Memory/Engineering_Journal/EJR-297_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP02_FETCH_GATE.md` as EJR-297.

Atomically move displaced legitimate root content:
- from `EJR/EJR-297_2026-08-22_HERMUZ_BLIND_LAW_PREDICTION_TEST.md`
- to `EJR/EJR-424_2026-08-22_HERMUZ_BLIND_LAW_PREDICTION_TEST.md`.

Successor `EJR-424` was complete-history proven VACANT under Lease299, workflow run `33410673926`, artifact `9764977768`.

## Mutation boundary

Allowed identity mutation:
- delete the root EJR-297 path;
- create the root EJR-424 path with the same content except first H1 identity changed from `EJR-297` to `EJR-424`.

Historical narrative references inside the displaced document are preserved; no cosmetic rewriting.

Forbidden under Repair300:
- modifying Memory EJR-297;
- rewriting external historical references merely for renumbering;
- cohort-baseline normalization;
- governance/REP promotion;
- Global Integrity promotion.

Validation required after functional repair:
- root EJR-297 path absent;
- root EJR-424 path present;
- Memory EJR-297 blob unchanged;
- Full-Stack SUCCESS;
- Internal-ID result inspected. If the only failure is deterministic cohort-count drift, normalization must occur in a separate lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
