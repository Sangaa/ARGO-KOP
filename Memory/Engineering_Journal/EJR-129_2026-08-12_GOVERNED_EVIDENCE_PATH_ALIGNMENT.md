# EJR-129 — Governed Evidence Path Alignment

Date: 2026-08-12
Status: Implemented / Awaiting CI evidence

## Finding

The end-to-end runtime-to-registry test used a relative trace path beginning with `evidence/runtime/...` while the repository evidence capture boundary already prefixes the governed root `Quality/Integration/evidence/runtime/`.

That combination could produce a doubled path in the integration proof. The production capture boundary itself was correct; the test was describing the target incorrectly.

## Correction

The integration test now calls `capture_repository_evidence(..., relative_name="execution_trace.json")` and consumes the returned canonical repository-relative path. The expected path is explicitly asserted as:

`Quality/Integration/evidence/runtime/execution_trace.json`

The registry candidate now uses that exact returned path.

## Why This Matters

This is a small correction with high value because the test must prove the same governed boundary used by the capture implementation. A passing test against a mismatched path would weaken confidence in the Seam.

The lesson is retained as engineering evidence:

> When a boundary owns path composition, callers must provide only the boundary-relative name and verify the returned canonical path.

## Scope

No new persistence layer was added. No canonical Memory mutation was introduced. No Seam was promoted solely because of this correction.

## Next

Run CI. If green, inspect the resulting artifact and execute the canonical audit before promoting the first repository-backed Seam. If red, use the failure as the next evidence-driven correction.
