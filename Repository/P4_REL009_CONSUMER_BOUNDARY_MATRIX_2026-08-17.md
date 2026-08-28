# P4 — REL-009 Consumer Boundary Matrix

Date: 2026-08-28
Status: `CLOSED / REGISTRY-SYNCHRONIZED / BOUNDED DIRECTIONAL SCOPE`
Authority: `GOV-013 / GOV-014 / GOV-015`

## Purpose
Protect `REL-009: RUN-010 → SRV-009` from speculative or over-broad promotion while preserving the bounded executable evidence now established and canonically synchronized.

This is a safety/evidence gate. It does not authorize a bidirectional or universal runtime relationship claim.

## Gate

| Gate | Condition | Final State |
|---|---|---|
| B01 | REL-009 exists in canonical registry | VERIFIED |
| B02 | Registry matches bounded directional disposition | VERIFIED — `REP-014` blob `d75f460d...` |
| B03 | RUN-010 distinguishes relationship description from universal runtime-path proof | VERIFIED |
| B04 | Automated safety test prevents accidental universal/executable overclaim | EXECUTION-VERIFIED |
| B05 | Boundary gate integrated into Full-Stack CI | VERIFIED |
| B06 | CI execution on merged P3/P4 main checkpoints | VERIFIED |
| B07 | Independent callable consumer source evidence | SOURCE-VERIFIED ON MAIN |
| B08 | Attributable RUN-010 → SRV-009 execution observation | EXECUTION-OBSERVED / ISOLATED INTEGRATION / EXACT-MAIN CI VERIFIED |
| B09 | Normal connected-spine negative runtime evidence | EXECUTION-VERIFIED |
| B10 | Negative runtime gate integrated into Full-Stack CI | VERIFIED |

## Merged Evidence

P3 clean proof:

`a538325bcde36d3a45f19583ca20d72d8f591e0a`

Exact-main verification:

- Full-Stack `33196013636` — SUCCESS;
- Runtime/Integration `33196013609` — SUCCESS;
- Real Mutation Matrix Regression `33196013638` — SUCCESS;
- M2 training `33196013623` — SUCCESS.

P4 semantic reconciliation:

`94a9bbb43432f3e098854571130778a498f76299`

Exact-main verification:

- Full-Stack `33196750118` — SUCCESS;
- Runtime/Integration `33196750113` — SUCCESS;
- M2 training `33196750126` — SUCCESS.

## Canonical Registry Synchronization

Transaction:

`MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`

Controlled mutation run `33197498585` — SUCCESS.

Verified:

- builder regressions: 3 passed;
- source registry blob `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- mutation commit `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob `d75f460d152898709044a31433e8ae4c705d9191`;
- request `APPLIED`;
- verified read-back true.

Canonical identity/type remain:

`RUN-010 → SRV-009 = CONSUMES`.

Canonical state:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

## Complete-Transaction Verification

First complete-transaction CI at `66cf5dde...` produced:

- Full-Stack `33199333266` — SUCCESS;
- Runtime/Integration `33199333252` — FAILURE in one stale integration assertion only;
- integrity/prototype jobs — SUCCESS.

The failing consumer was `Quality/Integration/test_control_plane_consumer_relationship_integrity.py`, which still asserted the historical absence of executable proof. C12 reconciled that semantic consumer without weakening the non-universal boundary.

Re-run at `58b1bae849481a22e76058b6f5ec6a4d05f88c46`:

- Full-Stack `33199477029` — SUCCESS;
- Runtime/Integration `33199477054` — SUCCESS.

Therefore the prior `REVALIDATION REQUIRED because executable evidence is absent` rationale is superseded for current operational interpretation.

## Final Disposition

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL / DISPOSITION-CLOSED`.

This closure is bounded:

- it does not mean every RUN-010 operation reaches SRV-009;
- it does not convert connected spine to production dispatch;
- it does not establish `SRV-009 → RUN-010`;
- provider-backed ENG-006/SRV-009 E2E remains a separate evidence class;
- it does not claim repository-wide graph closure or Connected-Baseline completion.

## Learning

`RETRIEVED/OBSERVED EXECUTION ≠ UNIVERSAL RUNTIME ROUTING`.

`IMPACT SEARCH MUST FIND SEMANTIC ASSERTION CONSUMERS, NOT ONLY THE FIRST FILE/PATH MATCHES`.

A broad audit PASS does not override a failing narrower integration consumer; both are required for closure.

## Final Merge Gate

This final closure wording requires exact-head CI before merge. No additional semantic change is authorized after that final-head verification.

---

End of Matrix
