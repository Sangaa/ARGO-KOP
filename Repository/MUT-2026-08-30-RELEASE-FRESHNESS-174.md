# MUT-2026-08-30-RELEASE-FRESHNESS-174

Date: 2026-08-30
Lease: `R71-20260830-RELEASE-FRESHNESS-174`
Execution role: HERMUZ
Re-entry baseline: `main@98c23b2489fab5684a3cbdd791402dbcbe2d5423`
Prewrite checkpoint: `main@86c6969d863e24b45db9f0c7a20623a7cbe1b332`
Protocol: `PROJECT_BOOTSTRAP + CORE-003 + GOV-013 + GOV-013A + GOV-014 + GOV-021 + GOV-027`
Status: `CLOSED / EVIDENCE-VERIFIED / BOUNDED / NO RELEASE MUTATION`

## Re-entry proof

Live `main` was independently rediscovered at `98c23b2489fab5684a3cbdd791402dbcbe2d5423` before this lease. That commit is the Room71 reconstruction supplement through Lease/partition 173, and current history showed no repository movement after it before this session began.

Current control evidence was re-read from `REP-001`, `REP-002`, `REP-013`, `REP-012`, `REP-011`, `REP-014`, `REP-015`, `REP-016`, Room71 current state, and the 170–173 reconstruction supplement.

Preserved holds include Core 136, provider authentication, external evidence at `RESOLVED_UNAUTHENTICATED`, Global Connected Baseline, IGT cognitive benefit, Architecture semantic/cross-layer certification, Engine connected/runtime/promotion gates, Services global certification, Interfaces runtime/provider-auth/external-trust claims, KNW-001..010 non-promotion, and no branch deletion authority.

## Gap proof

`REP-016` keeps Release as an open partition. `Repository/CONNECTED_BASELINE_RELEASE_PARTITION_ENUMERATION_2026-08-29.md` already closes exact physical enumeration and Foundation-scope classification, but explicitly leaves current-content usability/freshness review for `Release/INSTALLATION.md` and `Release/QUICK_START.md` open.

Direct current reads established:

- `Release/INSTALLATION.md` is `REL-003 / 1.0.0 / Approved` and explicitly describes repository/document preparation rather than executable deployment. Its initial-verification text uses root-style `VERSION.md` and `CHANGELOG.md` labels, while current repository paths are `Release/VERSION.md` and `Logs/CHANGELOG.md`.
- `Release/QUICK_START.md` is `REL-004 / 1.0.0 / Approved` and provides a Foundation-era first-user navigation flow. It does not include the later mandatory engineering/AI bootstrap gate.
- current `START_HERE.md`, `README.md` and `PROJECT_BOOTSTRAP.md` provide the current development/session onboarding path and explicitly require repository-first bootstrap before engineering mutation.
- `Release/VERSION.md` explicitly separates Official Release `1.0.0` from Development Baseline `3.2.1`.
- `Logs/CHANGELOG.md` likewise separates the latest official release from the current development baseline.

## Prior-learning / search reconciliation

Three materially different checks were used around the observed reference/freshness gap:

1. direct current-path reads of REL-003/REL-004 and current onboarding authorities;
2. repository search for Release freshness / REL-003 / REL-004 evidence;
3. direct-path verification of the current VERSION and CHANGELOG locations after search did not establish alternate active paths.

The negative search for a current `GOV-003_VERSIONING_POLICY` reference used by the old compatibility material was not converted into a destructive or architectural decision; the Release partition remains bounded by the stronger current `Release/VERSION.md` authority.

## Lease and collision gate

Semantic scope: determine the correct current disposition of REL-003/REL-004 without conflating Foundation Release 1.0.0 with development baseline 3.2.1.

Allowed mutation scope was limited to this transaction record, a new bounded evidence record if needed, and REL-003/REL-004 only if current authority proved in-place correction semantically legal. Core, Runtime, Engine, Services, Interfaces, Knowledge, canonical Governance, REP-001, REP-002, REP-014, Room71 current JSON and branch refs were forbidden.

Collision result:
- C1 file: PASS — unique transaction path; no Release target write.
- C2 semantic: PASS — Foundation-release semantics kept separate from current development onboarding.
- C3 baseline: PASS — official release 1.0.0 and development baseline 3.2.1 remain distinct.
- C4 authority: PASS — no release promotion/new-release authority asserted.
- C5 evidence: PASS — historical release statements retained as snapshot-scoped evidence.
- C6 handoff: PASS — no active Room71 lease was recorded at re-entry; latest supplement closed through 173.

## Disposition

The strongest supported result is:

`REL003_REL004_CURRENT_DEVELOPMENT_ONBOARDING = SUPERSEDED_FOR_CURRENT_SESSION_USE_BY_START_HERE_README_PROJECT_BOOTSTRAP`

while simultaneously:

`REL003_REL004_FOUNDATION_1_0_0_SCOPE = RETAINED / HISTORICAL_OFFICIAL_RELEASE_SUPPORTING_DOCUMENTATION`.

Therefore no in-place Release mutation is justified in this lease. Rewriting REL-003/REL-004 to describe current development main would risk erasing or conflating historical official-release semantics. The stale root-style reference labels are bounded usability debt inside Foundation-supporting documentation, not sufficient authority for silent semantic modernization.

## Verification

- prewrite persisted at `86c6969d863e24b45db9f0c7a20623a7cbe1b332` and was read back successfully;
- current main after prewrite was independently re-read and matched that checkpoint;
- `Logs/CHANGELOG.md` was directly verified at its current path;
- no protected Release artifact was mutated;
- no Runtime/Engine/Services/Interfaces/Knowledge or canonical authority surface was changed;
- no CI/runtime semantic promotion is claimed from this evidence-only closure.

## Bounded closure

`RELEASE_REL003_REL004_FRESHNESS_DISPOSITION_174 = CLOSED / EVIDENCE-VERIFIED / NO RELEASE MUTATION`.

Release partition remains OPEN because dependency/consumer validation, relationship authority and explicit whole-partition closure remain unresolved.

## Preserved non-claims / holds

- no new official release;
- no Release partition closure;
- no Connected Baseline closure;
- no provider-authentication proof;
- no external-evidence promotion beyond `RESOLVED_UNAUTHENTICATED`;
- no IGT cognitive-benefit claim;
- no Architecture/Engine/Services/Interfaces global certification;
- no KNW-001..010 promotion;
- no branch deletion.

## Resume-safe next legal action

Continue the Release partition only from fresh live-main evidence. The next bounded question is Release dependency/consumer and authority reconciliation: determine which REL-001..005/current VERSION surfaces are consumed by current repository artifacts, which references are historical-only, and whether that evidence justifies a Release relationship/status record or a whole-partition closure review. Do not update REP-001/REP-002 or REL-003/REL-004 unless a fresh gap and authority are independently proven.

## Learning

`HISTORICAL RELEASE DOCUMENT ≠ CURRENT DEVELOPMENT ONBOARDING CONTRACT`.

A stale-looking statement inside official-release supporting documentation is not automatically a mutation target. First align the semantic time/snapshot; preserve historical truth and route current use through current authority when that is the smaller, safer solution.
