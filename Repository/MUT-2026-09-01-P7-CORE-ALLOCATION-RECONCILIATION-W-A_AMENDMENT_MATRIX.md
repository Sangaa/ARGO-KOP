# AMENDMENT MATRIX — P7 CORE ALLOCATION RECONCILIATION W-A

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A`
State: `CLOSED / SUPERSEDED-BEFORE-MATERIAL-WRITE BY W-B / LEARNING RETAINED / RESUME-SAFE`

W-A correctly found that a direct canonical REP-012 version change would require REP-020 manifest synchronization and correctly required durable Core-allocation regression coverage.

W-B removed the REP-012 version-change condition before material mutation by selecting a non-replacing allocation addendum. Therefore REP-020 synchronization became inapplicable, while the focused regression requirement was retained and verified.

No W-A direct REP-012/REP-020 material mutation occurred.

Candidate `b1ded1d55ee5ab2f707d0e24cb5b03a5d1bd28e3` passed all four required workflows: Real Matrix `33539482726`, Full-Stack `33539482751`, M2 `33539482763`, Runtime `33539482791`.

`A CONDITIONAL CONTROL REQUIREMENT REMAINS VALID EVEN WHEN A LATER PRE-WRITE DECISION REMOVES THE CONDITION THAT WOULD HAVE ACTIVATED IT.`
