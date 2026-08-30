# MUT-2026-08-30-P2-EJR-REPLACEMENT-VACANCY-PROOF-206 — MUTATION MATRIX

Status: CLOSED / VERIFIED / EVIDENCE COMPLETE
Lease: R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206
Functional head: `2f3e139c2f9e096c058ae317db878efaa825e01f`

## Functional scope executed
- `.github/workflows/ejr-replacement-vacancy-proof-206.yml`
- this matrix

## Evidence
- Full history checkout and non-shallow assertion passed.
- Existing Lease-193 gate ran unchanged for `EJR-400`.
- Decision: `VACANT`.
- Artifact ID: `9737186617`.
- Artifact digest: `sha256:89bac3857098024d48256135d112292f13cad0866368c57a8ea2df3e3db8cfc1`.
- Current claims: none.
- Historical claims: none.
- History complete: true.
- History scope: all locally reachable refs.

## Exact-head checks
- Vacancy Proof `33329388744` — SUCCESS.
- Full-Stack `33329388713` — SUCCESS.
- Runtime `33329388749` — SUCCESS.
- M2 `33329388725` — SUCCESS.
- Real Mutation Matrix `33329388724` — SUCCESS.

## Packaging defect
A lease-only prewrite commit landed through the contents API before the Matrix. No functional mutation existed at that point. The governed pair was restored at `92a0d4fa3da630b9762e5d3685819775309ca309` before functional execution.

Rule retained:
`PREPARED ATOMIC TREE MUST BE ATTACHED WITH UPDATE_REF; CONTENTS-API FILE WRITE IS NOT A SUBSTITUTE FOR ATOMIC PREWRITE ATTACHMENT.`

## Preserved
No EJR identity/content/path mutation occurred. No REP-012/016/020 mutation. No authority promotion. Priority 2 / Phase 1 / Connected Baseline remain open.
