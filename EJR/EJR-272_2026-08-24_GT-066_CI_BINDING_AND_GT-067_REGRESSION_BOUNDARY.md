# EJR-272 — GT-066 CI Binding and GT-067 Regression Boundary

**Date:** 2026-08-24
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Scope:** Training / CI provenance / evidence reasoning
**Mutation class:** Documentation-only

## GT-066 — Historical CI Run / Artifact Binding

### Verified chain

A concrete successful run was independently retrieved:

- workflow: `Full-Stack Repository Audit`
- run_id: `32715454598`
- run_number: `1456`
- event: `pull_request`
- head_sha: `c1df6b127aefd70643aad519c8bf16e1200f86cd`
- head_branch: `probe/hermuz-gt014-20260824-v1`
- conclusion: `success`

The workflow job log proves the execution-side ref and SHA binding:

- fetched `aa9b0665c932a91a15868c417928d311b8a24a5c` as `refs/remotes/pull/27/merge`
- checked out `refs/remotes/pull/27/merge`
- resulting `HEAD = aa9b0665c932a91a15868c417928d311b8a24a5c`
- an explicit assertion required `CHECKOUT_SHA == aa9b0665c932a91a15868c417928d311b8a24a5c`
- the job emitted `ci-execution-identity.json` containing the workflow, run_id, event, ref, github_sha and checkout_sha.

The artifact surface independently returns:

- artifact: `ci-execution-identity`
- artifact_id: `9515708952`
- run_id: `32715454598`
- digest: `sha256:591129541d371c2427e624a956a342171b606cd4671e7d2e5a977800f028fe4c`
- artifact status: not expired

The artifact was downloaded and its payload was independently read. Its JSON content records:

`workflow=Full-Stack Repository Audit`
`run_id=32715454598`
`event=pull_request`
`ref=refs/pull/27/merge`
`github_sha=aa9b0665c932a91a15868c417928d311b8a24a5c`
`checkout_sha=aa9b0665c932a91a15868c417928d311b8a24a5c`

### Important reconciliation

The workflow run metadata identifies the source PR head as `c1df6b127...`, while the execution ref resolves to synthetic merge commit `aa9b0665...`. The run metadata also reports the head commit tree as `9e41a366...`, matching the previously resolved execution tree. This confirms that source-head identity and execution identity are distinct layers even when the resulting tree is the same.

The connector's `fetch_commit_workflow_runs(aa9b0665...)` returned no runs. This is **not** contradictory evidence: the available wrapper associates the run with the PR-triggered source head SHA, while the run log and artifact independently establish the execution SHA. Therefore the negative result is classified as a connector query-surface limitation, not absence of execution.

### GT-066 verdict

**GT-066 = VERIFIED / HISTORICAL RUN-REF-SHA-ARTIFACT BINDING ESTABLISHED**

The earlier GT-065 gap is closed for this observed execution.

The correct provenance chain is now:

`PR source head → PR event → execution ref → execution SHA → checkout SHA → Git tree → CI run → artifact`

The PR-recorded `merge_commit_sha` remains a separate metadata field and must not replace `execution_sha`.

## Additional observation — failed runtime run

A separate PR-triggered run exists:

- workflow: `ARGO Runtime Prototype and Integration Tests`
- run_id: `32715454434`
- run_number: `962`
- head_sha: `c1df6b127...`
- conclusion: `failure`
- attempt: `2`

Its `integration-tests` job failed in `Quality/Integration/test_evidence_reasoning_classification.py`, while the other listed jobs completed successfully. The run exposed 9 test failures, primarily Python constructor misuse (`multiple values for keyword argument` / missing required `evidence_layer`) rather than a CI checkout identity failure. The run has no artifacts through the available artifact surface.

This failure must remain classified as a **real test-suite failure**, not a provenance failure and not an artifact-missing execution failure.

## GT-067 — Evidence Reasoning Regression Boundary

The current failing test file contains failures around:

- explicit bound execution identity
- execution identity mismatch
- cross-binding mismatch
- correlated versus independent evidence
- provenance root/parent consistency

The observed exceptions occur before the intended semantic assertions because test fixture construction supplies duplicate keyword arguments or omits required fields. Therefore the immediate boundary is:

`test fixture construction failure ≠ semantic model verdict`

No semantic rule should be changed to make these tests pass. The next safe action is to inspect the current test fixture definitions and the `EvidenceObservation` constructor contract, reconcile the fixture/API mismatch, and then rerun the focused test set.

### GT-067 verdict

**GT-067 = BLOCKED / FIXTURE-CONTRACT MISMATCH BEFORE SEMANTIC EVALUATION**

This is actionable and localized. It is not evidence that the provenance model itself is wrong.

## Architectural learning

1. `head_sha`, `pr_merge_commit_sha`, `execution_sha`, `checkout_sha`, and `tree_sha` are different evidence roles.
2. A workflow run can be indexed by source-head SHA while executing from a synthetic merge SHA.
3. A connector returning no runs for an execution SHA does not prove no run exists when the connector's query semantics index PR runs by source head.
4. Artifact identity is a separate evidence object and should be bound through `run_id`, not inferred from a commit alone.
5. Missing artifacts on a failed run must not be converted into an execution failure category; the run conclusion remains the primary execution result.
6. Test fixture/API contract errors must be isolated from semantic evidence-rule failures.

## Session closure

- GT-064: VERIFIED / MULTI-STATE CI PROVENANCE
- GT-065: CLOSED BY NEW EVIDENCE / EXECUTION STATE AND RUN BINDING RECONCILED
- GT-066: VERIFIED
- GT-067: BLOCKED AT FIXTURE-CONTRACT LAYER
- Production logic mutation: NONE
- Documentation mutation: COMPLETED

**Next safe mutation:** inspect and reconcile the `EvidenceObservation` test fixture contract before modifying any evidence semantics.