# EJR-239 — P1 Mutation Matrix Preflight Gate

Date: 2026-08-17
Status: `CLOSED / CI-VERIFIED / REUSABLE-LEARNING`

## 1. Execution Identity
- Session / EJR: `EJR-239`
- Scope: P1 governance / mutation-safety control
- Starting HEAD: `1898e3b7e31fb599f42ae33af0efa5880480b2fd`
- Final verified HEAD: `14f1dc45deed5efec1ffa1baca0c45aa33376b1a`

## 2. Objective
Introduce a repository-controlled Mutation Matrix preflight that automatically checks whether high-risk canonical mutations are accompanied by a Mutation Matrix, while exempting documentation, tests, CI, templates, EJR/session records and Matrix files themselves.

## 3. Implemented Artifacts
- `Quality/Integration/check_mutation_matrix_preflight.py`
- `Quality/Integration/test_mutation_matrix_preflight.py`
- `.github/workflows/full-stack-audit.yml` — integrated preflight gate

## 4. Gate Semantics
Protected mutation scopes currently include:
- `Engine/`
- `Services/`
- `Runtime/`
- `Repository/REP-*`
- `Interfaces/`
- `Cognition/COG-*`
- `Decision/`
- `Memory/`

Exemptions include:
- `EJR/`
- `Quality/`
- `Templates/`
- `.github/`
- `Docs/`
- existing Mutation Matrix files

A protected change set without a Matrix fails the preflight.
A protected change set with a Matrix passes the preflight condition.

## 5. Verification
Regression coverage executed successfully for:
1. protected mutation without Matrix;
2. protected mutation with Matrix;
3. documentation-only change;
4. Matrix-only change.

Final Full-Stack CI evidence:
- Workflow: `333498182`
- Run: `32048615721`
- Job: `95442270593`
- P4 REL-009 consumer boundary gate: `SUCCESS`
- P4 negative runtime evidence gate: `SUCCESS`
- Mutation Matrix preflight regression: `SUCCESS`
- Mutation Matrix current-change enforcement: `SUCCESS`
- Repository-wide audit: `SUCCESS`
- Runtime evidence emission: `SUCCESS`
- Evidence uploads: `SUCCESS`

## 6. Failure and Recovery
The first integration run (`32048486524`) correctly failed at the new enforcement step, but the failure was in the CI environment rather than the Matrix rule: the workflow used `actions/checkout` with `fetch-depth: 1`, so the declared base SHA was not present locally for `git diff BASE...HEAD`.

The regression step itself passed before the failure boundary.

Recovery: changed the proven Full-Stack checkout to `fetch-depth: 0`, preserving the Matrix rule and re-running CI successfully.

## 7. Proven / Not Proven
### Proven
- The preflight logic is deterministic and model-independent.
- The current change-set enforcement runs successfully in the proven Full-Stack CI.
- The gate can distinguish protected mutations from exempt documentation/test/CI changes.

### Not Proven
- The preflight does not yet validate the semantic correctness of the Matrix contents; it verifies Matrix presence and change-set classification only.
- It does not replace the existing candidate/KEEP/unexpected-change validation performed by GOV-014 transaction controls.

## 8. Learning Extraction
Observation: enforcing Matrix presence is useful only when the CI runner can resolve both the base and head commits.

Root Cause: shallow checkout made repository history unavailable even though the GitHub event supplied a valid base SHA.

Lesson: a change-set safety gate must explicitly provision the evidence it consumes; CI configuration is part of the evidence boundary.

General Rule:
`Evidence-Consuming CI Gate => Provision Required Repository History First`

Additional rule:
`Matrix Presence Gate ≠ Matrix Semantic Validation`

Classification: `REUSABLE-LEARNING`

## 9. Knowledge Transfer
Transferred into:
- `Quality/Integration/check_mutation_matrix_preflight.py`
- `Quality/Integration/test_mutation_matrix_preflight.py`
- `.github/workflows/full-stack-audit.yml`
- this EJR record

The control is repository-native and model-independent.

## 10. Closure Gate
- [x] Execution evidence
- [x] Failure captured and root-caused
- [x] Recovery verified
- [x] Current-state / SHA control
- [x] CI verification
- [x] Learning extraction
- [x] Knowledge transfer
- [x] Boundary and limitations recorded
- [x] Next safe entry

## 11. Next Safe Entry
Future work may extend the preflight from Matrix presence to bounded Matrix semantic checks, but only with explicit Matrix/test evidence and without weakening the current presence gate.

---

End of EJR-239
