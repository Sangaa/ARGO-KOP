# GOV-018 — EVOLUTION GUARD

Status: CANDIDATE / NON-CANONICAL
Purpose: protect ARGO KOP from architectural lock-in while preserving evidence and integrity discipline.

## Core rule

Governance constrains safety, evidence, authority, provenance and verification. It MUST NOT prescribe a permanent implementation shape unless higher authority explicitly requires that shape.

`PROTOCOL = SAFETY + EVIDENCE + VERIFICATION`

`ARCHITECTURE = HYPOTHESIS UNTIL PROVEN`

## Evolution rules

1. A checkpoint/GT may define the evidence required for a decision, but must not predetermine the implementation unless the implementation is itself an approved authority constraint.
2. A test seam must remain replaceable when its purpose is evidence acquisition rather than production architecture.
3. Do not create a new file, model, adapter, registry or service solely because the current naming sequence expects one.
4. Prefer extending or consolidating an existing artifact when semantic ownership remains coherent.
5. File count reduction is not itself a goal; optimize for information density, traceability, inspectability and operational value.
6. Blob/EDI-like representations remain candidates until comparative evidence proves their net advantage.
7. Every material architectural decision must retain an explicit reversal path or migration boundary unless reversal is impossible by nature.
8. Periodically challenge accumulated structure: identify duplication, stale assumptions, unnecessary seams and artifacts whose only purpose is historical sequencing.
9. Historical EJR/GT decisions remain evidence of what was learned, not permanent commands for what must be built next.
10. When a new experiment disproves an earlier design assumption, preserve the historical evidence and update the current decision state; do not contort new work to preserve obsolete architecture.

## Anti-freeze gate

Before a material new structural mutation, ask:

- Is this required by authority or merely inherited from prior design?
- Does an existing artifact already provide the required capability?
- What is the smallest reversible change?
- What alternative representation would remain possible after this change?
- Are we adding structure because evidence requires it, or because the sequence expects it?

If the answer indicates structural lock-in without demonstrated benefit, HOLD and reassess.

## Scope

This candidate does not authorize migration, deletion, promotion, runtime change or bypass of existing governance. It is a design-protection rule only.

## Promotion condition

Promote to canonical governance only after review against existing governance, matrices and actual repository practice demonstrates that the rule removes repeatable architectural lock-in without weakening evidence discipline.
