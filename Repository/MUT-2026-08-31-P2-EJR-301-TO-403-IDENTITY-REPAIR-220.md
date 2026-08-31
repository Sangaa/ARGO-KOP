# R71-20260831-P2-EJR-301-TO-403-IDENTITY-REPAIR-220

Status: CLOSED / SUCCESSOR-VERIFIED / ONE-RECORD+CONSUMER REPAIR / RESUME-SAFE
Baseline: `main@a52f3902690e28933de7f61977da6298921b55b6`
Prewrite: `d3c5e7931228d0d4f7c86848843792864424d8bb`
Functional head: `a78bf0dd8760b036656515c39378261a1c0a2a09`
Source: `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`
Replacement: `EJR-403` — vacancy proven by Lease219 / run `33356981274` / artifact `9745435896`.
Retained allocation: `Memory/Engineering_Journal/EJR-301_2026-08-22_HERMUZ_P6_CI_EXECUTION_RECHECK.md`.
Direct governed consumer: `Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md`.

## Executed transaction
- old root EJR-301 GT-040 path removed;
- `EJR/EJR-403_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md` created with semantic body/chronology preserved and H1 identity changed to EJR-403;
- REP-021 updated in the same functional transaction to point to the EJR-403 learning record;
- Memory EJR-301 was not mutated.

Compare `d3c5e793...` → `a78bf0dd...` proves the bounded change set: one identity rename plus one direct consumer rewrite.

## Functional-head evidence
At `a78bf0dd8760b036656515c39378261a1c0a2a09`:
- Full-Stack Repository Audit `33357105886` — SUCCESS;
- Runtime Prototype and Integration Tests `33357106003` — SUCCESS;
- M2 Multi-Channel Proposal Training `33357105888` — SUCCESS;
- Internal Document-ID Audit `33357105926` — FAILURE only at the preserved memory→root census drift guard after tests and prior analyzers passed.

Artifact `9745485604`, digest `sha256:960cb6e1ab8fbca683aa4e746c93ed84ca435e6e3abe20f1e2456f8ba85e11da`, proved expected=33 / observed=32 / history_complete=true / sole incomplete=`__COHORT_COUNT_DRIFT__`. Internal-ID artifact `9745483825`, digest `sha256:a290795b99ef166c215d632c524edd8d9fe72ee81349807d794c3b54f943b3cc`, proved neither EJR-301 nor EJR-403 remained ambiguous.

This failure is preserved as historical evidence. It is not rewritten as success. Lease221 separately rebaselined the now-proven post-repair cohort 33→32 and exact-head Internal-ID then succeeded.

Real Mutation Matrix did not trigger on the functional repair diff; that is recorded as NOT APPLICABLE to that exact diff, not PASS/FAIL.

## Learning
A direct governed consumer rewrite belongs in the same bounded identity-repair transaction as the displaced record. A legitimate ambiguity-group removal must first surface through the drift guard; any baseline change is a separate successor mutation.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
