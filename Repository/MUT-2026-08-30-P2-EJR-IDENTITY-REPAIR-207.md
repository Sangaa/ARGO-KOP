# R71-20260830-P2-EJR-IDENTITY-REPAIR-207

Status: PREWRITE / ONE-RECORD REPAIR
Baseline: `main@c03b05ab21859adbe6e18518f60385e376cc798b`
Target displaced record: `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
Replacement identity: `EJR-400`
Replacement path: `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md`

## Authorization basis
- Lease204 classifies the root EJR-214 record as a legitimate later reuse requiring separate controlled repair.
- Lease206 proves `EJR-400 = VACANT` with complete locally reachable history, artifact ID `9737186617`.
- Current exact-path, semantic-ID, and control-plane-targeted searches establish no current operational consumer requiring synchronous rewrite. Current hits are analytical/reconstruction/provenance records describing the pre-repair state and are preserved as historical evidence.

## Repair objective
Repair exactly one displaced legitimate EJR identity without changing its semantic lesson, chronology, status, scope, or engineering conclusions.

## Authorized functional changes
1. Remove current path `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`.
2. Add `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md` with byte-equivalent semantic body except the document-level first H1 identity changes from `EJR-214` to `EJR-400`.
3. Finalize the mutation matrix in the same functional commit.

## Forbidden
- no mutation of the retained earlier EJR-214 owner;
- no additional EJR repairs;
- no edits to historical Room/Lease/census records solely to rewrite history;
- no REP-011/012/013/014/016/020 mutation without direct current-consumer evidence;
- no suppression or scanner weakening;
- no Priority2 / Phase1 / Connected Baseline closure.

## Required verification
- exact diff limited to old path removal, new path addition, and Matrix;
- Internal Document-ID Audit exact-head SUCCESS;
- inspect current ambiguity evidence to prove the old EJR-214 duplicate member is removed and EJR-400 is unique;
- applicable Full-Stack, Runtime, M2, Real Matrix checks PASS;
- read back new path and prove semantic preservation except identity H1;
- old path absent on current head;
- closure checkpoint remains resume-safe.
