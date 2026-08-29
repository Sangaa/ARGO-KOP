# MUT-2026-08-29 — COGNITION STATUS RECONCILIATION — 168

State: PREWRITE / NOT CLOSED
Role: HERMUZ via Room71
Baseline: `1fb81c444c1c08512f4427b4b90d6c00d8409129`
Scope: create bounded `Cognition/_FOLDER_STATUS.md` + regression only

## Evidence

Lease 145 enumerated the current Cognition Git tree with `truncated:false`: 35 tracked files and no folder status.

The tree includes:
- `COG-001..COG-009` historical/document family;
- two filenames beginning `COG-010`;
- multiple relationship/session/context contracts;
- Python support/execution artifacts;
- tests.

Semantic review established:
- `COG-010_REASONING_PIPELINE_BOUNDARY.md` explicitly declares `Document ID: COG-010` and `Status: Candidate / Integrity Hold`;
- `COG-010_INTELLIGENCE_LAYER.md` is a thin legacy explanatory file with no current metadata/Document ID block establishing it as the active COG-010 authority;
- COG-009 explicitly separates learning handoff from automatic canonical truth.

## Intended Mutation

Create a status surface that:
- records exact current physical inventory count and categories;
- preserves `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN`;
- records the bounded COG-010 identity ambiguity without promoting the Candidate;
- distinguishes documents/contracts/code/tests;
- preserves COG-009 learning/authority boundary;
- adds regression anchored to repository root.

## Non-Claims

No COG-010 promotion, no Intelligence authority transfer, no cognitive-benefit proof, no global Cognition certification, no Core136 mutation, no Room71 JSON rewrite.

## Close Gate

Status + regression + finalized Matrix must enter one final Git tree/commit and pass exact read-back plus applicable exact-head CI.
