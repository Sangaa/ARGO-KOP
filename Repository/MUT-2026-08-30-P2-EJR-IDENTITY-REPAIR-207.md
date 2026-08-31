# R71-20260830-P2-EJR-IDENTITY-REPAIR-207

Status: CLOSED / SUCCESSOR-VERIFIED / ONE-RECORD REPAIR / RESUME-SAFE
Baseline: `main@c03b05ab21859adbe6e18518f60385e376cc798b`
Functional repair commit: `912447da46af44ab0b9805e8f3d2723a524745b4`
Target displaced record: `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
Replacement identity/path: `EJR-400` / `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md`
Verification successors: Lease208 → Lease209

## Authorization basis
- Lease204 classified the root EJR-214 as legitimate later reuse requiring separate controlled repair.
- Lease206 proved `EJR-400 = VACANT` with complete locally reachable history.
- Current consumer searches did not establish a synchronous operational consumer rewrite requirement; historical analytical/provenance mentions were preserved.

## Functional repair
Exactly one displaced legitimate record was re-identified:
- old root path removed;
- new EJR-400 path added;
- first H1 changed `EJR-214` → `EJR-400`;
- semantic body, chronology, status, scope, conclusions, and learning remained otherwise preserved.

Direct re-read of pre-repair baseline `c03b05ab...` and current EJR-400 confirms the bodies match apart from document-level H1 identity.

## Exact-head evidence and discovered observability gap
At repair head `912447da46af44ab0b9805e8f3d2723a524745b4`, four applicable workflows triggered and passed, including Full-Stack run `33329699580` and M2 run `33329699596`; Internal Document-ID Audit did not trigger because its push filter lacked `EJR/**`. That missing verification path became the bounded defect repaired by Lease208.

Lease208 then successfully made direct EJR mutations trigger Internal-ID. Its first audit exposed a separate post-repair cohort-baseline drift, which Lease209 resolved without scanner weakening.

## Final successor verification
On `2092e90aa43df83a9731e31011d41990284b1654`:
- Internal Document-ID Audit `33352779923` — SUCCESS;
- artifact `9744172134` shows neither EJR-214 nor EJR-400 in ambiguity records;
- `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md` exists with H1 `EJR-400`;
- old root EJR-214 path is absent;
- census `9744173384` is 35/35, complete, CENSUSED;
- Full-Stack, Runtime/Integration, M2, and Real Mutation Matrix all PASS.

## Closure decision
Lease207 is CLOSED through an explicit successor-verification chain. The repair-head lack of Internal-ID execution is preserved as historical fact; closure relies on the later corrected trigger and current-tree exact audit evidence, not on retroactively claiming a run that did not occur.

## Learning
`A VALID MATERIAL REPAIR MAY REVEAL A SEPARATE VERIFICATION-SURFACE DEFECT. FIX THAT SURFACE AS A SUCCESSOR; DO NOT CONFLATE THE TWO MUTATIONS OR ERASE THE ORIGINAL EVIDENCE GAP.`

## Boundaries
No additional EJR repair authorized here. Priority 2 remains OPEN. Phase 1 remains OPEN. Connected-Baseline/global graph remains OPEN. Global integrity remains HOLD.
