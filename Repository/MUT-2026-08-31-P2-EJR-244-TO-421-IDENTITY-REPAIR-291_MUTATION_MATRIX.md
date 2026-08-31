# MUTATION MATRIX — EJR-244 → EJR-421 IDENTITY REPAIR 291

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-244-TO-421-IDENTITY-REPAIR-291
Opening main: `eff63514babc30c3d0805bac18f31316601676c6`
Execution role: HERMUZ
Functional repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Normalization head: `d481a4169a37ac086125b3853675c32f9aed8e14`

## Authority

Lease290 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-244 is RETAINED; later root EJR-244 is DISPLACED legitimate content; EJR-421 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33396768282`, artifact `9759617449`, digest `sha256:28a790a1c1bf3a3a4425602426ea3351be2f09c4c469add1e21723970a55d96c`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Executed functional mutation

At the fresh hard-gated parent, retained Memory EJR-244 was preserved byte-for-byte at blob `2fe0ad5eabfb708f7fd1c931156f96c250d425cf`.

Atomic commit `7e0fbe49cc337070985bd646b2a12a884f9ff11a`:
1. removed `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`;
2. created `EJR/EJR-421_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`;
3. changed only first H1 `# EJR-244 — ...` → `# EJR-421 — ...`;
4. preserved all remaining body/date/status/evidence and historical narrative text;
5. performed zero consumer rewrites.

## Repair-head verification

- Full-Stack run `33397181070`: SUCCESS.
- Internal Document-ID run `33397181051`: failure isolated to expected deterministic cohort-count drift.
- artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`: expected=16, observed=15, history_complete=true, classification_complete=false, decision=PARTIAL, incomplete only `__COHORT_COUNT_DRIFT__`.

## Separate normalization and final verification

Lease292 / Matrix292 changed only `EXPECTED_GROUP_COUNT = 16` → `15` and are CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

- normalization head `d481a4169a37ac086125b3853675c32f9aed8e14`;
- Full-Stack run `33397585419`: SUCCESS;
- Internal Document-ID run `33397585341`: SUCCESS;
- final census artifact `9759944326`, digest `sha256:a2a09aff7d6f6177b0abb0936807cc0b91764bd1d57331b9a04460aaa48f3612`;
- expected=15, observed=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Repair291 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
