# MUTATION MATRIX — P2 EJR SOURCE-SIGNATURE CENSUS 196

Transaction ID: `MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
State: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Source head: `afe52f71cef0041e7f58218d6846f9182c868f83`
Prewrite head: `7ea957bddbe726d1dc29d2e517703b59c5e03509`
Source audit blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`
Source workflow blob: `27a2a9106c5adf80bfb0d04fed56b0e4b0414f18`
Candidate census blob: `c9b9d2a571ca7973af3774ac21604a8d7776d0a0`
Candidate test blob: `f7d2e7109f20798b1814be3ca9c3c4a48f0dfc42`
Candidate workflow blob: `4c99bb7188faeb0673b62512d92977bef7b84562`

| Change ID | Section | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 196-001 | companion census analyzer | ADD | deterministic source signatures from existing `ambiguous_duplicate_records` | Y | N |
| 196-002 | EJR bounded census | ADD | EJR-only group/signature/cardinality counts without scanner allowlisting | Y | N |
| 196-003 | companion tests | ADD | metadata-only, H1-only, mixed, unknown-source visibility, cardinality and immutability | Y | N |
| 196-004 | Internal-ID workflow | UPDATE | trigger/run companion tests and emit/upload census JSON | Y | N |
| 196-005 | internal-ID gate and membership | KEEP | scanner source, ambiguity membership and pass/fail semantics remain untouched | Y | N |

## Authorized changed paths

1. `Quality/Integration/ejr_ambiguity_source_signature_census.py`
2. `Quality/Integration/test_ejr_ambiguity_source_signature_census.py`
3. `.github/workflows/internal-id-audit.yml`
4. `Repository/MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.
