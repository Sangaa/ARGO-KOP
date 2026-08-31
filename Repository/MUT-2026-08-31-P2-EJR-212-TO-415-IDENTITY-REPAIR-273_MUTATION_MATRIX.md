# MUTATION MATRIX — EJR-212 → EJR-415 IDENTITY REPAIR 273

Status: CLOSED / EXECUTION-VERIFIED
Transaction ID: MUT-2026-08-31-P2-EJR-212-TO-415-IDENTITY-REPAIR-273
Opening main: `a23c7cf7702125978a7991b8db5dbe642e12e311`
Prewrite head: `a7c3128fddf77e14d69dcc36aa7312e80e4ae033`
Execution lease: `bf2c22b2c7721939ca1202f35da907b5d11b8357`
Functional repair completed at: `24cb04ef430316c2fb9b9f6ab6af7eaf82bbe5df`
Successor baseline lease: 274
Execution role: HERMUZ

## Verified authority

Lease272 proved:
- earlier Memory EJR-212 = RETAINED;
- later root EJR-212 = DISPLACED legitimate content;
- EJR-415 = VACANT across complete reachable history and reserved for this repair.

## Verified repair

Final repair state:
- retained Memory EJR-212 blob remained `e0c49458311fc277eb1022ed29b2511882f468ff`;
- old root EJR-212 path absent;
- new root EJR-415 path present;
- only H1 identity changed in the root record; remaining body/date/status/relationship evidence preserved;
- no consumer rewrites.

The connector realized the authorized rename as target-create followed by old-path-delete; final compare from execution lease to repair completion classified the net EJR change as a rename (+1/-1). No rule promotion is made from this execution detail.

## Repair-head and successor verification

Repair head:
- Full-Stack #2405 / `33381941006`: SUCCESS;
- Internal-ID #64 / `33381940680`: clean except deterministic baseline drift;
- artifact `9754096972`, digest `sha256:f6d40232ae5ee20b428e95b3fc5706ceca638c928afb03718510bbf68cffda1b`: expected=22, observed=21, history_complete=true, sole incomplete `__COHORT_COUNT_DRIFT__`.

Lease274 normalized only baseline 22→21.

Normalized head:
- Internal-ID #65 / `33382121341`: SUCCESS;
- Full-Stack #2408 / `33382121314`: SUCCESS;
- artifact `9754166006`, digest `sha256:3b654b02d9d087c2e8b63ae22e34492014d5b3b42345d618384a2f4f95286c1c`;
- expected=21, observed=21, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

## Boundary

No retained Memory mutation, consumer rewrite, classifier semantic change, GOV/REP mutation, unrelated EJR change, or Global Integrity promotion occurred.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
