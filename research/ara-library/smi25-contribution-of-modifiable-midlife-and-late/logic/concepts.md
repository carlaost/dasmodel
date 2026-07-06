# Concepts

> Grounding: abstract-only. Definitions are constrained to what the abstract/metadata provide.

## Modifiable vascular risk factors
- **Notation**: —
- **Definition**: The exposure group consisting of hypertension, diabetes, and current smoking as defined in the abstract.
- **Boundary conditions**: Applies to the ARIC age-window analyses described in the abstract; other risk factors are not available from provided input.
- **Related concepts**: Hypertension, Diabetes, Current smoking, Population attributable fraction

## Hypertension
- **Notation**: BP
- **Definition**: Systolic BP >=130 mm Hg, diastolic BP >=80 mm Hg, or use of medication for BP.
- **Boundary conditions**: Abstract definition only; measurement protocol and repeated-measure handling are not available from provided input.
- **Related concepts**: Modifiable vascular risk factors, Blood pressure

## Diabetes
- **Notation**: —
- **Definition**: Fasting glucose >=126 mg/dL, nonfasting glucose >=200 mg/dL, self-reported physician's diagnosis, or use of any diabetes medication.
- **Boundary conditions**: Abstract definition only; laboratory protocols and medication classification details are not available from provided input.
- **Related concepts**: Modifiable vascular risk factors, Glucose

## Current smoking
- **Notation**: —
- **Definition**: Self-reported current smoking status.
- **Boundary conditions**: Abstract definition only; pack-years, former smoking, or validation details are not available from provided input.
- **Related concepts**: Modifiable vascular risk factors

## Incident dementia
- **Notation**: —
- **Definition**: Main outcome measured in the study, with analyses for dementia by age 80 years and separately after age 80 years.
- **Boundary conditions**: Diagnostic ascertainment method and adjudication details are not available from provided input.
- **Related concepts**: Population attributable fraction, ARIC

## Population attributable fraction
- **Notation**: PAF
- **Definition**: The estimated proportion of incident dementia attributable to having at least one vascular risk factor by age at risk factor measurement.
- **Boundary conditions**: Estimated by age 80 years and separately after 80 years; exact statistical formula and covariates are not available from provided input.
- **Related concepts**: Incident dementia, Modifiable vascular risk factors

## Age at risk factor measurement
- **Notation**: —
- **Definition**: Study baseline defined by age when risk factors were measured: 45-54 years, 55-64 years, and 65-74 years.
- **Boundary conditions**: The abstract includes an apparent omission in "age 45 to years"; the intended window is elsewhere stated as 45-54 years.
- **Related concepts**: Midlife, Late life, Population attributable fraction

## APOE e4 genotype
- **Notation**: APOE e4
- **Definition**: A subgrouping variable used to examine differences in attributable fractions, specifically noting higher fractions in noncarriers at age 55 years and older.
- **Boundary conditions**: Genotyping method, carrier definition, and subgroup denominators are not available from provided input.
- **Related concepts**: Subgroup analysis, Population attributable fraction
