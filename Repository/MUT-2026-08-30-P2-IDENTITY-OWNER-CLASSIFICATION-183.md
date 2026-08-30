# MUT-2026-08-30-P2-IDENTITY-OWNER-CLASSIFICATION-183

Date: 2026-08-30
Lease: `R71-20260830-P2-IDENTITY-OWNER-CLASSIFICATION-183`
Execution role: HERMUZ
Entry baseline: `main@d6b8059bb12d15e53d09fb9bc93ae94ee5b9a474`
Status: `PREWRITE / LEASE ACTIVE / P2 AMBIGUITY CLASSIFICATION`

## Trigger evidence

The repaired namespace-independent Internal Document-ID audit at `e04b073f268aa1291bbb747429d92ac69d83e9ec` completed successfully and emitted artifact `internal-document-id-audit-report` (`9728177701`). The artifact proves the detector contract is functioning while repository-wide identity reconciliation remains open:

- `tracked_files_scanned = 2052`
- `document_id_records = 1100`
- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `identity_scope_reconciled = false`
- `canonical_unindexed_records = 15`
- `ambiguous_duplicate_ids = 145`

Prefix distribution of the 145 ambiguous IDs:

- `EJR = 122`
- `REP = 15`
- `GOV = 2`
- `KRS = 2`
- `GEN = 1`
- `QLT = 1`
- `REL = 1`
- `RUN = 1`

## Prior evidence and learning

Direct repository evidence already proves that at least some EJR ambiguity is real and must not be auto-collapsed. `Repository/REP-020_SESSION_DELTA_2026-08-17_EJR013_CONFLICT.md` classifies the historical EJR-013 pair as a true unresolved duplicate identity and explicitly forbids rename/deletion/reassignment without an authoritative decision.

Other ambiguous groups include records whose filenames/artifact classes indicate that the H1 may identify the reviewed target rather than the evidence record itself, for example mutation matrices, reconciliation records, templates, and closure evidence. Existing learning already requires:

`IDENTIFIER TOKEN EQUALITY != IDENTITY COLLISION WHEN NAMESPACE + ARTIFACT CLASS DIFFER.`

Lease 182 additionally established:

`A REFERENCE TO AN ID IS NOT THE IDENTITY OF THE REFERENCING DOCUMENT.`

The remaining question is therefore not simply token equality. It is:

`Which observed ID occurrence is an identity owner, which is a historical/noncanonical owner, and which is a target/reference label belonging to another artifact class?`

## Bounded objective

Build a classification layer for the current 145 `ambiguous_duplicate_ids` before any identity mutation.

The first bounded pass will separate at least:

1. `PROVED_TRUE_DUPLICATE` — multiple artifacts genuinely claiming the same identity with no authoritative disposition.
2. `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` — one indexed/current owner plus records whose artifact class/title references that owner but does not establish independent ownership.
3. `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` — repeated parent-series H1 where distinct child/addendum identity may exist or be missing.
4. `HISTORICAL_OR_NONCANONICAL_SHADOW` — duplicate token is explicitly historical/noncanonical/superseded.
5. `UNRESOLVED` — evidence insufficient for any stronger classification.

## First-pass scope

Prioritize the 23 non-EJR ambiguous IDs because many have clear cross-artifact-class structure and can test the classification contract without rewriting historical journals.

Representative groups to inspect:

- `GOV-015`, `GOV-016`
- `GEN-001`
- `KRS-001`, `KRS-002`
- `QLT-001`
- `REL-009`
- `RUN-010`
- `REP-001`, `REP-002`, `REP-011`, `REP-012`, `REP-014`, `REP-016`, `REP-020` and other reported REP groups

EJR identities remain read-only under this lease except for evidence classification. No EJR rename/delete/reassignment is authorized.

## Allowed paths

- `Quality/Integration/internal_document_id_audit.py` only if a classification-only detector enhancement is proved necessary
- `Quality/Integration/test_internal_document_id_audit.py` only for regression coverage of proved classification semantics
- this Lease 183 record
- new bounded Repository evidence/closure record for classification results

## Forbidden paths

- any canonical identity owner mutation
- `EJR/**` mutation
- `Memory/**` mutation
- `Governance/**` mutation
- `Core/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- `Release/**`
- `Repository/REP-001_*`
- `Repository/REP-002_*`
- `Repository/REP-014_*`
- `Repository/REP-016_*`
- `PROJECT_STATUS.md`
- branch deletion
- force ref mutation

## C1-C6 collision gate

- **C1 path collision:** PASS — Lease 183 path is unique.
- **C2 semantic collision:** PASS — classification precedes identity mutation; no owner is changed.
- **C3 authority collision:** PASS — prior canonical/index authority remains untouched.
- **C4 promotion collision:** PASS — classification cannot promote P2 to CLOSED by itself.
- **C5 evidence collision:** PASS — artifact `9728177701` is deterministic exact-head evidence; EJR-013 proves at least one real duplicate class exists.
- **C6 handoff collision:** PASS — 179-182 are closed tooling repairs; 183 consumes their newly visible findings without reopening those repairs.

## Stop conditions

HOLD rather than mutate if:

- artifact class cannot be proven from current repository evidence;
- more than one plausible current identity owner remains;
- a cross-reference may depend on the exact historical identity;
- classification would require inventing a new ID or authority;
- detector changes would hide a true duplicate merely to reduce the ambiguity count.

## Learning candidate

`TITLE TOKEN MATCH != IDENTITY OWNERSHIP.`

`DUPLICATE-ID RECONCILIATION REQUIRES ARTIFACT-CLASS AND OWNER EVIDENCE, NOT TOKEN EQUALITY ALONE.`

Initial state:
`P2_IDENTITY_OWNER_CLASSIFICATION_183 = IN_PROGRESS / NO IDENTITY MUTATION AUTHORIZED`.
