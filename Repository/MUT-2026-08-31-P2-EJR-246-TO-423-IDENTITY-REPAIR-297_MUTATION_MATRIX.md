# MUTATION MATRIX — EJR-246 TO EJR-423 IDENTITY REPAIR 297

Status: PREWRITE / MUTATION AUTHORIZED AFTER HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-246-TO-423-IDENTITY-REPAIR-297
Opening main: `97826ce6864ef667b47253d661b889bf924bcc66`
Execution role: HERMUZ

## Proven prerequisites

Lease/Matrix296 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

- Memory EJR-246 is the retained first valid historical allocation.
- Root EJR-246 is legitimate displaced content.
- Candidate EJR-423 is reserved solely for the displaced root record.
- Complete-history vacancy proof run `33409267610` succeeded.
- Artifact `9764434172`, digest `sha256:f7ab8977442df306625d11897cfd79a7048ceb37af2a42efb7627729ed8ee202`, proves EJR-423 VACANT with no current or historical claims.
- Proof-head Full-Stack run `33409267656` succeeded.

## Authorized mutation

1. preserve `Memory/Engineering_Journal/EJR-246_2026-08-15_P65_SESSION_CLOSURE.md` byte-for-byte;
2. move `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md` to `EJR/EJR-423_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md` atomically;
3. change only the first H1 identity token from `EJR-246` to `EJR-423` in the displaced root content;
4. preserve all remaining body/date/status/evidence text byte-for-byte;
5. do not rewrite historical narrative references to EJR-246 cosmetically;
6. do not normalize MEMORY_TO_ROOT expected cohort count inside Repair297.

## Post-mutation hard gate

The exact repair head must be evaluated by repository CI. If Internal Document-ID fails solely because deterministic MEMORY_TO_ROOT cohort count drifts from expected 14 to observed 13 while history and all member classifications remain complete, that baseline update must occur only in a separate Lease298.

No governance promotion, REP promotion, or Global Integrity change is authorized.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
