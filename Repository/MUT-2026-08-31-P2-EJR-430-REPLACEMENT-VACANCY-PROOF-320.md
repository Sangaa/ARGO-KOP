# Lease 320 — EJR-430 Complete-History Vacancy Proof

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31
Parent: Lease319

## Candidate and proof
`EJR-430` was treated only as a successor candidate until complete-history execution.

Dedicated workflow `EJR-430 Vacancy Proof 320`, run `33422684323`, executed on proof head `eb4407cf280074a223d4efe0e90826257ac4428b` with full history and reported:
- candidate: EJR-430
- current_claims: []
- historical_claims: []
- history_complete: true
- history_scope: all locally reachable refs
- occupied: false
- vacant: true
- decision: VACANT

Artifact: `ejr-430-vacancy-proof`, ID `9769515369`, zip digest `sha256:99cc96a04d9384bc6a2e21e72e162f1076d3ce6b3b799ca522df0ab28a925223`.

## Lifecycle boundary
The workflow is triggered only by the one-time `p2_ejr430_vacancy_trigger.txt` path. Later valid allocation of EJR-430 does not retrigger the historical VACANT assertion merely because Lease320 records are closed.

## Authorization boundary
Lease320 proves vacancy only. Lease319 already authorized disposition. A separate repair lease/matrix is required before any EJR-240 → EJR-430 identity mutation.

Priority 2 remains OPEN.
Phase 1 remains OPEN.
Global Integrity remains HOLD.