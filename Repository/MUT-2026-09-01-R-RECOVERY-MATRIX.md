# R RECOVERY MUTATION MATRIX

Transaction: MUT-2026-09-01-R-RECOVERY
State: PRE-WRITE RECOVERY MATRIX
Incident commit: c38783c38962063a7fc38f6c99adad3547e4e6fd
Clean R candidate: c5c695597a6df18876ff83542c65bed2797fe98f

Incident: an unintended empty file was created at Repository/INVALID_SHOULD_NOT_CREATE.tmp while preparing the Transaction-R closure. The original R Matrix did not authorize that path.

Classification: IMPLEMENTATION_FAILURE. Existing GOV-014A is directly applicable; this is not a new governance gap. The incident commit remains preserved in Git history and this Matrix does not retroactively claim the original write was compliant.

Authorized recovery paths only:
1. REMOVE Repository/INVALID_SHOULD_NOT_CREATE.tmp.
2. CREATE Repository/R_UNAUTHORIZED_TMP_INCIDENT_2026-09-01.md.
3. UPDATE this Matrix with candidate and verification evidence.

KEEP:
- preserve all Transaction-R candidate paths and semantics;
- preserve REP-014 and Core status unchanged;
- no authority, relationship, certification, Phase-1, Connected-Baseline, or Global-PASS promotion;
- no history rewrite, reset, or force push.

Verification: recovery material commit must be exactly one commit after this Matrix commit and exactly the three authorized paths, followed by exact-head read-back and required CI/integration verification.

Learning: tool/action selection at a protected mutation boundary must be checked against the authorized Matrix action before invocation. This remains SESSION-LEARNING unless repeat evidence justifies promotion.
