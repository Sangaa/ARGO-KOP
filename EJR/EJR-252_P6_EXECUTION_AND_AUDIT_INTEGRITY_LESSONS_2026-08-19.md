# EJR-252 — P6 Execution & Audit Integrity Lessons

Date: 2026-08-19
Status: `RECORDED / RESUME-SAFE / NO GLOBAL PASS`
Authority: `GOV-013 + GOV-013A + GOV-014 + GOV-016`

## Incident Scope

P6 CI validation exposed several distinct failure classes. The failures must not be collapsed into a single runner failure.

## Findings

1. Direct execution of Python test modules can produce a false-positive when test functions are defined but no executable test entry point is invoked.
2. `unittest discover` is valid only when target files are actually discoverable by unittest (`TestCase` methods or equivalent supported structure).
3. P6 test selection must be deterministic; known target modules should not be hidden behind an unnecessarily broad wildcard when exact files are known.
4. A CI workflow mutation must preserve unrelated audit gates. A refactor that removes audit steps is a scope violation even if the targeted test is improved.
5. Governed execution ordering must be validated against the actual execution contract. A pre-write `read_current` safety check is not an accidental duplicate and must not be removed merely to satisfy an outdated expected sequence.
6. Relationship registry failures must distinguish missing data from an incorrect test expectation. `REL-003 | SRV-005 | ENG-004 | CONSUMES` was verified as present; duplicate insertion is prohibited.
7. Historical SHA evidence must not be blindly promoted to the current expected SHA. SHA mismatch requires baseline/reconciliation analysis before mutation.
8. `exit code 1` is only an execution failure signal, not the root cause. CI diagnostics must expose the first actionable failing test/error.
9. Missing workflow/status evidence is an evidence gap, never a PASS claim.

## New Mandatory Guardrails

- Every layered test module must be executable through a real test runner and discoverable as a test module.
- CI must use deterministic test selection for critical P1-P6 gates.
- Workflow changes must include a before/after gate inventory; unrelated gates must remain present unless explicitly authorized.
- Test failures must be classified as `RUNNER`, `LOGIC`, `DATA/GOVERNANCE`, `INTEGRITY/SHA`, or `WORKFLOW-SCOPE` before mutation.
- No expected hash may be updated without verifying why the actual file changed and recording the new baseline evidence.
- No relationship may be duplicated to silence a registry test.
- No PASS may be claimed without authoritative execution evidence.

## Current P6 Checkpoint

`d28f783b465a8964c061406677eb37089e34432e` is the current reconstruction point for the full audit workflow with deterministic P6 discovery.

Known repair already applied:
- P6 layered and reconciliation execution use explicit unittest discovery patterns.
- Full audit gates removed by an intermediate mutation were restored.
- ENG-006 sequence expectation was aligned with governed pre-write safety behavior.

## Verification Requirement

Before any further P6 mutation:

1. Obtain authoritative CI run/job evidence for the current checkpoint.
2. Capture the first failing test and full diagnostic context.
3. Verify that both P6 modules are discovered and executed.
4. Verify that unrelated audit gates remain present.
5. Only then mutate the specific failing layer.

## Closure Rule

P6 remains `UNDER VERIFICATION`. No global repository PASS is implied.

---

End of EJR-252
