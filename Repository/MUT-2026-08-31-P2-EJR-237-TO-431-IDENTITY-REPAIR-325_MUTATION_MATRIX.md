# MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 325-01 | `EJR/EJR-431_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | CREATE | displaced root content with first-H1 identity EJR-431; semantic body/date/chronology preserved | N | N |
| 325-02 | `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | DELETE | old root identity absent in same atomic tree | N | N |
| 325-03 | `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` | UPDATE | move semantic evidence references whose referent is root EJR-237 negative-runtime evidence to EJR-431 only | N | N |
| 325-04 | `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md` | UPDATE | move root-negative-runtime evidence heading/reference EJR-237 → EJR-431 only | N | N |
| 325-05 | `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md` | KEEP | retained earlier allocation byte-for-byte | Y | N |
| 325-06 | census expected baseline | KEEP | remain 6 during repair; expected drift failure must be preserved for separate rebaseline | Y | Y |

## KEEP REQUIREMENT
Preserve the displaced root record semantic body, original event date, execution evidence, chronology and historical internal session metadata; change only path/first-H1 identity required for current identity. Preserve Memory EJR-237 byte-for-byte. Rewrite only live semantic consumers whose referent is the displaced root negative-runtime evidence. Do not rewrite historical P2 census/baseline records, change `EXPECTED_GROUP_COUNT = 6`, reopen 317/318, perform new Runtime work, or promote Priority 2.

## Execution Evidence
Lease323 retained Memory EJR-237 and dispositioned the later root EJR-237. Lease324 workflow run `33426371329` at `7db1eaa45d0a86b64a19cc1b9f693d0eb02b1808` proved EJR-431 VACANT with complete locally reachable history; artifact `9770873918`, digest `sha256:2316b9f56376531d5248ea676326cc5d2bd374db5206d1427c7677421b8f3d12`.

Current root consumer review identified two live semantic evidence surfaces:
- EJR-418 P322 reconciliation update transfers `EJR-237 negative runtime evidence` into P322;
- REP-020 P322 contains the `EJR-237 Negative Runtime Evidence — Current Connected Spine` section and states the seam was revalidated through `EJR-237`.
These refer to the later root negative-runtime record and must follow its identity. Current deterministic census records zero exact-member-path consumers; historical analytical references remain historical and are not rewrite obligations.

## Closure
After one atomic functional tree require: successor present, old root path absent, Memory blob unchanged, both live semantic consumer surfaces self-consistent, exact diff bounded to these four functional paths, Full-Stack success, and Internal-ID inspected. If Internal-ID fails only because MEMORY_TO_ROOT expected=6/observed=5 with `__COHORT_COUNT_DRIFT__`, preserve that failure and perform rebaseline only in a separate lease. Any other failure blocks continuation.
