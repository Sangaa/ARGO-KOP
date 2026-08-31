# R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212

Status: CLOSED / VERIFIED-THROUGH-SUCCESSOR / RESUME-SAFE
Prewrite: `9211f7accd89ab1a597e0651fde909d0b6fcca20`
Functional head: `89c51d6aff95f86652a01153f2d842f4db0e7960`
Verification successor: `R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-213`
Target displaced record: `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`
Replacement identity/path: `EJR-401` / `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`

## Authorization basis
- Lease203 proved root EJR-211 was a distinct legitimate later reuse while Memory EJR-211 retained the earlier governed allocation.
- Lease204 required one-record collision-safe repair and first-valid-allocation retention.
- Lease211 proved EJR-401 VACANT with complete locally reachable history: artifact `9744595264`, current_claims=[], historical_claims=[], decision=VACANT.
- Repeated current-main exact path/name searches established no current operational consumer requiring synchronous rewrite; positive hits were historical Lease203/204 evidence.

## Functional mutation
Exactly one displaced record was repaired:
- removed `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`;
- added `EJR/EJR-401_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`;
- preserved the complete semantic body and chronology;
- changed only the document-level first H1 identity `EJR-211` → `EJR-401`.

Functional compare was limited to the old/new EJR path plus this Matrix. The retained Memory EJR-211, analyzers, tests, workflows, authority registries, and unrelated consumers were not changed.

## Repair-head evidence — preserved historically
At functional head `89c51d6aff95f86652a01153f2d842f4db0e7960`:
- Full-Stack Repository Audit `33354350713` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33354350756` — SUCCESS;
- M2 Multi-Channel Proposal Training `33354350815` — SUCCESS;
- Real Mutation Matrix Regression `33354350711` — SUCCESS;
- Internal Document-ID Audit `33354350722` — FAILURE.

The Internal-ID failure is not rewritten as success. Its job showed all tests and preceding analyzers PASS; only memory-to-root provenance census failed. Artifact `9744650333` proved expected=35, observed=34, history_complete=true, sole incomplete=`__COHORT_COUNT_DRIFT__`. Audit artifact `9744649112` proved EJR-211 and EJR-401 were both non-ambiguous.

## Successor reconciliation
Lease213 separately rebaselined only the proven post-repair cohort constant 35→34 while preserving the drift guard. On successor functional head `75160d7314bdcd79594447e3c50f2808ae1ccd5a`, all five gates passed including Internal-ID `33354533694`; census artifact `9744704885` proved 34/34 CENSUSED with no incomplete IDs.

Therefore the one-record repair is verified through its bounded verification-surface successor. Historical failure evidence remains accurate and intact.

## Current identity result
- displaced root EJR-211 path absent;
- replacement EJR-401 path present;
- semantic body preserved except H1 identity;
- EJR-211 absent from current ambiguity records;
- EJR-401 absent from current ambiguity records;
- retained Memory EJR-211 unchanged.

## Boundaries preserved
Priority 2 remains OPEN. Phase 1 remains OPEN. Repository-wide identity/content/relationship reconciliation remains OPEN. Connected-Baseline/global graph validation remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS is claimed.

## Next legal action
Do not reopen EJR-211/EJR-401 or baseline 34 without contradictory/new evidence. Re-enter Priority 2 from current evidence and select the next displaced identity only after current consumer-risk comparison and a separate replacement-vacancy proof.
