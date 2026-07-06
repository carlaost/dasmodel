# Library metrics — V2

Genre-aware, gates-vs-rankers, verified grounding. 16 ARAs.

## Genres

- `ahm26b-trends-and-disparities-in-alzheimer-disease` → **other** (code=False, open_data=True, trials=0)
- `aku25-population-attributable-fractions-associated-with-alzheimer` → **cohort_study** (code=False, open_data=False, trials=0)
- `ala26-trends-in-alzheimer-s-disease-mortality` → **other** (code=False, open_data=True, trials=0)
- `alb26-early-detection-of-alzheimer-s-disease` → **cohort_study** (code=False, open_data=True, trials=0)
- `als26-early-onset-alzheimer-s-disease-mortality` → **other** (code=False, open_data=True, trials=0)
- `che26-diagnostic-performance-of-plasma-p-tau217` → **meta_analysis** (code=False, open_data=True, trials=0)
- `cum26-alzheimer-s-disease-drug-development-pipeline` → **clinical_trial** (code=False, open_data=True, trials=8)
- `huu25-apoe-e4-alzheimer-s-risk-converges` → **single_cell_spatial** (code=True, open_data=True, trials=0)
- `jes26-efficacy-and-safety-of-donanemab-in` → **clinical_trial** (code=False, open_data=False, trials=1)
- `kes25-the-alzheimer-s-disease-diagnosis-and` → **clinical_trial** (code=False, open_data=False, trials=0)
- `pal25-alzheimer-s-association-clinical-practice-guideline` → **guideline** (code=False, open_data=False, trials=0)
- `sal25-trailblazer-alz-4-a-phase-3` → **clinical_trial** (code=False, open_data=False, trials=1)
- `sal26-plasma-emtbr-tau243-and-p-tau217` → **cohort_study** (code=False, open_data=False, trials=1)
- `the25-blood-phosphorylated-tau-for-the-diagnosis` → **meta_analysis** (code=False, open_data=False, trials=0)
- `tit26-automated-high-throughput-quantification-of-plasma` → **assay_method** (code=False, open_data=False, trials=0)
- `woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms` → **assay_method** (code=False, open_data=True, trials=0)

## Discrimination diagnostic (which rankers actually vary here)

| Ranker | n | mean | stdev | range | verdict |
|---|---|---|---|---|---|
| corrective_science_score | 16 | 3.312 | 3.386 | 12 | **discriminating** |
| dead_end_density | 16 | 0.101 | 0.1414 | 0.5 | **discriminating** |
| environment_completeness | 16 | 0.696 | 0.3842 | 1.0 | **discriminating** |
| executable_reproduction_L3 | 0 | — | — | — | insufficient_data |
| falsifiability_presence | 16 | 1.0 | 0.0 | 0.0 | **non_discriminating** |
| grounding_verified | 8 | 0.979 | 0.0375 | 0.095 | **low_variance** |
| negative_result_share | 16 | 0.078 | 0.1024 | 0.333 | **discriminating** |
| translation_trial_linkage | 16 | 0.688 | 1.9274 | 8 | **discriminating** |
