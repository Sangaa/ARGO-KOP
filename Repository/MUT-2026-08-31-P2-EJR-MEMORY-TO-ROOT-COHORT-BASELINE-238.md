# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-238

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: separate cohort baseline successor after EJR-208→EJR-407 repair.

Prewrite: `927a851309359b93603107e62f11e4bfa8741555`.
Functional head: `c25874dddb57c0adcbddce51f2bbe40f6115f972`.

Authorized functional change only:
`Quality/Integration/ejr_memory_to_root_provenance_census.py`
`EXPECTED_GROUP_COUNT = 30` → `29`.

Compare proved one file / one addition / one deletion; classifier, scanner, evidence boundary, tests, workflows, EJR records, consumers, and authority semantics were unchanged.

Exact functional-head verification:
- Internal-ID `33362098103`: SUCCESS;
- Full-Stack `33362098152`: SUCCESS;
- Runtime `33362098072`: SUCCESS;
- M2 `33362098095`: SUCCESS;
- Real Mutation Matrix: NOT APPLICABLE to the census-only diff.

Deterministic census artifact `9747038968`, digest `sha256:6c0384953491f06e88d50f37bb39e14fe8dd3d1ae5e60ff640f47d85caa80005`, proved expected_group_count=29, observed_group_count=29, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], with EJR-208 and EJR-407 absent from the remaining cohort.

Current governed MEMORY_TO_ROOT baseline after this successor is 29.
