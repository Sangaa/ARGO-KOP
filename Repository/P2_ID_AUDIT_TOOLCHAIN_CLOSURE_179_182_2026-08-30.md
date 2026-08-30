# P2 INTERNAL DOCUMENT-ID AUDIT TOOLCHAIN CLOSURE — LEASES 179–182

Date: 2026-08-30
Execution role: HERMUZ / Room71
Verified HEAD: `e04b073f268aa1291bbb747429d92ac69d83e9ec`
Scope: audit-tool coverage, parser semantics, failure observability, identity-source semantics
State: `CLOSED / EXECUTION-VERIFIED / PRIORITY-2 DATA REVIEW REMAINS OPEN`

## Closure boundary

This record closes the tooling-repair chain only. It does **not** claim that repository-wide Priority-2 identity reconciliation is complete.

The chain repaired four distinct defects:

1. **179 — coverage defect**: fixed namespace allowlisting excluded directly present identities such as `COG-*`, `DEC-*`, `REL-*`, `BOOTSTRAP-001`, and `PROJECT_STATUS`.
2. **180 — fallback grammar defect**: a generic H1 fallback accepted arbitrary uppercase title tokens such as `ARGO` from `# ARGO KOP`.
3. **181 — failure-observability defect**: pytest failure prevented deterministic audit output from surviving the failing workflow.
4. **182 — identity-source defect**: body references such as `Document ID: P6-SCOPE-001` inside an EJR could be misread as the EJR identity, and explicit metadata plus H1 fallback were incorrectly treated as competing authorities.

## Current semantics after 182

The current audit now applies the following bounded contract:

- qualified document metadata `Document ID` is the primary identity source;
- structural first-H1 identity is a fallback only when qualified metadata is absent;
- body references to another artifact's Document ID do not become the referencing document's identity;
- human/series/relationship H1 text does not override explicit metadata identity;
- multiple disagreeing qualified metadata Document IDs in the same metadata preamble are treated as a real intra-document conflict;
- namespace discovery is not constrained by a fixed allowlist;
- active indexed duplicate checking, filename/internal-ID alignment, and Governance document-level collision checks remain active;
- failed audit runs preserve the deterministic JSON report as a workflow artifact without converting the failure to PASS.

## Exact-head verification

All four automatically triggered verification surfaces passed on the same repair HEAD `e04b073f268aa1291bbb747429d92ac69d83e9ec`:

| Surface | Run | Result |
|---|---:|---|
| Internal Document-ID Audit | `33298557071` | `SUCCESS` |
| ARGO Runtime Prototype and Integration Tests | `33298557080` | `SUCCESS` |
| Full-Stack Repository Audit | `33298557075` | `SUCCESS` |
| M2 Multi-Channel Proposal Training | `33298557081` | `SUCCESS` |

The successful Internal Document-ID run preserved deterministic artifact:

- artifact name: `internal-document-id-audit-report`
- artifact ID: `9728177701`
- artifact digest: `sha256:3361d0cd444e8280510cb87b96d327f0d51cea9f969f722af4208da5b264902f`
- artifact HEAD: `e04b073f268aa1291bbb747429d92ac69d83e9ec`

## Deterministic report disposition

The exact-head report proves:

- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `duplicate_active_ids = {}`
- `filename_internal_id_mismatches = []`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `identity_scope_reconciled = false`

The last value is intentionally **not** promoted to PASS. Remaining data-review populations include:

- 15 `canonical_unindexed_paths`;
- 145 `ambiguous_duplicate_ids` under the current broad classification;
- 42 deferred-domain records.

The 145 ambiguous keys are not pre-classified as 145 real authority collisions. Current distribution is dominated by EJR/evidence surfaces and records whose H1 names a parent/subject identity. Current observed key-prefix distribution:

- `EJR`: 122
- `REP`: 15
- `GOV`: 2
- `KRS`: 2
- `GEN`: 1
- `QLT`: 1
- `REL`: 1
- `RUN`: 1

This population requires artifact-class / authority-owner classification before any rename, archive, index, or identity mutation is legal.

## Learning promoted as bounded engineering evidence

1. `AUDIT GREEN != DOMAIN COVERAGE`.
2. `DETECTOR EXPANSION FAILURE MAY BE NEW EVIDENCE, NOT REGRESSION`.
3. `GENERIC PARSING != UNCONSTRAINED PARSING`.
4. `A FAILING AUDIT MUST PRESERVE ITS FAILURE EVIDENCE`.
5. `A REFERENCE TO AN ID IS NOT THE IDENTITY OF THE REFERENCING DOCUMENT`.
6. `PRIMARY/FALLBACK DETECTION MUST NOT TURN THE FALLBACK INTO A SECOND AUTHORITY`.
7. `TOOLING REPAIR CLOSED != REPOSITORY-WIDE IDENTITY RECONCILIATION CLOSED`.

## Lease dispositions

- `P2_ID_AUDIT_COVERAGE_179 = CLOSED / EXECUTION-VERIFIED / TOOLING SUBGATE`
- `P2_ID_AUDIT_PARSER_180 = CLOSED / EXECUTION-VERIFIED / TOOLING SUBGATE`
- `P2_ID_AUDIT_OBSERVABILITY_181 = CLOSED / EXECUTION-VERIFIED / TOOLING SUBGATE`
- `P2_ID_AUDIT_IDENTITY_SOURCE_182 = CLOSED / EXECUTION-VERIFIED / TOOLING SUBGATE`
- `PRIORITY_2_REPOSITORY_WIDE_IDENTITY_RECONCILIATION = OPEN / DATA CLASSIFICATION REQUIRED`

## Next legal action

Classify the exact remaining ambiguous population by semantic role and authority class before changing any identity owner. At minimum distinguish:

`ACTIVE_CANONICAL_OWNER / HISTORICAL_OR_ARCHIVED_OWNER / EVIDENCE_ABOUT_IDENTITY / JOURNAL_OR_SESSION_RECORD / PARENT_SERIES_LABEL / TRUE_COMPETING_IDENTITY / UNRESOLVED`.

No mass rename, deletion, archive move, or automatic indexing is authorized by this closure.
