# MUTATION MATRIX — EJR-241 DISPOSITION + EJR-416 VACANCY PROOF 275

Status: PREWRITE / EVIDENCE-ONLY EXECUTION
Transaction ID: MUT-2026-08-31-P2-EJR-241-DISPOSITION-AND-416-VACANCY-PROOF-275
Opening main: `c421044c3e8c9782a3344f0b465f041411bf15f8`
Execution role: HERMUZ

## Selection evidence

The normalized MEMORY_TO_ROOT census contains 21 groups. EJR-241 is selected by fresh risk/consumer/chronology evidence rather than numeric order:
- both current members are distinct legitimate records;
- Memory member is dated 2026-08-15 while root member is dated 2026-08-17;
- current census reports only the two historical baseline references for exact EJR-241 ID and zero exact member-path consumers;
- fresh exact old-root-path search returned zero consumers;
- this makes EJR-241 a low-coupling candidate for first-valid-allocation disposition analysis.

## Authorized evidence work

1. Preserve both EJR-241 members byte-for-byte.
2. Classify retained/displaced identity only from chronology/current evidence.
3. Add a dedicated complete-history vacancy-proof workflow for candidate EJR-416 using the existing fail-closed `Quality/Integration/ejr_allocation_vacancy_gate.py`.
4. Upload and inspect deterministic vacancy evidence.
5. Record proof results in this lease/matrix only after execution.

## Exclusions

No EJR/Memory rename, delete, move, H1/body mutation, consumer rewrite, cohort baseline change, classifier/test semantic change, GOV/REP mutation, or Global Integrity promotion is authorized in Lease275.

## Verification contract

- workflow must use `fetch-depth: 0` and prove the checkout is non-shallow;
- candidate EJR-416 must produce current_claims=[], historical_claims=[], history_complete=true, decision=VACANT before reservation;
- Full-Stack must remain successful on the proof head;
- if EJR-416 is not VACANT, no repair may be opened and another candidate ID requires a separate proof;
- any future EJR-241 identity repair requires a separate successor Mutation Matrix and fresh hard gates.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
