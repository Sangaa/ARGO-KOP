# P315 — Governance Preflight Repair

Status: `CLOSED / ISOLATED / GOVERNANCE-REPAIRED`

P314 CI failed its repository-audit mutation gate because the protected `connected_spine_runner.py` change was accompanied by a matrix whose filename was not discoverable by the preflight convention. The matrix content was present, but discovery returned zero matrices.

Repair: created `Repository/MUT-2026-08-27-P315-SPINE-CONSUMER_BINDING_MUTATION_MATRIX.md` using the repository's discoverable `_MUTATION_MATRIX.md` naming convention and removed the duplicate non-discoverable matrix.

No runtime behavior, registry, authority, or mainline state was changed by this repair.

The prior CI failure is retained as evidence; no PASS is claimed until a new PR workflow evaluates the corrected change set.

`P315 = CLOSED`
`PREFLIGHT = REPAIR APPLIED / AWAITING CI`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
`SESSION = CLOSED`
