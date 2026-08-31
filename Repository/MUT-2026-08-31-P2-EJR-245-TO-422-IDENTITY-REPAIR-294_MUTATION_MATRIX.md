# MUTATION MATRIX — EJR-245 TO EJR-422 IDENTITY REPAIR 294

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-245-TO-422-IDENTITY-REPAIR-294
Opening main: `229afce4a6b354254ff1a9b4146628bef9edfbf1`
Execution role: HERMUZ
Functional repair head: `d5ebe81889edc8b72459f2135ba2603cc32eda0a`

## Proven prerequisites

Lease/Matrix293 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

- Memory EJR-245 is the retained first valid historical allocation.
- Root EJR-245 is legitimate displaced content.
- EJR-422 was complete-history-vacancy-proven and reserved solely for that displaced root record by run `33402344919`, artifact `9761723214`, digest `sha256:f584fccd977b27da606a9f1bf464c17e512f460d4aaaef8bb0ed87b39a10e7ba`.

## Executed mutation

One atomic Git tree/commit:
1. preserved `Memory/Engineering_Journal/EJR-245_2026-08-15_P64_SESSION_CLOSURE.md` unchanged, blob `6ff20a7adb4d54f43189217e0ceb1565093bc81a`;
2. deleted `EJR/EJR-245_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`;
3. created `EJR/EJR-422_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`, blob `112791a841b67da3d568fcc1a4beba54a12422db`;
4. changed only the first H1 identity token from EJR-245 to EJR-422 and preserved the remaining body text.

## Repair-head gate

- Full-Stack run `33402907617`: SUCCESS.
- Internal Document-ID run `33402907681`: FAILURE only because deterministic MEMORY_TO_ROOT baseline still expected 15 while observed cohort was 14.
- exact repair-head census artifact `9761968609`, digest `sha256:3a0614c948c9cb8d133000be54b3292b7d7c03490a802453e13c3a60cf8e1200`: history_complete=true, decision=PARTIAL, sole incomplete group `__COHORT_COUNT_DRIFT__`.

No baseline change was performed inside Repair294.

## Separate Lease295 verification

Lease295 changed only `EXPECTED_GROUP_COUNT = 15` to `14` at `f0875f4b0ee68dadfddb585530451669929832ed`.

Final gates:
- Full-Stack run `33403240740`: SUCCESS.
- Internal Document-ID run `33403240765`: SUCCESS.
- final census artifact `9762099086`, digest `sha256:8fd78bcb0fa025989cd16bd30c74d54a9bdc29429ea3d6e44df69b91e5966193`: expected=14, observed=14, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No governance promotion, REP promotion, or Global Integrity change was authorized or executed by Matrix294.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
