# REP-001 MUTATION MATRIX

Transaction ID: `MUT-2026-08-17-REP001-001`
Source Blob SHA: `067adc90433e5435df220b46882e8c1888fffd2d`
Section Matrix: `MUT-2026-08-17-REP001-001_SECTION_MATRIX.md`

## Intended Changes

| Change ID | Section ID | Target | Action | Expected Content | Authority Evidence | Applied | Verified |
|---|---|---|---|---|---|:---:|:---:|
| REP001-CHG-001 | REP001-SEC-04 | Repository Layer | UPDATE | Add `Repository/REP-004_REPOSITORY_NAVIGATION.md` | `Repository/_FOLDER_STATUS.md` approved/reviewed inventory | Y | Y |
| REP001-CHG-002 | REP001-SEC-04 | Repository Layer | UPDATE | Add `Repository/REP-005_REPOSITORY_COMPONENTS.md` | `Repository/_FOLDER_STATUS.md` approved/reviewed inventory | Y | Y |
| REP001-CHG-003 | REP001-SEC-04 | Repository Layer | UPDATE | Add `Repository/REP-007_REPOSITORY_GOVERNANCE.md` | `Repository/_FOLDER_STATUS.md` approved/reviewed inventory | Y | Y |
| REP001-CHG-004 | REP001-SEC-04 | Repository Layer | UPDATE | Add `Repository/REP-008_REPOSITORY_BASELINE.md` | `Repository/_FOLDER_STATUS.md` approved/reviewed inventory | Y | Y |
| REP001-CHG-005 | REP001-SEC-16 | Intelligence Domain | UPDATE | Explicitly index `Intelligence/INT-001_INTELLIGENCE_LAYER.md` | `Intelligence/_FOLDER_STATUS.md` Status COMPLETED / Canonical Yes / Approved | Y | Y |
| REP001-CHG-006 | REP001-SEC-16 | Intelligence Domain | UPDATE | Explicitly index `Intelligence/INT-002_PATTERN_EXTRACTION.md` | `Intelligence/_FOLDER_STATUS.md` Status COMPLETED / Canonical Yes / Approved | Y | Y |
| REP001-CHG-007 | REP001-SEC-16 | Intelligence Domain | UPDATE | Explicitly index `Intelligence/INT-003_ANOMALY_DETECTOR.md` | `Intelligence/_FOLDER_STATUS.md` Status COMPLETED / Canonical Yes / Approved | Y | Y |

## Preservation Matrix

All other Section Matrix rows are explicit `KEEP` requirements.

For every KEEP row:

`Original Section Content == Candidate Section Content`

The comparison MUST be content-equivalent/byte-equivalent as applicable to the construction representation.

## Required Pre-Commit Conditions

- `SECTION_COUNT_UNCHANGED = Y`
- `SECTION_ORDER_UNCHANGED = Y` unless explicitly specified
- `KEEP_MISMATCHES = 0`
- `UNEXPECTED_ADDITIONS = 0`
- `UNEXPECTED_DELETIONS = 0`
- `IDENTITY_PATH_MISMATCHES = 0`
- `AUTHORITY_EVIDENCE_GAPS = 0`
- `EXPECTED_CHANGES_PRESENT = 7`
- `APPLIED = Y` for all 7 after candidate construction
- `VERIFIED = Y` for all 7 after post-commit read-back

## Post-Commit Reconciliation

- Controlled mutation workflow: `32012425470` — SUCCESS.
- Mutation-triggering commit: `4853af786a965b9dfbfddb52716989f6c314796a`.
- Current `main`: `713fb73b203f5d1c9e30005123f5fd140a21640e`.
- Candidate SHA-256 emitted during pre-commit validation: `05119f986bc693347bb1bbc9fa4d16db8566947bcc2cbeed554dded3c9726d2b`.
- Current REP-001 read-back confirms all seven required additions.
- Request file is removed from current main after the controlled commit.

## Boundary

This matrix authorizes only the seven listed inventory additions. It does not authorize:

- Core promotion beyond P356;
- Knowledge promotion;
- Runtime changes;
- relationship graph changes;
- semantic authority changes;
- P2 closure by declaration.

---

End of Mutation Matrix
