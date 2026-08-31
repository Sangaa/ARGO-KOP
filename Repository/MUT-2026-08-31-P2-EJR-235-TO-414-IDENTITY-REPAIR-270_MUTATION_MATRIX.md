# MUTATION MATRIX — EJR-235 → EJR-414 IDENTITY REPAIR 270

Status: PREWRITE / EXECUTION NOT AUTHORIZED YET
Transaction ID: MUT-2026-08-31-P2-EJR-235-TO-414-IDENTITY-REPAIR-270
Opening main: `3e462e1bb03924b7112fc4c540a90ce54957a4f8`

## Authority chain

- Lease268 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and retains the earlier Memory EJR-235 allocation while classifying the later root EJR-235 allocation displaced.
- Lease269 and Matrix269 are CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.
- Lease269 complete-history artifact `9752355789`, digest `sha256:f987d0135c46eb83c6b2b039a4e034d5313eb1f753b5b407cbdea2a6398a38e9`, proves EJR-414 VACANT with `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `decision=VACANT`.
- EJR-414 is reserved for exactly one bounded replacement allocation for the displaced root EJR-235 identity.

## Fresh current-state evidence

Retained Memory member:
`Memory/Engineering_Journal/EJR-235_2026-08-14_P53_SESSION_CLOSURE.md`
blob `28216a14168c44875273f7edd5747dfd54e92f3d`.

Displaced root source:
`EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`
blob `a326b6195ecd66b26d8b379706c8965e78bde153`.

Candidate successor path:
`EJR/EJR-414_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`
returned 404 at pre-write read.

Source H1 is `# EJR-235 — GOV-015 Fixture/Test Field Validation`. Historical body/footer ends with `End of EJR-235` and must remain preserved.

Fresh exact-old-path search surfaced only Lease268 historical disposition evidence. No direct executable/operational consumer requiring rewrite is established. Historical governance/provenance references describing EJR-235 must remain unchanged.

## Authorized mutation boundary after pre-write validation

Only after this Matrix commit passes required repository gates and a separate execution lease is opened, one bounded repair may:
1. retain the Memory EJR-235 file unchanged;
2. remove `EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`;
3. create `EJR/EJR-414_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`;
4. preserve root semantic body/date/chronology byte-for-byte except H1 identity `EJR-235` → `EJR-414`;
5. preserve historical body/footer text including `End of EJR-235`;
6. perform zero consumer rewrites unless a fresh executable consumer is established immediately before execution;
7. keep the deterministic MEMORY_TO_ROOT expected baseline at 23 inside Repair270;
8. keep Global Integrity at HOLD.

## Expected repair-head behavior

Repair270 is expected to resolve one MEMORY_TO_ROOT ambiguity while preserving baseline 23. Therefore a repair-head census result `expected=23 / observed=22` is acceptable only if all other identity/chronology/provenance stages are clean and the sole incompleteness is `__COHORT_COUNT_DRIFT__`. Any baseline correction must be a separate successor lease.

## Hard gate before functional mutation

Immediately before mutation:
- re-discover live `main`;
- require it to equal the Repair270 execution-lease head;
- re-read source and require blob `a326b6195ecd66b26d8b379706c8965e78bde153`;
- re-read retained Memory member and require blob `28216a14168c44875273f7edd5747dfd54e92f3d`;
- require exact EJR-414 successor path still absent;
- repeat consumer check and abort if a new executable/operational consumer is established.

No functional EJR mutation is authorized by this pre-write Matrix itself.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.