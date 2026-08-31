# R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212

Status: PREWRITE / ONE-RECORD REPAIR
Baseline: `main@88c1e90a6c6ddad5bd021c8a6a1fb1ac58b9e05b`
Target displaced record: `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`
Replacement identity: `EJR-401`
Replacement path: `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`

## Authorization basis
- Lease203 proves root EJR-211 is a distinct legitimate later identity reuse while Memory EJR-211 is the governed earlier referent.
- Lease204 establishes first-valid-allocation retention and classifies the later root record as displaced legitimate content requiring collision-safe replacement.
- Lease211 proves EJR-401 VACANT with complete locally reachable history, artifact `9744595264`.
- Repeated exact-path/name searches establish no current operational consumer requiring synchronous rewrite; current positive hits are historical Lease203/204 evidence.

## Repair objective
Repair exactly one displaced legitimate EJR identity without changing its semantic lesson, chronology, status, scope, relationship conclusions, or engineering evidence.

## Authorized functional changes
1. Remove current path `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`.
2. Add `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` with the same body except document-level first H1 identity changes from `EJR-211` to `EJR-401`.
3. Finalize this lease's Mutation Matrix in the same atomic functional commit.

## Verification-surface rule
Do not pre-normalize `ejr_memory_to_root_provenance_census.py`. The current fail-on-drift guard must observe the post-repair cohort honestly. If the repair removes one MEMORY_TO_ROOT_EJR ambiguity group and the established baseline therefore drifts, record that failure and handle any justified baseline recalibration only in a bounded successor.

## Forbidden
- no mutation of retained Memory EJR-211;
- no additional EJR repairs;
- no edits to historical Lease203/204/211 records to rewrite history;
- no consumer rewrite without direct current operational evidence;
- no analyzer/scanner suppression or baseline change in this lease;
- no REP-012/014/016/020 mutation;
- no Priority2/Phase1/Connected-Baseline/global closure.

## Required verification
- exact functional diff limited to old path removal, new path addition, Matrix;
- read back new path and prove semantic preservation except H1 identity;
- old path absent;
- Internal Document-ID Audit must trigger automatically because EJR/** is covered;
- inspect deterministic ambiguity and provenance evidence;
- applicable Full-Stack / Runtime / M2 / Real Matrix checks PASS;
- if Internal-ID fails only on proven cohort count drift, open a separate successor rather than weakening the guard.
