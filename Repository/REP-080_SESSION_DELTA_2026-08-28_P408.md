# P408 — Authorization ID Boundary Observation

Date: 2026-08-28
Status: `CLOSED / SOURCE-VERIFIED / EXECUTION-PENDING / CALLER-UNPROVEN / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Reviewed P407 and prior learning before mutation. Applied exact-head attribution, NO RUN != PASS, repair-only-on-observed-failure, and the prohibition on manufacturing authorization/provenance.

## FINDING
A current governed integration path already exists from the cognitive-loop prototype through an explicit human authorization gate. The prototype returns `authorization.status = AUTHORIZED` when approved, but its authorization object contains only status/approved fields and does not provide an `authorization_id`.

The RUN-010 handoff contract explicitly requires an `authorization_id` and fails closed when it is absent. Therefore the existing prototype authorization is evidence of authorization-state behavior, but it is not a sufficient source of execution authorization identity for the production handoff contract.

## MUTATION
Added one isolated negative integration test proving this boundary. It verifies:
1. prototype approval reaches `AUTHORIZED`;
2. no `authorization_id` is produced by that prototype path;
3. execution remains non-executing;
4. the RUN-010 handoff contract rejects the authorization object with `HANDOFF_AUTHORIZATION_ID_REQUIRED`.

Added a prewrite Mutation Matrix for the test-only change.

## DECISION
This closes an ambiguity: an existing authorization gate was identified, but it is not the required governed authorization source for ENG-006 handoff because it lacks execution authorization identity. No caller was invented and no runtime wiring was changed.

The correct next construction question is not "how to fabricate an authorization_id"; it is whether ARGO has an existing governed authorization record/service that owns issuance and identity of execution authorization. If none exists, the project needs an explicitly authorized design decision before creating one.

## EVIDENCE STATE
- Existing authorization gate: `PROVEN`
- Authorization identity source suitable for production handoff: `UNPROVEN`
- RUN-010 caller reachability: `UNPROVEN`
- Isolated negative boundary test: `SOURCE-VERIFIED`
- Exact-head CI: `PENDING`
- Production side effects: `NOT AUTHORIZED`
- Canonical promotion: `NOT JUSTIFIED`

## LEARNING DISPOSITION
No new learning claimed. This is an application of existing boundaries: authorization state is not equivalent to authorization identity; a downstream contract requirement cannot be satisfied by inference.

## CHECKPOINT
`P408 -> exact-head CI -> identify governed authorization identity owner -> only then evaluate caller construction`

## CLOSE
`CLOSED / SOURCE-VERIFIED / EXECUTION-PENDING / AUTHORIZATION-ID-SOURCE-UNPROVEN / NO RUNTIME MUTATION / NO PROMOTION`
