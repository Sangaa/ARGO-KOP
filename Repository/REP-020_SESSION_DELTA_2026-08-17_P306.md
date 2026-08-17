# P306 — CONTROL-PLANE RECONCILIATION DELTA

Date: 2026-08-17
Status: Recorded / Priority 1 Reconciliation / Integrity Hold
Checkpoint: P306

## Scope
Git-native preparation for full-content-preserving synchronization of REP-011 and REP-012 with P305.

## Current Identities
- REP-011 blob: `77ad9a18827099e54ddd8dd16a278535d226abbd`
- REP-012 blob: `5b51e0b468e479842d7d83468e8e7c20a06ec1b1`
- P305 evidence: `7d2ce804510fff20f0809d75539e47bf2bb103eb`

## Finding
The repository-native low-level Git path is available (`blob → tree → commit`), but the actual canonical-file mutation is deliberately not executed in this checkpoint because the complete modified blobs must be constructed and verified without any content loss.

## Decision
`REP-011` and `REP-012` remain unchanged. No synchronization claim is made.

## Required Postconditions for the eventual mutation
1. Preserve the complete current file content.
2. Add only the minimum P305/P306 binding evidence.
3. Create new blobs for the complete modified files.
4. Create one tree/commit preserving all unrelated paths.
5. Advance `main` only after the tree is verified.
6. Full-read both canonical files after commit.
7. Re-read `REP-013/014/015/016/020` and record CI against the resulting HEAD.

## Learning
A native write mechanism existing is not itself permission to use it: the mutation payload must also be proven content-preserving.

## State
- Priority 1: OPEN
- REP-011/012 internal binding lag: OPEN
- ENG-006 → SRV-009 executable proof: OPEN
- Integrity: HOLD
- Global PASS: NOT CLAIMED

---

End of P306
