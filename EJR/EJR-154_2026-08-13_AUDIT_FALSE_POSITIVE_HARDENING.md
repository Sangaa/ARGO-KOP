# EJR-154 — Audit False-Positive Hardening

Date: 2026-08-13

## Trigger

The first real repository-wide audit execution completed successfully and produced 79 candidates across 695 files. Manual inspection of the evidence showed that the reference extractor was interpreting Markdown-like text embedded inside Python test strings as real references, and was also treating ordinary prose containing path-like tokens as references.

## Correction

- Markdown references are now extracted only from actual Markdown link syntax.
- Python references are extracted from the Python AST import nodes rather than generic text patterns.
- Existing path normalization remains responsible for local target resolution.
- Candidate findings remain non-architectural evidence until independently verified.

## Verified regression intent

The test suite now explicitly proves that a Python string such as `[B](B.md)` does not become a repository broken-reference finding, while real Markdown links and syntactic Python imports remain discoverable.

## Next step

Wait for CI on the hardened audit engine, then rerun the repository-wide audit. Compare the new GAP Map against the first 79-candidate baseline and independently verify the remaining negative findings before any architectural repair or Motor Gate decision.

## Session-safe resume

If the session ends now, resume from commit `d0631ea8b670df8b8c52dcb291f442d4bcaeb807`, inspect its CI run, then inspect the next Full-Stack Repository Audit artifact. Do not reuse the 79-candidate baseline as a final GAP list.
