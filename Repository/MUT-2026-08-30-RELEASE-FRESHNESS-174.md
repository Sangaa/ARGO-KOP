# MUT-2026-08-30-RELEASE-FRESHNESS-174

Date: 2026-08-30
Lease: `R71-20260830-RELEASE-FRESHNESS-174`
Execution role: HERMUZ
Baseline: `main@98c23b2489fab5684a3cbdd791402dbcbe2d5423`
Protocol: `PROJECT_BOOTSTRAP + CORE-003 + GOV-013 + GOV-013A + GOV-014 + GOV-021 + GOV-027`
Status: `PREWRITE / LEASE ACTIVE / MUTATION NOT YET AUTHORIZED`

## Re-entry proof

Live `main` was rediscovered at `98c23b2489fab5684a3cbdd791402dbcbe2d5423`; the latest commit is the Room71 reconstruction supplement through Lease/partition 173. No repository movement after that supplement was observed in current main history.

Current control evidence was re-read from `REP-001`, `REP-002`, `REP-013`, `REP-012`, `REP-011`, `REP-014`, `REP-015`, `REP-016`, Room71 current state, and the 170–173 reconstruction supplement.

Preserved holds include Core 136, provider authentication, external evidence at `RESOLVED_UNAUTHENTICATED`, Global Connected Baseline, IGT cognitive benefit, Architecture semantic/cross-layer certification, Engine connected/runtime/promotion gates, Services global certification, Interfaces runtime/provider-auth/external-trust claims, KNW-001..010 non-promotion, and no branch deletion authority.

## Gap proof

`REP-016` keeps Release as an open partition. `Repository/CONNECTED_BASELINE_RELEASE_PARTITION_ENUMERATION_2026-08-29.md` already closes exact physical enumeration and Foundation-scope classification, but explicitly leaves current-content usability/freshness review for `Release/INSTALLATION.md` and `Release/QUICK_START.md` open.

Direct current reads establish a bounded freshness gap:

- `Release/INSTALLATION.md` is `REL-003 / 1.0.0 / Approved` and says installation is repository/document preparation rather than executable software deployment. It also instructs initial verification of root `VERSION.md` and `CHANGELOG.md`, while current repository authority locates these as `Release/VERSION.md` and `Logs/CHANGELOG.md`.
- `Release/QUICK_START.md` is `REL-004 / 1.0.0 / Approved` and presents a generic repository-reading workflow. It does not direct a current engineering/AI session through mandatory `PROJECT_BOOTSTRAP.md` before work, despite current Bootstrap/README making that gate mandatory.
- `Release/VERSION.md` explicitly separates Official Release `1.0.0` from Development Baseline `3.2.1`; therefore Foundation-release historical truth must not be overwritten merely to describe current development main.

This is a usability/freshness review gap, not evidence that REL-003/004 should be silently rewritten as development-baseline documents.

## Work Lease

Semantic scope: determine the correct current disposition of REL-003/REL-004 without conflating Foundation Release 1.0.0 with development baseline 3.2.1.

Allowed write paths for this lease:
- `Repository/MUT-2026-08-30-RELEASE-FRESHNESS-174.md`
- a new Release evidence/disposition record under `Repository/` if justified by the review
- `Release/INSTALLATION.md` and/or `Release/QUICK_START.md` only if current authority proves an in-place correction is semantically legal and does not rewrite historical release truth

Forbidden paths:
- `Core/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- canonical Governance
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Repository/ROOM071_CURRENT_STATE.json`
- branch deletion or branch ref mutation

Required checks before any protected mutation:
- re-read live HEAD and every intended target;
- preserve Foundation Release 1.0.0 scope;
- verify current paths/consumers for VERSION/CHANGELOG/Bootstrap references;
- same-change-set Mutation Matrix if a protected Release file is mutated;
- read-back;
- smallest sufficient relevant checks, then Full-Stack / Runtime-Integration / M2 when the protected mutation gate requires them.

Handoff destination: resume-safe Release partition evidence plus next legal action; no global promotion.

## Collision gate C1–C6

- C1 file collision: PASS for this prewrite; new unique transaction path, no target Release mutation yet.
- C2 semantic collision: PASS WITH BOUNDARY; Foundation release semantics and current development onboarding semantics are explicitly separated.
- C3 baseline collision: PASS; authoritative development baseline remains 3.2.1 and official release remains 1.0.0.
- C4 authority collision: PASS FOR REVIEW ONLY; this lease grants no release promotion or new official release authority.
- C5 evidence collision: PASS; historical Release claims remain evidence for 1.0.0 and are not converted into present development claims.
- C6 handoff collision: PASS; no active Room71 lease is recorded on current control state, and the latest supplement closes through 173.

## Current decision

`RELEASE_FRESHNESS_174 = LEASED / REVIEW IN PROGRESS`.

No Release-file mutation is authorized merely from the observed drift. The next step is to classify whether the correct solution is historical-scope retention plus a current onboarding pointer/evidence record, or a bounded in-place correction that preserves 1.0.0 semantics.

## Non-claims

- no new release;
- no Release partition closure;
- no Connected Baseline closure;
- no authority promotion;
- no capability expansion;
- no branch deletion.
