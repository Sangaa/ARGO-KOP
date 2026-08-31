# Mutation Matrix — Lease 306 — EJR-247 → EJR-426 Identity Repair

Status: OPEN / PRE-MUTATION
Date: 2026-08-31

| Surface | Mutation | Protected impact | Reversible |
|---|---|---:|---:|
| `EJR/EJR-247_2026-08-17_MULTI_CHANNEL_TRAINING_COMPLETION.md` | delete displaced root allocation | journal identity | yes via parent |
| `EJR/EJR-426_2026-08-17_MULTI_CHANNEL_TRAINING_COMPLETION.md` | create successor identity | journal identity | yes via parent |
| `Memory/Engineering_Journal/EJR-247_2026-08-15_P66_SESSION_CLOSURE.md` | preserve unchanged | none | n/a |

## Guardrails

- Successor vacancy proof is already complete and artifact-inspected under Lease305.
- Atomic Git tree/commit/ref mutation required; no intermediate duplicate state.
- Body preservation required; only first H1 identity changes in successor root.
- Historical narrative references remain untouched.
- No Runtime/Core/Governance semantic mutation.

## Rollback

Return `main` to the repair parent if atomic post-state or audits reveal a non-baseline defect.
