# Environment

This is a **systematic literature review** — an analytical work. The review team ran no model
training, produced no code, and released no dataset. There is therefore no runnable artifact to
capture in `src/` (a lone `environment.md` is the correct, complete `src/` layer here).

- **Language/runtime**: analytical — none (no code produced by the review team).
- **Framework**: not applicable. (The review *reports on* frameworks used by the 68 reviewed studies — see evidence/tables/table6.md and evidence/figures/figure42.md: PyTorch 35, TensorFlow 13, Keras 2, MATLAB 2, Theano 2, AWS SageMaker 1, Not reported 19.)
- **Hardware**: n/a (no experiments run by the review team).
- **Key dependencies**: n/a.
- **Random seeds**: n/a.
- **Protocols**: PRISMA 2020 [60]; methodological review framework [59]. No PROSPERO registration ID reported. Two independent reviewers with consensus adjudication. Search executed 20 February 2025 across five databases (Scopus, Web of Science, ScienceDirect, IEEE Xplore, PubMed). See `logic/solution/study_design.md`.

## Code availability
- **Review team code**: NONE. No code-availability statement and no GitHub/GitLab/Zenodo/OSF/figshare/Dryad repository authored by the review team (verified in `sources.yaml`). The review only *analyzes* the code-availability practices of the 68 reviewed studies (Table 6, Fig. 42b: ~15% share code).

## Data availability
- **Review team data**: NONE released. Data Availability statement verbatim: "No datasets were generated or analysed during the current study." (per `sources.yaml`).
- **No clinical trials**: no NCT identifiers appear anywhere in the paper.

## Data sources used by the *reviewed* studies (Table 7, §10)
These are the cohorts/datasets the 68 reviewed primary studies drew on — recorded here for
reproducibility context. All are third-party resources; the review itself accesses none of them
directly.

| Dataset | Subjects | Modalities | Longitudinal | Access type | Link / identifier |
|---------|----------|------------|--------------|-------------|-------------------|
| ADNI | ~2,750 | MRI, PET, DTI, CSF, genetic, clinical, cognitive | Yes | Controlled / application-based | http://adni.loni.usc.edu |
| OASIS | 3,000+ | sMRI, PET, cognitive | Yes | Open (registration) | http://www.oasis-brains.org |
| AIBL | ~2,500 | MRI, PET, CSF, genetic, clinical/cognitive, lifestyle | Yes | Controlled / application-based | https://aibl.csiro.au |
| Kaggle AD (4-class) | 6,400 | sMRI | No | Open | kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images |
| Kaggle AD (medical-scan) | 8,000 | sMRI | No | Open | kaggle.com/datasets/arjunbasandrai/medical-scan-classification-dataset |
| UK Biobank | 500,000+ | sMRI, DWI, SWI, genomic, proteomic, lifestyle, clinical | Yes | Controlled / application-based | https://www.ukbiobank.ac.uk/ |
| NACC | 47,000+ | neuropathology, genetic, imaging (UDS) | Yes | Request-based | https://www.niagads.org/datasets/nacc |
| HUASHAN-MCI | — (not stated) | sMRI | — | Institutional (Huashan Hospital) | — |
| AANLIB (Whole Brain Atlas) | — (not stated) | sMRI, CT, PET | No | Open (educational) | https://www.med.harvard.edu/aanlib/ |
| Dong-A University Hospital cohort | 593+ | sMRI, PET, CSF, clinical/cognitive | Yes | Institutional (Korean cohort) | — (see Shin et al. [162]) |

Notes: subject counts are as reported in Table 7 (`~` and `+` reproduced verbatim). Access-type
labels are inferred from each resource's well-known access model, not stated numerically in the paper.
Other cohorts referenced in individual studies (e.g. ADNI-1/2/3/GO/4 sub-phases, OASIS-1/2/3/4,
ADNI2, C-PAS, AANLIB) are sub-collections of the above.
