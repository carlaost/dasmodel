# Environment

This is a **clinical-trial long-term extension (LTE) report** — an analytical study of existing
trial and external-cohort data. There is no released code repository, no data-availability/IPD-
sharing statement, and no code-availability statement in this paper's text (verified by full-text
search of the retrieved PDF for "SAS", "R version", "R package", "code availab", "data availab",
"repository", "GitHub", "Vivli", "IPD" — only "WeightIt R package" and the publisher name
"Elsevier Masson SAS" matched, the latter a false positive). No concrete code artifact exists to
capture in `src/execution/`.

- **Language/runtime**: Statistical software only. The propensity-score weighting uses the
  **WeightIt R package** (inverse probability weighting, generalized linear model, ATT estimand);
  no R or WeightIt version is stated in the paper. No other software/version is named for the
  MMRM, Cox proportional hazards, or AUC/time-progression analyses.
- **Framework**: Standard statistical procedures — mixed model for repeated measures (MMRM), Cox
  proportional hazards model, propensity score weighting (WeightIt), AUC / time-progression
  back-calculation, observation-time-adjusted incidence rate (OAIR) computation. No public
  analysis scripts released.
- **Hardware**: n/a (analytical work).
- **Data sources**:
  - **TRAILBLAZER-ALZ 2 individual participant data** (NCT04437511; sponsor Eli Lilly and
    Company, per the "Declaration of interest" section — all listed authors report employment
    with Eli Lilly and Company). No data-sharing/access statement is present in this paper (the
    companion post-hoc EU-eligible-population analysis by Jessen et al. [10.1016/j.tjpad.2026.100605]
    states IPD is available on request via Vivli for this same underlying trial, but that
    statement does not appear in this paper's own text).
  - **ADNI** (Alzheimer's Disease Neuroimaging Initiative; adni.loni.usc.edu) — external
    comparison cohort for the LTE efficacy analyses (propensity-weighted). Launched 2003 as a
    public-private partnership (PI Michael W. Weiner, MD); funded by the National Institute on
    Aging (NIH Grant U19AG024904), with historical contributions from NIBIB, the Canadian
    Institutes of Health Research, and numerous private-sector partners via the Foundation for
    the National Institutes of Health (listed in full in the paper's Acknowledgements). Access is
    via ADNI's standard data-application process (adni.loni.usc.edu).
  - Reaccumulation-rate modeling additionally draws on three earlier donanemab studies: a
    phase 1b study (NCT02624778), TRAILBLAZER-ALZ (phase 2; NCT03367403), and TRAILBLAZER-EXT
    (phase 2 LTE parts B and C; NCT04640077).
- **Key dependencies**: WeightIt (R); no versions specified for any statistical software in this
  paper.
- **Protocols**: TRAILBLAZER-ALZ 2 phase 3 protocol (NCT04437511); "all procedures were performed
  in compliance with relevant laws and institutional guidelines and have been approved by the
  appropriate institutional committees;" written informed consent from participants and study
  partners (§2.1). All statistical analyses are exploratory and not controlled for multiplicity
  (§2.5).
- **Random seeds**: Not specified in paper.
- **Generative AI disclosure**: The paper states "No generative AI or AI-assisted technologies
  were used in the preparation of this manuscript."

## Underlying clinical trial (grounded, cross-checked against the paper's own text)
- **NCT**: NCT04437511
- **Title** (per ClinicalTrials.gov): "A Study of Donanemab (LY3002813) in Participants With
  Early Alzheimer's Disease (TRAILBLAZER-ALZ 2)"
- **Phase**: PHASE3 (per the paper: "76-week, phase 3, randomized, double-blind, parallel-group,
  multicenter, placebo-controlled trial", §2.1)
- **Sponsor**: Eli Lilly and Company (per the paper's Funding and Declaration of interest
  sections: "This study was funded by Eli Lilly and Company")
- **Additional NCTs referenced for the reaccumulation model**: NCT02624778 (phase 1b),
  NCT03367403 (TRAILBLAZER-ALZ, phase 2), NCT04640077 (TRAILBLAZER-EXT, phase 2 LTE parts B/C)
- **Source**: Cross-referenced against §2.1 Trial design and §2.5.2 Biomarkers of `paper.pdf`
  (`paper.pdf` p2, p4).
