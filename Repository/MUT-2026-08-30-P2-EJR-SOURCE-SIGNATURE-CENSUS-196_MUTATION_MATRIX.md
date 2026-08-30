# MUTATION MATRIX — P2 EJR SOURCE-SIGNATURE CENSUS 196

Transaction ID: `MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Source head: `afe52f71cef0041e7f58218d6846f9182c868f83`
Prewrite heads: `9ee7028b868b896a86cf7784b51ec286a067fa5a`, `7ea957bddbe726d1dc29d2e517703b59c5e03509`
Functional head: `32021e605f5410de2a4833c73cbeca5350c1cbd6`
Source audit blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`
Source workflow blob: `27a2a9106c5adf80bfb0d04fed56b0e4b0414f18`
Candidate census blob: `c9b9d2a571ca7973af3774ac21604a8d7776d0a0`
Candidate test blob: `f7d2e7109f20798b1814be3ca9c3c4a48f0dfc42`
Candidate workflow blob: `4c99bb7188faeb0673b62512d92977bef7b84562`

| Change ID | Section | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 196-001 | companion census analyzer | ADD | deterministic source signatures from existing `ambiguous_duplicate_records` | Y | Y |
| 196-002 | EJR bounded census | ADD | EJR-only group/signature/cardinality counts without scanner allowlisting | Y | Y |
| 196-003 | companion tests | ADD | metadata-only, H1-only, mixed, unknown-source visibility, cardinality and immutability | Y | Y |
| 196-004 | Internal-ID workflow | UPDATE | trigger/run companion tests and emit/upload census JSON | Y | Y |
| 196-005 | internal-ID gate and membership | KEEP | scanner source, ambiguity membership and pass/fail semantics remain untouched | Y | Y |

## Functional verification

Exactly four functional paths changed and no unexpected paths were observed.

Exact-head runs at `32021e605f5410de2a4833c73cbeca5350c1cbd6`:

- Internal-ID `33315075640` — SUCCESS
- Full-Stack `33315075636` — SUCCESS
- Runtime/Integration `33315075614` — SUCCESS
- M2 `33315075651` — SUCCESS
- Real Matrix `33315075663` — SUCCESS

Census artifact `9733176940`, digest `sha256:1bd941ff549e22bc91a41adb836fc9ff770abdbdb0c9f30913a0ad61e2af047c`.

Observed EJR census: `121` ambiguous groups = `115 FIRST_H1_FALLBACK_ONLY` + `6 MIXED`; no metadata-only EJR ambiguity group. The mixed set is exactly `EJR-003`, `EJR-026`, `EJR-180`, `EJR-181`, `EJR-182`, `EJR-183`.

No EJR mutation, ambiguity suppression, REP-012/016/020 mutation, authority promotion, Priority-2 closure, Phase-1 closure, or Global PASS was authorized or performed.
