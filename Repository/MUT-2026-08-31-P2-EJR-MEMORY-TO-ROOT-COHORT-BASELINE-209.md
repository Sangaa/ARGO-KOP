# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-209

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Parent verification lease: `R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208`
Prewrite: `19ff6beeae781627fd6d41be997c998ebf8fe1dc`
Functional head: `2092e90aa43df83a9731e31011d41990284b1654`

## Trigger and diagnosis
Lease208 restored automatic `EJR/**` trigger coverage. Its exact-head Internal Document-ID Audit run `33329835211` correctly triggered but exposed one isolated pre-existing post-repair drift: `ejr_memory_to_root_provenance_census.py` expected 36 classifier-selected `MEMORY_TO_ROOT_EJR` groups while the live state contained 35. All test execution and prior analyzers passed; only this census exited PARTIAL with `__COHORT_COUNT_DRIFT__`.

The reduction is proven and authorized, not unexplained loss: Lease207 re-identified the displaced root `EJR-214` record as vacancy-proven `EJR-400`, eliminating exactly one ambiguity group.

## Prior-learning application
- Lease202 fail-on-count-drift behavior: `DIRECTLY APPLICABLE` and preserved.
- Lease207 one-record identity repair: `DIRECTLY APPLICABLE` causal evidence.
- Lease206 atomic prewrite rule: `DIRECTLY APPLICABLE`; Lease+Matrix were attached through atomic tree/commit/update_ref before functional mutation.

## Functional mutation
Exactly one analyzer baseline constant changed:
- `EXPECTED_GROUP_COUNT = 36` → `EXPECTED_GROUP_COUNT = 35`

No classifier logic, drift guard, history gate, test semantics, EJR content/path/identity, ownership decision, suppression, or authority boundary was changed.

Functional compare `19ff6beeae781627fd6d41be997c998ebf8fe1dc...2092e90aa43df83a9731e31011d41990284b1654` contains only:
- `Quality/Integration/ejr_memory_to_root_provenance_census.py` — 1 addition / 1 deletion;
- Lease209 Mutation Matrix synchronization.

## Execution evidence
All exact-head checks on `2092e90aa43df83a9731e31011d41990284b1654` passed:
- Internal Document-ID Audit `33352779923` — SUCCESS;
- Full-Stack Repository Audit `33352779939` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33352780016` — SUCCESS;
- M2 Multi-Channel Proposal Training `33352779922` — SUCCESS;
- Real Mutation Matrix Regression `33352779936` — SUCCESS.

Deterministic census artifact:
- artifact `ejr-memory-to-root-provenance-census` / ID `9744173384`;
- digest `sha256:9d53f740536c5b8349bf5bf037c8fce75ee5b563307d8e06b3756df1e2b31cd9`;
- `expected_group_count = 35`;
- `observed_group_count = 35`;
- `history_complete = true`;
- `classification_complete = true`;
- `decision = CENSUSED`;
- `incomplete_group_ids = []`.

Internal-ID artifact:
- artifact `internal-document-id-audit-report` / ID `9744172134`;
- digest `sha256:c67c083b0e480706c7a0e708983294223bf96b4cee8c0793a57260b4756611d7`;
- neither `EJR-214` nor `EJR-400` is present in `ambiguous_duplicate_records`;
- current `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md` exists with H1 `EJR-400`;
- old root path `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md` is absent.

## Learning promoted
`WHEN A DRIFT GUARD CORRECTLY FAILS AFTER A SEPARATELY AUTHORIZED IDENTITY REPAIR, REBASELINE ONLY FROM PROVEN POST-REPAIR STATE; PRESERVE THE GUARD AND ITS FAILURE SEMANTICS.`

## Boundaries preserved
Priority 2 remains OPEN. Phase 1 remains OPEN. Repository-wide identity/content/relationship reconciliation remains OPEN. Connected-Baseline/global graph validation remains OPEN. Global integrity remains HOLD. No `BOOTED / INTEGRITY PASS` is claimed.

## Next legal action
Reconcile the verification chain for Lease208 and Lease207 using the successor evidence above. Their historical failed/missing exact-head audit evidence must remain recorded accurately; successor evidence may close the dependency gap but must not rewrite history.
