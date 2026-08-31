# Lease 311 — EJR-248 Disposition and EJR-428 Complete-History Vacancy Proof

Status: OPEN / EVIDENCE GATE
Date: 2026-08-31
Scope: Priority 2 MEMORY_TO_ROOT_EJR identity reconciliation

## Evidence
- Current deterministic cohort baseline: 9.
- EJR-248 has two current H1 members with namespace sequence MEMORY_EJR → ROOT_EJR.
- `Memory/Engineering_Journal/EJR-248_2026-08-15_P67_SESSION_CLOSURE.md` predates the root member and represents the first valid observed EJR-248 allocation.
- `EJR/EJR-248_2026-08-18_TODAY_BUILD_PLAN_AND_SESSION_CLOSURE.md` is a later, semantically distinct journal allocation.

## Disposition
Apply the first-valid historical allocation rule: retain EJR-248 for the Memory journal unless contradictory stronger evidence appears. The later root journal is the displacement candidate.

No identity mutation is authorized until complete-history vacancy proof establishes that candidate successor EJR-428 is VACANT.

## Required gate
Run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-428` from a non-shallow complete-history checkout and preserve the resulting artifact. Current code-search absence alone is not vacancy proof.

## Non-claims
- No ownership promotion.
- No root rename yet.
- No baseline normalization yet.
- Global Integrity remains HOLD.
