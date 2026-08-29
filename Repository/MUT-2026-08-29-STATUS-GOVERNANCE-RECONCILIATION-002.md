# MUT-2026-08-29-STATUS-GOVERNANCE-RECONCILIATION-002

Transaction ID: `MUT-2026-08-29-STATUS-GOVERNANCE-RECONCILIATION-002`
Baseline: `main@596600efd1f39f88b8991efeaeb99aaf16857180`
Lease: `R71-20260829-STATUS-GOV-RECON-002`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + GOV-013A repository-first multi-instance execution`
Status: `CLOSED / ROOT STATUS SYNCHRONIZED / GOVERNANCE IDENTITY HOLD EXPLICIT`
Authority: `NONE BEYOND APPLICABLE GOVERNANCE`

## Objective

Close every currently provable control-plane status point while refusing false closure of repository-wide or Governance identity claims.

Primary targets:

1. synchronize `PROJECT_STATUS.md` with verified 2026-08-28/29 mainline evolution;
2. correct stale Governance folder-clean claims;
3. reconcile `REP-001` only to the extent supported by current identity/path/authority evidence;
4. preserve all unrelated content and repository-wide holds;
5. record any new identity collision as an explicit hold rather than normalizing it by assumption.

## Entry Evidence

Observed live HEAD at entry: `596600efd1f39f88b8991efeaeb99aaf16857180`.

Current Room 71 state showed no active lease and ranked:

1. root status synchronization;
2. Governance/REP-001 inventory reconciliation;
3. external evidence lifecycle;
4. global connected baseline;
5. IGT cognitive benefit proof;
6. branch hygiene.

`PROJECT_STATUS.md` was last audited 2026-08-25 and still described the file-local seam scanner as the latest checkpoint, while main now contains bounded P4 closure, Experience Spine advisory projection, IGT experiment/evidence chain, untrusted external-evidence intake, and Room 71 multi-instance control.

`Governance/_FOLDER_STATUS.md` was last audited 2026-08-08 and claimed `GOVERNANCE BASELINE CLEAN`, but current Governance contains later effective/proposed/session amendments and multiple reused Governance identity prefixes not represented by that evidence record.

## Identity Finding

The following current paths were directly observed:

- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` — explicitly declares `Document ID: GOV-013A`, Approved / Canonical Addendum;
- `Governance/GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md` — title uses `GOV-013A`, proposed integration into GOV-013;
- `Governance/GOV-013A_HERMUZ_SESSION_WORKGROUP_CONTINUATION_AMENDMENT.md` — title uses `GOV-013A`, Approved Session Operating Amendment / Canonical Addendum;
- `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` — title uses `GOV-013A`, Canonical Amendment / Effective;
- `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md` — separately present and not yet reconciled.

Further direct review confirmed heading-family collisions for `GOV-015`, `GOV-016`, and `GOV-017`, where active and/or proposed documents currently share the same numeric heading identity. `GOV-014` also has more than one current governance artifact using the same numeric family, and prior REP-001/REP-002 tests establish only `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` as the indexed GOV-014 path.

Therefore the former folder-level statement `active Governance artifacts have unique logical Document IDs` is not reusable as current proof.

This transaction does **not** invent a numbering convention or rename these artifacts without a dedicated identity migration analysis.

## Audit Blind-Spot Repair

The existing `Quality/Integration/internal_document_id_audit.py` parsed only three-digit IDs from explicit metadata and could therefore miss:

- explicit suffixed IDs such as `GOV-013A`;
- heading-level collisions when one or more documents omit `Document ID` metadata.

The audit was extended to:

- observe one optional alphabetic suffix on identifier-shaped metadata;
- record heading identities separately from authority-bearing explicit Document IDs;
- report `heading_identity_collisions` and `governance_heading_identity_collisions`;
- set `governance_identity_hold_required` when such current Governance collisions exist;
- refuse `identity_scope_reconciled` while those collisions remain.

A regression test now requires the current `GOV-013A`, `GOV-015`, `GOV-016`, and `GOV-017` collisions to be visible and verifies that Governance folder status remains an explicit HOLD rather than a false CLEAN result.

This detector does not decide which artifact is canonical and does not authorize renumbering.

## Controlled Mutation Matrix

| Change | Target | Action | Result |
|---|---|---|---|
| C1 | `Repository/ROOM071_CURRENT_STATE.json` | UPDATE | lease opened and will be closed after final control-state write |
| C2 | this transaction record | ADD/UPDATE | evidence and failure-to-learning recorded |
| C3 | `Governance/_FOLDER_STATUS.md` | UPDATE | stale CLEAN claim reopened as current identity re-audit HOLD |
| C4 | `PROJECT_STATUS.md` | UPDATE | recent verified chain synchronized; global holds preserved |
| C5 | `REP-001_MASTER_INDEX.md` | HOLD / NO MUTATION | no inventory promotion while identity-family ownership remains ambiguous |
| C6 | `Quality/Integration/internal_document_id_audit.py` | UPDATE | current identity-family blind spot repaired without authority promotion |
| C7 | `Quality/Integration/test_internal_document_id_audit.py` | UPDATE | regression guard established |
| C8 | Room 71 | UPDATE | close lease with bounded handoff |

All unrelated sections remained `KEEP`.

## Failure-to-Learning Record

### Failure

The first synchronized `PROJECT_STATUS.md` mutation changed its document version from `3.3.7` to `3.4.0` without a separate governed version-change decision.

### Evidence

On HEAD `2250ee913d4638e3b3cc24ed5da19cd795038d39`:

- Full-Stack Repository Audit = `SUCCESS`;
- Internal Document-ID Audit = `SUCCESS`;
- M2 Multi-Channel Proposal Training = `SUCCESS`;
- Runtime/Integration workflow = `FAILURE` because the `integrity-tests` job failed while prototype and integration jobs passed.

The exact failing assertions were:

- `test_version_authority_consistency.py::test_status_document_version_is_not_mistaken_for_platform_baseline`;
- `test_version_authority_regressions.py::test_project_status_document_version_is_not_treated_as_platform_release_version`.

Both require `Version: 3.3.7` in `PROJECT_STATUS.md` while separately verifying development baseline `3.2.1` and official release `1.0.0`.

### Classification

`MODEL_ASSUMPTION_FAILURE + IMPLEMENTATION_FAILURE`.

The status content required synchronization; document-version promotion did not follow from that requirement.

### Corrective Pattern

`Content synchronization != document-version authority.`

When a governed status document has a version protected by explicit regression tests, content reconciliation must preserve that version unless a separate version-change transaction establishes why the version itself should advance and updates all governing evidence consistently.

The repair restored `PROJECT_STATUS.md` to `Version: 3.3.7` while preserving the verified Aug 29 content update. Repair commit: `50befc922bb9c9b68409cb258ede2bc2ced8b428`.

The failed tests were not weakened or rewritten to accept the accidental version bump.

## Closure Evidence

Exact verification head after repair and transaction learning capture:

`177191cd270c343b03a2d0d0b9a233ea4a8ffedf`

Observed GitHub Actions on that exact SHA:

- `ARGO Runtime Prototype and Integration Tests` — run `33236457769` — `SUCCESS`;
- `Full-Stack Repository Audit` — run `33236457710` — `SUCCESS`;
- `M2 Multi-Channel Proposal Training` — run `33236457723` — `SUCCESS`.

The current Governance status was re-read and shows `INTEGRITY WARNING / CURRENT IDENTITY RE-AUDIT`, not CLEAN.

The current root status was re-read and now reflects P4 bounded closure, Experience Spine/IGT/Room71 evolution, external-evidence lifecycle boundaries and the Governance identity HOLD while preserving release/baseline authority.

## Closed Points

- `CONTROL-PLANE-ROOT-STATUS-SYNC` — `CLOSED` for the current Aug 29 verified snapshot.
- `GOVERNANCE-FOLDER-STALE-CLEAN-CLAIM` — `CLOSED` by replacing stale CLEAN reuse with a current bounded HOLD.
- `INTERNAL-DOCUMENT-ID-AUDIT-HEADING/SUFFIX-BLIND-SPOT` — `CLOSED` with executable regression coverage.
- `PROJECT-STATUS-VERSION-REGRESSION` — `CLOSED` after restoring governed document version and observing green CI.

## Explicit Remaining HOLD

`GOVERNANCE-REP001-INVENTORY-RECONCILIATION` remains **OPEN / HARD SEMANTIC HOLD**.

Reason: `REP-001` cannot safely promote or normalize Governance inventory while current identity-family ownership/status semantics are unresolved. The next legal work is a dedicated Governance identity classification/migration transaction, not cosmetic index editing.

## Non-Claims

- Governance identity family is not globally reconciled.
- Repository-wide connected baseline is not closed.
- Experience Spine cognitive benefit is not proven.
- External evidence authenticity is not proven by quarantine or local resolver mechanics.
- Branches are not safe to bulk-delete.
- A heading collision alone does not decide canonical ownership.

## Learning Candidates Promoted as Session Evidence

1. A folder-status evidence record can become dangerously stale even when its original audit was correct. Freshness is a dependency of a CLEAN claim.
2. A shared amendment prefix can evolve into identity-family ambiguity; family membership and unique logical identity are separate concepts.
3. Metadata-only identity audits are insufficient when live repository documents express identity in headings or filenames without complete metadata. Detection and authority must remain separate.
4. Content synchronization is not permission to increment a governed document version. Version changes are independent mutations when regression or authority contracts bind them.
5. A failed CI can reveal a hidden authority contract that is stronger than the status prose itself; the correct response is to reconcile the mutation to that contract, not weaken the test.

## Final Disposition

This transaction is `CLOSED` for root-status synchronization, stale Governance-status reopening, audit-observability repair and the version-regression correction.

It intentionally hands off unresolved Governance canonical identity ownership as a separate transaction.
