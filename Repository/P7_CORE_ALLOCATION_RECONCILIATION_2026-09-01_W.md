# Priority 7 — Core Allocation Reconciliation — Transaction W

Date: 2026-09-01
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / CORE ALLOCATION EVIDENCE 18-OF-18 / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-CORE-ALLOCATION-20260901`
Material candidate: `b1ded1d55ee5ab2f707d0e24cb5b03a5d1bd28e3`

## Result

Explicit Certification Review V routed Priority 7 back to the missing allocation gate. W/W-A/W-B resolved the bounded evidence problem without weakening REP-013 or rewriting the long canonical REP-012 body.

The governed non-replacing REP-012 Core allocation addendum records the exact current 18 top-level Core paths as `ALLOCATED` under REP-012 allocation semantics. The focused Integrity regression binds physical inventory, self-excluding Core index semantics, allocation coverage and legacy/noncanonical CORE-000 treatment.

Canonical REP-012 and REP-020 were not mutated; W-A's manifest synchronization condition became inapplicable when W-B removed the REP-012 version change before material mutation.

## Atomicity

Material candidate compare from W-B pre-write HEAD `f0f564b68cd6e0f957327839db40316ea73c22cf` to candidate `b1ded1d55ee5ab2f707d0e24cb5b03a5d1bd28e3`:

`1 COMMIT / 7 AUTHORIZED PATHS / 0 UNEXPECTED EXPANSION`.

## Exact-head CI

Candidate `b1ded1d55ee5ab2f707d0e24cb5b03a5d1bd28e3` passed all four required workflows:

- Real Mutation Matrix Regression `33539482726` — SUCCESS;
- Full-Stack Repository Audit `33539482751` — SUCCESS;
- M2 Multi-Channel Proposal Training `33539482763` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33539482791` — SUCCESS.

Runtime overall conclusion is SUCCESS; no failure recovery transaction is required.

## Bounded closure

W closes only the Core allocation-evidence corrective transaction.

It does not certify Core, close `CROSS-LAYER VALIDATION OPEN`, close Priority 7, or claim repository-wide REP-012 population completeness.

A fresh Explicit Core Certification Review is now the next bounded candidate action **only after live-main rediscovery and current evidence re-read**. That review must decide whether the verified addendum satisfies REP-013's allocation prerequisite and whether any other blocker remains.

## Learning retained

`ALLOCATION IS A LOCATION/OWNERSHIP FACT, NOT A SEMANTIC CERTIFICATE.`

`A VALID PRE-WRITE AMENDMENT MAY BE SUPERSEDED BEFORE MATERIAL MUTATION WHEN NEW EVIDENCE REMOVES ITS TRIGGER; PRESERVE THE VALID LEARNING AND DOCUMENT THE SUPERSESSION.`

`LOWER-RISK ADDITIVE EVIDENCE IS PREFERRED TO A WHOLE-FILE CONTROL-PLANE REWRITE WHEN BOTH CAN EXPRESS THE SAME BOUNDED FACT WITHOUT AUTHORITY LOSS.`
