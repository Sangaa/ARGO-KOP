# MUT-2026-08-31-P2-EJR-235-DISPOSITION-AUTHORIZATION-268

Status: OPEN / AUTHORIZATION RECORDED / VERIFICATION PENDING
Scope: Disposition-only classification for the current two-member EJR-235 MEMORY_TO_ROOT group.
Opening main: `5110931da7780972b920a6bf35c211e204b04da7`
Pre-write Matrix268: `1b696932ba9643402ec3442a4f462266c08402a3`

## Evidence

Execution-verified Lease267 census established EJR-235 as `MEMORY_EJR → ROOT_EJR`, distinct content, zero external exact-ID references, and zero exact member-path references.

Direct readback and path history establish:
- `Memory/Engineering_Journal/EJR-235_2026-08-14_P53_SESSION_CLOSURE.md` is the earlier allocation, introduced by commit `7b7daffe7605950d3826975322236e7eca075574` at 2026-08-14T21:10:02Z.
- `EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md` is the later allocation, introduced by commit `9a3d2e314662cff7f9e7d6586c40bc6dc53f06ff` at 2026-08-17T16:26:49Z.

The two records have materially different session subjects and bodies. This is an identity collision, not duplicate content.

## Disposition

- RETAIN: Memory EJR-235 as the earlier valid identity allocation.
- DISPLACED: root EJR-235 as the later distinct allocation requiring a new identity.
- No current consumer rewrite obligation is established by the verified census.
- No replacement identity is selected here.

## Boundaries

This record authorizes disposition only. It does not authorize rename, content mutation, replacement-number allocation, vacancy claim, consumer rewrite, census-baseline change, or integrity promotion.

A separate successor lease must prove a candidate replacement identity vacant across complete reachable history before any repair is authorized.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Next safe step

After this authorization commit passes repository gates, close Lease268 and open a separate replacement-vacancy proof. Candidate selection must be re-derived from current state; apparent absence is not vacancy proof.