# MUTATION MATRIX — P2 EJR AMBIGUITY OBSERVABILITY 191

Transaction ID: `MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
State: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Entry head: `17d9b2273307c476c886ce630a2dfd46e1d4d937`
Prewrite head / functional parent: `774d9b83c9d6b6ccc3ada51fde3ff4193d702acc`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 191-001 | `Quality/Integration/internal_document_id_audit.py` | UPDATE | add structured `ambiguous_duplicate_records` companion output from existing ArtifactRecord facts; preserve all existing ambiguity/pass-fail semantics | Y | N |
| 191-002 | `Quality/Integration/test_internal_document_id_audit.py` | UPDATE | regress mixed explicit/H1 ambiguity observability while proving legacy ambiguity output and identity hold are unchanged | Y | N |
| 191-003 | this Matrix | UPDATE IN SAME FUNCTIONAL CHANGE SET | bind exact functional commit and verification evidence | Y | N |

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

## Exact source/candidate identities

- scanner source blob: `482dac833210131c609c0d896fc9e8e4a78c8718`.
- scanner candidate blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`.
- test source blob: `bb770b98caf215add1be4ecd51bb2ae5d23dcf9d`.
- test candidate blob: `25b22f7d5794d8720ad31496e5bf9985d623df12`.

The scanner source was reconstructed byte-for-byte and independently verified by reproducing the exact Git blob SHA before candidate transformation.

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
- candidate diff must show only the companion-field construction/return and one bounded regression test;
- read-back code/test/Matrix;
- Internal Document-ID Audit SUCCESS;
- Full-Stack Repository Audit SUCCESS;
- Runtime/Integration and M2 SUCCESS where triggered;
- structured current-head artifact must expose ambiguity member identity-source details without reducing raw ambiguity by policy;
- Priority 2 global remains OPEN.

## Construction-tool incident

A local git-clone attempt failed because the execution runtime could not resolve `github.com`. No repository mutation depended on that copy. Construction continued from exact GitHub blob content only.

A first manually reconstructed candidate was rejected before Git object creation because it did not preserve source comments/docstrings. This was a pre-commit candidate rejection, not a repository defect or mutation.

Learning:
`CANDIDATE CONSTRUCTION CONVENIENCE MUST NOT OVERRIDE ZERO-TOUCH SOURCE PRESERVATION.`
