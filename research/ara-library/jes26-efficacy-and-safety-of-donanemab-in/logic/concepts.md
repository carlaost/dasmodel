# Concepts

## EU-indicated population
- **Notation**: —
- **Definition**: The subset of TRAILBLAZER-ALZ 2 participants matching the EU marketing authorisation: adults with early symptomatic AD who are APOE ε4 non-carriers or heterozygotes (i.e., APOE ε4 non-homozygotes).
- **Boundary conditions**: Defined by APOE genotype only; does not apply the additional EU clinical contraindications.
- **Related concepts**: EU-eligible population, APOE ε4

## EU-eligible population
- **Notation**: —
- **Definition**: The EU-indicated population further excluding, at baseline, participants with superficial siderosis, concomitant anticoagulant use, or uncontrolled hypertension (defined here as seated systolic BP ≥140 mmHg and diastolic BP ≥90 mmHg). Represents patients expected to be treated in European clinical practice.
- **Boundary conditions**: Post-hoc, retrospectively defined from baseline covariates; an EU-eligible external control could not be built for the LTE because siderosis, anticoagulant use, and BP were not collected in ADNI.
- **Related concepts**: EU-indicated population, APOE ε4, superficial siderosis

## APOE ε4 carrier status (non-carrier / heterozygote / homozygote)
- **Notation**: ε4/ε4 (homozygote), ε3/ε4 or ε2/ε4 (heterozygote), non-carrier (no ε4 allele)
- **Definition**: Apolipoprotein E ε4 allele count. Donanemab's EU/UK indication covers non-carriers and heterozygotes only; ε4 homozygotes are excluded because ARIA risk rises with ε4 allele count.
- **Boundary conditions**: Homozygotes (ε4/ε4) are absent from these analyses by design.
- **Related concepts**: ARIA, EU-indicated population

## Conservative hybrid imputation (J2R/CIR)
- **Notation**: J2R / CIR
- **Definition**: The EMA-required missing-data handling method for clinical-scale efficacy: jump-to-reference (J2R) for values missing due to serious, severe, or symptomatic ARIA or death, and copy increment reference (CIR) for all other missing causes. Both derive imputed values from the reference (placebo) cohort, minimising treatment-effect differences and thus more conservative than no imputation.
- **Boundary conditions**: Applied to placebo-controlled-period clinical scales; NOT applied to LTE analyses (incompatible with propensity reweighting). Also used for amyloid CFB (Table 3).
- **Related concepts**: Jump-to-reference, copy increment reference, MMRM

## Jump-to-reference (J2R)
- **Notation**: J2R
- **Definition**: Imputation replacing a missing value with the reference (placebo) cohort value at that timepoint.
- **Boundary conditions**: Used for missingness due to serious/severe/symptomatic ARIA or death.
- **Related concepts**: Copy increment reference, conservative hybrid imputation

## Copy increment reference (CIR)
- **Notation**: CIR
- **Definition**: Imputation replacing a missing value with a value estimated to reflect the observed change-over-time trend in the reference (placebo) arm.
- **Boundary conditions**: Used for missingness due to all causes other than serious/severe/symptomatic ARIA or death.
- **Related concepts**: Jump-to-reference, conservative hybrid imputation

## Percent slowing
- **Notation**: —
- **Definition**: The adjusted mean change-from-baseline treatment difference at 76 weeks divided by the adjusted mean change-from-baseline with placebo at 76 weeks, times 100; 95% CIs estimated using the Delta method.
- **Boundary conditions**: Interpreted relative to the clinically relevant scale range, not the full theoretical range (see iADRS restricted-range discussion).
- **Related concepts**: iADRS, CDR-SB, MMRM

## Amyloid-related imaging abnormalities (ARIA-E, ARIA-H)
- **Notation**: ARIA, ARIA-E, ARIA-H
- **Definition**: Treatment-related imaging findings with amyloid-targeting therapies: ARIA-E is edema/effusion; ARIA-H is microhemorrhages and hemosiderin deposits (including superficial siderosis). Classified by seriousness, symptomatic status, and maximum radiographic severity (mild/moderate/severe); detected by MRI or TEAE cluster.
- **Boundary conditions**: Risk increases with APOE ε4 allele count; isolated ARIA-H = no concurrent ARIA-E in the same analysis period.
- **Related concepts**: APOE ε4, superficial siderosis, infusion-related reaction

## Amyloid clearance / Centiloids
- **Notation**: CL
- **Definition**: Amyloid plaque burden measured by amyloid PET on the Centiloid (CL) scale; amyloid clearance is defined as achieving a plaque level <24.1 CL.
- **Boundary conditions**: Clearance percentages computed with Wilson score CIs; one-sample frequency test used for the null of 0% negative.
- **Related concepts**: Amyloid PET, P-tau217

## Clinical outcome scales (iADRS, CDR-SB, CDR-G, ADAS-Cog13, ADCS-iADL, MMSE)
- **Notation**: —
- **Definition**: iADRS (integrated AD Rating Scale, 0–144, lower = worse); CDR-SB (Clinical Dementia Rating–Sum of Boxes, 0–18, higher = worse); CDR-G (CDR–Global, 0–3, higher = worse, staging); ADAS-Cog13 (0–85, higher = worse); ADCS-iADL (0–59, lower = worse); MMSE (0–30, lower = worse).
- **Boundary conditions**: For most EU-eligible participants, baseline iADRS clustered in a ~36-point band (85–121), so treatment effects should be interpreted against the relevant range, not 0–144.
- **Related concepts**: Percent slowing, time saved

## Treatment course completion criteria
- **Notation**: —
- **Definition**: Amyloid-based criteria in TRAILBLAZER-ALZ 2 that, once met, triggered a blinded switch of the participant to placebo (limited-duration dosing). Participants met these criteria by 24, 52, or 76 weeks.
- **Boundary conditions**: 74.8% of early-start LTE participants received placebo for the entirety of the LTE after completion.
- **Related concepts**: LTE, early-start, delayed-start, amyloid clearance

## Long-term extension (LTE) with early-start / delayed-start groups
- **Notation**: —
- **Definition**: A 78-week blinded extension of TRAILBLAZER-ALZ 2. Early-start = randomised to donanemab in the placebo-controlled period; delayed-start = randomised to placebo, with donanemab initiated during the LTE. Efficacy assessed vs a propensity-weighted ADNI external control (no internal placebo).
- **Boundary conditions**: Total follow-up 154 weeks; hybrid imputation not applied; early-vs-delayed comparison confounded by baseline severity differences and unequal exposure.
- **Related concepts**: Propensity score weighting, ADNI external control, treatment course completion criteria

## Propensity score weighting / ADNI external control
- **Notation**: —
- **Definition**: A method reweighting so that baseline disease characteristics of TRAILBLAZER-ALZ 2 arms are balanced against an untreated external comparison cohort drawn from the Alzheimer's Disease Neuroimaging Initiative (ADNI), used because the LTE had no internal placebo.
- **Boundary conditions**: Cannot be combined with J2R/CIR imputation; EU-eligible weighting infeasible (contraindication variables absent from ADNI); external cohort may differ in study conduct, era, and geography.
- **Related concepts**: LTE, conservative hybrid imputation

## Time saved (time-progression model)
- **Notation**: —
- **Definition**: The estimated additional time it would take the placebo arm to reach the same CDR-SB change observed in the donanemab arm at the end of the placebo-controlled period, from a time-progression model for repeated measures.
- **Boundary conditions**: Reported for the EU-eligible overall and low-medium tau populations under hybrid imputation.
- **Related concepts**: CDR-SB, percent slowing
