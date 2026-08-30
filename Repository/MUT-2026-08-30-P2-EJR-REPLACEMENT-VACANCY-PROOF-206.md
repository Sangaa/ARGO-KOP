# R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206

Status: PREWRITE / EVIDENCE-ONLY
Baseline: main@a622ae60dd4c19420cbd60c55e6dc3c3ccac401f
Target repair candidate: EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md
Replacement candidate under test: EJR-400

## Goal
Prove or reject EJR-400 as a collision-safe replacement identity using the execution-verified Lease-193 vacancy gate with complete locally reachable Git history before any EJR identity mutation is authorized.

## Prior evidence
- Room 204 identifies root EJR-214 as a legitimate later reuse that must be displaced in a separate execution lease.
- Room 205 resumes that exact legal priority.
- Current direct code search for `EJR-400`, commit search for `EJR-400`, and current EJR directory inspection expose no current claim, but search absence is not vacancy proof.
- `Quality/Integration/ejr_allocation_vacancy_gate.py` is the authoritative execution-verified reference for this bounded proof.

## Authorized scope
1. Add one evidence-only workflow that checks out full history (`fetch-depth: 0`).
2. Run the existing vacancy gate unchanged against `EJR-400`.
3. Upload the deterministic JSON report.
4. Do not mutate, rename, delete, reassign, normalize, suppress, or allocate any EJR record in this lease.

## Decision gate
- VACANT => EJR-400 becomes eligible for a separate repair-execution lease; this lease itself does not allocate it.
- OCCUPIED => reject EJR-400 and select another candidate in a successor proof.
- HISTORY_INCOMPLETE => fail closed; no allocation.

## Preserved boundaries
Priority 2 remains OPEN. Phase 1 remains OPEN. Global Connected Baseline remains OPEN. No control-plane semantic authority is promoted.
