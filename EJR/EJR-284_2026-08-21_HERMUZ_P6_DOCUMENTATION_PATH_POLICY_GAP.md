# EJR-284 — HERMUZ P6 Documentation-Path Policy Gap

## Status
CLOSED — GOVERNANCE GAP DOCUMENTED / NO UNSAFE MUTATION

## Evidence
- Fresh current-HEAD validation: Run `32372278927`.
- Current-HEAD execution identity matched the validated commit `05ed5deb6c06aec54642719fb39d12dbf5ecb7bd`.
- Mutation Matrix regression passed; the historical `REP001-001` AssertionError did not recur.
- P6 correlation produced `PARTIAL` because `EJR/EJR-281_2026-08-20_HERMUZ_MUTATION_MATRIX_TITLE_COMPATIBILITY_FIX.md` was `UNMAPPED`.

## Finding
The current P6 implementation correlates changed paths using governed exact-path evidence. The repository does not currently contain an explicit authoritative policy stating whether documentation-only `EJR/*.md` paths must be mapped or explicitly excluded from impact correlation.

## Decision
Do not add a relationship or REP-020 mapping solely to convert `UNMAPPED`/`PARTIAL` into `MAPPED`/`PASS`. No relationship evidence was established for EJR-281, and REP-020 is not sufficient authority for inventing one.

## Boundary
This record documents a governance-policy gap. It does not authorize runtime changes, relationship promotion, or classifier changes.

## Next Safe Step
Resolve the documentation-path eligibility policy through canonical governance authority. Only after that decision may implementation or matrix mutation be considered.

## Learning
`UNMAPPED` is an observation from the correlation engine, not proof of a missing relationship. Detection, classification, authorization, and relationship proof remain separate gates.
