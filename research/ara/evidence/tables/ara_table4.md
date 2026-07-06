# Table 4: Rigor Auditor effectiveness on the mutation benchmark

**Source**: Table 4, §7.5 (ARA-Native Review Systems — Level 2)
**Caption**: "Rigor Auditor effectiveness on the mutation benchmark (23 ARAs × 5 injection types). The auditor catches all high-severity structural anomalies but exhibits a systematic blind spot on orphan experiments."
**Screenshot**: ara_table4.png
**Extraction type**: raw_table

| Injection type | Expected severity | n | Detected |
|----------------|-------------------|---|----------|
| Fabricated claim | Critical | 23 | 23 (100%) |
| Rebutted-branch leak | Critical | 23 | 23 (100%) |
| Over-claim (scope) | Major | 23 | 23 (100%) |
| Missing falsification | Major | 23 | 21 (91%) |
| Orphan experiment | Minor | 23 | 5 (22%) |
| Overall | — | 115 | 95 (82.6%) |
