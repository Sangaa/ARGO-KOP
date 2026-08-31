# MUT-2026-08-31-P2-EJR-233-TO-413-IDENTITY-REPAIR-266

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: One-record Priority-2 identity repair: displaced root EJR-233 → EJR-413.
Opening main: `c35d939f56dcc173f976f247d51fbb60816de1ea`
Pre-write Matrix266: `1c8acaa26282f9901cb54863b0c539ed1bc2b542`
Execution lease commit: `af8a6027cdf5d6227f6dd8c703b160ccfcd6dcb7`
Functional repair head: `a47c20d9b065533107f47cecc1e82e92bf8847f6`
Normalized successor: Lease267 / functional head `338732cd880a8f6d1a12672aa2e2980c26b49fa6` / closure `4dad24937cf4e4bc1702e3e6302cadd2b6bae0b3`.

## Authority and disposition

- Lease264 retained the earlier Memory EJR-233 and classified the later root allocation displaced.
- Lease265 proved EJR-413 VACANT across complete reachable history and reserved it for exactly one bounded replacement allocation.
- Repair266 retained `Memory/Engineering_Journal/EJR-233_2026-08-14_P51_SESSION_CLOSURE.md`, removed the displaced root EJR-233 path, created `EJR/EJR-413_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md`, changed only the root H1 identity EJR-233 → EJR-413, and preserved semantic body/date/chronology and historical footer `End of EJR-233`.
- No direct executable/operational consumer requiring rewrite was established; historical disposition references remain unchanged as provenance evidence.

## Exact repair-head verification

The Repair266 functional head preserved `EXPECTED_GROUP_COUNT = 24`. Identity, chronology, lineage, provenance, Full-Stack, Runtime, Mutation Matrix and M2 evidence were clean; the Internal-ID channel failed only at deterministic MEMORY_TO_ROOT cohort drift.

Repair266 census artifact `9751379903`, digest `sha256:4d71b41256ea0d308769d61f10145efecb1ba07eee6067218f77f7f1c055abf8`, proved:
- expected_group_count=24
- observed_group_count=23
- history_complete=true
- classification_complete=false
- decision=PARTIAL
- sole incompleteness=`__COHORT_COUNT_DRIFT__`

This was classified as bounded post-repair baseline drift, not a repair defect.

## Normalized successor

Lease267 executed the separate established baseline-successor pattern. Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed from `EXPECTED_GROUP_COUNT = 24` to `23`; no classifier logic, tests, workflows, EJR/Memory/GOV/REP/history or Global Integrity state changed.

Lease267 exact-head verification:
- Internal Document-ID Audit #60 / run `33374897233`: SUCCESS
- Full-Stack Repository Audit #2375 / run `33374897260`: SUCCESS
- ARGO Runtime Prototype and Integration #2149 / run `33374897257`: SUCCESS
- M2 #1032 / run `33374897254`: SUCCESS

Final census artifact `9751501145`, digest `sha256:d83115ddec53c17e030f985affe8d7b251db38432d18037ebb77dcce2a4330b1`, proves expected=23, observed=23, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

## Learning / transfer disposition

No new governance rule is promoted. This is another execution-confirmed application of the existing Repair → separate deterministic cohort-baseline successor pattern already proven by Leases258 and 263.

## Final boundary and resume

Repair266 and normalized successor Lease267 are CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next safe entry: after validating this closure commit, select the next Priority-2 target from the current verified 23-group MEMORY_TO_ROOT census using fresh consumer/risk/chronology evidence. Do not assume historical ordering.