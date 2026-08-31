# MUT-2026-08-31-P2-EJR-406-REPLACEMENT-VACANCY-PROOF-231

Status: PREWRITE / VACANCY PROOF ONLY
Candidate: `EJR-406`
Parent authorization: Lease230 / EJR-173 displaced-root disposition

Code search and commit search currently return no EJR-406 claim, but search absence is treated as discovery only. This lease proves allocation vacancy through `Quality/Integration/ejr_allocation_vacancy_gate.py` on complete reachable history.

No EJR owner, consumer, baseline, analyzer semantics, or authority surface may be changed by this lease.

Success condition: workflow artifact reports `history_complete=true`, `current_claims=[]`, `historical_claims=[]`, `occupied=false`, `vacant=true`, `decision=VACANT`.
Failure/HISTORY_INCOMPLETE blocks allocation.
