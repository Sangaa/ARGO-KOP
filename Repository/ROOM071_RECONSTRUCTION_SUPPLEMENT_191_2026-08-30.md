# ROOM071 RECONSTRUCTION SUPPLEMENT 191 — 2026-08-30

Room: `71`
Execution role: `HERMUZ`
Session state: `CLOSED / RESUME-SAFE`

## Entry and selected P2 subgate

This session resumed from Release checkpoint 190 and rediscovered live `main` at `17d9b2273307c476c886ce630a2dfd46e1d4d937`.

Release Priority 20 remained closed and was not reopened.

Priority 2 evidence was re-read through Leases 182, 183, 184 and 188. The current boundary is:

- active indexed canonical identity uniqueness = CLOSED / PASS;
- historical/provenance identity traceability = OPEN;
- EJR ambiguity remains the largest provenance-sensitive population;
- no bulk rename/delete/suppression is authorized.

Lease 191 selected a tooling/observability subgate before any identity mutation.

## Functional result

The current internal Document-ID audit now emits `ambiguous_duplicate_records` beside the unchanged `ambiguous_duplicate_ids` field.

Each ambiguous member exposes existing scanner facts:

- path;
- identity source (`DOCUMENT_ID_FIELD` or `FIRST_H1_FALLBACK`);
- canonical marker;
- active-index membership;
- status;
- deferred-domain state;
- filename prefix.

No ambiguity member is suppressed and `identity_scope_reconciled` semantics remain unchanged.

Prewrite commit:

`774d9b83c9d6b6ccc3ada51fde3ff4193d702acc`

Functional commit:

`044c5c41c31f98d944c663b33cc73d88784a71d6`

Exact functional changed set:

1. `Quality/Integration/internal_document_id_audit.py` — +16 / -0;
2. `Quality/Integration/test_internal_document_id_audit.py` — +37 / -0;
3. `Repository/MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191_MUTATION_MATRIX.md` — transaction binding only.

Unexpected paths = 0.

## Exact-head verification

Functional SHA `044c5c41c31f98d944c663b33cc73d88784a71d6`:

- Internal Document-ID Audit `33309485540` — SUCCESS;
- Full-Stack Repository Audit `33309485534` — SUCCESS;
- M2 Multi-Channel Proposal Training `33309485537` — SUCCESS;
- Real Mutation Matrix Regression `33309485557` — SUCCESS;
- Runtime Prototype and Integration Tests `33309485602` — SUCCESS.

Internal-ID artifact:

- ID `9731526902`;
- digest `sha256:92e07c6b47bf17d97f76e8a2557acd039101a5fddde366c18f452202c38ae67d`;
- exact head `044c5c41c31f98d944c663b33cc73d88784a71d6`.

Post-write read-back confirmed:

- scanner blob `50454dd20a2a5691f788c4580cce234dac13f0c1`;
- test blob `25b22f7d5794d8720ad31496e5bf9985d623df12`.

## Construction learning

A local clone attempt failed due execution-runtime DNS. It did not affect repository truth or mutation safety.

A first candidate reconstruction was rejected before repository mutation because it risked omitting source comments/docstrings. The final candidate was constructed from complete GitHub blob content and its source SHA was reproduced before transformation.

Learning persisted:

`CANDIDATE CONSTRUCTION CONVENIENCE MUST NOT OVERRIDE ZERO-TOUCH SOURCE PRESERVATION.`

`STRUCTURED EVIDENCE IS SAFER THAN REPEATED MANUAL RECONSTRUCTION.`

## Closed scope and preserved holds

`P2_EJR_AMBIGUITY_OBSERVABILITY_191 = CLOSED / EXECUTION-VERIFIED`.

Preserved:

- Priority 2 historical/provenance scope = OPEN;
- Phase 1 overall = OPEN;
- Global Connected Baseline = OPEN;
- Provider Authentication = HARD HOLD where applicable;
- Memory full-folder integrity = NOT CERTIFIED;
- Global `BOOTED / INTEGRITY PASS` = NOT CLAIMED.

## Next safe entry

1. Rediscover live `main`.
2. Re-read this checkpoint, Lease/Matrix 191, Lease 184 EJR stratification and current Memory Engineering Journal status.
3. Obtain the newest Internal-ID report/evidence from an exact current head.
4. Build the **EJR provenance group census** from `ambiguous_duplicate_records`.
5. Start with groups containing at least one `DOCUMENT_ID_FIELD` member; these are higher-information groups than H1-only repeats.
6. For each selected group inspect:
   `IDENTITY SOURCE → PATH/DATE/CONTENT → GIT HISTORY → REFERENCES → CONSUMERS → OWNER/SHADOW/REUSE DISPOSITION`.
7. Do not rename/delete/suppress any EJR until ownership and provenance consumers are proven.
8. If a true current identity defect is proven, open a new bounded lease + same-change-set Mutation Matrix before mutation.
9. Close the next session with exact-head verification and deterministic handoff.

Session state:

`CLOSED / RESUME-SAFE / P2 OBSERVABILITY-191 CLOSED / EJR PROVENANCE GROUP CENSUS NEXT`.
