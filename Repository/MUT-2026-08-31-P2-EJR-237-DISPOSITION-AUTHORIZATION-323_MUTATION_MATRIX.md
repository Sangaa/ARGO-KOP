# MUT-2026-08-31-P2-EJR-237-DISPOSITION-AUTHORIZATION-323 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-237-DISPOSITION-AUTHORIZATION-323
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 323-01 | `Repository/MUT-2026-08-31-P2-EJR-237-DISPOSITION-AUTHORIZATION-323.md` | CREATE | evidence-only disposition for EJR-237 | Y | Y |
| 323-02 | current EJR-237 member files | KEEP | no rename/delete/reassignment/allocation | Y | Y |
| 323-03 | MEMORY_TO_ROOT baseline | KEEP | remain 6 during disposition | Y | Y |

## KEEP REQUIREMENT
Both EJR-237 members were preserved byte-for-byte during disposition. No successor was allocated, no current evidence consumer was rewritten, baseline remained 6, and 317/318 and Priority ordering were unchanged.

## Execution Evidence
Current deterministic cohort is 6/6 CENSUSED after Lease322: EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296. EJR-237 has exactly two distinct members and zero exact-member-path consumers in the current census.

Direct Git history proves:
- Memory member first allocation `51057be94fe4981258c0a02cbc1461a1e43e72d8` at 2026-08-15T05:15:05Z;
- root member first allocation `93248a0f5feb2abb5b84db3dfd9c19ba1e8e5b6d` at 2026-08-17T16:46:35Z.

Current semantic evidence surfaces `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` and `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md` refer specifically to the later root EJR-237 negative-runtime evidence and are preserved as future consumer rewrite obligations.

No evidence reviewed invalidates the earlier Memory allocation. Lease323 therefore explicitly retains Memory EJR-237 and classifies the later root EJR-237 as the displacement candidate.

## Closure
Disposition is CLOSED / VERIFIED / RESUME-SAFE. Next legal action is candidate discovery plus a separate complete-history vacancy proof before identity mutation.
