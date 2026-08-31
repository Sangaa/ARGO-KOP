# MUTATION MATRIX — EJR-246 TO EJR-423 IDENTITY REPAIR 297

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-246-TO-423-IDENTITY-REPAIR-297
Opening main: `97826ce6864ef667b47253d661b889bf924bcc66`
Execution role: HERMUZ
Functional repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`

## Verified execution

Lease/Matrix296 proved EJR-423 complete-history VACANT and reserved it solely for displaced root EJR-246.

Repair297 atomically removed `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md` and created `EJR/EJR-423_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`. Only the first H1 identity token changed. Memory EJR-246 remained byte-identical at blob `cae56a17e41cc3ea979d89a563158a29e7f80bdc`.

Repair-head Full-Stack run `33409682009`: SUCCESS. Internal Document-ID run `33409681899` failed solely because deterministic MEMORY_TO_ROOT baseline drifted expected 14 -> observed 13. Artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`, showed history_complete=true and sole incomplete group `__COHORT_COUNT_DRIFT__`.

Lease298 separately normalized the cohort baseline. Final Full-Stack run `33410030347` and Internal Document-ID run `33410030407` both succeeded; final artifact `9764755806`, digest `sha256:3afc1559b1bfb2d712d3cdd4899b853ffa693b985ca10b1e9db6a1ea2d9093f0`, proves 13/13, CENSUSED, no incomplete groups.

No governance promotion, REP promotion, or Global Integrity change was executed.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
