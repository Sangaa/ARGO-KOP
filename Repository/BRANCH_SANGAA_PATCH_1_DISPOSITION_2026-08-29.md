# Branch Disposition — `Sangaa-patch-1`

Date: 2026-08-29  
Lease: `R71-20260829-BRANCH-HYGIENE-014`  
Role: HERMUZ  
Baseline at lease entry: `main@586a662d275204395269d0d86306c17172560ea0`

## Scope

Classify one branch only. No branch deletion is authorized by this record.

## Observed branch identity

- Branch: `Sangaa-patch-1`
- Tip: `2dbf5839d9173f9094f9a2992cb36a7c68acacf8`
- Tip commit message: `Delete Future`
- Tip parent: `b8393bcfaa01e2fd25af6f853c824c76ffc384ca`
- Unique tip change: deletion of the one-line historical file path `Future`.
- Compare against current `main` reports the branch as `diverged`, with current main thousands of commits ahead and the branch carrying one branch-side commit.

## Current-main reconciliation

Direct current-path retrieval of `Future` resolves as a **directory**, not a file. Therefore the historical branch-side deletion of a file named `Future` cannot be replayed as a current deletion without changing the meaning of the present namespace.

This is a semantic evolution, not evidence that the branch commit should be merged now.

## Disposition

`Sangaa-patch-1 = SUPERSEDED / HISTORICAL-EVIDENCE-PRESERVED / NO-MERGE-REQUIRED`

Reasoning:

1. the only branch-side change concerns a historical file identity that no longer matches the current path type;
2. current main has evolved far beyond the branch base;
3. merging the old deletion is neither required to obtain the present main state nor safe to interpret as a deletion of the current `Future/` directory;
4. the commit remains useful as provenance showing that an earlier file-form `Future` artifact was intentionally removed.

## Deletion decision

`BRANCH DELETE = NOT AUTHORIZED BY THIS TRANSACTION`

Classification is intentionally separated from physical branch deletion. A later cleanup transaction may delete only after repository policy, provenance retention, and the complete branch-classification set permit it.

## Learning captured

A branch that deleted a historical **file** cannot be judged against a current **directory of the same path string** by name alone. Branch hygiene must compare object identity/type and semantic evolution, not only path text or ahead/behind counts.

## Non-claims

- This record does not classify any other branch.
- This record does not declare all stale branches safe to delete.
- This record does not treat branch age as proof of obsolescence.
- This record does not mutate `Future/`.

## Close candidate

This bounded branch subpoint is eligible for closure after read-back and live-main reconciliation confirm this record is persisted without conflicting concurrent mutation.
