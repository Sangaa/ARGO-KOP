# EJR-148 — Full-Stack GAP MAP Hardening

## Scope
Harden the repository-wide audit so detected broken local references are promoted into the actionable GAP MAP instead of remaining only in raw audit output.

## Change
- `Quality/Integration/full_stack_audit_report.py` now classifies `broken_reference_candidates` as `BROKEN_REFERENCE` with `HIGH` severity.
- `Quality/Integration/test_full_stack_audit_report.py` adds regression coverage for a missing local Markdown target.

## Evidence discipline
A broken-reference candidate is a discovery finding, not proof of architectural invalidity. Architectural review remains required before deletion, replacement, or redesign.

## Validation
CI must validate this change before the finding is treated as part of the verified baseline.

## Next target
Run the repository-wide audit on current contents, independently recheck material absence findings, then use the resulting GAP MAP to determine the exact Motor Gate boundary.

## Session-safe checkpoint
This task is independently closable: source mutation, regression coverage, and journal entry are all committed before moving to the next task.
