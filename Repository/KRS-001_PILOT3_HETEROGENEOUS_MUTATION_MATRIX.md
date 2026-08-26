# KRS-001 Pilot 3 — Heterogeneous Artifact Mutation Matrix

Transaction: `MUT-2026-08-26-KRS001-PILOT3-HETERO-001`
Status: `PRE-WRITE / OPEN`
Authority: `GOV-013 + GOV-014`
Base SHA: `6fa37433a195f9820d5242cfe923956533d76f85`

## Objective
Test KRS-KO/0.2 against one heterogeneous artifact that is not a canonical interface, without replacing the source artifact or authorizing bulk migration.

## Selected Artifact
`Repository/KRS-001_PILOT_MUTATION_MATRIX.md`

Reason: this control artifact contains policy/authority assertions, temporal/currentness claims, evidence classifications, historical closure state, and integrity constraints. It therefore tests the schema outside the interface-specific boundary already exercised by INTF-006.

## Prior-Learning Gate
- GOV-013 Mandatory Prior-Learning Retrieval: applied before mutation.
- Pilot 1 learning: relationship paths alone are insufficient; relationship semantics/evidence class must be explicit. `DIRECTLY APPLICABLE`.
- Pilot 2 learning: exact mutation-SHA correlation is required before execution closure; successful historical runs cannot close a new mutation. `DIRECTLY APPLICABLE`.
- KRS-001 v0.2 gate: second pilot must be heterogeneous and must test policy assertions, temporal validity, and control authority. `DIRECTLY APPLICABLE`.
- Pilot 3 runtime/provenance matrix: structural relationships must remain distinct from runtime evidence; absent runtime evidence must not be inferred. `TRANSFERABLE`.

## Required Verification
1. Fetch the current selected artifact at HEAD and establish exact blob identity.
2. Identify source authority, currentness, temporal validity, provenance, and historical evidence.
3. Identify each material relationship and classify its semantics/evidence class.
4. Compare the artifact against KRS-KO/0.2 required fields without forcing interface-specific fields.
5. Identify the smallest verified schema gap, if any.
6. If a gap is verified, mutate only the supplemental pilot object required for this heterogeneous test.
7. Re-read every changed artifact and validate source authority remains unchanged.
8. Validate applicable relationships/index state and applicable CI/integration evidence.
9. Close only with exact mutation SHA and reconciled evidence; otherwise record the precise hold.

## Non-Goals
- No source replacement.
- No bulk migration.
- No schema promotion to v0.3 solely from this pilot.
- No runtime-verification claim unless exact execution evidence exists.
- No relationship promotion based on path presence alone.

## Closure Requirement
This matrix remains `OPEN` until the selected artifact has passed the currentness/relationship review and the next mutation or explicit no-mutation decision is recorded with exact SHA and evidence.
