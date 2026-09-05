# P12 Models Relationship/Content Transaction B — Unit 13 Release Compatibility Matrix

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Unit: `13 — Models ↔ Release compatibility`
State: `MATERIAL COMPLETE / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Entry evidence

- Unit-12 exact-head `2f5b91058af537d8a1cb6c3ffd950aab539d702d` passed all four required workflow families.
- Models status synchronization was applied and re-read at `ce12e2b3c557cff2ffeac95b7f22343c3d8b38c2` without dropping the stable historical-disposition or registry-open markers.
- `Release/VERSION.md` is authoritative for platform version dimensions: official release `1.0.0`, development baseline `3.2.1`.
- Current active Model artifacts carry independent artifact versions while aligning their development baseline to `3.2.1`.

## Material sequence

| Step | Surface | Action | Result |
|---|---|---|---|
| U13-1 | Models active set + Release/VERSION | direct compatibility review | no artifact/release dimension conflation found |
| U13-2 | `REP-014_PRIORITY12_MODELS_RELEASE_COMPATIBILITY_EVIDENCE_2026-09-05_K.tsv` | create bounded evidence | artifact version / baseline / release dimensions separated |
| U13-3 | `test_models_p12_release_compatibility.py` | add executable guard | prevents future release/baseline/version conflation and blind MOD-009 recreation |
| U13-4 | this Matrix | bind transaction evidence | exact-head validation pending |

## Semantic conclusion

`ARTIFACT_VERSION != DEVELOPMENT_BASELINE != OFFICIAL_RELEASE`.

Historical `MOD-009_VERSION_MODEL.md` is not recreated. No distinct Models-owned version responsibility or consumer gap is proven; current release/baseline authority remains with `Release/VERSION.md`.

This unit does not modify Release authority, promote Models, register REP-014 relationship IDs, or close Transaction B / Priority 12.

## Next boundary after exact-head success

`Specifications ↔ Models concrete authority/consumer reconciliation → safe canonical REP-014 write → final status/queue/closure review`.
