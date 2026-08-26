# KRS-001 Pilot 3 — P236 Consumer Change Matrix

Status: `PRE-WRITE / OPEN`
Branch: `hermuz/p234-safe-gate`
Parent: `P235 / REP-032`

## Objective
Authorize the smallest non-production consumer change required to make the deterministic harness consume and attest the exact contract artifact blob.

## Allowed Mutation
Add a side-effect-free adapter/test seam only. It may receive an exact expected blob SHA and artifact bytes, verify the SHA, then pass the verified artifact content into the existing harness. It must not alter canonical contracts, production runtime, schema version, or external I/O behavior.

## Required Attestation
The test output must contain:
- expected blob SHA;
- computed/observed blob identity;
- equality result;
- harness execution result;
- external side-effect = false.

## Gates
- one isolated branch;
- no main mutation;
- exact source blob must be fetched from the repository;
- mismatch => HOLD/failure, never inferred success;
- post-write read-back;
- applicable CI evidence must bind to the resulting commit.

## Non-Goals
No production promotion, no schema promotion, no KO mutation, no merge.

## Closure
P236 remains open until the implementation mutation and its exact-SHA execution evidence are independently read back and closed.
