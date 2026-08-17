# EJR-220

---

# MUTATION INTEGRITY AUDIT AND PREVENTION

Date: 2026-08-17
Status: Validated Operational Correction

## Result

A repository-wide focused audit of recent high-risk mutations found:

- REP-001 transaction 001: Matrix evidence present and closed.
- REP-001 transaction 002: Matrix and Section Matrix exist; transaction remains explicitly pre-write until candidate/write closure is evidenced.
- REP-002 synchronization: dedicated mutation-matrix evidence exists.
- REP-014 REL-003: actual mutation existed without a dedicated pre-write Matrix artifact. This is recorded as `MATRIX-GAP` and repaired by a clearly labeled retroactive Matrix record.
- REP-016: no canonical replacement mutation was established by this audit; the previously created delta is not treated as a canonical file rewrite.

## Root Cause

The recurring failure mode is the combination of:

1. full-file replacement semantics for small localized changes;
2. model/session state being mistaken for repository current state;
3. transaction evidence being recorded without enforcing a Matrix artifact as a pre-write gate.

## Corrective Actions

1. Added `Repository/MUT-2026-08-17-REP014-REL003-001_MUTATION_MATRIX.md` as a retroactive traceability repair.
2. Added `Repository/MUTATION_MATRIX_AUDIT_2026-08-17.md` as the cross-transaction audit record.
3. Upgraded GOV-014 from v1.0.0 to v1.0.1 so a controlled mutation is not Matrix-compliant unless the Matrix artifact exists before the repository write and is linked to the transaction.
4. Explicitly distinguished retroactive traceability repair from proof of original pre-write compliance.

## Future-Model Rule

A model MUST resolve:

`HEAD → target file → current blob SHA → Section Matrix → Mutation Matrix → candidate → pre-commit validation → write → HEAD read-back → Matrix reconciliation`

before claiming a high-risk mutation complete.

The latest EJR is context only; it is never a substitute for current repository state.

## Large-File Preservation Rule

For a large authoritative document, the candidate MUST be reconstructed from the complete source document. A delta or summary is not sufficient to perform a full replacement.

Every untouched unit is an explicit `KEEP` requirement. Unexpected changes abort the write.

## Closure

Mutation safety is now a repository-level control rather than a model-memory expectation.

`MATRIX-GAP` found in REL-003 is preserved as historical evidence and is not relabeled as pre-write compliant.

---

End of EJR-220
