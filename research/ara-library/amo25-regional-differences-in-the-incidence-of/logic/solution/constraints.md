# Constraints, Assumptions, and Limitations

## Boundary conditions
- Single state (South Carolina), single calendar year of diagnosis (2021).
- Population restricted to registrants aged 50–110 years; younger/older records excluded.
- Four public health regions (Low Country, Midlands, Pee Dee, Upstate) as the geographic unit.
- Cases and rates derive from *diagnosed and registered* ADRD; the SCADR is a registry, not a population census of disease.

## Assumptions
- A1: SCADR 2021 records validly represent new (incident) ADRD diagnoses; physician/neurologist ICD-10-CM coding is accurate.
- A2: ACRPE population estimates are valid denominators; the 2020 US census is an appropriate standard population for age adjustment.
- A3: The natural-log-population offset correctly accounts for differing PHR population sizes so IRRs are comparable.
- A4: Missing-region cases (n = 3,910) can be handled via proportional-redistribution and extreme-case sensitivity analyses without invalidating primary estimates.

## Known limitations (stated by the authors)
- **No individual-level risk factors measured**: did not assess vascular factors within PHRs, nor education, lifestyle (smoking, alcohol use), environmental pollution, or sleep patterns; cannot relate these to ADRD incidence per PHR.
- **Registry-inherent bias**: cannot rule out underreporting, underdiagnosis, or missing county/zip and measurement errors, which may bias estimates.
- **COVID-19 context**: study conducted after the SC COVID-19 lockdown; potential (unquantified) effect on ADRD case reporting.
- **Diagnosed-population scope**: retrospective cohort based on individuals diagnosed and reported in the SCADR; incidence estimates may not fully capture the true ADRD burden in the entire SC population.
- **Residual confounding**: registry data limit ability to control for all potential confounders; residual confounding cannot be ruled out.
- **No causal inference**: observational design; associations only — "not intended to establish causal associations."

## Internal source discrepancies (reproduced verbatim, not corrected)
- Figure 1 region/disposition boxes sum to 18,755, not the stated analytic N = 18,955 (200 short).
- Table 2, VaD "Low Country vs. Upstate" CI printed "(0.94–0.850)" (lower bound exceeds upper bound); AD "Pee Dee vs. Upstate" p printed "<0.0002".
- Age-specific prose vs Table 3: Discussion's "<65 AD/VaD/Mixed highest in Pee Dee" contradicts Table 3 (Upstate highest for AD, Mixed among <65); 75–84 "Midlands lowest across all types" is inexact for AD and Other (Low Country lower). See claims.md C05 and evidence/tables/table3.md.

## Strengths (stated)
- SCADR is relatively large and representative (vs CDC and National Alzheimer's Association reports).
- Log-population offset enables valid comparison across differently sized PHRs.
- Sensitivity analyses demonstrate robustness of PHR estimates under differing missing-data assumptions.
