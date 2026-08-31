# Mutation Matrix — Lease 305 — EJR-247 Disposition / EJR-426 Vacancy Proof

Status: OPEN / PRE-MUTATION
Date: 2026-08-31

## Proposed Changes

| Path | Change | Authority impact | Runtime impact | Reversible |
|---|---|---:|---:|---:|
| `Repository/MUT-2026-08-31-P2-EJR-247-DISPOSITION-AND-426-VACANCY-PROOF-305.md` | evidence record | none | none | yes |
| `.github/workflows/ejr-replacement-vacancy-proof-305.yml` | complete-history evidence workflow | none | CI-only | yes |

## Protected-Surface Assessment

- No Core/Governance/Architecture/Runtime/Service semantic mutation.
- No EJR identity mutation in this lease.
- No canonical promotion.
- Successor allocation remains blocked until `VACANT` artifact is inspected.

## Rollback

Delete the evidence workflow/record if the gate design proves invalid. A non-VACANT decision requires no identity rollback because no identity mutation is authorized in this lease.
