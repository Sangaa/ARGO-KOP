# MUTATION MATRIX — P2 EJR AMBIGUITY OBSERVABILITY 191

Transaction ID: `MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
State: `PREWRITE / NOT YET APPLIED`
Entry head: `17d9b2273307c476c886ce630a2dfd46e1d4d937`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 191-001 | `Quality/Integration/internal_document_id_audit.py` | UPDATE | add structured `ambiguous_duplicate_records` companion output from existing ArtifactRecord facts; preserve all existing ambiguity/pass-fail semantics | N | N |
| 191-002 | `Quality/Integration/test_internal_document_id_audit.py` | UPDATE | regress mixed explicit/H1 ambiguity observability while proving legacy ambiguity output and identity hold are unchanged | N | N |
| 191-003 | this Matrix | UPDATE IN SAME FUNCTIONAL CHANGE SET | bind exact functional commit and verification evidence | N | N |

## KEEP requirement

All scanner logic not explicitly required for the new companion field is KEEP. In particular:

- `ambiguous_duplicate_ids` construction and membership;
- `identity_scope_reconciled` expression;
- active canonical duplicate logic;
- filename alignment;
- metadata preamble/Document ID parsing;
- Governance heading collision behavior;
- deferred-domain and legacy classification behavior.

Unexpected semantic or path change = HARD HOLD.

## Expected functional changed-file set

Exactly:

1. `Quality/Integration/internal_document_id_audit.py`
2. `Quality/Integration/test_internal_document_id_audit.py`
3. `Repository/MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191_MUTATION_MATRIX.md`

Lease record already exists as prewrite evidence and is not required in the functional change set.

## Required verification

- final live-parent recheck;
- force=false fast-forward;
- exact changed-set compare / unexpected paths = 0;
- read-back code/test/Matrix;
- Internal Document-ID Audit SUCCESS;
- Full-Stack Repository Audit SUCCESS;
- Runtime/Integration and M2 SUCCESS where triggered;
- structured current-head artifact must reveal ambiguity member identity-source details without reducing raw ambiguity by policy;
- Priority 2 global remains OPEN.
