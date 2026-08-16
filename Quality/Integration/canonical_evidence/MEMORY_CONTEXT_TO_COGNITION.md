# Canonical Evidence — Memory → Context → Cognition

Status: CERTIFICATION_BUILT / CONTROLLED_SYNTHETIC
Side effect: false

## Contract

`Cognition/CONTEXT_MEMORY_SELECTION_CONTRACT.md`

The contract restricts historical-memory selection to records directly scoped to the current task or project, preserves provenance, keeps selected records labeled `HISTORICAL_EVIDENCE`, and explicitly prevents truth, decision, or execution authority promotion.

## Runtime

`Cognition/context_memory_selector.py` performs the bounded task/project scope selection and labels selected records as historical evidence.

`Cognition/context_loader.py` creates the cognition input while preserving `current_facts`, historical evidence, provenance requirement, and the non-active historical-context boundary.

## Test

`Quality/Integration/test_memory_to_context_selection_boundary.py`

The integration test verifies in-scope selection, out-of-scope exclusion, historical provenance preservation, and that historical evidence is not promoted into current facts.

## Trace

`Quality/Integration/canonical_evidence/MEMORY_CONTEXT_TO_COGNITION_TRACE.json`

The controlled synthetic trace records `CONTEXT_READY`, `historical_is_active_context=false`, `provenance_required=true`, and `side_effect=false`.

## Boundary

This evidence certifies the Memory → Context → Cognition boundary only. It does not certify semantic relevance scoring, truth promotion, decision authority, or execution authority.
