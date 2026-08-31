# R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208

Status: CLOSED / SUCCESSOR-VERIFIED / RESUME-SAFE
Parent repair lease: `R71-20260830-P2-EJR-IDENTITY-REPAIR-207`
Functional commit: `8b6ab2b830deafffec7ff725417d7fa31547937d`
Verification successor: `R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-209`

## Defect repaired
The Internal Document-ID Audit scanned EJR state and ran EJR-specific analyzers but its push filter omitted `EJR/**`. Lease208 added only `EJR/**` to `.github/workflows/internal-id-audit.yml`; audit logic, test semantics, ambiguity handling, and EJR content were unchanged.

## Historical verification truth
The functional push at `8b6ab2b830deafffec7ff725417d7fa31547937d` successfully triggered Internal Document-ID Audit run `33329835211`. This proves the observability/configuration repair itself worked.

That run did **not** pass. All test execution and prior deterministic analyzers succeeded, but `ejr_memory_to_root_provenance_census.py` failed on `__COHORT_COUNT_DRIFT__`: expected 36 groups, observed 35. This failure is preserved as evidence and is not rewritten as success.

## Successor resolution
Lease209 proved the drift was the legitimate post-Lease207 state, preserved the drift guard, rebaselined only the expected cohort from 36 to 35, and closed execution-verified.

On Lease209 functional head `2092e90aa43df83a9731e31011d41990284b1654`:
- Internal Document-ID Audit `33352779923` — SUCCESS;
- census artifact `9744173384` — expected=35, observed=35, complete=true, decision=CENSUSED;
- Internal-ID artifact `9744172134` — EJR-214 and EJR-400 absent from ambiguity records;
- Full-Stack `33352779939` — SUCCESS;
- Runtime/Integration `33352780016` — SUCCESS;
- M2 `33352779922` — SUCCESS;
- Real Mutation Matrix `33352779936` — SUCCESS.

## Closure decision
Lease208 is CLOSED because its exact authorized trigger addition is proven effective, and the independent defect exposed by its first exact-head run was resolved and execution-verified by the bounded successor Lease209. The original failed run remains part of the causal evidence chain.

## Learning promoted
`AN AUDIT THAT SCANS A DOMAIN BUT DOES NOT TRIGGER ON DIRECT MUTATIONS OF THAT DOMAIN HAS AN OBSERVABILITY COVERAGE GAP; FIX TRIGGER COVERAGE WITHOUT WEAKENING THE AUDIT.`

## Boundaries
Priority 2 OPEN. Phase 1 OPEN. Global integrity HOLD. No global PASS or Connected-Baseline closure claimed.
