# Environment

This is a **secondary, analytical study** — no primary experiment, no released code. The authors did
not publish an analysis code repository (confirmed: no code-availability statement; verified
`sources.yaml` `code: []`, no GitHub/GitLab/Zenodo/OSF repository exists). The environment below is
what the paper states plus the verified data source.

- **Language/runtime**: R version 3.5.2 (used to produce the age-standardised prevalence/death/DALY
  plots and the SDI smoothing-spline analysis). No other language stated.
- **Framework**: Not specified in paper (plotting/statistics libraries not named). Underlying
  estimation is IHME's GBD pipeline software (DisMod-MR 2.1; MR-BRT), run by IHME, not by the authors.
- **Hardware**: n/a (analytical; not specified).
- **Data sources**:
  - **Global Burden of Disease (GBD) Study 2021** — the sole data source. Estimates for fatal and
    non-fatal outcomes and supplementary methodological details obtained from:
    - IHME GHDx GBD Results Tool — http://ghdx.healthdata.org/gbd-results-tool
    - GBD Compare / VizHub — https://vizhub.healthdata.org/gbd-compare/
  - **Access type**: OPEN (publicly available). Data-availability statement (verified via PMC
    PMC11868542 and confirmed in `sources.yaml`): "The data used for these analyses are all publicly
    available at http://ghdx.healthdata.org/gbd-results-tool."
  - **Identifier**: GBD 2021 (cause = "Alzheimer's disease and other dementias"; location = "North
    Africa and Middle East" region and its 21 constituent countries; years 1990–2021).
  - No NCT clinical-trial identifier, no PROSPERO registration, no data accession numbers apply
    (this is not a trial or a systematic review; verified `sources.yaml` `clinical_trials: []`).
  - See [../data/dataset.md](../data/dataset.md) for full provenance.
- **Key dependencies**: R 3.5.2; GBD 2021 GHDx exports. Upstream: DisMod-MR 2.1, MR-BRT (IHME).
- **Protocols**: No preregistration/PROSPERO. Ethics: reviewed and approved by the Ethics Committee
  of Shahid Beheshti University of Medical Sciences, Tehran, Iran
  (IR.SBMU.RETECH.REC.1403.067). Uses only publicly available, de-identified aggregate GBD estimates.
- **Random seeds**: Not specified in paper. (GBD uncertainty is via 1000 posterior draws; the 95% UI
  is the 2.5th–97.5th percentile of sorted draws — an upstream IHME procedure.)
- **Funding**: GBD study funded by the Bill & Melinda Gates Foundation (no role in this manuscript).
  This report funded by Shahid Beheshti University of Medical Sciences (Grant No. 43010066), with
  partial support from Tabriz University of Medical Sciences (Grant No. 75883).
- **Identifiers**: DOI 10.1038/s41598-025-89899-w; PMID 40016362; PMCID PMC11868542. Open access
  under CC BY-NC-ND 4.0.
