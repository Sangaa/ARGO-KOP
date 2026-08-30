# MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179

Date: 2026-08-30
Lease: `R71-20260830-P2-ID-AUDIT-COVERAGE-179`
Execution role: HERMUZ
Entry baseline: `main@d4a6dd1b475602d5674fca838dd185c5c25a6931`
Status: `PREWRITE / LEASE ACTIVE / TOOLING COVERAGE REPAIR`

## Gap proved

Priority 2 is defined as an exhaustive repository-wide duplicate-ID audit, but current `Quality/Integration/internal_document_id_audit.py` recognizes explicit `Document ID` values only when their prefix is present in a fixed namespace list.

Current list omits directly verified repository families including at least:
- `COG-*` (Cognition);
- `DEC-*` (Decision);
- `REL-*` (Release document IDs);
- root explicit identities such as `BOOTSTRAP-001` and `PROJECT_STATUS`.

Therefore a green result from the current implementation cannot support an exhaustive repository-wide internal Document-ID claim.

Classification:
`AUDIT COVERAGE DEFECT / FALSE-NEGATIVE RISK / PRIORITY-2 CANNOT CLOSE`.

## Prior learning applied

- Tool-limited evidence constrains claim scope.
- A successful audit is not proof beyond the exact scope the audit can observe.
- Identifier token equality does not imply collision across namespace/artifact class.
- Negative/clean findings require evidence that the detector actually covers the claimed population.

## Planned repair

Modify only:
- `Quality/Integration/internal_document_id_audit.py`;
- `Quality/Integration/test_internal_document_id_audit.py`.

Design:
1. Extract values from the explicit `Document ID` field using a generic controlled token pattern instead of a hardcoded namespace allowlist.
2. Preserve document-level heading collision logic as a narrower numeric-ID concern.
3. Preserve filename/internal-ID mismatch checking only where a filename explicitly carries a numeric-style ID prefix.
4. Emit a path→Document-ID coverage map so tests and evidence can prove which explicit identities were observed.
5. Add current-tree regression assertions for representative formerly invisible identities: `COG-009`, `DEC-009`, `REL-001`, `BOOTSTRAP-001`, `PROJECT_STATUS`.
6. Run the dedicated Internal Document-ID Audit plus Full-Stack/Runtime/M2 as applicable after the atomic code+test commit.

## Boundaries

- This repair expands observation; it does not auto-resolve duplicates it may expose.
- No canonical domain artifact, index, relationship registry or authority will be mutated in this lease.
- Priority 2 may close only if expanded audit evidence plus required identity decisions/control-plane reconciliation support it.

## C1–C6

- C1 PASS — unique lease record.
- C2 PASS — audit observability only.
- C3 PASS — no release/baseline mutation.
- C4 PASS — test/tool output cannot manufacture identity authority.
- C5 PASS — gap directly visible in current source code and verified repository identities.
- C6 PASS — follows current REP-016 Priority 2 global-scope open state.

Initial state:
`P2_ID_AUDIT_COVERAGE_179 = IN_PROGRESS`.
