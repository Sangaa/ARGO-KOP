# MUT-2026-08-31-P2-EJR-233-TO-413-IDENTITY-REPAIR-266

Status: OPEN / EXECUTION-PENDING
Scope: One-record Priority-2 identity repair: displaced root EJR-233 → EJR-413.
Opening main: `c35d939f56dcc173f976f247d51fbb60816de1ea`
Pre-write Matrix266: `1c8acaa26282f9901cb54863b0c539ed1bc2b542`

## Authority

- Lease264 retained the earlier Memory EJR-233 and classified the later root EJR-233 allocation displaced.
- Lease265 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and proves EJR-413 VACANT across complete reachable history; artifact `9751158049` proves `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `occupied=false`, `vacant=true`, `decision=VACANT`.
- EJR-413 is reserved for exactly one bounded replacement allocation: this repair.

## Fresh source evidence

Current displaced source:
`EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md`

Source blob at pre-write read:
`f78a69c14793fb8331fe0096e656bfd1957a94a7`

The source H1 is `# EJR-233 — GOV-015 First Execution Application`. Historical body/footer text ends with `End of EJR-233` and must remain preserved.

## Consumer obligations

Fresh searches for the exact old path and EJR-233 surfaced historical Lease264 disposition evidence. These references remain unchanged because they describe the historical path/identity accurately.

No direct executable/operational consumer requiring rewrite has been established. Lease263 deterministic census had established zero external exact-ID and zero exact-member-path refs for the group before governance evidence was added. Repair266 therefore performs zero consumer rewrites unless a fresh executable consumer appears before execution.

## Pre-write validation

Matrix266 commit `1c8acaa26282f9901cb54863b0c539ed1bc2b542` passed:
- Full-Stack Repository Audit #2370 / run `33374290784`: SUCCESS
- ARGO Runtime Prototype and Integration #2144 / run `33374290786`: SUCCESS
- Real Mutation Matrix Regression #205 / run `33374290791`: SUCCESS
- M2 #1027 / run `33374290897`: SUCCESS

## Authorized atomic mutation

One functional tree mutation may:
1. retain `Memory/Engineering_Journal/EJR-233_2026-08-14_P51_SESSION_CLOSURE.md` unchanged;
2. remove `EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md`;
3. create `EJR/EJR-413_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md`;
4. preserve root semantic body/date/chronology byte-for-byte except H1 identity `EJR-233` → `EJR-413`;
5. preserve historical footer/body text including `End of EJR-233`;
6. update Matrix266 in the same functional commit to `FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING`.

## Baseline boundary

`EXPECTED_GROUP_COUNT = 24` must remain unchanged inside Repair266. An exact repair-head result `expected=24 / observed=23` is acceptable only when the sole incompleteness is `__COHORT_COUNT_DRIFT__`; any correction belongs to a separate successor lease.

## Hard gate

Immediately before mutation, re-discover live main and re-read the source. Abort if main is not this lease commit, if source blob is not `f78a69c14793fb8331fe0096e656bfd1957a94a7`, if the EJR-413 target path exists, or if a new executable consumer is established.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.