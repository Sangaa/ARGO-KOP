# REP-020 — SESSION DELTA 2026-08-16 — P213

## Objective
Resolve a verified cross-layer reference inconsistency between the Knowledge Lifecycle and the current Document Lifecycle authority.

## Discovery

`Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md` still referenced the retired path `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md`, while the active document-lifecycle authority is `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md` after the GOV-005 identity collision migration.

The retired target does not exist on current main.

## Mutation

Updated `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md` to reference:

`Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`

Added:

`Quality/Integrity/test_knowledge_lifecycle_reference.py`

The regression guard requires the current target to exist, the retired target to remain absent, and the stale reference to remain absent from KNW-004.

## Verification Boundary

The canonical Knowledge Lifecycle content was preserved apart from the verified path correction. No lifecycle authority was expanded and no cross-lifecycle equivalence was introduced.

## Status

`CROSS_LAYER_REFERENCE_REPAIRED / REGRESSION_GUARDED / REPOSITORY INTEGRITY OPEN`

Commits:
- `414443e36132d48e8659e67fa8aa0dc36bc324c3`
- `549a60a9444f79f43c035456d691b10e67ec73d7`

## Next Priority

Continue cross-layer reference resolution in Memory / Learning and AI / Knowledge consumers. Re-read every affected canonical artifact before any further mutation. Do not promote any revalidation-held domain based solely on path repair.
