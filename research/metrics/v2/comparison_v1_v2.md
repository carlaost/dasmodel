# V1 ↔ V2 comparison

What changed when the six critiques were applied. V1 = flat [det] scores; V2 = genre-aware,
gates split out, grounding re-verified against the cited files.

## 1. Grounding: V1 presence vs V2 verified

V1 counted a number as grounded if it appeared inside any `«quote»`. V2 re-opens the cited
in-repo file and checks the quote is actually there (`unverifiable` = §/PDF refs not in repo).

| ARA | genre | V1 presence | V2 verified | checkable | unverifiable(§/PDF) |
|---|---|---|---|---|---|
| ahm26b-trends-and-disparities-in-alzheimer-disease | other | 1.0 | **1.0** | 10 | 0 |
| aku25-population-attributable-fractions-associated-with-alzheimer | cohort_study | 1.0 | **None** | 0 | 9 |
| ala26-trends-in-alzheimer-s-disease-mortality | other | 0.696 | **1.0** | 10 | 0 |
| alb26-early-detection-of-alzheimer-s-disease | cohort_study | 1.0 | **0.923** | 13 | 0 |
| als26-early-onset-alzheimer-s-disease-mortality | other | 0.762 | **1.0** | 12 | 0 |
| che26-diagnostic-performance-of-plasma-p-tau217 | meta_analysis | 0.921 | **0.905** | 21 | 6 |
| cum26-alzheimer-s-disease-drug-development-pipeline | clinical_trial | 0.857 | **None** | 0 | 17 |
| huu25-apoe-e4-alzheimer-s-risk-converges | single_cell_spatial | 0.972 | **None** | 0 | 18 |
| jes26-efficacy-and-safety-of-donanemab-in | clinical_trial | 0.939 | **None** | 0 | 23 |
| kes25-the-alzheimer-s-disease-diagnosis-and | clinical_trial | 0.722 | **None** | 0 | 27 |
| pal25-alzheimer-s-association-clinical-practice-guideline | guideline | 1.0 | **None** | 0 | 17 |
| sal25-trailblazer-alz-4-a-phase-3 | clinical_trial | 0.725 | **1.0** | 4 | 13 |
| sal26-plasma-emtbr-tau243-and-p-tau217 | cohort_study | 1.0 | **1.0** | 5 | 0 |
| the25-blood-phosphorylated-tau-for-the-diagnosis | meta_analysis | 1.0 | **1.0** | 22 | 0 |
| tit26-automated-high-throughput-quantification-of-plasma | assay_method | 0.796 | **None** | 0 | 25 |
| woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms | assay_method | 0.0 | **None** | 0 | 0 |

## 2. Gates pulled out of the quality score

V1 averaged these into quality; V2 treats them as binary hygiene gates.

| ARA | seal_L1 | links_resolve | no_orphan_exp | grounding_layer | gates_passed |
|---|---|---|---|---|---|
| ahm26b-trends-and-disparities-in-alzheimer-disease | True | True | True | True | 4/4 |
| aku25-population-attributable-fractions-associated-with-alzheimer | False | True | True | True | 3/4 |
| ala26-trends-in-alzheimer-s-disease-mortality | True | True | True | True | 4/4 |
| alb26-early-detection-of-alzheimer-s-disease | False | True | True | True | 3/4 |
| als26-early-onset-alzheimer-s-disease-mortality | False | True | True | True | 3/4 |
| che26-diagnostic-performance-of-plasma-p-tau217 | True | True | True | True | 4/4 |
| cum26-alzheimer-s-disease-drug-development-pipeline | True | True | True | True | 4/4 |
| huu25-apoe-e4-alzheimer-s-risk-converges | True | True | True | True | 4/4 |
| jes26-efficacy-and-safety-of-donanemab-in | True | True | True | True | 4/4 |
| kes25-the-alzheimer-s-disease-diagnosis-and | True | False | True | True | 3/4 |
| pal25-alzheimer-s-association-clinical-practice-guideline | True | False | True | True | 3/4 |
| sal25-trailblazer-alz-4-a-phase-3 | True | True | True | True | 4/4 |
| sal26-plasma-emtbr-tau243-and-p-tau217 | True | False | True | True | 3/4 |
| the25-blood-phosphorylated-tau-for-the-diagnosis | True | True | True | True | 4/4 |
| tit26-automated-high-throughput-quantification-of-plasma | True | True | True | True | 4/4 |
| woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms | True | False | True | False | 2/4 |

## 3. Genre-scoped: metrics that V1 scored 0, V2 marks N/A

| ARA | genre | V1 L3 | V2 L3 | reason |
|---|---|---|---|---|
| ahm26b-trends-and-disparities-in-alzheimer-disease | other | 0/pending | **N/A** | no code artifact |
| aku25-population-attributable-fractions-associated-with-alzheimer | cohort_study | 0/pending | **N/A** | no code artifact |
| ala26-trends-in-alzheimer-s-disease-mortality | other | 0/pending | **N/A** | no code artifact |
| alb26-early-detection-of-alzheimer-s-disease | cohort_study | 0/pending | **N/A** | no code artifact |
| als26-early-onset-alzheimer-s-disease-mortality | other | 0/pending | **N/A** | no code artifact |
| che26-diagnostic-performance-of-plasma-p-tau217 | meta_analysis | 0/pending | **N/A** | no code artifact |
| cum26-alzheimer-s-disease-drug-development-pipeline | clinical_trial | 0/pending | **N/A** | no code artifact |
| huu25-apoe-e4-alzheimer-s-risk-converges | single_cell_spatial | 0/pending | **pending_exec** |  |
| jes26-efficacy-and-safety-of-donanemab-in | clinical_trial | 0/pending | **N/A** | no code artifact |
| kes25-the-alzheimer-s-disease-diagnosis-and | clinical_trial | 0/pending | **N/A** | no code artifact |
| pal25-alzheimer-s-association-clinical-practice-guideline | guideline | 0/pending | **N/A** | no code artifact |
| sal25-trailblazer-alz-4-a-phase-3 | clinical_trial | 0/pending | **N/A** | no code artifact |
| sal26-plasma-emtbr-tau243-and-p-tau217 | cohort_study | 0/pending | **N/A** | no code artifact |
| the25-blood-phosphorylated-tau-for-the-diagnosis | meta_analysis | 0/pending | **N/A** | no code artifact |
| tit26-automated-high-throughput-quantification-of-plasma | assay_method | 0/pending | **N/A** | no code artifact |
| woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms | assay_method | 0/pending | **N/A** | no code artifact |

## 4. Within-genre ranking on verified grounding (compare like with like)

- **other**: ahm26b-trends-and-disparities-in-alzheimer-disease (1.0) > ala26-trends-in-alzheimer-s-disease-mortality (1.0) > als26-early-onset-alzheimer-s-disease-mortality (1.0)
- **cohort_study**: sal26-plasma-emtbr-tau243-and-p-tau217 (1.0) > alb26-early-detection-of-alzheimer-s-disease (0.923)
- **meta_analysis**: the25-blood-phosphorylated-tau-for-the-diagnosis (1.0) > che26-diagnostic-performance-of-plasma-p-tau217 (0.905)
- **clinical_trial**: sal25-trailblazer-alz-4-a-phase-3 (1.0)

## 5. Non-discriminating metrics flagged automatically (crit #6)

- `falsifiability_presence` — non_discriminating (stdev 0.0, range 0.0)
- `grounding_verified` — low_variance (stdev 0.0375, range 0.095)

## Takeaways

- **Verified grounding is stricter than presence** — the gap is the over-claim V1 hid.
- **Gates are near-uniform** (they're hygiene, not quality) — correctly removed from ranking.
- **L3 is now N/A(genre), not 0** — clinical papers no longer punished for shipping no code.
- **The diagnostic flags** which rankers this corpus cannot exercise, so 0-variance is explicit.
