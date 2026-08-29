# MUT-2026-08-29-STATUS-GOVERNANCE-RECONCILIATION-002

Transaction ID: `MUT-2026-08-29-STATUS-GOVERNANCE-RECONCILIATION-002`
Baseline: `main@596600efd1f39f88b8991efeaeb99aaf16857180`
Lease: `R71-20260829-STATUS-GOV-RECON-002`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + GOV-013A repository-first multi-instance execution`
Status: `ACTIVE / BOUNDED RECONCILIATION`
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

`Governance/_FOLDER_STATUS.md` was last audited 2026-08-08 and claims `GOVERNANCE BASELINE CLEAN`, but current Governance contains later effective/proposed/session amendments and multiple `GOV-013A`-prefixed artifacts not represented by that evidence record.

## Identity Finding

The following current paths were directly observed:

- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` — explicitly declares `Document ID: GOV-013A`, Approved / Canonical Addendum;
- `Governance/GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md` — title uses `GOV-013A`, proposed integration into GOV-013;
- `Governance/GOV-013A_HERMUZ_SESSION_WORKGROUP_CONTINUATION_AMENDMENT.md` — title uses `GOV-013A`, Approved Session Operating Amendment / Canonical Addendum;
- `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` — title uses `GOV-013A`, Canonical Amendment / Effective;
- `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md` — separately present and not yet reconciled in this transaction.

Therefore the previous folder-level statement `active Governance artifacts have unique logical Document IDs` is not reusable as current proof.

This transaction does **not** invent a new numbering convention or rename these artifacts without a dedicated identity migration analysis.

## Controlled Mutation Matrix

| Change | Target | Action | Boundary |
|---|---|---|---|
| C1 | `Repository/ROOM071_CURRENT_STATE.json` | UPDATE | open serialized lease only |
| C2 | this transaction record | ADD | evidence / handoff only |
| C3 | `Governance/_FOLDER_STATUS.md` | UPDATE | replace stale clean claim with current bounded warning and observed collision |
| C4 | `PROJECT_STATUS.md` | UPDATE | synchronize recent verified chain and current queue without global-clean claim |
| C5 | `REP-001_MASTER_INDEX.md` | CONDITIONAL | update Governance inventory only if identity state can be represented without false canonicalization |
| C6 | Room 71 | UPDATE | close only after read-back + CI evidence |

All unrelated sections are `KEEP`.

## Non-Claims

- Governance identity family is not yet globally reconciled.
- Repository-wide connected baseline is not closed.
- Experience Spine cognitive benefit is not proven.
- External evidence authenticity is not proven by quarantine or local resolver mechanics.
- Branches are not safe to bulk-delete.

## Learning Candidate

A folder-status evidence record can become **dangerously stale even when its original audit was correct**. The existence of later governance amendments is sufficient to invalidate reuse of a historical `CLEAN` claim as current proof. Status freshness must therefore be treated as a dependency of the claim, not metadata decoration.

A second learning candidate is that a family prefix such as `GOV-013A` can evolve from one addendum into multiple semantically distinct addenda. Once that happens, inventory reconciliation must distinguish **family membership** from **unique logical identity**; silently treating filenames as unique identities bypasses the repository's own canonicalization rule.
