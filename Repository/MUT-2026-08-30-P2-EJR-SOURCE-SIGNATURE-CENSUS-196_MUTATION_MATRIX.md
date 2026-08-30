# MUTATION MATRIX — P2 EJR SOURCE-SIGNATURE CENSUS 196

Transaction ID: `MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
State: `PREWRITE / NOT APPLIED`
Source head: `afe52f71cef0041e7f58218d6846f9182c868f83`
Source audit blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`

| Change ID | Section | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 196-001 | companion census analyzer | ADD | deterministic source signatures from existing `ambiguous_duplicate_records` | N | N |
| 196-002 | EJR bounded census | ADD | EJR-only group/signature/cardinality counts without scanner allowlisting | N | N |
| 196-003 | companion tests | ADD | metadata-only, H1-only, mixed, unknown-source visibility, cardinality and immutability | N | N |
| 196-004 | internal-ID gate and membership | KEEP | scanner source, ambiguity membership and pass/fail semantics remain untouched | N | N |

## Authorized changed paths

1. `Quality/Integration/ejr_ambiguity_source_signature_census.py`
2. `Quality/Integration/test_ejr_ambiguity_source_signature_census.py`
3. `Repository/MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.
