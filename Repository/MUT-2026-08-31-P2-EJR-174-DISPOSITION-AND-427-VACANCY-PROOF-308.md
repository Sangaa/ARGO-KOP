# MUT — EJR-174 Disposition and EJR-427 Vacancy Proof — Lease 308

Date: 2026-08-31
Status: OPEN / EVIDENCE GATE
Priority: P2 Internal Document-ID Audit

## Scope
Resolve only the disposition gate for the current H1 ambiguity pair carrying `EJR-174`, and prove whether `EJR-427` is a valid successor allocation candidate. This lease performs no identity mutation.

## Current evidence
- Current deterministic MEMORY_TO_ROOT_EJR census is complete at 10 groups.
- `Memory/Engineering_Journal/EJR-174_2026-08-13_SERVICES_MATRIX_REVIEW.md` is the earlier valid allocation surface.
- `EJR/EJR-174_2026-08-14_MATRIX_UPDATE_NOTE.md` is a later independent root allocation.
- The two records have distinct content and distinct purposes.
- Under the first-valid historical allocation rule, the Memory record retains `EJR-174` unless stronger contrary evidence appears.
- The later root record is therefore the displacement candidate, subject to successor vacancy proof.

## Candidate successor
`EJR-427`

Current search absence is discovery only and is not accepted as vacancy proof.

## Required gate
Run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-427` from a complete-history checkout and require `decision = VACANT` before any rename, delete, reassignment, or identity mutation.

## Decision boundary
If complete-history proof returns VACANT and Full-Stack remains green, Lease 308 may close with authorization for a separate repair lease. Otherwise stop and preserve both current identities unchanged.

## Integrity
Global Integrity remains HOLD. Priority 2 and Phase 1 remain OPEN.
