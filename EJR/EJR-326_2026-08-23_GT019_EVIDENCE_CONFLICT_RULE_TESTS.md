# EJR-326 — GT-019 Evidence Conflict Rule Controlled Tests

Date: 2026-08-23
Status: COMPLETED / CONTROLLED TEST RECORD
Protocol: GOV-013 + GOV-018 Candidate + CELM-001
Parent: EJR-325

## Objective

Test the newly integrated ENG-001 evidence reasoning rules against existing repository evidence without changing production logic or external workflows.

## Test 1 — Authority resolves a baseline conflict

### Evidence

- `Release/VERSION.md` declares current Development Baseline `3.2.1` and is the authoritative source for the baseline/release distinction.
- Historical `REP-012` evidence contained `3.3.0`.
- `Governance/GOV-013_BASELINE_AUTHORITY_RECONCILIATION_2026-08-14.md` records the reconciliation.

### Evaluation

Claim type: `NORMATIVE`
Target: current Development Baseline
Same proposition: YES
Mutually exclusive values: YES

Classification:

`CONTRADICTION`

Resolution:

`CONTRADICTION → RESOLVED BY AUTHORITY`

Winning evidence: explicit authoritative baseline declaration (`3.2.1`).

Rejected shortcut: higher numeric value does not win merely because it is higher.

Result: **PASS**

## Test 2 — Artifact metadata and payload are different corroborating layers

### Evidence

GT-017 records:

- artifact metadata binds `ci-execution-identity` to workflow run `32548603868`;
- artifact payload declares `run_id`, event, ref, `github_sha` and `checkout_sha`;
- independent correlation converges on the same execution identity.

### Evaluation

Claim family: execution identity
Evidence layers: artifact metadata + artifact payload
Same proposition: materially compatible
Mutually exclusive outcomes: NO

Classification:

`DIFFERENT EVIDENCE LAYERS` + `CORROBORATED`

The two surfaces strengthen identity confidence but neither changes the other surface's semantics.

Result: **PASS**

## Test 3 — Artifact policy result remains unresolved and does not become PASS

### Evidence

GT-017 records that `ci-impact-correlation` reports:

- `changed_path_count: 1`
- `mapped_path_count: 0`
- `overall: POLICY_UNRESOLVED`
- `promotion: NO_AUTO_PROMOTION`

The same training record establishes that the artifact does not prove P6 PASS.

### Evaluation

Claim type: `DERIVED RESULT / POLICY STATE`
Target: impact-correlation decision
Producer conclusion: unresolved

Classification:

`UNRESOLVED`

Reason: the artifact explicitly reports an unresolved policy mapping and no automatic promotion. The evidence transport, artifact digest, or successful download cannot alter that semantic result.

Result: **PASS — protected unresolved state preserved**

## Test 4 — Textual difference alone is not contradiction

### Evidence pair

- Workflow/run exists.
- Correlation artifact reports `POLICY_UNRESOLVED`.

### Evaluation

These observations describe different propositions:

`run existence/execution identity` versus `policy correlation outcome`.

Classification:

`DIFFERENT EVIDENCE LAYERS`

Not `CONTRADICTION`.

Result: **PASS**

## Test conclusion

The new reasoning rules correctly produce three materially different outcomes:

1. `CONTRADICTION → RESOLVED BY AUTHORITY`
2. `DIFFERENT EVIDENCE LAYERS / CORROBORATED`
3. `UNRESOLVED` as a protected non-promotion state

This validates the conceptual decision boundary against current repository evidence. It does not yet establish runtime execution of the reasoning engine implementation.

## Knowledge Delta

**KD-024 — Contradiction is a classification before resolution**

A contradiction must first be detected, then resolved through legitimate precedence; resolution must not be hidden inside the contradiction detector.

**KD-025 — Unresolved is not failure**

An explicitly unresolved policy/evidence state can be a correct engine output when the evidence does not justify promotion or a single resolved conclusion.

## Closure

`Execute → Document → Read-back → Verify → Close`

Next safe continuation:

`GT-020 — determine the minimal structured evidence object needed for ENG-001 to carry claim type, evidence layer, authority, identity, temporal validity and resolution state without creating a new model prematurely.`
