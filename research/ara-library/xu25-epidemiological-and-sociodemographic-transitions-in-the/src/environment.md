# Environment

This is a **GBD 2021 secondary statistical analysis** (descriptive tabulation, joinpoint regression, restricted cubic splines, quantile regression, and a comparative-risk-assessment risk-factor decomposition), **not a computational software release or wet-lab study**. There is no released code repository, no released dataset with accessions, and no registered clinical trial associated with this work (confirmed by `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`; and by the paper's own "Data availability" statement: "No datasets were generated or analysed during the current study"). Accordingly there is **no `src/execution/` code stub** — the statistical methodology is prose/formula-based and lives in `logic/solution/statistical_methods.md` (the joinpoint, RCS, quantile-regression, and PAF formulas are transcribed there as printed equations, per §Methods); no analysis script, notebook, or software package is published with or referenced by this paper, so manufacturing a code stub would only duplicate the formulas already captured in prose.

- **Language/runtime**: R, version 3.6.0 (§Methods "Statistical analysis": "The above statistical description and analyses were performed using the R program (Version 3.6.0)."). No specific R package names are stated in the main text.
- **Framework/methods**:
  - Joinpoint (segmented log-linear) regression for temporal trend estimation (APC/EAPC/AAPC).
  - Restricted cubic splines (4 knots) for the region-year SDI-burden association.
  - Quantile regression (5th/25th/50th/75th/95th percentiles) for the 204-country, 2021 cross-sectional SDI-burden association.
  - GBD comparative risk assessment (population attributable fraction) for risk-factor decomposition.
  - Full formula specifications: `logic/solution/statistical_methods.md`.
- **Hardware**: n/a (statistical analysis of aggregate estimates, not a computational pipeline with stated compute requirements).
- **Tools**: none named beyond the R runtime; no specific joinpoint-regression software package (e.g., NCI Joinpoint Regression Program) is named in the main text — not specified in paper.

## Data sources

- **Primary data source**: GBD 2021 estimates, queried from the Global Health Data Exchange (GHDx, http://ghdx.healthdata.org/) and the GBD Results Tool (http://ghdx.healthdata.org/gbd-results-tool). Access: open (public query tool); no unified dataset artifact is released by this paper itself.
- **Underlying GBD input sources** (per refs 15-16, described in more detail in the paper's own — unprovided — Supplementary Material): household surveys, censuses, hospital records, administrative records, vital statistics, verbal autopsies, and systematic literature search.
- **Risk-factor exposure/relative-risk data**: sourced from GBD 2021 Risk Factors Collaborators (ref 17), reusing that study's comparative-risk-assessment methodology and underlying exposure/RR estimates (not re-derived in this paper).
- **No accession identifiers**: no PROSPERO, NCT, GHDx query-string, or repository ID is stated in the paper's main text beyond the general GHDx/GBD-Results-Tool URLs above.

## Protocols
- No PROSPERO registration or other protocol pre-registration identifier appears anywhere in the paper's full text — not specified in paper.
- Ethical approval was deemed not applicable: "The list of all data sources used in GBD 2021 is publicly available at the Global Health Data Exchange website... therefore, ethical proof does not applicable to this study." (§Methods "Ethics statement"; repeated in §Declarations "Ethics approval and consent to participate").

## Code / Clinical trials
- **Code**: none (per `sources.yaml`). No GitHub/GitLab/Zenodo/OSF/Bitbucket repository referenced anywhere in the paper.
- **Clinical trials**: none (per `sources.yaml`). No NCT identifier; this is a GBD secondary analysis, not an interventional trial.

## Random seeds
- Not applicable (no released computational pipeline with stochastic components stated; joinpoint/RCS/quantile-regression fits are deterministic given the input GBD estimates).

## Funding
- National Natural Science Foundation of China [grant number 72204211]; the Natural Science Fund for Colleges and Universities in Jiangsu Province [grant number 22KJD310005]. "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript." (§Funding)
