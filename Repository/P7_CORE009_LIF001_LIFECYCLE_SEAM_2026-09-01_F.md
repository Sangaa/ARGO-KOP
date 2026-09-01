# P7 CORE-009 ↔ LIF-001 Lifecycle Seam — Transaction F

Date: 2026-09-01  
Priority: 7  
Transaction: `F`  
Status: `CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`

## Entry evidence

- Transaction-E final closure head was re-read before continuation and current `main` was rediscovered.
- Transaction-F prewrite authority head: `253e8c6d21558781d7c6f8e06489caf3b9ac966c`.
- `Core/CORE-009_PLATFORM_LIFECYCLE.md` at entry was v1.4.0 and still named the document lifecycle as `GOV-005` plus retired path `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md`.
- `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md` is the current canonical document lifecycle and records the former Lifecycle GOV-005 identity/path as retired collision provenance.
- `Lifecycle/_FOLDER_STATUS.md` independently confirms active LIF-001 and retired active-path cleanup.

## Classification

`CURRENT CORE SEMANTIC / AUTHORITY-PATH DRIFT`.

The stale CORE-009 identity/path is not retained as current authority merely because it is historical text. Current repository evidence requires canonical LIF-001.

## Relationship result

Direct source evidence supports two documentary directions:

```text
CORE-009 → LIF-001 = REFERENCES
LIF-001  → CORE-009 = REFERENCES
```

No evidence supports promotion of this seam to `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, or `CONSUMES`.

Planned registry dispositions:

- `REL-063`: `DOCUMENT-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY`
- `REL-064`: `PLATFORM-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY`

## Candidate mutation

The governed candidate is designed as one atomic Git change set containing:

- CORE-009 semantic identity/path correction and v1.4.1;
- REP-014 v1.2.8 with REL-063/064;
- current control-plane manifest refresh for REP-014 v1.2.8;
- Core and Lifecycle bounded status synchronization;
- focused lifecycle-boundary regression;
- this evidence record;
- Transaction-F Mutation Matrix binding.

The candidate preserves:

- separate platform/document lifecycle authority;
- active `Governance/GOV-005_REVIEW_STANDARD.md` identity;
- historical provenance of retired Lifecycle GOV-005 without recreating that active path;
- Core and Lifecycle certification holds;
- Phase-1/global/Connected-Baseline open boundaries.

## CI gate

Required exact-head validation remains pending. Any required workflow failure reopens `GOV-013 §9B HARD HOLD` before further construction.

## Resume-safe boundary

If candidate CI is green, close Transaction F with exact workflow evidence. If any required check fails, diagnose first meaningful failure and repair only under governed matrix authorization.
