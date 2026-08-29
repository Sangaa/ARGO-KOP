# MUT-2026-08-29 — QLT-001 SEMANTIC REPAIR — 155

State: PREWRITE / NOT CLOSED
Role: HERMUZ via Room71
Baseline: `bef5889592e930b2697a4f0bdc48f58275720808`
Scope: Quality/QLT-001 semantic correction + bounded regression only

## Trigger

Lease 154 classified three stale or over-wide semantics inside `Quality/QLT-001_QUALITY_ASSURANCE.md`:

1. an obsolete related-path name `Governance/GOV-005_DOCUMENT_LIFECYCLE_STANDARD.md`, while current canonical GOV-005 is `Governance/GOV-005_REVIEW_STANDARD.md`;
2. wording that can be read as universal automatic rejection by SRV-009 although current SRV-009 establishes governed validation/hold behavior rather than proof that every Quality violation is automatically rejected in every execution path;
3. an `Automated Rollback` claim tied to RUN-001, while current RUN-001/RUN-009 specify `FAULT/HOLD -> preserve evidence -> synchronize -> validate -> governed recovery`, not automatic repository rollback.

The audit-log wording also exceeds current execution evidence if read as proof of immutable storage under `Logs/`.

## Intended Mutation

- preserve `QLT-001` identity and version unless separate version authority changes it;
- preserve Quality `INTEGRITY HOLD` semantics;
- correct GOV-005 path;
- replace automatic rollback language with current governed FAULT/HOLD + recovery semantics;
- bound SRV-009 rejection language to applicable validation/update controls;
- bound logging language so traceability is required but storage immutability/path is not claimed without evidence;
- add an executable regression guarding the corrected semantic boundaries.

## Non-Claims

This transaction will not:
- certify Quality globally;
- promote QLT-002..005;
- prove universal runtime enforcement;
- prove immutable log storage;
- close Connected Baseline globally;
- modify Core 136, Room71 canonical JSON, or PR #89.

## Close Gate

Finalized Matrix + QLT-001 + regression must enter one final Git tree/commit, followed by read-back and exact-head CI where available.
