# Study Design (Post-hoc Analysis of TRAILBLAZER-ALZ 2)

## Underlying trial
- **Trial**: TRAILBLAZER-ALZ 2, phase 3, randomised, double-blind, multicentre, placebo-controlled (NCT04437511; sponsor Eli Lilly and Company). Assessed donanemab for early symptomatic AD (mild cognitive impairment or mild dementia due to AD) over 76 weeks. Primary report: Sims et al. 2023 [2].
- **Drug**: Donanemab — monoclonal antibody against a form of β-amyloid present only in brain amyloid plaques.
- **Randomised total**: 1736 participants in the 76-week placebo-controlled period; 1447 were APOE ε4 non-homozygotes.
- **Treatment course completion**: Amyloid-based criteria; on success, participants were switched (blinded) to placebo (limited-duration dosing).

## Analysis populations
- **EU-indicated population**: APOE ε4 non-carriers or heterozygotes (non-homozygotes). Reported in the Supplement.
- **EU-eligible population** (primary focus): EU-indicated minus baseline superficial siderosis, anticoagulant use, or uncontrolled hypertension. Placebo N=604, Donanemab N=614 (Table 1). Safety analysis N: placebo 603, donanemab 609 (Table 4).
- **Low-medium tau subpopulation**: Defined by ¹⁸F-flortaucipir PET (per Sims et al. [2]); analysed for time-saved.

## Placebo-controlled-period analyses (76 weeks)
- **Clinical outcomes**: iADRS, CDR-SB (+6 domains), ADAS-Cog13, ADCS-iADL, MMSE via MMRM with conservative hybrid J2R/CIR imputation (and original no-imputation methodology for comparison). See `statistical_methods.md`.
- **Progression**: CDR-G analysed via Cox proportional hazards (next-stage progression; progression to CDR-G ≥2).
- **Disease stabilisation**: Proportion with no CDR-SB progression (CFB ≤0) at 52/76 weeks via generalized mixed model.
- **Time saved**: Time-progression model for repeated measures (CDR-SB), overall and low-medium tau.
- **Biomarkers**: Amyloid PET (Centiloids), amyloid clearance (<24.1 CL) at weeks 24/52/76, plasma P-tau217, via MMRM.
- **Safety**: Descriptive summaries in all drug-exposed participants (TEAEs, deaths, SAEs, discontinuations, ARIA-E/H, IRR, radiographic severity).

## Long-term extension (LTE)
- **Design**: 78-week blinded extension (154 weeks total) for participants completing the placebo-controlled period; no internal placebo comparator.
- **Groups**: Early-start (randomised donanemab) vs delayed-start (randomised placebo, donanemab initiated in the LTE).
- **Comparator**: Propensity-weighted external control drawn from ADNI, balancing baseline disease characteristics (per Zimmer et al. [7]). Hybrid J2R/CIR imputation NOT applied (incompatible with propensity reweighting). EU-eligible weighting infeasible (contraindication variables absent from ADNI) — LTE used the non-homozygote population.
- **Endpoints reported here (narratively; full data in Supplement/[7])**: Increasing treatment effect over 154 weeks; early-start 29% lower next-stage progression risk than delayed-start (CDR-G); maintained amyloid clearance after treatment completion; safety consistent with the established profile.

## Data provenance and software
- Trial IPD available on request via Vivli (see `src/environment.md`, `data/dataset.md`). External control from ADNI (adni.loni.usc.edu).
- Most analyses in SAS v9.4; some time-based progression analyses in R v4.3.0.
- All analyses post-hoc, exploratory, not controlled for multiplicity.
