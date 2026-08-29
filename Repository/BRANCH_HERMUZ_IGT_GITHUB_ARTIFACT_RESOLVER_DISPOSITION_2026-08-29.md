# Branch Disposition — hermuz/igt-github-artifact-resolver-20260828

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-033`
Authority: `OPERATIONAL CLASSIFICATION ONLY`

## Evidence

Compared from `main@07c97ba6c0567b6a09bbf617613fdfd0147ce68c`:
- branch diverged;
- ahead_by 6;
- behind_by 149;
- merge base `90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa`.

Principal branch implementation:
`Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` branch blob `0e5cd30a92b698f0ee80cb91ce9de508afe86387`.

Current main contains a later successor blob `1e0c20f93f3e3e3d3c6a0c809b0775990fe407f9` which preserves immutable GitHub participant/attestation acquisition and additionally adds generic quarantine `acquire_external` re-acquisition while explicitly refusing to authenticate model/provider claims.

## Semantic direction

The blob difference is forward evolution on main, not evidence of missing branch work. Replaying the historical branch implementation would remove the later generic quarantine acquisition capability.

## Disposition

`FUNCTIONAL_LINEAGE_PRESENT / MAIN_HAS_HARDENED_EXTENDED_SUCCESSOR / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Non-claims

GitHub immutable artifact acquisition proves exact artifact acquisition/provenance only within its bounded resolver semantics. It does not prove provider/model execution authenticity, participant truth, authority, or cognitive effect.

No CI claim is made for this documentation-only classification.

## Learning

Branch hygiene must compare semantic direction when blobs differ. A newer main implementation that strictly preserves the historical behavior and adds bounded fail-closed capability is a successor, not a merge gap.
