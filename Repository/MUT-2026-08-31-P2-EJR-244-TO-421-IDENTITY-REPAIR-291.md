# MUT-2026-08-31-P2-EJR-244-TO-421-IDENTITY-REPAIR-291

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: bounded identity repair for displaced root EJR-244 using successor EJR-421.
Opening main: `eff63514babc30c3d0805bac18f31316601676c6`
Pre-write Matrix291: `c7731f4530aeea41df4d1133f40d12f51c773d32`
Authority: closed Lease290 + complete-history EJR-421 vacancy proof.
Functional repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Normalization head: `d481a4169a37ac086125b3853675c32f9aed8e14`

## Hard gate

- retained Memory EJR-244: `Memory/Engineering_Journal/EJR-244_2026-08-15_P62_SESSION_CLOSURE.md`, blob `2fe0ad5eabfb708f7fd1c931156f96c250d425cf`;
- displaced root source before repair: `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`, blob `4c62b2f8b9151255a87d83c87829f3bafe1c0f54`;
- EJR-421 complete-history vacancy proof: run `33396768282`, artifact `9759617449`, digest `sha256:28a790a1c1bf3a3a4425602426ea3351be2f09c4c469add1e21723970a55d96c`, decision=VACANT;
- verified pre-repair census reported zero exact-member-path consumers for the EJR-244 pair.

## Executed functional repair

A single atomic Git-tree commit `7e0fbe49cc337070985bd646b2a12a884f9ff11a` removed `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md` and created `EJR/EJR-421_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`.

Only the first H1 identity changed from `EJR-244` to `EJR-421`; the remaining displaced-root record content was preserved, including historical narrative text. Retained Memory EJR-244 remained byte-for-byte at blob `2fe0ad5eabfb708f7fd1c931156f96c250d425cf`. Zero consumer rewrites were performed.

## Repair-head evidence

- Full-Stack run `33397181070`: SUCCESS.
- Internal Document-ID run `33397181051`: expected failure caused solely by deterministic cohort baseline drift.
- repair-head census artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`:
  - expected_group_count=16;
  - observed_group_count=15;
  - history_complete=true;
  - classification_complete=false;
  - decision=PARTIAL;
  - incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`] only.

## Separate normalization

Lease292 / Matrix292 normalized only `EXPECTED_GROUP_COUNT = 16` → `15` at functional normalization head `d481a4169a37ac086125b3853675c32f9aed8e14` and are CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

Final verification:
- Full-Stack run `33397585419`: SUCCESS.
- Internal Document-ID run `33397585341`: SUCCESS.
- final census artifact `9759944326`, digest `sha256:a2a09aff7d6f6177b0abb0936807cc0b91764bd1d57331b9a04460aaa48f3612`.
- expected=15, observed=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Repair291 is therefore CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
