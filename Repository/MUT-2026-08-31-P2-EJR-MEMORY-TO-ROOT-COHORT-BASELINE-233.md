# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-233

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Predecessor: Lease232 repair `EJR-173 → EJR-406`

Repair-head evidence authorized one baseline-only mutation. Functional head `b29d29379598f1554c518461503bbe998d8037b1` changed only `EXPECTED_GROUP_COUNT = 31`→`30` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`. Compare `c13fe3b898863e113e1a082531e6b4984aa65053`→`b29d293...` proved one file with one addition and one deletion only.

Exact functional-head verification:
- Internal-ID `33361269760`: SUCCESS;
- Full-Stack `33361269731`: SUCCESS;
- Runtime `33361269737`: SUCCESS;
- M2 `33361269738`: SUCCESS;
- Real Matrix: NOT APPLICABLE to the census-only functional diff because its path filter did not trigger.

Census artifact `9746770011`, digest `sha256:52705bdb43b64ae11760d9bacf22c832aa7f19aefebe68287ac2e52d3f89eb8a`, proved expected=30, observed=30, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].

No classifier/scanner/evidence-boundary/test/workflow/EJR/consumer semantics changed. Current controlled MEMORY_TO_ROOT baseline is 30.
