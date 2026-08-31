# MUTATION MATRIX — EJR-245 TO EJR-422 IDENTITY REPAIR 294

Status: PREWRITE / MUTATION AUTHORIZED AFTER HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-245-TO-422-IDENTITY-REPAIR-294
Opening main: `229afce4a6b354254ff1a9b4146628bef9edfbf1`
Execution role: HERMUZ

## Proven prerequisites

Lease/Matrix293 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

- Memory EJR-245 is the retained first valid historical allocation.
- Root EJR-245 is legitimate displaced content.
- Candidate EJR-422 is reserved solely for the displaced root record.
- Complete-history vacancy proof run `33402344919` succeeded.
- Artifact `9761723214`, digest `sha256:f584fccd977b27da606a9f1bf464c17e512f460d4aaaef8bb0ed87b39a10e7ba`, proves EJR-422 VACANT with no current or historical claims.
- Proof-head Full-Stack run `33402344855` succeeded.

## Authorized mutation

1. preserve `Memory/Engineering_Journal/EJR-245_2026-08-15_P64_SESSION_CLOSURE.md` byte-for-byte;
2. move `EJR/EJR-245_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md` to `EJR/EJR-422_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md` atomically;
3. change only the first H1 identity token from `EJR-245` to `EJR-422` in the displaced root content;
4. preserve all remaining body/date/status/evidence text byte-for-byte;
5. do not rewrite historical narrative references to EJR-245 cosmetically;
6. do not normalize MEMORY_TO_ROOT expected cohort count inside Repair294.

## Post-mutation hard gate

The exact repair head must be evaluated by repository CI. If Internal Document-ID fails solely because deterministic MEMORY_TO_ROOT cohort count drifts from expected 15 to observed 14 while history and all member classifications remain complete, that baseline update must occur only in a separate Lease295.

No governance promotion, REP promotion, or Global Integrity change is authorized.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
