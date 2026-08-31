# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-221

Status: OPEN / PREWRITE AUTHORITY
Baseline: `main@a78bf0dd8760b036656515c39378261a1c0a2a09`
Predecessor repair: Lease220 — root EJR-301 re-identified to vacancy-proven EJR-403 with direct consumer REP-021 updated atomically.

## Evidence basis
Lease220 exact-head Internal Document-ID Audit run `33357105926` failed only at the deterministic memory-to-root provenance census after tests and all prior analyzers passed. Artifact `9745485604`, digest `sha256:960cb6e1ab8fbca683aa4e746c93ed84ca435e6e3abe20f1e2456f8ba85e11da`, proves:
- expected_group_count = 33;
- observed_group_count = 32;
- history_complete = true;
- classification_complete = false;
- decision = PARTIAL;
- incomplete_group_ids = [`__COHORT_COUNT_DRIFT__`].

Internal-ID artifact `9745483825`, digest `sha256:a290795b99ef166c215d632c524edd8d9fe72ee81349807d794c3b54f943b3cc`, shows neither EJR-301 nor EJR-403 remains in ambiguous_duplicate_records. All 32 selected groups are individually complete. Full-Stack `33357105886`, Runtime/Integration `33357106003`, and M2 `33357105888` succeeded on the repair head.

## Allowed functional mutation
Exactly one semantic constant in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
- `EXPECTED_GROUP_COUNT = 33` → `EXPECTED_GROUP_COUNT = 32`.

No classifier, scanner, evidence boundary, failure semantics, tests, EJR record, consumer, REP authority surface, or unrelated file may be changed except this Lease and its Mutation Matrix/closure evidence.

## Required verification
At the exact functional head:
1. Internal Document-ID Audit must SUCCESS.
2. Deterministic memory-to-root census must report 32/32, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].
3. EJR-301 and EJR-403 must remain non-ambiguous.
4. Full-Stack Repository Audit, Runtime Prototype/Integration, and M2 must SUCCESS.
5. Real Mutation Matrix is applicable only on a diff matching its governed path filter; non-trigger is recorded as NOT APPLICABLE, never fabricated.

## Learning rule
A direct governed consumer rewrite belongs in the same identity-repair transaction as the displaced record. If that valid repair removes one classifier-selected ambiguity group, preserve the guard failure first, then rebaseline separately from proven post-repair state without weakening the guard.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
