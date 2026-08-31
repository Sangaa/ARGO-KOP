# Lease 314 — EJR-234 Disposition and EJR-429 Complete-History Vacancy Proof

Status: OPEN / EVIDENCE-ONLY / NO IDENTITY MUTATION
Date: 2026-08-31

## Scope
Resolve the remaining MEMORY_TO_ROOT_EJR ambiguity for EJR-234 without changing either current member until a complete-history successor-vacancy gate passes.

## Current evidence
- Memory member: `Memory/Engineering_Journal/EJR-234_2026-08-14_P52_SESSION_CLOSURE.md`.
- Root member: `EJR/EJR-234_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md`.
- Memory allocation commit/time: `162d53acf143ee19026be33d89e004e49b18cb68` / `2026-08-14T21:04:10Z`.
- Root allocation commit/time: `5a06ddc258f8010198d0fc834fc84f18ffa28d49` / `2026-08-17T16:23:56Z`.
- Both records are semantically legitimate and distinct.

## Disposition candidate
Apply the first-valid historical allocation rule: retain EJR-234 for the earlier Memory allocation unless stronger evidence invalidates that allocation. No such invalidating evidence was found in the current review. The later root record is therefore the displacement candidate.

## Successor candidate
`EJR-429` is a candidate only. Current search absence is discovery evidence and is not a vacancy proof.

## Hard gate
Repair is prohibited until `.github/workflows/ejr-replacement-vacancy-proof-314.yml` executes with complete history and its artifact reports all of:
- `candidate = EJR-429`
- `history_complete = true`
- `current_claims = []`
- `historical_claims = []`
- `decision = VACANT`

## Non-claims
- No identity mutation is authorized by opening this lease.
- No authority or governance promotion is implied.
- Global Integrity remains HOLD.
